from datetime import datetime
def on_config(config, **kwargs):
    config.copyright = f"© {datetime.now().year}"