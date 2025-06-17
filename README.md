# University-Specific Retrieval-Augmented Generation (RAG) System

## Overview

This project investigates the design and implementation of a **Retrieval-Augmented Generation (RAG)** system tailored for managing academic and administrative queries within the Department of Data Science at Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU). 

By integrating document retrieval with the generative capabilities of Large Language Models (LLMs), the system enables accurate, contextually grounded responses using both public and private university-related data.

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

## System Components

- **Document Loader**: Ingests and preprocesses university PDFs, websites, and emails.
- **Embedding Model**: Converts text to vectors using state-of-the-art models (e.g., OpenAI or Nomic).
- **Vector Store**: Stores embeddings for efficient similarity search using FAISS.
- **Retriever**: Uses Dense Passage Retrieval or Hybrid Retrieval techniques to fetch relevant chunks.
- **Generator (LLM)**: Synthesizes final answers from the retrieved context using models like LLaMA 3.1 or GPT-4o-mini.
- **Evaluation**: Utilizes Retrieval-Augmented Generation Assessment (RAGAS) to evaluate precision, groundedness, and relevance.

## Example Use Cases

- **"What is the application deadline for Winter 2025?"**
- **"Can I enroll in this course as a minor?"**
- **"What documents are required for enrollment?"**

## Data Sources

- **Public**: FAU departmental websites, module handbooks, academic policy PDFs.
- **Private**: Anonymized student emails and official advisory responses.

⚠️ All private data is handled with strict adherence to privacy and security regulations (GDPR-compliant).

## Significance

This project contributes a scalable AI-based academic assistant that:
- Reduces response time for common student queries
- Lowers administrative workload
- Enhances overall student experience

It also serves as a blueprint for extending RAG systems to other university departments or academic institutions.

## License

For academic and research use only. Contact the author for reuse permissions.

## Author

**Ekaansh Khosla**  
M.Sc. Data Science, FAU Erlangen-Nürnberg  
Email: ekaanshkhosla007@gmail.com

---
