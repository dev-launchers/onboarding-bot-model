#!/bin/bash

file_url="https://github.com/huggingface/transformers/blob/v4.37.2/src/transformers/pipelines/__init__.py#L531"
local_file_name="instruct_pipeline.py"

# Download the file using curl
curl -o "$local_file_name" "$file_url"
