# Vector DB-Based RAG with Local LLM

This project demonstrates a simple use of a vector database (Qdrant) for Retrieval-Augmented Generation (RAG) with a local language model (TinyLlama).

## Overview
- **Modular Code**: Simple and easy to understand.
- **Vector DB**: Uses Qdrant for an in-memory vector database.
- **Encoding**: Utilizes `sentence_transformers` for encoding.

## Prerequisites
1. Download a model (e.g., TinyLlama-1.1B-Chat-v1.0.F16.llamafile) from [Mozilla Ocho GitHub](https://github.com/Mozilla-Ocho/llamafile).
2. Run the model locally to serve chat requests on `http://localhost:8080`.

## Running the Project
Execute the following command:
```bash
TOKENIZERS_PARALLELISM=false python<your-version> main.py
```

## Note
This is not production-level code and users are encouraged to update it as needed.

## Credits
This project is highly influenced with the concepts discussed in [learn-retrieval-augmented-generation](https://github.com/alfredodeza/learn-retrieval-augmented-generation) and is its refactored version.
