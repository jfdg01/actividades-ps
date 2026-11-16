"""Corre los pasos de la Actividad 2 y dibuja cada terminal en ps-6/img/.

Uso: python3 capturas.py   (desde cualquier carpeta)

msieve corre en Windows (con wine) y tarda minutos, así que su figura sale
de msieve.txt, la salida guardada de una ejecución sin el msieve.dat del
enunciado. El resto de los comandos corre cada vez.
"""
import html
import subprocess
import tempfile
from pathlib import Path

LAB = Path(__file__).resolve().parent
IMG = LAB.parent.parent / "img"
N_HEX = "D7561B33645530BCC67C2AD1278AFA8B0556233074CC20849458FC9F62EF9629"
P = "306987831065370542406424007106753576023"
Q = "317274462273091628471429937331739406719"

PASOS = {
    "a2-modulo": [
        "openssl rsa -in rsa_clavepublica.pem -pubin -text -modulus",
        f'echo "ibase=16; {N_HEX}" | BC_LINE_LENGTH=0 bc',
    ],
    "a2-clave-privada": [
        "gcc get_priv_key.c -lcrypto -o get_priv_key 2>&1 | grep -m3 error",
        "gcc get_priv_key_openssl3.c -lcrypto -Wno-deprecated-declarations -o get_priv_key",
        f"./get_priv_key {P} {Q} 65537 > claveprivada.pem",
        "cat claveprivada.pem",
        "openssl pkey -in claveprivada.pem -pubout | diff - rsa_clavepublica.pem && echo 'misma clave pública'",
    ],
    "a2-descifrado": [
        "openssl rsautl -decrypt -inkey claveprivada.pem -in mensaje_cifrado.txt; echo",
        "openssl pkeyutl -decrypt -inkey claveprivada.pem -in mensaje_cifrado.txt; echo",
    ],
}


def correr(comandos):
    salida = []
    for c in comandos:
        r = subprocess.run(c, shell=True, cwd=LAB, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        salida.append(f"$ {c}\n{r.stdout}".rstrip("\n"))
    return "\n".join(salida)


def dibujar(nombre, texto):
    lineas = texto.splitlines()
    ancho = max(len(l) for l in lineas) * 9 + 48
    alto = len(lineas) * 20 + 40
    cuerpo = "".join(
        f'<span class="cmd">{html.escape(l)}</span>\n' if l.startswith("$ ") else html.escape(l) + "\n"
        for l in lineas
    )
    pagina = f"""<html><body style="margin:0;background:#1e1e1e">
<style>pre{{margin:0;padding:20px 24px;font:15px/20px 'Space Mono',monospace;color:#ddd}}
.cmd{{color:#8fd18f}}</style><pre>{cuerpo}</pre></body></html>"""
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(pagina)
    subprocess.run(
        ["google-chrome", "--headless", "--hide-scrollbars", f"--window-size={ancho},{alto}",
         f"--screenshot={IMG / (nombre + '.png')}", f.name],
        check=True, capture_output=True,
    )


if __name__ == "__main__":
    for nombre, comandos in PASOS.items():
        dibujar(nombre, correr(comandos))
    # ponytail: msieve.txt es la salida real, recortada a mano a las líneas que cuentan
    dibujar("a2-msieve", (LAB / "msieve.txt").read_text())
    (LAB / "get_priv_key").unlink()
