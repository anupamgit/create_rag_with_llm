# Vector DB-Based RAG with Local LLM

This project demonstrates a simple use of a vector database (Qdrant) for Retrieval-Augmented Generation (RAG) with a language model.

## Overview
- **Modular Code**: Simple and easy to understand.
- **Vector DB**: Uses Qdrant for an in-memory vector database.
- **Encoding**: Utilizes `sentence_transformers` for encoding.

## Prerequisites

### Using OpenAI API
1. Set up an OpenAI account and obtain your API key from [OpenAI API Keys](https://platform.openai.com/account/api-keys).
2. Create a `.env` file in the project directory and add your API key:
    ```plaintext
    OPENAI_API_KEY=your-api-key-here
    ```

### Using Local Model
1. Download a model (e.g., TinyLlama-1.1B-Chat-v1.0.F16.llamafile) from [Mozilla Ocho GitHub](https://github.com/Mozilla-Ocho/llamafile).
2. Run the model locally to serve chat requests on `http://localhost:8080`. You can do this by navigating to the directory containing the model file and executing:
    ```bash
    ./TinyLlama-1.1B-Chat-v1.0.F16.llamafile
    ```

## Running the Project
Execute the following command:
```bash
TOKENIZERS_PARALLELISM=false python<your-version> main.py
```
Setting TOKENIZERS_PARALLELISM to false will avoid some warnings when running locally, depending on your model.

## Note
This is not production-level code and users are encouraged to update it as needed.

## Credits
This project is highly influenced with the concepts discussed in [learn-retrieval-augmented-generation](https://github.com/alfredodeza/learn-retrieval-augmented-generation) and is its refactored version.
