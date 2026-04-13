# Jupyter Lab Configuration
# This file configures Jupyter Lab settings for the project

c = get_config()

# Server settings
c.ServerApp.ip = '127.0.0.1'
c.ServerApp.open_browser = False
c.ServerApp.port = 8888

# Notebook settings
c.FileContentsManager.delete_to_trash = False

# Extensions
c.ServerApp.jpserver_extensions = {
    'jupyterlab': True,
}

# Terminal settings
c.ServerApp.terminals_enabled = True

# File browser
c.FileContentsManager.pre_save_hook = None
