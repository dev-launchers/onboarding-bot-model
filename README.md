# Onboarding Bot Model

## Table of Contents

- [Overview](#overview)
- [Team](#team)
- [Structure](#structure)
    - [Models](#models)
    - [Langchains](#langchains)
- [Installation](#installation)
    - [Notebook](#notebook)
    - [Informations](#Informations)
- [License](#license)

## Overview

The [Dev Launchers](https://devlaunchers.org) website is a community of aspiring developers eager to learn and gain experience. As such, projects are [open-source](https://en.wikipedia.org/wiki/Open_source) and ambitious, allowing members to enhance their skills.

The [ChatBot](https://en.wikipedia.org/wiki/Chatbot) project is valuable to this international community working across different time zones. To integrate a new member, it is crucial to be able to address their questions. This becomes challenging when the part of the community capable of responding is located 12 time zones away from the new member. Therefore, it was essential to have a service capable of answering questions, even in the middle of the night.

The purpose of this project is to design an intelligent chatbot, entirely built with open-source components, to answer questions about the teams and projects of an organization. We strive to understand how the different layers of a [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) [Langchain](https://python.langchain.com/docs/get_started/introduction) work in order to design code that strikes a balance between readability and the performance of the frameworks used.

## Team

If you've joined Dev Launchers, you've learned that participating in an online project means forgetting earthly boundaries and adopting the true international borders: [UTC & GMT](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

To assist this team, information is available about their roles and locations in this [Notebook](TEAM.ipynb) (If you're unable to read this file, refer to the [Installation](#installation) chapter of this [Markdown](https://en.wikipedia.org/wiki/Markdown)).

## Structure

The subfolders listed below contain key steps in our research for creating a functional, convenient, and maintainable chatbot.

### Models 

The [models](models/MODELS.md) folder contains open-source [LLMs](https://en.wikipedia.org/wiki/Large_language_model).

### Langchains 

The [langchains](langchains/LANGCHAINS.md) folder contains [components](https://python.langchain.com/docs/integrations/components) of the langchain [pipeline](https://en.wikipedia.org/wiki/Instruction_pipelining).

## Installation

### Notebook

For read Notebooks on the Mac.

On Mac, open the terminal, copy and paste the following line of code. Then, press the Enter key (↩︎) to execute:
```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && brew install python && brew install jupyter && (pip install folium || pip3 install folium)
```
After installing the necessary tools, most people read their notebooks using [Visual Studio Code](https://code.visualstudio.com).

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

## License

[MIT License](LICENSE.md)

Copyright (c) [2024] [Dev Launchers]