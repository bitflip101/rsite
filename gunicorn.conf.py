# gunicorn.conf.py

import os

# Number of worker processes. A general rule of thumb is 2-4 workers per core.
workers = 3

# The socket to bind to. Use a Unix socket for reverse proxy setups.
# For local testing, can use an IP address and port.
# bind = "127.0.0.1:8000"

# Using NGINX
# bind = "unix:/run/gunicorn.sock"  ### 

# Using this user-writeable path (/run/ is a system folder only root has acces)
# bind = "unix:/home/rolito/Dev/py/Rsite/rsite/gunicorn.sock"
bind = os.environ.get("GUNICORN_SOCK_PATH", "unix:/tmp/gunicorn.sock")

# The Gunicorn worker class to use. 'sync' is the default.
# Consider 'gevent' or 'gthread' for I/O-bound applications.
worker_class = 'sync'

# Timeout for workers.
timeout = 30

# Log settings.
accesslog = '-' # '-' means log to stdout
errorlog = '-'  # '-' means log to stdout