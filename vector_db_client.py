from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer


class VectorDBClient:
    def __init__(self, collection_name):
        self.encoder = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )  # Model to create embeddings
        self.collection_name = collection_name
        self.qdrant = QdrantClient(":memory:")
        self.qdrant.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=models.VectorParams(
                size=self.encoder.get_sentence_embedding_dimension(),
                distance=models.Distance.COSINE,
            ),
        )

    def upload_data(self, data, relevant_column):
        self.qdrant.upload_points(
            collection_name=self.collection_name,
            points=[
                models.PointStruct(
                    id=idx,
                    vector=self.encoder.encode(doc[relevant_column]).tolist(),
                    payload=doc,
                )
                for idx, doc in enumerate(data)
            ],
        )

    def search(self, user_prompt, top_k=5):
        search_result = self.qdrant.search(
            collection_name=self.collection_name,
            query_vector=self.encoder.encode(user_prompt).tolist(),
            limit=top_k,
        )
        return search_result


# Based on https://github.com/alfredodeza/learn-retrieval-augmented-generation/blob/main/examples/3-applied-rag/embeddings.ipynb
