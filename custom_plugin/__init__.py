#from githubcommit.handlers import setup_handlers
# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'custom_plugin',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "notebook",
        "dest": "custom_plugin",
        "src": "static",
        "require": "custom_plugin/main"
    }]

 def load_jupyter_server_extension(nbapp):
     setup_handlers(nbapp.web_app)
