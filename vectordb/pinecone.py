import pinecone
from pinecone.exceptions import PineconeException

from typing import List, Optional, Union
from langchain.docstore.document import Document
from langchain.embeddings.base import Embeddings
from langchain.vectorstores.pinecone import Pinecone

from utils.constants import VectorDatabaseConstants
from utils.configurations import  settings


class CustomPinecone(Pinecone):
    def __init__(
        self,
        embedding_function: Embeddings.embed_documents,
        text_key: str,
        namespace: Optional[str] = None,
    ):
        index = self.connect_to_vectorstore()
        self._embedding_function = embedding_function
        super().__init__(index, embedding_function, text_key, namespace)

    def connect_to_vectorstore(self):
        """code for connecting to pinecone database"""

        pinecone.init(
            api_key=settings.PINECONE_API_KEY,
            environment=settings.PINECONE_ENV,
        )
        index = pinecone.Index(settings.PINECONE_INDEX)
        return index
    

    def upsert_documents(self, documents: List[dict], ids: List[str] = None):
        """insert single data raw into pinecone database with index"""
        try:
            upload_data = []
            for i, docs in enumerate(documents):
                docs["metadata"][self._text_key] = docs["text_content"]
                embeddings = self._embedding_function(docs["text_content"])
                upload_data.append(
                    {
                        "id": docs["id"],
                        "values": embeddings,
                        "metadata": docs["metadata"],
                    }
                )
            self._index.upsert(
                vectors=upload_data, batch_size=32
            )
            return ids
        except PineconeException as pinecone_issue:
            print(f"Pinecone: {pinecone_issue}")

    def delete_documents(self, ids: List[Union[str, int]], **kwargs):
        """delete one or more rows of date in pinecone database with given id(s)"""
        try:
            delete_ids = [str(_id) for _id in ids]
            return self._index.delete(ids=delete_ids, namespace=self._namespace)
        except PineconeException as pinecone_issue:
            print(f"Pinecone: {pinecone_issue}")
    def search_documents(
        self,
        query: str,
        top_k: int,
        book_ids: List[str] = None,
    ) -> List[Document]:
        """Search the pinecone database and retrieve relevant documents."""
        if book_ids is None:
            book_ids = []
        if book_ids:
            response = (
                self._index.fetch(ids=book_ids, namespace=self._namespace)
            ).to_dict()
            relevant_documents = self._format_fetch(response)
        else:
            relevant_documents = self.similarity_search(query, top_k)
        return relevant_documents

    def update_documents(self, docs: list[Document]):
        """Update one or more documents in the pinecone database."""
        raise NotImplementedError("pinecone update method implementation is pending")

    def _format_fetch(self, response_data: dict) -> List[Document]:
        res_keys = list(response_data["vectors"].keys())
        documents = []
        for key in res_keys:
            metadata = response_data["vectors"].get(key).get("metadata")
            if self._text_key in metadata:
                text = metadata.pop(self._text_key)
                documents.append(Document(page_content=text, metadata=metadata))

        return documents

    @staticmethod
    def _clean_metadata(relevant_documents: List[Document]) -> List[Document]:
        meta_fields = ["productDisplayName", "source_id", "tokens"]
        for doc in relevant_documents:
            doc.metadata = {x: doc.metadata.get(x, "") for x in meta_fields}
        return relevant_documents


pinecone = CustomPinecone(
    embedding_function=VectorDatabaseConstants.VECTOR_EMBEDDING.value.embed_query,
    text_key="text",
)
