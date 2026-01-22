from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AppConfig:
    name: str
    env: str
    root_path: Path
    addons_path: list[Path]


@dataclass(frozen=True)
class DBConfig:
    host: str
    port: int
    user: str
    password: str
    name: str


@dataclass(frozen=True)
class Config:
    app: AppConfig
    db: DBConfig

