# ps-3: Protocolos de Seguridad, Tema 3

- **One report** for the three Tema 3 activities (3.1 OpenSSL, 3.2 tráfico SSL, 3.3 auditoría SSL). One `.md`, one PDF via `md-to-pdf`, one section per activity. Authors, header and reference style: copy `informe-3.1-bolivar-dibo.md`.
- **Screenshots: real program, user's format.** Never mock a capture.
  - Terminal: open `gnome-terminal` with the user's profile (Gruvbox dark, bg `#282828`, fg `#ebdbb2`, JetBrains Mono 14; the profile is in dconf `/org/gnome/terminal/`), run the command in it, capture that window.
  - GUI (Wireshark, browser, SSL Labs): launch the real app, load the real data, capture its window.
  - Screenshots must look like a person made them: no script names, odd profile names, stray tabs or temp paths in titles, tab bars, prompts or status bars. Use the app's own features (Wireshark "Mark packet"), default profiles, and leave pixels unedited.
- AWS: key `~/.ssh/JavierDiboClaves.pem`, user `ec2-user`. Instance details live in project memory.
