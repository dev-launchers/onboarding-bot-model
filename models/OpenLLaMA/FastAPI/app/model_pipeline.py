import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

CACHE = "cache"
OFFLOAD = "offload"

tokenizer = AutoTokenizer.from_pretrained(CACHE, padding_side="left")
model = AutoModelForCausalLM.from_pretrained(CACHE, device_map="auto", torch_dtype=torch.bfloat16, offload_folder=OFFLOAD)


def generate_text_from(input_text):
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    return tokenizer.decode(outputs[0])