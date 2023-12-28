from transformers import T5Tokenizer, T5ForConditionalGeneration

COMPETITOR = "google/flan-t5-base"

tokenizer = T5Tokenizer.from_pretrained(COMPETITOR)
model = T5ForConditionalGeneration.from_pretrained(COMPETITOR)

tokenizer.save_pretrained("app/cache")
model.save_pretrained("app/cache")