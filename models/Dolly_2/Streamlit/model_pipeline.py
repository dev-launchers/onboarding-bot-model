import torch
from instruct_pipeline import InstructionTextGenerationPipeline
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-3b", padding_side="left")
model = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-3b", device_map="auto", torch_dtype=torch.bfloat16, offload_folder="offload")

generate_text = InstructionTextGenerationPipeline(model=model, tokenizer=tokenizer)

def generate_text_from(input):
    res = generate_text(input)
    return res[0]["generated_text"]