import datetime
import pandas as pd
import os
pd.set_option('display.max_columns', None)
import json

with open('json_configs.json') as config_file:
    config = json.load(config_file)


def convert_to_json():
  df = pd.read_csv(config['filename'], 
                 names = config['column_names'],
                dtype = "unicode"
                )
  df = df.astype(config['column_mapping'])

  if len(config['date_cols']):
    for date_col in config['date_cols']:
      change_date_format(df, date_col)
  else:
    print('empty date_cols list!')

  if len(config['non_str_cols']):
    for non_str_col in config['non_str_cols']:
      convert_to_string(df, non_str_col)
  else:
    print('no column to convert, all good..')

  df.to_json(config['output_file'], orient='records', lines=True)


def change_date_format(df, column):
    df[column] = df[column].map(lambda x: datetime.datetime.strftime(x, "%Y-%m-%dT%H:%M:%S.%fZ"))

def convert_to_string(df, non_str_cols):
    df[non_str_cols] = df[non_str_cols].str.replace(r"\\0", r"\\u0000")


if __name__ == "__main__":
  convert_to_json()

    