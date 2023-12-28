from transformers import T5Tokenizer, T5ForConditionalGeneration

COMPETITOR = "google/flan-t5-base"
CACHE = "cache"
OFFLOAD = "offload"

tokenizer = T5Tokenizer.from_pretrained(CACHE)
model = T5ForConditionalGeneration.from_pretrained(CACHE, offload_folder=OFFLOAD)

def generate_text_from(input_text):
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)