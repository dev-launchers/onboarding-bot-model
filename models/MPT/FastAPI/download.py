from transformers import AutoModelForCausalLM, AutoTokenizer

COMPETITOR = "mosaicml/mpt-7b"

tokenizer = AutoTokenizer.from_pretrained(COMPETITOR)
model = AutoModelForCausalLM.from_pretrained(COMPETITOR)

tokenizer.save_pretrained("app/cache")
model.save_pretrained("app/cache")