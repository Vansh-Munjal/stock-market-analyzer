from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load once globally
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

def generate_report(ticker, trend, rsi, note):
    prompt = (
        f"Stock: {ticker}\n"
        f"Trend: {trend}\n"
        f"RSI: {rsi}\n"
        f"Note: {note}\n"
        f"Summary:"
    )

    inputs = tokenizer.encode(prompt, return_tensors="pt", max_length=512, truncation=True)

    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_length=150,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            early_stopping=True
        )

    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated.split("Summary:")[-1].strip()
