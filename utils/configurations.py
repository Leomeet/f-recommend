import os
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, validator, BaseModel
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
    IMAGES_PATH: str = str(os.path.join(project_root,"data","images"))
    class Config:
        case_sensitive = True

class SearchObject(BaseModel):
    gender: Optional[List] = ["All"]
    category: Optional[List] = ["All"]
    sub_category: Optional[List] = ["All"]
    article_type: Optional[List] = ["All"]
    base_color: Optional[List] = ["All"]
    season: Optional[List] = ["All"]
    #year
    usage: Optional[List] = ["All"]
    search: Optional[str] = "All"
    
    @property
    def search_query(self):
        return f"{self.join_list(self.gender)} :: {self.join_list(self.category)} :: {self.join_list(self.sub_category)} :: {self.join_list(self.article_type)} :: {self.join_list(self.base_color)} :: {self.join_list(self.season)} :: ___ :: {self.join_list(self.usage)} :: {self.join_list(self.search)}"

    def join_list(self, values):
        if isinstance(values, list):
            return ", ".join(values)
        return values

settings = Settings()
