from fastapi import FastAPI
from core.database import get_session,init_db

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()
    session = next(get_session())
    
