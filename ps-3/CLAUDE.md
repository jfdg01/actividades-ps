# ps-3: Protocolos de Seguridad, Tema 3

- **Un informe** para las tres actividades del Tema 3 (3.1 OpenSSL, 3.2 tráfico SSL, 3.3 auditoría SSL): `informe-tema3-bolivar-dibo.md`. Tiene una sección por actividad. Su cabecera, sus autores y el estilo de sus referencias son el modelo de los informes de los otros temas.
- **Las capturas: el programa real, con el formato del usuario.** Una captura nunca es un montaje.
  - El terminal: abre `gnome-terminal` con el perfil del usuario (Gruvbox dark, fondo `#282828`, texto `#ebdbb2`, JetBrains Mono 14; el perfil está en dconf `/org/gnome/terminal/`). Ejecuta el comando en él, y captura esa ventana.
  - La interfaz gráfica (Wireshark, el navegador, SSL Labs): abre la aplicación real, carga los datos reales, y captura su ventana.
  - Una captura parece hecha por una persona: sin nombres de scripts, nombres de perfil raros, pestañas sueltas ni rutas temporales en los títulos, las pestañas, los prompts o las barras de estado. Usa las funciones de la propia aplicación ("Mark packet" de Wireshark) y los perfiles por defecto, y no edites los píxeles.
- AWS: la clave es `~/.ssh/JavierDiboClaves.pem`, y el usuario es `ec2-user`. Los datos de las instancias están en la memoria del proyecto.
