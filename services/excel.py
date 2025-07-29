import pandas as pd
import os
from Config import Config
from pandas.conftest import index


def append_to_excel(new_data):
    df_new = pd.DataFrame([new_data])

    df_combined = None

    if os.path.exists(Config.EXCEL_FILENAME):
        df_existing = pd.read_excel(Config.EXCEL_FILENAME)
        df_combined = pd.concat([df_existing,df_new], ignore_index = True)
    else:
        df_combined = df_new

    df_combined.to_excel(Config.EXCEL_FILENAME, index= False)
    print("Zapisano do pliku EXCEL")