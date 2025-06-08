import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers import api_router
from core.config import settings 

app = FastAPI()

app.include_router(api_router, prefix=settings.router_prefix.api)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app", 
        host=settings.run.host, 
        port=settings.run.port, 
        reload=True,
        )