import sys, os
sys.path.append( os.path.abspath('./') )
import json
from datetime import datetime

from configs.config import DATA_PATH

KEEP_UPTO = 5

json_files = [file for file in os.listdir(DATA_PATH) if file.endswith('.json')]

json_files = json_files[ : KEEP_UPTO]

def get_titles_data():
    titles_list = []
    date_list = []

    for file in json_files:
        filepath = os.path.join(DATA_PATH, file)
        with open(filepath, 'r') as file_handle:
            file_data = json.load(file_handle)

        for item in file_data.keys():
            title, date = item.split('__|__')[1].lower(), item.split('__|__')[0]
            titles_list.append(title)
            date_list.append( datetime.strptime( date, "%d %b, %Y") )

    print( f"Start: {min(date_list).date()}, End: {max(date_list).date()}, #Articles: {len(titles_list)}")

    return titles_list
