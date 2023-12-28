from transformers import T5Tokenizer, T5ForConditionalGeneration

COMPETITOR = "google/flan-t5-base"

tokenizer = T5Tokenizer.from_pretrained(COMPETITOR)
model = T5ForConditionalGeneration.from_pretrained(COMPETITOR)

def generate_text_from(input_text):
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)