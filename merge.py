"""merge_data joins two datasets"""


import pandas as pd

def merge_data(df_left, df_right, merge_col):
    final_df=df_left.merge(df_right, on=[merge_col])
    return final_df