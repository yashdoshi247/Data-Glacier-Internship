import yaml
import re
def read_config_file(path):
    with open(path,'r') as file:
        try:
            return yaml.safe_load(stream=file)
        except Exception as e:
            return e

def header_preprocessor(header_list):
    header_preprocessed_list=[]
    for header in header_list:
        header_preprocessed = header.lower() # Converting header to lower case
        header_preprocessed = header_preprocessed.strip() # Removing extra spaces
        header_preprocessed = re.sub("[\s_@]+","_",header_preprocessed) # Substituting special characters
        header_preprocessed_list.append(header_preprocessed) # Appending preprocessed header to list
    return header_preprocessed_list

def column_header_validation(df_columns,config_columns):
    df_cols_preprocessed = header_preprocessor(df_columns)
    config_cols_preprocessed = header_preprocessor(config_columns)

    if df_cols_preprocessed==config_cols_preprocessed:
        return "Column validation passed"
    elif len(df_cols_preprocessed)==len(config_cols_preprocessed):
        print("Length of columns is same but column names are different")
        print(f"Following column headers not present in config file: {[x for x in df_cols_preprocessed if x not in config_cols_preprocessed]}")
        print(f"Following columns of config file not found in dataframe: {[x for x in config_cols_preprocessed if x not in df_cols_preprocessed]}")
    else:
        print("Entire column validation failed (both names and length are different)")
        print(f"Following columns of dataframe not found in config file: {[x for x in df_cols_preprocessed if x not in config_cols_preprocessed]}")
        print(f"Following columns of config file not found in dataframe: {[x for x in config_cols_preprocessed if x not in df_cols_preprocessed]}")
