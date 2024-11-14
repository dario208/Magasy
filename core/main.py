from fastapi import FastAPI
from core.database import get_session,init_db
from api.routes.routes import routers
app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()
    session = next(get_session())
    
app.include_router(routers)