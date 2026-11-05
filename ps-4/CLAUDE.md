# ps-4: Protocolos de Seguridad, Tema 4

Un informe para las actividades 4.2 (fail2ban) y 4.3 (CheckTLS): `informe-tema4-bolivar-dibo.md`. La actividad 4.1 (el servidor SSH) la hace el compañero.

## Actividad 4.2: fail2ban

Las dos instancias son las del Tema 3. Sus IP públicas cambian con cada arranque: léelas en la consola de AWS.

- **El servidor:** `JavierDiboAct1` (RHEL 10.2). `sshd` solo acepta claves. La instancia no tiene `firewalld` ni `iptables`, así que el ban usa `nftables`. fail2ban sale de EPEL 10, con el paquete `fail2ban-server`. El metapaquete `fail2ban` instala también `firewalld` y `sendmail`.
- **El atacante:** `JavierDiboAct2`, con un bucle de 6 `ssh` con un usuario que no existe. `JavierDiboAct2` tiene un servidor Vault de otra asignatura: no lo toques.
- **`/etc/fail2ban/jail.local`:**

  ```ini
  [DEFAULT]
  bantime   = 300
  findtime  = 600
  maxretry  = 5
  banaction = nftables-multiport
  banaction_allports = nftables-allports
  ignoreip  = 127.0.0.1/8 ::1 <IP pública del portátil>

  [sshd]
  enabled = true
  backend = systemd
  ```

  `jail.conf` usa `iptables` en las dos acciones del ban, y `jail.local` las cambia a `nftables`. `ignoreip` evita que un error deje fuera al portátil.
- **El modo del filtro `sshd`:** `normal`, el modo por defecto. Cuenta 1 fallo por cada conexión con un usuario que no existe, así que el ban llega en la 5.ª conexión. `mode = aggressive` cuenta también la línea `Connection closed … [preauth]`: 2 fallos por conexión, y el ban en la 3.ª. `normal` no cuenta una conexión a un usuario real sin la clave correcta, que no puede entrar sin contraseñas. El informe explica los dos modos.
- **La prueba** muestra la IP del atacante baneada en `fail2ban-client status sshd` y en `nft list ruleset`. También muestra el acceso del portátil durante el ban, y el desbaneo a los 300 s. Los bans de bots de Internet entran en un párrafo corto.
- **Las mejoras sin activar:** `bantime.increment` y la jaula `recidive`. El informe las explica, pero no las activa, porque cambian los 300 s del enunciado para una IP que reincide.

## Actividad 4.3: CheckTLS

- **Las cuentas:** `@gmail.com` es la cuenta limpia. `@mailinator.com` es la cuenta con deficiencias, porque su MX tiene un certificado autofirmado. La reserva es `@guerrillamail.com`, porque su certificado nombra otro host. La UJA no sirve: su MX es de Google, el mismo servidor que Gmail.
- **La salida:** un `.txt` por cuenta en `lab/`, con el texto del resultado, y capturas del navegador en `img/`.

## El informe

- La cabecera y el estilo son los de `ps-3/informe-tema3-bolivar-dibo.md`. Tiene las secciones 4.1, 4.2 y 4.3, y la 4.1 queda vacía para el compañero.
- Las capturas siguen las reglas de `ps-3/CLAUDE.md`: el terminal real con el perfil Gruvbox, y el navegador real.
