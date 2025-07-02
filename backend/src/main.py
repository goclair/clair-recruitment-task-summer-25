from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER
from src.db.session import init_async_engine
from src.routes import projects

# Init database
init_async_engine(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

# Init app
app = FastAPI(title="Clair recruitment task API", version="1.0.0")

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(projects.router, prefix="/projects")
