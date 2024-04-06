[↖️ Back to main](../README.md)

# Langchains

## Table of Contents

- [Overview](#overview)
- [Structure](#structure)

## Overview
### [LLM](https://youtu.be/zizonToFXDs?si=JeXqRIGJDaYDtacE)

A [LLM](https://youtu.be/zizonToFXDs?si=JeXqRIGJDaYDtacE), or Large Language Model, is an artificial intelligence algorithm capable of providing responses by interpolating millions of documents integrated into its memory.

### [Retrieval](https://python.langchain.com/docs/modules/data_connection/)

To communicate a source of documentation with a language model, it is necessary to standardize it for communication. This is illustrated in the following graph.

![Pipeline (Load, transform, embed, store, retrieve)](https://python.langchain.com/assets/images/data_connection-95ff2033a8faa5f3ba41376c0f6dd32a.jpg)

The Pipeline consists of a sequence of processes necessary to create our database that can communicate with our artificial intelligence:

- **[Load](https://python.langchain.com/docs/integrations/document_loaders):** From sources such as the association's website, its GitHub account, its databases, etc., scripts download files that will be used as references to formulate the AI's responses to user questions.

- **[Transform](https://python.langchain.com/docs/integrations/document_transformers):** All downloaded documents have different formats, whether they are manuals in markdown, PDF articles, HTML pages, and many more. The purpose of transformation is to standardize all these formats to extract indexed paragraphs. It is interesting to note that the length of paragraphs is limited (chunk), and they slightly overlap in this specific case.

- **[Embed](https://python.langchain.com/docs/integrations/text_embedding):** We have chosen an encoder based on [Bert](https://youtu.be/t45S_MwAcOw?si=mltl_21ijp_rqijO). Before this encoder, the Google search engine worked with keywords, but now it works with clusters of words forming expressions/contexts. So "my four-legged companion" and "man's best friend" will be closer than "Sick as a dog" and "You can't teach an old dog new tricks" even though both contain `Dog`. In essence, embedding translates sentences into coordinates in the multiverse.

- **[Store](https://python.langchain.com/docs/integrations/vectorstores):** A VectorStore database is optimized to contain paragraphs, the metadata attached to them, and their translation into coordinates (vectors). The functions to call the rows are also adapted to this new content.

- **[Retrieve](https://python.langchain.com/docs/modules/data_connection/retrievers/):** The Retriever is simply the vessel function to navigate our multidimensional universe.

### RAG

RAG stands for Retrieval Augmented Generation. After asking a question to RAG, three things happen:
1. Your question goes through the Retriever and is compared to the vector database to find the lines with the context closest to your question.
2. The lines and your question are combined into a prompt. For example: Answer `{question}` using only `{context}`.
3. The prompt is sent to the LLM and obtains a response.

The LLM, having the answer in the question, only reformulates and requires little general knowledge. This is the entire advantage of a RAG, which can work with a lightweight and economical language model. Artificial intelligence is an abuse of language; keep in mind that it is vulgarly an algorithm for text interpolation.

## Structure

### Retrieval

The [load](./load/) folder contains different document loaders.

The [transfrom](./transform/) folder contains functions for split documents in chunks.

The [embed](./embed/) folder contains the function for capture the semantic meaning of the texts.

The [store](./store/) folder contains the database to support efficient storage and searching of these embeddings.

The [retrieve](./retrieve/) folder contains the fonction for be abble to do semantic search.

### RAG

The [chain](./chain/) folder contains the fonction for chain who allows for retrieving the document corpus, conversation history, user question, and sending all of this to a LLM that returns an answer.


## **interesting link for airflow update vector store**

* [Indexation](https://python.langchain.com/docs/modules/data_connection/indexing)