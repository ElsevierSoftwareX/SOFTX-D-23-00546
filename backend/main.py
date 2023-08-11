import uvicorn
from apps.files.routers import router
from config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()


# include local origins including react ========================
origins = [
    "http://165.246.44.247:3030",  # Add your frontend URL here
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3030",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# mongodb client startup & connect with DB server ==============
@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
    app.mongodb = app.mongodb_client[settings.DB_NAME]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


# include file routers & run ===================================
app.include_router(router, tags=["files"], prefix="/file")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
