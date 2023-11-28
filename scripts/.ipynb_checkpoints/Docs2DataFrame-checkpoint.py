import pandas as pd

def convert(docs, necessary_field, wanted_field):
    # Converting the data raw data into dataframe
    materials = []
    for material in docs:
      material = dict(material)
      materials.append(material)
    df = pd.DataFrame(materials)
    df = df[necessary_field+wanted_field]
    
    return df