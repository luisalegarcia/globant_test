""" Get info from .xml files """
# import libraries
from lxml import etree
import os 
import pandas as pd

def read_files():
    path = "data/origin"

    # list all files to get info 
    data_list = os.listdir(path)
    data = pd.DataFrame(columns=["id", "title", "abstract", "directorate", "division"])

    # read each file 
    for i in data_list: 
        tree = etree.parse(os.path.join(path,i))
        abstract = tree.find('//AbstractNarration')
        abstract = ' '.join(abstract.itertext())
        title = tree.find('//AwardTitle')
        title = ' '.join(title.itertext())
        directorate = tree.find("//Directorate/LongName")
        directorate = ' '.join(directorate.itertext())
        division = tree.find("//Division/LongName")
        division  = ' '.join(division.itertext())
        data = pd.concat([data, pd.DataFrame({"id": [i], "title": [title] ,"abstract" : [abstract], "directorate" : [directorate], "division" : [division]})])
    return data 


## save the data
# data = read_files()
# data.to_parquet("data.parquet")
