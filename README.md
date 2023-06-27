# Innovation Research Lab - Robot Control

Control Qbot GRAY by sending a socket message with 3 double values.

The message contains [Rotation, Speed, Shutdown] where the first two values control movement of the robot, and the third is a flag where sending a 1 causes the robot to shutdown.

The website lets you connect to the robot using a python socket. If the site is refreshed the connection will break, and the site must be relaunched.

## Usage
Run `python manage.py runserver <PORT>` and connect to `127.0.0.1:<PORT>`.

Use the VS Code build task "Run Django Website" by pressing `Ctrl+Shift+B` to start the site on port 3000.
