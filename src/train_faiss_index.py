import sys, os
sys.path.append( os.path.abspath('./') )

from src.generate_sentence_embeddings import get_sentence_embeddings
from src.data_ingestion.fetch_data_from_json import get_titles_data
from configs.config import BATCH_SIZE_SENTENCES_BERT, NBITS_FAISS, BERT_EMBEDDING_DIMENSION
import numpy as np
import faiss

# List of sentences to tokenize and encode
sentences = get_titles_data()
N = len(sentences)

combined_embeddings = None

for i in range(0, N, BATCH_SIZE_SENTENCES_BERT):
    temp_arr = get_sentence_embeddings(sentences, i, i+BATCH_SIZE_SENTENCES_BERT)

    if combined_embeddings is None:
        combined_embeddings = temp_arr
    else:
        combined_embeddings = np.concatenate((combined_embeddings, temp_arr), axis=0)

    del(temp_arr)
    print(f" Shape of array: {combined_embeddings.shape}")


#Intialize faiss lSH index
index = faiss.IndexLSH(BERT_EMBEDDING_DIMENSION, NBITS_FAISS)

# Train index
index.train(combined_embeddings)

#Add index to the data
index.add(combined_embeddings)

#Search a Query
Question = "Why HDFC Bank share is not performing well?"
question_encoded = get_sentence_embeddings([Question.lower()], 0, 1)
print(question_encoded.shape)

# Perform a search
Distances, Indices = index.search(question_encoded, 5)

for i in range(5):
    print(f"{sentences[Indices[i]]} ,  distance - {Distances[i]}") 