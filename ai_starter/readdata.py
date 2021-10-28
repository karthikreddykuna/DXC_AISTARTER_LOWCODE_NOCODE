import json
import pandas as pd
import urllib.parse #input data
from flatten_json import flatten

def flatten_json_into_dataframe(json_data):
    #flatten the nested JSON data into a data frame
    try:
        json_data_flattened = [flatten(d) for d in json_data]
        df = pd.DataFrame(json_data_flattened)
        return(df)
    except:
        try:
            df = pd.DataFrame(json_data).T
            return(df)
        except:
            raise Exception("Uploaded JSON file is not in proper structure. Please choose different file.")

#Read JSON file from remote
def read_data_frame_from_remote_json(json_url):
    with urllib.request.urlopen(json_url) as url:
        json_data = json.loads(url.read().decode())
    df = flatten_json_into_dataframe(json_data)
    return(df)

def read_data_frame_from_remote_csv(csv_url, col_names = [], names=None, sep=',',  delim_whitespace=False, header = 'infer', skiprows=None, error_bad_lines=True, encoding=None):
    df = pd.read_csv(csv_url, sep=sep, delim_whitespace=delim_whitespace, header = header, names=names, skiprows=skiprows, error_bad_lines=error_bad_lines, encoding=encoding)
    if col_names != []:
        df.columns = col_names
    return(df)

