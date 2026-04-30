#!/bin/bash
set -e
echo "=== RAG Quality Gate ==="
echo "Running retrieval evaluation..."
python evaluate_retrieval.py --threshold 0.8 || { echo "FAILED: Precision below 0.8"; exit 1; }
echo "Running hallucination check..."
python hallucination_check.py --threshold 0.05 || { echo "FAILED: Hallucination rate above 5%"; exit 1; }
echo "All quality gates passed. Safe to deploy."
