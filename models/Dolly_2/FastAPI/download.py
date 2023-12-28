from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-3b")
model = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-3b")

tokenizer.save_pretrained("app/cache")
model.save_pretrained("app/cache")