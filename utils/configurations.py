import os
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, validator
from pathlib import Path
from dotenv import load_dotenv

project_root = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(project_root, ".env")

load_dotenv(dotenv_path)


class Settings(BaseSettings):
    PROJECT_ROOT: str = str(project_root)
    PINECONE_ENV = os.environ.get("PINECONE_ENV")
    PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
    PINECONE_INDEX = os.environ.get("PINECONE_INDEX")
    PINECONE_NAMESPACE = os.environ.get("PINECONE_NAMESPACE")

    class Config:
        case_sensitive = True

settings = Settings()
