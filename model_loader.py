from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

def load_chat_model(model_name="microsoft/phi-2"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float32,
        device_map="auto"
    )
    
    return pipeline("text-generation", model=model, tokenizer=tokenizer)
