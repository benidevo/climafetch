import os
from typing import Union

from src.config.dev import DevConfig
from src.config.prod import ProdConfig

env = os.getenv("ENV", "dev")
CONFIGMAPS = {"dev": DevConfig, "prod": ProdConfig}

settings: Union[DevConfig, ProdConfig] = CONFIGMAPS.get(env)()  # type: ignore
