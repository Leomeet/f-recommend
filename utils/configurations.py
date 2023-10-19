import os
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings

from pathlib import Path
from dotenv import load_dotenv

project_root = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(project_root, ".env")
print(dotenv_path)
load_dotenv(dotenv_path)



class Settings(BaseSettings):
    PROJECT_ROOT: str = str(project_root)
    PINECONE_ENV: str = os.environ.get("PINECONE_ENVIORNMENT")
    PINECONE_API_KEY: str = os.environ.get("PINECONE_API_KEY")
    PINECONE_INDEX: str = os.environ.get("PINECONE_INDEX")
    PINECONE_NAMESPACE: str = os.environ.get("PINECONE_NAMESPACE")

    class Config:
        case_sensitive = True


settings = Settings()
