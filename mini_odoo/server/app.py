from mini_odoo.registry import Registry
from mini_odoo.env import Env

def create_app(config):
    registry = Registry()
    registry.load_modules(config.app.addons_path)

    env = Env(
        config=config,
        registry=registry,
        db=None,  # DB comes later
    )
    return env
