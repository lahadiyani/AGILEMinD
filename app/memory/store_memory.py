from memory.base_memory import BaseMemory
from typing import List, Tuple
import psycopg2
import psycopg2.extras
import uuid
import datetime

class InMemoryBuffer(BaseMemory):
    def __init__(self, max_len=100):
        self.buffer = []
        self.max_len = max_len

    def add(self, role, content, metadata):
        self.buffer.append((role, content, metadata))
        if len(self.buffer) > self.max_len:
            self.buffer.pop(0)

    def retrieve(self, query, limit=10):
        return self.buffer[-limit:]

    def clear(self):
        self.buffer.clear()


class PostgresMemory(BaseMemory):
    def __init__(self, dsn: str, namespace: str = "default"):
        self.conn = psycopg2.connect(dsn)
        self.ns = namespace
        self._init_table()

    def _init_table(self):
        with self.conn.cursor() as c:
            c.execute(f"""
                CREATE TABLE IF NOT EXISTS memory (
                    id UUID PRIMARY KEY,
                    namespace TEXT,
                    role TEXT,
                    content TEXT,
                    metadata JSONB,
                    created_at TIMESTAMP DEFAULT NOW()
                );
            """)
            self.conn.commit()

    def add(self, role, content, metadata):
        with self.conn.cursor() as c:
            c.execute("""
                INSERT INTO memory (id, namespace, role, content, metadata)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                str(uuid.uuid4()), self.ns, role, content, psycopg2.extras.Json(metadata)
            ))
            self.conn.commit()

    def retrieve(self, query: str, limit: int = 10):
        with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
            c.execute("""
                SELECT role, content, metadata
                FROM memory
                WHERE namespace = %s
                ORDER BY created_at DESC
                LIMIT %s
            """, (self.ns, limit))
            results = c.fetchall()
        return [(r["role"], r["content"], r["metadata"]) for r in results]

    def clear(self):
        with self.conn.cursor() as c:
            c.execute("DELETE FROM memory WHERE namespace = %s", (self.ns,))
            self.conn.commit()
