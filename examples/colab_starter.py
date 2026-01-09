# Colab-friendly starter: inference with a Hugging Face transformer
# Run on Google Colab: install transformers first: !pip install -q transformers

from transformers import pipeline

MODEL = "distilbert-base-uncased-finetuned-sst-2-english"  # change as needed

def sentiment(texts):
    nlp = pipeline("sentiment-analysis", model=MODEL)
    return nlp(texts)

if __name__ == "__main__":
    samples = [
        "I love this workshop!",
        "This is a challenging problem but exciting to solve."
    ]
    print(sentiment(samples))
