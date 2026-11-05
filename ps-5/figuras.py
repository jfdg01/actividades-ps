#!/usr/bin/env python3
"""Genera las figuras SVG del informe de QUIC en img/. Solo usa la stdlib.

Sigue las reglas de ~/md-to-pdf/docs/charts.md: los colores, el factor T y la fuente.
Uso: python3 -I figuras.py
"""
from pathlib import Path

SURFACE, INK, INK2 = "#fcfcfb", "#0b0b0b", "#52514e"
GRID, AXIS = "#e1e0d9", "#c3c2b7"
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
FONT = "Space Grotesk, sans-serif"
T = 1.2
OUT = Path(__file__).parent / "img"


def text(x, y, s, size=11, fill=INK2, weight=400, anchor="start"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size * T:.1f}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>')


def svg(w, h, body):
    defs = (f'<defs><marker id="flecha" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" '
            f'markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="{INK2}"/></marker></defs>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            + defs + "".join(body) + "</svg>")


def capa(x, y, w, h, color, nombre, detalle=""):
    """Una capa de la pila: caja con una franja de color a la izquierda."""
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{SURFACE}" stroke="{AXIS}"/>',
           f'<rect x="{x}" y="{y}" width="8" height="{h}" rx="4" fill="{color}"/>']
    cy = y + h / 2
    if detalle:
        out += [text(x + 22, cy - 3, nombre, 12, INK, 600), text(x + 22, cy + 15, detalle, 10)]
    else:
        out.append(text(x + 22, cy + 5, nombre, 12, INK, 600))
    return out


def fig_pila():
    W, H = 760, 416
    xl, xr, cw = 20, 390, 350
    rows = [(60, 48), (116, 92), (256, 48), (312, 48)]  # (y, alto): aplicación, cifrado, transporte, red
    b = [text(xl, 36, "HTTP/2 sobre TCP", 13, INK, 600), text(xr, 36, "HTTP/3 sobre QUIC", 13, INK, 600)]
    (ya, ha), (yc, hc), (yt, ht), (yn, hn) = rows
    # HTTP/2 sobre TLS y TCP
    b += capa(xl, ya, cw, ha, AXIS, "HTTP/2")
    b += capa(xl, yc, cw, hc, ORANGE, "TLS 1.3", "handshake y registros cifrados")
    b += capa(xl, yt, cw, ht, BLUE, "TCP", "fiabilidad, orden, congestión")
    b += capa(xl, yn, cw, hn, AXIS, "IP")
    # HTTP/3 sobre QUIC y UDP
    b += capa(xr, ya, cw, ha, AXIS, "HTTP/3")
    b += [f'<rect x="{xr}" y="{yc}" width="{cw}" height="{hc}" rx="8" fill="{SURFACE}" stroke="{AXIS}"/>',
          f'<rect x="{xr}" y="{yc}" width="8" height="{hc}" rx="4" fill="{BLUE}"/>',
          text(xr + 22, yc + 24, "QUIC", 12, INK, 600),
          text(xr + 22, yc + 42, "flujos, fiabilidad, congestión", 10)]
    px, pw = xr + 22, cw - 40
    b += [f'<rect x="{px}" y="{yc + 54}" width="{pw}" height="28" rx="6" fill="{GRID}"/>',
          f'<rect x="{px + 8}" y="{yc + 63}" width="10" height="10" rx="2" fill="{ORANGE}"/>',
          text(px + 26, yc + 73, "TLS 1.3, solo el handshake", 10, INK)]
    b += capa(xr, yt, cw, ht, AXIS, "UDP", "solo los puertos")
    b += capa(xr, yn, cw, hn, AXIS, "IP")
    # La frontera entre el espacio de usuario y el núcleo
    yf = (yc + hc + yt) / 2
    b += [f'<line x1="{xl - 20}" y1="{yf}" x2="{W - 20}" y2="{yf}" stroke="{INK2}" stroke-width="1.5"/>',
          text(W - 20, yf - 8, "espacio de usuario ↑", 10, INK2, 400, "end"),
          text(W - 20, yf + 18, "núcleo del sistema ↓", 10, INK2, 400, "end")]
    # Leyenda
    ly = H - 16
    for i, (c, s) in enumerate([(BLUE, "el transporte fiable"), (ORANGE, "el cifrado")]):
        x = xl + i * 220
        b += [f'<rect x="{x}" y="{ly - 10}" width="10" height="10" rx="2" fill="{c}"/>',
              text(x + 16, ly, s, 11, INK)]
    return svg(W, H, b)


