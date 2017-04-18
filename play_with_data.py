import pandas as pd
list_of_columns = ["year","week","SMN","VCI","TCI","VHI",]
frame_id_1 = pd.read_csv('vhi_1.csv',header = 1, names = list_of_columns, delim_whitespace=True, index_col=False)
frame_id_1.insert(3,"SMK",frame_id_1["SMN"].str.split(',').str.get(1))
frame_id_1["SMN"] = frame_id_1["SMN"].str.split(",").str.get(0)
print(list(frame_id_1.columns.values))
print(frame_id_1[:3])