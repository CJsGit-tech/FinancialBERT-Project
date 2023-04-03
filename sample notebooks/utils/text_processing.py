import torch
from summarizer import Summarizer
from transformers import AutoModel, AutoConfig, AutoTokenizer,AutoModelForSequenceClassification
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, accuracy_score, f1_score


#######################################################################################################################
# Summarizer
def get_summarizer(model_name):
    # Find and setup model from the HuggingFace API
    custom_config = AutoConfig.from_pretrained(model_name)
    custom_config.output_hidden_states=True
    custom_tokenizer = AutoTokenizer.from_pretrained(model_name)
    custom_model = AutoModel.from_pretrained(model_name, config=custom_config)

    # Initiate the bert-extractive summarizar
    model = Summarizer(custom_model=custom_model, custom_tokenizer=custom_tokenizer)
    return model

def perform_summarizer(text_body, model, ratio = 0.5, return_embeddings = False):
    text_body = text_body.strip()
    text_body = text_body.replace('\n',' ')

    # Return Summary
    summary = model(body = text_body, ratio = ratio, max_length = 600)

    if return_embeddings:
        embeddings = model.run_embeddings(summary, aggregate = 'mean', num_sentences = num_sent)
        return summary, embeddings

    return summary

def txt_cln(text):
    text = text.replace('\n\n','')
    text = text.strip()
    text = " ".join(text.split())
    return text

def text_filter(df):
    df['cnt_len'] = df['text'].apply(lambda x: len(str(x).split()))
    df = df[df['cnt_len'] > 20]
    df['text'] = df['text'].apply(txt_cln)
    return df

#######################################################################################################################
# Topic
def get_sentiment_model(model,from_tf=False):
    tokenizer = AutoTokenizer.from_pretrained(model)
    model = AutoModelForSequenceClassification.from_pretrained(model,from_tf=from_tf)
    return tokenizer, model

def get_topic_model(model,from_tf=False):
    tokenizer = AutoTokenizer.from_pretrained(model)
    model = AutoModelForSequenceClassification.from_pretrained(model,from_tf=from_tf)
    return tokenizer, model

######################################################################################################################
# Model Metric and Evaluattion
def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    f1 = f1_score(labels, preds, average="weighted")
    acc = accuracy_score(labels, preds)
    return {"accuracy": acc, "f1": f1}
