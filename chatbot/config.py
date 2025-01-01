import os

OPENAI_KEY = os.getenv("OPENAI_KEY", "your key")                               
HUGGINFACEHUB_API_TOKEN = os.getenv("HUGGINFACEHUB_API_TOKEN", "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")    


providers = ["openai","huggingface"]

LLM_PROVIDER = "huggingface" 

# repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"


vector_db_dir = "./vector_db"
documents_parent_dir = "./"