[↖️ Back to main](../README.md)

# Langchains

## Table of Contents

- [Overview](#overview)
- [Competition](#competition)
- [Structure](#structure)

...

## Overview

[Retrieval](https://python.langchain.com/docs/modules/data_connection/) 

![Pipeline (Load, split, embed, store, retrieval)](https://python.langchain.com/assets/images/data_connection-95ff2033a8faa5f3ba41376c0f6dd32a.jpg)

## Competition

1. [Load](https://python.langchain.com/docs/integrations/document_loaders) and [transform](https://python.langchain.com/docs/integrations/document_transformers)

| Statut |   Type                                            | Method |
|--------|---------------------------------------------------|--------|
| ✅     | [Markdown](langchains/extract_from/readme_urls/)  | URL    |
| ✅     | [Markdown](langchains/extract_from/readme_files/) | Files  |
| 🔜     | Python                                            |        |
|        |                                                   |        |

2. Split

| Statut |   Type                                              | Info |
|--------|-----------------------------------------------------|------|
| ✅     | [Markdown](langchains/documents_from/readme_files/) | [Info](https://python.langchain.com/docs/modules/data_connection/document_transformers/markdown_header_metadata) |
| 🔜     | Python                                              | |
|        |                                                     | |

3. [Embed](https://python.langchain.com/docs/integrations/text_embedding)

| Statut | Name                                                    | Info |
|--------|---------------------------------------------------------|------|
| ✅     | [Awadb](langchains/documents_from/readme_files/)        | [Info](https://python.langchain.com/docs/integrations/text_embedding/awadb) |
| ✅     | [Hugging Face](langchains/documents_from/readme_files/) | [Info](https://python.langchain.com/docs/integrations/text_embedding/huggingfacehub) |
|        |                                                         | |

4. [Store](https://python.langchain.com/docs/integrations/vectorstores)

| Statut | Name                                                | Info |
|--------|-----------------------------------------------------|------|
| ✅     | [Annoy](langchains/documents_from/readme_files/)        | [Info](https://python.langchain.com/docs/integrations/vectorstores/annoy) |
| ✅     | [Awadb](langchains/documents_from/readme_files/)        | [Info](https://python.langchain.com/docs/integrations/vectorstores/awadb) |
| ✅     | [Chroma](langchains/documents_from/readme_files/)        | [Info](https://python.langchain.com/docs/integrations/vectorstores/chroma) |
| ✅     | [FAISS](langchains/documents_from/readme_files/)        | [Info](https://python.langchain.com/docs/integrations/vectorstores/faiss) |
| ✅     | [LanceDB](langchains/documents_from/readme_files/)        | [Info](https://python.langchain.com/docs/integrations/vectorstores/lancedb) |
| 🔜     | Pinecone                                             | [Info](https://python.langchain.com/docs/integrations/vectorstores/pinecone) |
| ✅     | [Qdrant](langchains/documents_from/readme_files/)        | [Info](https://python.langchain.com/docs/integrations/vectorstores/qdrant) |
| ✅     | [scikit-learn](langchains/documents_from/readme_files/)        | [Info](https://python.langchain.com/docs/integrations/vectorstores/sklearn) |
| ✅     | [TileDB](langchains/documents_from/readme_files/)        | [Info](https://python.langchain.com/docs/integrations/vectorstores/tiledb) |
| ✅     | [USearch](langchains/documents_from/readme_files/)        | [Info](https://python.langchain.com/docs/integrations/vectorstores/usearch) |
| 🔜     | [vearch](langchains/documents_from/readme_files/)        | [Info](https://python.langchain.com/docs/integrations/vectorstores/vearch) |
|        |                                                         | |

## Structure

...