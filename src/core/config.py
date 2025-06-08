from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "0.0.0.0" 
    port: int = 8000

class RouterPrefix(BaseModel):
    api: str = "/api"

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    router_prefix: RouterPrefix = RouterPrefix()
    pass


settings = Settings()