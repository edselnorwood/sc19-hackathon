import pandas as pd 
import numpy as np 
import requests
import csv

def get_data(url, filename):
    r = requests.get(url)
    decoded_re = decode(r)
    cr = to_csv(decoded_re)
    data_list = csv_to_list(cr)
    headers = get_headers(data_list)
    datatree_ready = create_datatree(data_list, headers)
    print (datatree_ready.describe())

def decode(re, format="utf"):
    return (re.content.decode(format))

def to_csv(decoded_re):
    return (csv.reader(decoded_re.splitlines(), delimiter=","))

def csv_to_list(cr):
    data_list = list(cr)
    return (data_list)

def get_headers(data_list):
    headers = data_list[13]
    return (headers)

def create_datatree(data_list, headers):
    datatree_data = pd.DataFrame(data_list)
    datatree_data.columns = headers
    datatree_data.set_index("Time")
    datatree_ready = datatree_data.iloc[14:]
    datatree_ready.set_index("Time")
    return (datatree_ready)