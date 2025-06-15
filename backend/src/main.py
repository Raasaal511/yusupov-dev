import uvicorn
from fastapi import FastAPI

from features.auth.routers import auth_app
from features.admin.routers import admin_app


app = FastAPI()

app.include_router(auth_app)
app.include_router(admin_app)

if __name__ == "__main__":
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True) # используется в dev версии
