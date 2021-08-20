import pandas as pd
import random
import logging

def ingest_and_clean(link):
    data = pd.read_excel(link)
    return [d[0].upper() for d in data.values]

def create_groups(list_of_items):
    Groups = {}
    list_of_items = list_of_items
    items = list_of_items.copy()
    for idx in range(len(list_of_items)):
        selected_item = random.choice(items)
        try:
            Groups[chr(ord('@')+1+idx%8)]=\
            Groups[chr(ord('@')+1+idx%8)]+[selected_item]
        except:
            Groups[chr(ord('@')+1+idx%8)] = [selected_item]
        items.remove(selected_item)
    return Groups

def make_groups_a_dataframe(groups):
    try:
        return pd.DataFrame(groups)
    except Exception as e:
        logging.error(e)
        return None
    
if __name__=='__main__':
    datalink = './Data science tool set copy.xlsx'
    groups_dict = create_groups(ingest_and_clean(datalink))
    groups_df = make_groups_a_dataframe(groups_dict)
    print(groups_df)