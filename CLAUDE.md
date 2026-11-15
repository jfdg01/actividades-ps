# actividades-ps: Protocolos de Seguridad

Una carpeta por tema: `ps-3/` (Tema 3), `ps-4/` (Tema 4), `ps-5/` (Tema 5, el trabajo en pareja sobre QUIC, con informe y diapositivas) y `ps-6/` (Tema 6). Cada carpeta tiene su `CLAUDE.md` cuando lo necesita.

## Las diapositivas

`md-to-pdf` no hace diapositivas. Marp las genera desde un `.md` con `---` entre diapositivas, y usa el Chrome del sistema:

```bash
cd ps-5 && CHROME_PATH=/usr/bin/google-chrome npx -y @marp-team/marp-cli@latest diapositivas-quic-bolivar-dibo.md --pdf --allow-local-files
```

`--allow-local-files` deja a Marp leer `img/`. El PDF es una salida del build y entra en git, como el del informe.

## El PDF de un informe

`md-to-pdf` (en el `PATH`, repo `~/md-to-pdf`) convierte un `.md` en un PDF junto a él:

```bash
md-to-pdf ps-3/informe-tema3-bolivar-dibo.md                 # -> ps-3/informe-tema3-bolivar-dibo.pdf
md-to-pdf ps-3/informe-tema3-bolivar-dibo.md -o /tmp/x.pdf   # prueba, no deja nada en el repo
```

La build lee solo dos cosas, las dos en el directorio del informe:

- El front matter del `.md`: `title`, `subtitle`, `comment`, `author`, `logo`, `locale`.
- `img/`: cada figura `![...](img/…)`, y el logo de la portada, `img/logo_uja.webp`. Un archivo que falta rompe la build.

La build no lee `lab/` (certificados, claves, la página de prueba, las capturas de tráfico).

Las fuentes van con `md-to-pdf`. Una máquina nueva necesita `bash ~/md-to-pdf/install.sh` una vez (`uv sync` y el enlace del `PATH`), y las librerías de Pango (`libpango-1.0-0`, `libpangoft2-1.0-0`).

## Las reglas

- Una figura del informe va en `img/`, y el `.md` la nombra como `img/<nombre>.png`.
- El PDF es una salida de la build: se reconstruye desde el `.md` y no se edita. Entra en git junto a su `.md`, porque es lo que se entrega.
