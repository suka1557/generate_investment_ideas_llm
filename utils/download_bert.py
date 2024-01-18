import os, sys
sys.path.append(os.path.abspath('./'))

from configs.config import BERT_MODEL_NAME, BERT_MODEL_DIR

from transformers import BertModel, BertTokenizer 



# Load the model and tokenizer from Hugging Face model hub
model = BertModel.from_pretrained(BERT_MODEL_NAME)
tokenizer = BertTokenizer.from_pretrained(BERT_MODEL_NAME)

# Save the model and tokenizer locally
model.save_pretrained(BERT_MODEL_DIR)
tokenizer.save_pretrained(BERT_MODEL_DIR)
