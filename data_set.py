import pandas as pd
import matplotlib.pyplot as plt


def df_func(file):
    list_of_columns = ["year", "week", "SMN", "SMK", "VCI", "TCI", "VHI", ]
    frame_id = pd.read_csv(file, names=list_of_columns, engine='python', delimiter='\,\s+|\,|\s+', skiprows=1)

    return frame_id
# take files and push in dataframe(pandas's table)


def percent_func(file):
    list_of_columns = ["year", "week"]
    list_percent = [str(x) for x in range(0, 105, 5)]
    list_of_columns.extend(list_percent)
    frame_id = pd.read_csv(file, names=list_of_columns, engine='python', delimiter='\,\s+|\,|\s+', skiprows=1)
    # print(list(frame_id.columns.values))
    return frame_id



def vhi_in_year(frame, year):
    year_frame = frame[frame.year == year]
    max_vhi, min_vhi = year_frame["VHI"].max(), year_frame["VHI"].min()
    print("maximum vhi of "+'year ' + str(max_vhi)+" and min is "+str(min_vhi))
    year_frame.plot(x='week', y='VHI', style='y--')
    plt.show()

# min and max vhi
def vhi_of_percent(frame, percent):
    dict_of_years = {}
    list_of_years = []
    for year in range(1981, 2018):
        short_frame = frame[frame.year == str(year)][['0', '5', '10', '15']]  # part of frame with one year,and percent<=15
        list_sum = 0
        for i in list(short_frame.columns.values):
            list_sum += short_frame[i].mean()
        dict_of_years[str(year)] = list_sum
    series_year = pd.Series(dict_of_years)
    for key in series_year.keys():
        if series_year[key] > percent:
            list_of_years.append(key)
    print(list_of_years)
    return list_of_years


vhi_in_year(df_func("D:\laba1\\vhi_1_2017-02-21 17_28_01.csv"), "1998") #analise one year,min and max, plot
frame = percent_func("percent_vhi_1.csv")  #table with a percent of vhi
list_of_bad_years = vhi_of_percent(frame, 5) #check province level of VHI
# /home/gtfonewb/laba1/data_set.py