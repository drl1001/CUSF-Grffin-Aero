#module that work on the simulation data from the Excel spreadsheet 

import pandas as pd

def convert_from_excel(filename,sheet):
    '''function that takes an excel filname and the sheetname in the document as arguments. 
    filename - a string with .xlsx extension
    sheetname - a string with the name of the desired spreadsheet in the Excel document.'''

    df = pd.read_excel(filename,sheet)
    sim = df.to_numpy()
    return sim
