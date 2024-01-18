import sys, os
sys.path.append( os.path.abspath('./') )

from transformers import BertModel, BertTokenizer
from configs.config import BERT_MODEL_DIR


# Load the model and tokenizer from the local directory
def load_bert_model_tokenizer(path = BERT_MODEL_DIR):
    model = BertModel.from_pretrained(path)
    tokenizer = BertTokenizer.from_pretrained(path)
    print('Model and tokenizer loaded successfully')

    return model, tokenizer