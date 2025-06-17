# University-Specific Retrieval-Augmented Generation (RAG) System

## Overview

This project investigates the design and implementation of a **Retrieval-Augmented Generation (RAG)** system tailored for managing academic and administrative queries within the Department of Data Science at Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU). 

By integrating document retrieval with the generative capabilities of Large Language Models (LLMs), the system enables accurate, contextually grounded responses using both public and private university-related data.

## Web Interface

The screenshots below demonstrate the query-to-answer flow in our RAG-based chatbot.

<p align="center">
  <img src="User enters query.png" alt="User enters query" width="80%"><br>
  <span style="font-size: 120px;">⬇️</span><br>
  <img src="System generates answer.png" alt="System generates answer" width="80%">
</p>

**Figure:** The user enters a question (top), and the system responds with an answer (bottom) retrieved and generated using university documents.

## Motivation

The Department of Data Science receives a high volume of student queries related to:
- **Admissions** (e.g., deadlines, eligibility, scholarships)
- **Academics** (e.g., course selection, prerequisites, exam schedules)

Much of this information is fragmented across university portals, while other details are only available through private email exchanges with Student Advisory. This results in:
- Delays and frustration for students
- Increased administrative burden on staff

The RAG chatbot aims to address both problems by offering an intelligent, centralized solution.

## Objectives

- **Design** a RAG-based chatbot system that integrates public (websites, PDFs) and private (anonymized emails) data sources.
- **Develop** a retrieval pipeline that efficiently indexes and fetches relevant information using vector-based search and contrastive learning.
- **Deploy** a generative model (LLM) to generate accurate and coherent responses grounded in retrieved content.
- **Evaluate** system performance using both manual inspection and automated metrics such as [RAGAS](https://huggingface.co/spaces/RAGAS/ragas-space).

## Project Structure

```
RAG_FULL_PROJECT_ALSO_PRIVATE_DATA_LATEST/
├── app/                            # FastAPI backend with UI
│   ├── api/                        # Full pipeline - From loading the documents, storing them and retrieving them
│   │   ├── __init__.py
│   │   └── queries.py              
│   ├── static/                     # Static files (CSS, images)
│   │   ├── logo.png
│   │   └── style.css
│   ├── templates/                  # HTML templates for UI
│   │   └── index.html
│   ├── utils/                      # Core logic for retrieval and processing
│   │   ├── __init__.py
│   │   ├── document_loader.py      # loading the document and do chunking and finally storing them in datastructure
│   │   ├── multi_query.py          # Multi-query logic
│   │   ├── rec_fusion.py           # RAG-fusion logic
│   │   └── vector_store.py         # Storing the retrieved document in vector store
│   ├── config.py                   # Application configuration
│   └── main.py                     # FastAPI app entry point
│
│
├── evaluation/                     # Performance evaluation notebooks
│   ├── Direct_query/               # Direct query evaluation
│   │   ├── ChatGPT_Nomic.ipynb     # using ChatGPT and Nomic Embeddings
│   │   ├── ChatGPT_OpenAI.ipynb    # using ChatGPT and OpenAI Embeddings
│   │   ├── llama3.1_Nomic.ipynb    # using Llama3.1 and Nomic Embeddings
│   │   ├── llama3.1_OpenAI.ipynb   # using Llama3.1 and OpenAI Embeddings
│   │   ├── llama3.3_Nomic.ipynb    # using Llama3.3 and Nomic Embeddings
│   │   └── llama3.3_OpenAI.ipynb   # using Llama3.3 and OpenAI Embeddings
│   │
│   ├── HyDE/                       # Hypothetical Document Expansion evaluation
│   │   ├── ChatGPT_Nomic.ipynb     # using ChatGPT and Nomic Embeddings
│   │   ├── ChatGPT_OpenAI.ipynb    # using ChatGPT and OpenAI Embeddings
│   │   ├── llama3.1_Nomic.ipynb    # using Llama3.1 and Nomic Embeddings
│   │   ├── llama3.1_OpenAI.ipynb   # using Llama3.1 and OpenAI Embeddings
│   │   ├── llama3.3_Nomic.ipynb    # using Llama3.3 and Nomic Embeddings
│   │   └── llama3.3_OpenAI.ipynb   # using Llama3.3 and OpenAI Embeddings
│   │
│   ├── Multi_query/                # Multi-query evaluation
│   │   ├── ChatGPT_Nomic.ipynb     # using ChatGPT and Nomic Embeddings
│   │   ├── ChatGPT_OpenAI.ipynb    # using ChatGPT and OpenAI Embeddings
│   │   ├── llama3.1_Nomic.ipynb    # using Llama3.1 and Nomic Embeddings
│   │   ├── llama3.1_OpenAI.ipynb   # using Llama3.1 and OpenAI Embeddings
│   │   ├── llama3.3_Nomic.ipynb    # using Llama3.3 and Nomic Embeddings
│   │   └── llama3.3_OpenAI.ipynb   # using Llama3.3 and OpenAI Embeddings
│   │
│   └── RAG_Fusion/                 # RAG Fusion evaluation
│       ├── ChatGPT_Nomic.ipynb     # using ChatGPT and Nomic Embeddings
│       ├── ChatGPT_OpenAI.ipynb    # using ChatGPT and OpenAI Embeddings
│       ├── llama3.1_Nomic.ipynb    # using Llama3.1 and Nomic Embeddings
│       ├── llama3.1_OpenAI.ipynb   # using Llama3.1 and OpenAI Embeddings
│       ├── llama3.3_Nomic.ipynb    # using Llama3.3 and Nomic Embeddings
│       └── llama3.3_OpenAI.ipynb   # using Llama3.3 and OpenAI Embeddings
│
├── Dockerfile                      # For containerizing the application
└── requirements.txt                # Python dependencies
```
## Significance

This project contributes a scalable AI-based academic assistant that:
- Reduces response time for common student queries
- Lowers administrative workload
- Enhances overall student experience

It also serves as a blueprint for extending RAG systems to other university departments or academic institutions.
