import typer
import importlib
from mini_odoo.server.app import create_app

app = typer.Typer()

def load_config(name: str):
    module = importlib.import_module(f"mini_odoo.config.{name}")
    return module.config

@app.command()
def shell(config: str = "dev"):
    cfg = load_config(config)
    env = create_app(cfg)

    import code
    code.interact(local={"env": env})

@app.command()
def start(config: str = "dev"):
    cfg = load_config(config)
    env = create_app(cfg)
    print(f"Mini-Odoo started in {cfg.app.env} mode")

if __name__ == "__main__":
    app()