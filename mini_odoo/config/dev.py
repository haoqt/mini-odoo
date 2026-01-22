from pathlib import Path
from .base import Config, AppConfig, DBConfig

ROOT = Path(__file__).resolve().parents[2]

config = Config(
    app=AppConfig(
        name="mini-odoo",
        env="dev",
        root_path=ROOT,
        addons_path=[ROOT / "addons"],
    ),
    db=DBConfig(
        host="localhost",
        port=5432,
        user="odoo",
        password="odoo",
        name="mini_odoo",
    ),
)
