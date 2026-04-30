-- Lab 2: Vector search with pgvector
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    metadata JSONB,
    embedding vector(384)
);

CREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops);

-- Insert example
-- INSERT INTO documents (content, embedding) VALUES ('example', '[0.1, 0.2, ...]');

-- Search
-- SELECT id, content, embedding <=> '[query vector]' AS distance
-- FROM documents ORDER BY distance LIMIT 5;
