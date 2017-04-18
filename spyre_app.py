from spyre import server
import re
import pandas as pd
import urllib.request
import json

list_of_province_name = []
for x in range(1,28):
    filedata = open("/home/gtfonewb/laba1/vhi_{}.csv".format(x),'r')
    stringname = filedata.readline()
    result = re.findall(r'\S+', stringname)[6]
    if result[-1] == ',':
        result = result[:-1]
    list_of_province_name.append(result)
    list_of_province_id = [x for x in range(1,28)]
    our_dict = dict(zip(list_of_province_name,list_of_province_id))


class IndexPlot(server.App):
    title = "VHI,VCI,TCI"

    inputs = [{     "type":'dropdown',
                    "label": 'Province',
                    "options" : [{"label": "{}".format(key),"value" : "{}".format(our_dict[key])}
                                 for key in our_dict.keys()],
                    "key": 'provinceID',
                    "action_id": "update_data"},

              {     "type":'dropdown',
                    "label": 'Year',
                    "options": [{"label" : "{}".format(x), "value" : "{}".format(x)} for x in range(1981,2018)],
                    "key": 'yearfrom',
                    "action_id": "update_data"},

              {     "type": 'dropdown',
                    "label": 'Index',
                    "options": [{"label": "{}".format(x) ,"value": "{}".format(x)} for x in ["VHI","TCI","VCI"]],
                    "key": 'index',
                    "action_id": "update_data"},
    ]
    controls = [{    "type" : "hidden",
                    "id" : "update_data"}]

    tabs = ["Plot","Table"]

    outputs = [{ "type" : "plot",
                    "id" : "plot",
                    "control_id" : "update_data",
                    "tab" : "Plot"},
                { "type" : "table",
                    "id" : "table_id",
                  "tab" : "Table",
                  "control_id" : "update_data",
                    "on_page_load" : True }]

    def getData(self, params):
        api_url = "/home/gtfonewb/laba1/vhi_{}.csv".format(params["provinceID"])
        list_of_columns = ["year", "week", "SMN", "SMK", "VCI", "TCI", "VHI", ]
        frame_id = pd.read_csv(api_url, names=list_of_columns, engine='python', delimiter='\,\s+|\,|\s+', skiprows=1)
        year_frame = frame_id[frame_id.year == str(params["yearfrom"])]
        return year_frame

    def getPlot(self, params):
        df = self.getData(params)
        plt_obj = df.plot(x='week', y=params['index'], style='y--')
        fig = plt_obj.get_figure()
        return fig

app = IndexPlot()
app.launch(port=9093)