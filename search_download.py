import urllib.request
import datetime


def download():
    for obj_id in range(1, 28):
        url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID={}&year1=1981&year2=2017&type=Mean".format(
            obj_id)
        vhi_url = urllib.request.urlopen(url).read()
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        out = open('vhi_{}_{}.csv'.format(obj_id, dt), 'wb')
        out.write(vhi_url)
        out.close()
        print("dataset " + str(obj_id) + " download")
# for percent

def download_vhi():
    for obj_id in range(1,28):
        url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID={}&year1=1981&year2=2017&type=VHI_Parea".format(
            obj_id)
        vhi_url = urllib.request.urlopen(url).read()
        out = open("percent_vhi_{}.csv".format(obj_id), 'wb')
        out.write(vhi_url)
        out.close()
        print("percent"+str(obj_id))
download_vhi()
