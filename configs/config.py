import os
PROJECT_ROOT = (os.path.abspath('./'))

BERT_MODEL_NAME = "bert-base-uncased"
BERT_MODEL_DIR =  os.path.join( PROJECT_ROOT,  "models/bert/base-uncased/" )

DATA_PATH = os.path.join(os.path.abspath('../../'), 'scrape_web')

