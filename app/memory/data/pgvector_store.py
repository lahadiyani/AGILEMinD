# app/memory/data/pgvector_store.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from pgvector.sqlalchemy import Vector
import numpy as np

Base = declarative_base()

class VectorDocument(Base):
    __tablename__ = "vector_documents"

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    embedding = Column(Vector(768))  # ubah dimensi sesuai embedding

class PGVectorStore:
    def __init__(self, db_url: str = "postgresql+psycopg://user:pass@localhost/dbname"):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_documents(self, docs: list[dict]):
        """
        docs = [{'content': str, 'embedding': np.ndarray}]
        """
        session = self.Session()
        for doc in docs:
            session.add(VectorDocument(
                content=doc['content'],
                embedding=doc['embedding'].tolist()
            ))
        session.commit()
        session.close()

    def similarity_search(self, query_embedding: np.ndarray, top_k=5):
        session = self.Session()
        results = session.query(VectorDocument).order_by(
            VectorDocument.embedding.cosine_distance(query_embedding.tolist())
        ).limit(top_k).all()
        session.close()
        return [{"content": r.content, "score": None} for r in results]
