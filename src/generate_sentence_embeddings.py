import sys, os
sys.path.append( os.path.abspath('./') )

from utils.load_bert import load_bert_model_tokenizer
from src.data_ingestion.fetch_data_from_json import get_titles_data
from configs.config import BATCH_SIZE_SENTENCES_BERT

import torch
import numpy as np

model, tokenizer = load_bert_model_tokenizer()

# List of sentences to tokenize and encode
sentences = get_titles_data()
N = len(sentences)

def get_sentence_embeddings(sentences, start_index, end_index):

    # Tokenize and encode the sentences
    tokenized_inputs = tokenizer(sentences[start_index:end_index], padding=True, truncation=True, return_tensors='pt')

    # Forward pass through the BERT model
    with torch.no_grad():
        outputs = model(**tokenized_inputs)

    # Get the embeddings (pooled output) for each sentence
    sentence_embeddings = outputs.pooler_output
    
    # Convert the embeddings to a numpy array
    sentence_embeddings_np = sentence_embeddings.numpy()

    del(outputs, tokenized_inputs, sentence_embeddings)

    return sentence_embeddings_np

combined_embeddings = None

for i in range(0, N, BATCH_SIZE_SENTENCES_BERT):
    temp_arr = get_sentence_embeddings(sentences, i, i+BATCH_SIZE_SENTENCES_BERT)

    if combined_embeddings is None:
        combined_embeddings = temp_arr
    else:
        combined_embeddings = np.concatenate((combined_embeddings, temp_arr), axis=0)

    del(temp_arr)
    print(f" Shape of array: {combined_embeddings.shape}")