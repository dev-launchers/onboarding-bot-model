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

### Information

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

### Run locally
To run the bot locally, please make sure to have these applications downloaded locally:

- git
- docker
- Linux wsl (If on windows)

Next, you should create a folder somewhere in your system to download the front-end and back-end source code

.

└── Bot<br>
&emsp;├── Front-End<br>
&emsp;└── Back-End

Download the frontend branch and backend from these two branched:

Frontend (devlaunchers staging/gptbot):

```shell
!git clone https://github.com/dev-launchers/dev-launchers-platform.git
```

Backend (devlaunchers onboarding-bot):

```shell
!git clone https://github.com/dev-launchers/onboarding-bot.git
```

(Note: The frontend will be running on port 3000, and the backend will be running on port 5000. These are local ports.)


Now, we can setup the backend.

In order to set up and deploy the backend in a testing environment, you must make sure that docker is installed and running. The docker image which will be created will take up about 9GB worth of storage on your system. First, you must enter the key in the .env file. If you have an Openai key to use, replace “INSERT KEY HERE” with your openai key. Now that you have your key all set up, we can now create the docker image. Make sure to insert the key without quotes.

In order to create the image, enter this command in the directory of the onboarding-bot repo (It can be any name you give it):

```shell
!docker build -t flaskserver .
```

This will initiate a container from the image (You can change “flaskTest1” to whatever name you want for the container)

```shell
!docker run --env-file ./.env --name=flaskTest1 -p=5000:5000 flaskserver
```

Now that your docker image is up and running, test it by typing the command in your terminal:

```shell
(Windows) curl -X POST -d "string=hello" http://localhost:5000/question
```
```shell
(Linux) wget --post-data="string=hello" http://localhost:5000/question
```

It should respond back to your prompt. If it works, then you are ready to move onto the frontend. If not, check your API key and make sure it is not incorrect.

To set up the front-end, nagivate to the front-end file and type these commands in:

```shell
!yarn
```
```shell
!yarn install
```
```shell
!yarn workspace @devlaunchers/app dev
```

You should then be able to navigate to http://localhost:3000/gptbot

There, you can test out the onboarding bot from the front-end design!

## License

[MIT License](LICENSE.md)

Copyright (c) [2024] [Dev Launchers]
