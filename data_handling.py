import pandas as pd
import os
import numpy as np
import datetime
import line_plot
import matplotlib.pyplot as plt





path = os.getcwd()
files = os.listdir(path +'\Excel_files')

sheets_dict = pd.read_excel(f'Excel_files\\SnP_Data_Combined.xlsx', sheet_name=None)
#sheets_dict = pd.read_excel(f'Excel_files\\Bloomberg_Data_Separated.xlsx', sheet_name=None)

for name, sheet in sheets_dict.items():
    print(f'Processing {name}')
    file_path = f'Saved_dataframes\\{name}.csv'
    sheet = sheet.dropna(how='all')

    sheet.index = pd.to_datetime(sheet['Date'])
    #reindexing to make dates line up
    idx = pd.date_range(sheet.index[0], sheet.index[-1])[::-1] # dates are backwards for bloomberg with last day first
    sheet = sheet.reindex(idx, fill_value=None)

    sheet['Price'].interpolate(inplace=True) # use interpolate instead of forward fill to reduce unecessary variance between datapoints
    line_plot.line_plot(sheet['Price'], name)
    sheet.to_csv(file_path, encoding='utf-8', index=False)

print('Done')