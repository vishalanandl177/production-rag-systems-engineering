# Production RAG Platform — Capstone

Build the complete enterprise RAG platform:

```bash
docker compose up -d          # Start infrastructure
python ingest.py              # Ingest documents
python api.py                 # Start RAG API
python evaluate.py            # Run quality evaluation
python load_test.py           # Load test with locust
```

## Components
1. Document ingestion pipeline
2. Qdrant with hybrid search + reranking
3. FastAPI with streaming + caching
4. AI agents with tool calling
5. Hallucination detection
6. OpenTelemetry observability
7. Prompt injection defense
8. Kubernetes deployment
