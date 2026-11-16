# Actividades de Protocolos de Seguridad

Los informes de las actividades de la asignatura Protocolos de Seguridad (Universidad de Jaén, 2026/2027), de Miguel Bolívar García y Javier Francisco Dibo Gómez.

| Tema | Fuente | PDF |
|---|---|---|
| Tema 3: Protocolos de capa de transporte | [`ps-3/informe-tema3-bolivar-dibo.md`](ps-3/informe-tema3-bolivar-dibo.md) | [PDF](ps-3/informe-tema3-bolivar-dibo.pdf) |
| Tema 4: Protocolos de capa de aplicación | [`ps-4/informe-tema4-bolivar-dibo.md`](ps-4/informe-tema4-bolivar-dibo.md) | [PDF](ps-4/informe-tema4-bolivar-dibo.pdf) |
| Tema 5: QUIC (informe) | [`ps-5/informe-quic-bolivar-dibo.md`](ps-5/informe-quic-bolivar-dibo.md) | [PDF](ps-5/informe-quic-bolivar-dibo.pdf) |
| Tema 5: QUIC (diapositivas) | [`ps-5/diapositivas-quic-bolivar-dibo.md`](ps-5/diapositivas-quic-bolivar-dibo.md) | [PDF](ps-5/diapositivas-quic-bolivar-dibo.pdf) |
| Tema 6: sslstrip y HSTS (actividad 1) | [`ps-6/informe-tema6-actividad1-bolivar-dibo.md`](ps-6/informe-tema6-actividad1-bolivar-dibo.md) | [PDF](ps-6/informe-tema6-actividad1-bolivar-dibo.pdf) |
| Tema 6: ataque a un certificado débil (actividad 2) | [`ps-6/informe-tema6-actividad2-bolivar-dibo.md`](ps-6/informe-tema6-actividad2-bolivar-dibo.md) | [PDF](ps-6/informe-tema6-actividad2-bolivar-dibo.pdf) |

## El formato de los informes

Cada informe es un Markdown que [md-to-pdf](https://github.com/jfdg01/md-to-pdf) convierte en un PDF con portada, índices, figuras numeradas y referencias cruzadas. Las instrucciones de instalación y la sintaxis del formato están en su `README.md`.

```bash
md-to-pdf ps-4/informe-tema4-bolivar-dibo.md
```

El PDF sale junto al `.md`. La build lee solo el `.md` y la carpeta `img/` de su directorio. Las diapositivas salen con Marp, y el comando está en `CLAUDE.md`.
