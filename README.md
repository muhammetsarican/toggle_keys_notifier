# Toggle Keys Notifier

Toggle keys notifier is a gui app that shows you a box when toggle keys opened or closed

## Running the project at startup automatically as a service

Clone the project

```bash
  git clone https://github.com/muhammetsarican/toggle_keys_notifier.git
```

Create the folder that includes project

```bash
  mkdir /opt/scripts
```

Move the project to directory

```bash
  mv toggle_keys_notifier /opt/scripts/
```

Give the sudo privilege from visudo

```bash
  sudo visudo
```

Add this line at the end of file

```bash
$USER ALL=(ALL) NOPASSWD: /python/env/pyenv/bin/python /opt/scripts/toggle_keys_notifier/main.py
```

Create the folder that includes service file

```bash
  mkdir $HOME/.config/systemd/user
```

Create the service file

```bash
  nano $HOME/.config/systemd/user/toggle_keys_notifier.service
```

### $HOME/.config/systemd/user/toggle_keys_notifier.service

```bash
[Unit]
Description=Toggle Keys Notifier (GUI with root access)
After=graphical-session.target

[Service]
Type=simple
ExecStart=/usr/bin/bash -c 'sudo /python/env/pyenv/bin/python /opt/scripts/toggle_keys_notifier/main.py'
Environment=DISPLAY=:1
Environment=XDG_RUNTIME_DIR=/run/user/1000
Restart=on-failure

[Install]
WantedBy=default.target

```

Reload and restart the service:

```bash
systemctl --user daemon-reload
systemctl --user restart toggle_keys_notifier.service
```

Check logs:

```bash
journalctl --user -u toggle_keys_notifier.service --no-pager
```

## Feedback

If you have any feedback, please reach out to me at [muhammetsarican.com](mailto:muhammetsarican.info@gmail.com)

## Authors

- [@muhammetsarican](https://www.github.com/muhammetsarican)
