import pandas as pd 
import numpy as np 
import requests
import csv
'''
pyCHORDS v0.1
Authors:
Edsel Norwood
Walter Asbell
Tony Guy
Ishan Paranjape
'''


# This fucntion is the main function that is initally called.
def get_data(base_url, filename):
    r = requests.get(base_url)
    decoded_re = decode(r)
    cr = to_csv(decoded_re)
    data_list = csv_to_list(cr)
    headers = get_headers(data_list)
    datatree_ready = create_datatree(data_list, headers)
    return (datatree_ready)

# This function decodes the read data.
def decode(re, format="utf"):
    return (re.content.decode(format))

# This function reads decoded data using csv.reader. 
def to_csv(decoded_re):
    return (csv.reader(decoded_re.splitlines(), delimiter=","))

# This function converts csv data into a list
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
