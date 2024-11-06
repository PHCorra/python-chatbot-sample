from fastapi import FastAPI
from controllers.chat_controller import router as routes

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Test API using LangChain and FastAPI"
)

app.include_router(routes)
# RUN WITH uvicorn src.main:app
