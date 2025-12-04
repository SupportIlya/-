# app/main.py
from app.routers import users, login, descriptions  # ← products заменён на descriptions

app = FastAPI()
app.include_router(users.router)
app.include_router(login.router)
app.include_router(descriptions.router)   # ✅