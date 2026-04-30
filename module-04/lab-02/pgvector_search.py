"""Lab 2: pgvector search with Python."""
import psycopg2
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

# conn = psycopg2.connect("postgresql://user:pass@localhost/ragdb")
# cur = conn.cursor()
# query_vec = model.encode("deploy python app").tolist()
# cur.execute("SELECT content, embedding <=> %s::vector AS dist FROM documents ORDER BY dist LIMIT 5", (str(query_vec),))
print("See pgvector_setup.sql for schema, then use this script to query.")
