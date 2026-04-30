"""Lab 1: OpenTelemetry tracing for RAG pipeline."""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

provider = TracerProvider()
provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(provider)
tracer = trace.get_tracer("rag-service")

def rag_with_tracing(question):
    with tracer.start_as_current_span("rag_pipeline"):
        with tracer.start_as_current_span("embed_query"):
            pass  # embedding logic
        with tracer.start_as_current_span("retrieve"):
            pass  # retrieval logic
        with tracer.start_as_current_span("generate"):
            pass  # LLM call
    return "answer"

rag_with_tracing("test question")
