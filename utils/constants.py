from langchain.embeddings import HuggingFaceBgeEmbeddings
from enum import Enum

class HuggingFaceEmbeddings(Enum):
    model_name = "BAAI/bge-large-en-v1.5"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': True}

    @classmethod
    def get_embeddings_model(cls):
        # returning huggingface embeddings model
        # use: model.embed_query("hi this is harrison")
        return HuggingFaceBgeEmbeddings(
            model_name=cls.model_name,
            model_kwargs=cls.model_kwargs,
            encode_kwargs=cls.encode_kwargs,
        )