def paquete(x, y, color, tipo, contenido):
    """Un paquete QUIC: cuadro de color, tipo en negrita y tramas en gris. Devuelve (svg, ancho)."""
    w = 30 + (len(tipo) * 7.6 + len(contenido) * 6.6) * T * 10 / 11
    return [f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="26" rx="6" fill="{SURFACE}" stroke="{color}" stroke-width="1.5"/>',
            f'<rect x="{x + 8:.1f}" y="{y + 8}" width="10" height="10" rx="2" fill="{color}"/>',
            f'<text x="{x + 24:.1f}" y="{y + 18}" font-family="{FONT}" font-size="{10 * T:.1f}" fill="{INK2}">'
            f'<tspan font-weight="600" fill="{INK}">{tipo}</tspan> · {contenido}</text>'], w


def fig_handshake():
    W = 760
    xc, xs = 130, 690  # las líneas de vida del cliente y del servidor
    b = []
    for x, s in ((xc, "Cliente"), (xs, "Servidor")):
        b += [f'<rect x="{x - 60}" y="10" width="120" height="34" rx="8" fill="{GRID}"/>',
              text(x, 32, s, 12, INK, 600, "middle")]
    vuelos = [  # (y de salida, y de llegada, del cliente, paquetes)
        (70, 110, True, [(BLUE, "Initial", "ClientHello")]),
        (130, 250, False, [(BLUE, "Initial", "ServerHello"),
                           (ORANGE, "Handshake", "EncryptedExtensions, Certificate"),
                           (ORANGE, "Handshake", "CertificateVerify, Finished"),
                           (AQUA, "1-RTT", "datos 0,5-RTT (opcional)")]),
        (270, 310, True, [(ORANGE, "Handshake", "Finished"), (AQUA, "1-RTT", "STREAM: la petición")]),
        (330, 370, False, [(AQUA, "1-RTT", "HANDSHAKE_DONE, STREAM: la respuesta")]),
    ]
    yfin = 400
    for x in (xc, xs):
        b.append(f'<line x1="{x}" y1="44" x2="{x}" y2="{yfin}" stroke="{AXIS}" stroke-width="2"/>')
    for y0, y1, del_cliente, paquetes in vuelos:
        x0, x1 = (xc, xs) if del_cliente else (xs, xc)
        b.append(f'<line x1="{x0}" y1="{y0}" x2="{x1 + (-4 if del_cliente else 4)}" y2="{y1}" '
                 f'stroke="{INK2}" stroke-width="1.5" marker-end="url(#flecha)"/>')
        # Los paquetes del vuelo, apilados en el centro, sobre un fondo que tapa la flecha
        alto = 30 * len(paquetes) - 4
        ytop = (y0 + y1) / 2 - alto / 2
        for i, p in enumerate(paquetes):
            w = paquete(0, 0, *p)[1]
            b += paquete((xc + xs) / 2 - w / 2, ytop + 30 * i, *p)[0]
    # El RTT del cliente, entre su primer envío y la llegada del vuelo del servidor
    xb = xc - 30
    b += [f'<path d="M{xb + 8},70 H{xb} V250 H{xb + 8}" fill="none" stroke="{INK}" stroke-width="1.5"/>',
          text(xb - 8, 165, "1 RTT", 12, INK, 600, "end"),
          f'<circle cx="{xc}" cy="270" r="5" fill="{AQUA}" stroke="{SURFACE}" stroke-width="2"/>',
          text(xb - 8, 275, "la petición", 10, INK2, 400, "end"),
          text(xb - 8, 291, "sale aquí", 10, INK2, 400, "end")]
    # La comparación: RTT antes de la primera petición
    y = yfin + 40
    b.append(text(40, y, "Los RTT antes de la primera petición", 12, INK, 600))
    b.append(text(40, y + 18, "menos es mejor", 10))
    escala, x0 = 180, 320
    for i, (s, rtt, nota) in enumerate([("TCP + TLS 1.3", 2, "2 RTT"),
                                        ("QUIC, conexión nueva", 1, "1 RTT"),
                                        ("QUIC, reanudación con 0-RTT", 0, "0 RTT, datos en el primer vuelo")]):
        yb = y + 36 + i * 34
        b.append(text(x0 - 12, yb + 15, s, 11, INK, 400, "end"))
        L = rtt * escala
        if L:
            b.append(f'<path d="M{x0},{yb} H{x0 + L - 4} A4,4 0 0 1 {x0 + L},{yb + 4} V{yb + 16} '
                     f'A4,4 0 0 1 {x0 + L - 4},{yb + 20} H{x0} Z" fill="{INK2}"/>')
        b.append(text(x0 + L + 8, yb + 15, nota, 11, INK, 600 if L else 400))
    b.append(f'<line x1="{x0}" y1="{y + 30}" x2="{x0}" y2="{y + 30 + 3 * 34}" stroke="{AXIS}"/>')
    return svg(W, y + 30 + 3 * 34 + 10, b)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    (OUT / "pila.svg").write_text(fig_pila(), encoding="utf-8")
    (OUT / "handshake.svg").write_text(fig_handshake(), encoding="utf-8")
    print("img/pila.svg img/handshake.svg")
