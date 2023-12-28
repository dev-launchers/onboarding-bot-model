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

1. Creation based on the [ChatGPT API](https://platform.openai.com/docs/api-reference).
2. Feasibility study using a list of 13 popular Open Source LLMs of 2023.
    * 🆕 [Llama 2](https://huggingface.co/meta-llama/Llama-2-7b)
    * 🆕 [OpenLLaMA](https://huggingface.co/openlm-research/open_llama_7b) ([GitHub project](https://github.com/openlm-research/open_llama))
    * 🚼 [Falcon](https://huggingface.co/tiiuae/falcon-7b)
    * ✅ [Dolly 2.0](https://huggingface.co/databricks/dolly-v2-12b) ([GitHub project](https://github.com/databrickslabs/dolly))
    * 🆕 [MPT](https://huggingface.co/mosaicml/mpt-30b) ([GitHub project](https://github.com/mosaicml/llm-foundry/))
    * 🆕 Guanaco ([GitHub project](https://github.com/artidoro/qlora))
    * 🚼 [Bloom](https://huggingface.co/bigscience/bloom) ([GitHub project](https://github.com/bigscience-workshop/xmtf#models))
    * 🆕 Stanford Alpaca ([GitHub project](https://github.com/tatsu-lab/stanford_alpaca))
    * 🆕 OpenChatKit ([GitHub project](https://github.com/togethercomputer/OpenChatKit)) ([database](https://github.com/togethercomputer/OpenDataHub))
    * 🆕 GPT4All ([GitHub project](https://github.com/nomic-ai/gpt4all))
    * ✅ [FLAN-T5](https://huggingface.co/google/flan-t5-base) ([GitHub project](https://github.com/lm-sys/FastChat))
    * 🆕 [WizardLM](https://huggingface.co/WizardLM) ([GitHub project](https://github.com/nlpxucan/WizardLM))
    * 🆕 [Mistral](https://huggingface.co/mistralai) ([Documentation](https://docs.mistral.ai/quickstart))
    * _✅ Good ; 🚼 bad first attempt ; 🆘 unstartable ; 🆕 to try_

3. Comparison of results with [MLflow](https://mlflow.org).
4. [Fine-Tuning](https://huggingface.co/docs/transformers/training) of the chosen model(s).
5. Testing within the [Dev Launchers](https://devlaunchers.org) community.

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