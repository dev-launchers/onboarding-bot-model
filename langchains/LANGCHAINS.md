[↖️ Back to main](../README.md)

# Langchains

## Table of Contents

- [Overview](#overview)
- [Structure](#structure)

## Overview

[Retrieval](https://python.langchain.com/docs/modules/data_connection/) 

![Pipeline (Load, transfrom, embed, store, retrieve)](https://python.langchain.com/assets/images/data_connection-95ff2033a8faa5f3ba41376c0f6dd32a.jpg)

Pipeline : ([Load](https://python.langchain.com/docs/integrations/document_loaders),
            [transfrom](https://python.langchain.com/docs/integrations/document_transformers),
            [embed](https://python.langchain.com/docs/integrations/text_embedding), 
            [store](https://python.langchain.com/docs/integrations/vectorstores), 
            [retrieve](https://python.langchain.com/docs/modules/data_connection/retrievers/))

## Structure

The [load](./load/) folder contains different document loaders.

The [transfrom](./transform/) folder contains functions for split documents in chunks.

The [embed](./embed/) folder contains the function for capture the semantic meaning of the texts.

The [store](./store/) folder contains the database to support efficient storage and searching of these embeddings.

The [retrieve](./retrieve/) folder contains the fonction for be abble to do semantic search.


## **interesting link for airflow update vector store**

* [Indexation](https://python.langchain.com/docs/modules/data_connection/indexing)