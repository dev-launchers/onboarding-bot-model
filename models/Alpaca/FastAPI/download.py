from transformers import AutoModelForCausalLM, AutoTokenizer

COMPETITOR = "tatsu-lab/alpaca-7b-wdiff"

tokenizer = AutoTokenizer.from_pretrained(COMPETITOR)
model = AutoModelForCausalLM.from_pretrained(COMPETITOR)

tokenizer.save_pretrained("app/cache")
model.save_pretrained("app/cache")