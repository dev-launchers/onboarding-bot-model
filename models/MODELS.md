[↖️ Back to main](../README.md)

# Models

## Table of Contents

- [Overview](#overview)
- [Competition](#competition)
- [Structure](#structure)
    - [Jupyter](#jupyter)
    - [Streamlit](#streamlit)
    - [FastAPI](#fastapi)
- [Installation](#installation)
    - [Jupyter Notebook](#jupiter-notebook)
    - [Streamlit & FastAPI](#streamlit--fastapi)

## Overview

Development of the current [chatbot](https://github.com/dev-launchers/onboarding-bot) by the team, utilizing the [ChatGPT API](https://platform.openai.com/docs/api-reference).

The [models](../models) folder contains open-source [LLMs](https://en.wikipedia.org/wiki/Large_language_model) are being tested with the aim of including the best among them in the [RAG](../langchains/LANGCHAINS.md) we are going to set up. You can try out the different pre-installed language models in the subfolders named after them in the `models` directory.

## Competition

Feasibility study using a list of popular Open Source LLMs.

| 🐳 | 🦜 | Competitor | Statut    | GitHub          | Hugging Face    |
|----|----|------------|-----------|-----------------|-----------------|
| ✅ | 🔜 | [Open LLaMA](OpenLLaMA/) | Ready       | [Code](https://github.com/openlm-research/open_llama)      | [Model](https://huggingface.co/openlm-research/open_llama_7b) |
| ✅ | ✅ | [Dolly 2.0](Dolly_2/)    | Ready       | [Code](https://github.com/databrickslabs/dolly)            | [Model](https://huggingface.co/databricks/dolly-v2-12b) |
| ✅ | 🔜 | [MPT](MPT/)              | Ready       | [Code](https://github.com/mosaicml/llm-foundry/)           | [Model](https://huggingface.co/mosaicml/mpt-30b) |
| ✅ | 🔜 | [Alpaca](Alpaca/)        | Ready       | [Code](https://github.com/tatsu-lab/stanford_alpaca)       | [Model](https://huggingface.co/tatsu-lab/alpaca-7b-wdiff) |
| ✅ | 🔜 | [FLAN-T5](FLAN_T5/)      | Ready       | [Code](https://github.com/lm-sys/FastChat)                 | [Model](https://huggingface.co/google/flan-t5-base) |
| 🚼 | 🔜 | [Llama 2](Llama_2/)      | In progress |                                                            | [Model](https://huggingface.co/meta-llama/Llama-2-7b) |
| 🚼 | 🔜 | [Falcon](Falcon/)        | In progress |                                                            | [Model](https://huggingface.co/tiiuae/falcon-7b) |
| 🚼 | 🔜 | [Guanaco](Guanaco/)      | In progress | [Code](https://github.com/artidoro/qlora/)                 | |
| 🚼 | 🔜 | [Bloom](Bloom/)          | In progress | [Code](https://github.com/bigscience-workshop/xmtf#models) | [Model](https://huggingface.co/bigscience/bloom) |
| 🚼 | 🔜 | [GPT NeoXT](GPT_NeoXT/)  | In progress | [Code](https://github.com/togethercomputer/OpenChatKit/blob/main/docs/GPT-NeoXT-Chat-Base-20B.md) | [Model](https://huggingface.co/togethercomputer/GPT-NeoXT-Chat-Base-20B) |        
| 🚼 | 🔜 | [WizardLM](WizardLM/)    | In progress | [Code](https://github.com/nlpxucan/WizardLM)               | [Model](https://huggingface.co/WizardLM) |
| 🆘 | 🔜 | [GPT4All](GPT4All/)      | Unstartable | [Code](https://github.com/nomic-ai/gpt4all)                | |
| 🆘 | 🔜 | [Mistral](Mistral/)      | Unstartable |                                                            | [Model](https://huggingface.co/mistralai) |
|    |    |                                 |             |                                                            | |

## Structure

The following subfolders present the steps for validating a model used locally, interfaced, and then in a container without errors. We take [Dolly 2](Dolly_2/) as an example, which is functioning correctly.

### Jupyter

The [Jupyter](Dolly_2/Jupyter) folder contains the open-source LLMs tested on local machine.

### Streamlit

The [Streamlit](Dolly_2/Streamlit) folder contains the same model in a user-friendly interface.

### FastAPI

The [FastAPI](Dolly_2/FastAPI) folder completes this process by automating the installation of the model in a Dockerized API, making it usable in production.

## Installation

### Jupiter Notebook

For read Jupiter on the Mac, follow the same instruction as [Notebook](../README.md#notebook).

### Streamlit & FastAPI

The chatbots are in their respective folders with an application launcher `autorun.sh` to install each of them without specific knowledge.

On Mac, open the terminal and type:
```shell
cd
```
Drag the **`folder`** containing the file `autorun.sh`, then press the Enter key (↩︎).

_If you have done it correctly, the **`~`** between your machine's name (`name@MacBook-Pro-of-Name`) and the **`%`** sign should display the name of the `folder` instead._

Execute the following line of code by pressing the Enter key (↩︎):
```shell
sh autorun.sh
```
Wait a moment, the model should open in your default web browser.