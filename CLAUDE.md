# actividades-ps: Protocolos de Seguridad

Una carpeta por tema: `ps-3/` (Tema 3), `ps-4/` (Tema 4, sin entregar) y `ps-5/` (Tema 5, el trabajo en pareja sobre QUIC, con informe y diapositivas). Cada carpeta tiene su `CLAUDE.md` cuando lo necesita.

## Las diapositivas

`md-to-pdf` no hace diapositivas. Marp las genera desde un `.md` con `---` entre diapositivas, y usa el Chrome del sistema:

```bash
cd ps-5 && CHROME_PATH=/usr/bin/google-chrome npx -y @marp-team/marp-cli@latest diapositivas-quic-bolivar-dibo.md --pdf --allow-local-files
```

`--allow-local-files` deja a Marp leer `img/`. El PDF es una salida del build, como el del informe.

## Build a report PDF

`md-to-pdf` (on `PATH`, repo `~/md-to-pdf`) turns a `.md` into a PDF next to it:

```bash
md-to-pdf ps-3/informe-tema3-bolivar-dibo.md          # -> ps-3/informe-tema3-bolivar-dibo.pdf
md-to-pdf ps-3/informe-tema3-bolivar-dibo.md -o /tmp/x.pdf   # test build, nothing lands in the repo
```

The build reads only two things, both inside the report's directory:

- The `.md` front matter: `title`, `subtitle`, `comment`, `author`, `logo`, `locale`.
- `img/`: every `![...](img/…)` figure, plus the cover logo `img/logo_uja.webp`. A missing file breaks the build.

Nothing else is needed. `lab/` (certificates, keys, test page) is not read by the build. The `.md` only quotes `lab/ca_actividad1.crt` inside command examples.

Fonts ship with `md-to-pdf`. A fresh machine needs `bash ~/md-to-pdf/install.sh` once (`uv sync` + the `PATH` link) and the Pango libraries (`libpango-1.0-0`, `libpangoft2-1.0-0`).

## Rules

- A figure in the report goes in `img/` and is referenced as `img/<name>.png`.
- The PDF is a build output. Rebuild it from the `.md`; do not edit it.
