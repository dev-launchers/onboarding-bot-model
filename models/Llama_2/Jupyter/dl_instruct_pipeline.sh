#!/bin/bash

file_url="https://huggingface.co/databricks/dolly-v2-3b/raw/main/instruct_pipeline.py"
local_file_name="instruct_pipeline.py"

# Téléchargez le fichier à l'aide de curl
curl -o "$local_file_name" "$file_url"