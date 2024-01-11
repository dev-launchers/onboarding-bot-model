# Onboarding Bot Model

## Table of Contents

- [Overview](#overview)
- [Scenario](#scenario)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Files](#files)
- [External Help links](#external-help-links)
- [License](#license)

## Overview

The [Dev Launchers](https://devlaunchers.org) website is a community of aspiring developers eager to learn and gain experience. As such, projects are open-source and ambitious, allowing members to enhance their skills.

The [ChatBot](https://en.wikipedia.org/wiki/Chatbot) project is valuable to this international community working across different time zones. To integrate a new member, it is crucial to be able to address their questions. This becomes challenging when the part of the community capable of responding is located 12 time zones away from the new member. Therefore, it was essential to have a service capable of answering questions, even in the middle of the night.

## Scenario

1. 🕒 Development of the current [chatbot](https://github.com/dev-launchers/onboarding-bot) by the team, utilizing the [ChatGPT API](https://platform.openai.com/docs/api-reference).
2. 🕒 Feasibility study using a list of popular Open Source LLMs of 2023.

| 🐳 | Competitor | Statut    | GitHub          | Hugging Face    | Info    |
|----|------------|-----------|-----------------|-----------------|---------|
| 🚼 | [Llama 2](models/Llama_2/)     | In progress |                                                            | [Model](https://huggingface.co/meta-llama/Llama-2-7b) | |
| ✅ | [OpenLLaMA](models/OpenLLaMA/) | Ready       | [Code](https://github.com/openlm-research/open_llama)      | [Model](https://huggingface.co/openlm-research/open_llama_7b) | |
| 🚼 | [Falcon](models/Falcon/)       | In progress |                                                            | [Model](https://huggingface.co/tiiuae/falcon-7b) | |
| ✅ | [Dolly 2.0](models/Dolly_2/)   | Ready       | [Code](https://github.com/databrickslabs/dolly)            | [Model](https://huggingface.co/databricks/dolly-v2-12b) | |
| ✅ | [MPT](models/MPT/)             | Ready       | [Code](https://github.com/mosaicml/llm-foundry/)           | [Model](https://huggingface.co/mosaicml/mpt-30b) | |
| 🚼 | [Guanaco](models/Guanaco/)     | In progress | [Code](https://github.com/artidoro/qlora/)                 | | |
| 🚼 | [Bloom](models/Bloom/)         | In progress | [Code](https://github.com/bigscience-workshop/xmtf#models) | [Model](https://huggingface.co/bigscience/bloom) | |
| ✅ | [Alpaca](models/Alpaca/)       | Ready       | [Code](https://github.com/tatsu-lab/stanford_alpaca)       | [Model](https://huggingface.co/tatsu-lab/alpaca-7b-wdiff) | |
| 🚼 | [GPT NeoXT](models/GPT_NeoXT/) | In progress | [Code](https://github.com/togethercomputer/OpenChatKit/blob/main/docs/GPT-NeoXT-Chat-Base-20B.md) | [Model](https://huggingface.co/togethercomputer/GPT-NeoXT-Chat-Base-20B) |         |
| 🆘 | [GPT4All](models/GPT4All/)     | Unstartable | [Code](https://github.com/nomic-ai/gpt4all)                | | |
| ✅ | [FLAN-T5](models/FLAN_T5/)     | Ready       | [Code](https://github.com/lm-sys/FastChat)                 | [Model](https://huggingface.co/google/flan-t5-base) | |
| 🚼 | [WizardLM](models/WizardLM/)   | In progress | [Code](https://github.com/nlpxucan/WizardLM)               | [Model](https://huggingface.co/WizardLM) | |
| 🆘 | [Mistral](models/Mistral/)     | Unstartable |                                                            | [Model](https://huggingface.co/mistralai) | [Documentation](https://docs.mistral.ai/quickstart) |
|    |                                |             |                                                            | | |

3. 📝 Compile and rewrite the readme.md files, procedures, create team descriptions, and consolidate documentation for the tools used.
4. 📝 Comparison of results with [MLflow](https://mlflow.org).
5. 📝 [Fine-Tuning](https://huggingface.co/docs/transformers/training) of the chosen model(s).
6. 📝 Testing within the [Dev Launchers](https://devlaunchers.org) community.

## Installation

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

## Usage

You can try out the different pre-installed language models in the subfolders named after them in the `models` directory.

## Dependencies

- The project is implemented in `Python 3.11.6`.
- All dependencies are include in `requirements.txt` files.

### Informations

To obtain the list of installed libraries on the Mac.

On Mac, open the terminal and type:
```shell
cd
```
Drag the **`folder`** where you want to create the file `config_mac.txt`, then press the Enter key (↩︎).

Execute the following line of code by pressing the Enter key (↩︎):

```shell
pip3 freeze > config_mac.txt
```

## Files

- models\name\FastAPI\\`autorun.sh`: Launch script for download, install and start the application.
- models\name\FastAPI\\`Dockerfile`: Contains all the commands a user could call on the command line to assemble the image.
- models\name\FastAPI\\`requirements.txt`: The libraries required for the script.
- models\name\FastAPI\app\\`main.py`: The script of the web application.

## External Help links

* [ChatBot Llama](https://blog.streamlit.io/how-to-build-a-llama-2-chatbot/)
    * [ChatBot Llama Exemple](https://llama2.streamlit.app)

* [ChatBot Streamlit](https://github.com/streamlit/llm-examples/tree/main)
    * [ChatBot Streamlit Exemple](https://llm-examples.streamlit.app)

* [ChatGPT API](https://platform.openai.com/docs/introduction)
    * [fine-tuning Chat-GPT](https://platform.openai.com/docs/guides/fine-tuning)

## License

MIT License

Copyright (c) [2023] [Dev Launchers]