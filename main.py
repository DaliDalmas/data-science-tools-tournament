import pandas as pd
import random
import logging

def ingest_and_clean(link):
    """
    This function uses the supplied link to get excel document the
    gets the column of items to be grouped.
    The function returns a list of items to be grouped.
    """
    data = pd.read_excel(link)
    return [d[0].upper() for d in data.values]

def create_groups(list_of_items):
    """
    This function gets the list of items groups the items
    and retuns a dictionary of groups
    """
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
    """
    This function take a dictionary of groups and converts it into a dataframe.
    I returns a pandas dataframe.
    """
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