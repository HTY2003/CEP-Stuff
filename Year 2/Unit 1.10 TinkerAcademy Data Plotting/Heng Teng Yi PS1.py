import pandas as pd, numpy as np
import json
import urllib.request
import matplotlib.pyplot as plt
import plotly
from plotly.graph_objs import *
import time
plotly.offline.init_notebook_mode()

#Part 1 - Data Acquisition
for month in range(1,8):
    name = "DAILYDATA_S109_20170" + str(month) + ".csv"
    monthdata = pd.read_csv(name, encoding="ISO-8859-1")
    if month == 1:
        df = monthdata
    else:
        df = pd.concat([df, monthdata])

#Part 2 - Plotting with Matplotlib
    #Settings for Graph
df["datetime"] = pd.to_datetime(df.loc[:,'Year':'Day'])
x = df["datetime"].values
print(x)
time.sleep(30)
'''temp_dict = {'Mean Temperature (°C)': 'Mean Temp','Maximum Temperature (°C)': "Max Temp",'Minimum Temperature (°C)':"Min Temp"}
wind_dict = {'Mean Wind Speed (km/h)': "Mean Wind Speed", 'Max Wind Speed (km/h)': 'Max Wind Speed'}
plt.style.use('fivethirtyeight')
plt.figure(figsize=(30,15))

    #Plotting and Saving of Temperature Graph
plt.title("Temparatures of Ang Mo Kio from January-July 2017 / °C", fontsize=20)
for major in ['Mean Temperature (°C)','Maximum Temperature (°C)','Minimum Temperature (°C)']:
    y = df[major].values
    y_pos = df[major].values[-1] - 0.1
    plt.text(x[-1], y_pos, temp_dict[major], fontsize=15)    
    plt.plot(x, y - 0.1, lw=1.5)
plt.savefig("Heng Teng Yi_temp.png")

    #Clearing of Temperature Graph
plt.clf()

    #Plotting and Saving of Wind Speed Graph
plt.title("Wind Speed of Ang Mo Kio from January-July 2017 in km/h", fontsize=20)
for major in['Mean Wind Speed (km/h)', 'Max Wind Speed (km/h)']:
    y = df[major].values
    y_pos = df[major].values[-1] - 0.1
    plt.text(x[-1], y_pos, wind_dict[major], fontsize=15, verticalalignment = "center")    
    plt.plot(x, y - 0.1, lw=1.5) 
plt.savefig('Heng Teng Yi_wind.png')

#Part 3 - Plotting with plot.ly
    #Requesting and Storing of data in a dictionary
url = "https://api.data.gov.sg/v1/environment/pm25"
request = urllib.request.Request(url)
request.add_header('api-key','J37WFZplQd6woIFmuUcTud1fU7uwUyLj')
response = urllib.request.urlopen(request)
unparsed_data = response.read()
data = json.loads(unparsed_data.decode('utf-8'))
data = dict(json.loads(json.dumps(data, indent=4)))

    #Obtaining Average PM 2.5 Reading for the whole of SG
avereading = 0
loc_no = 0
for reading in data['items'][0]['readings']['pm25_one_hourly'].values():
    avereading += reading
    loc_no += 1
avereading /= loc_no
print("Average PM 2.5 Reading across Singapore = " + str(avereading) + " µm/m3")

    #Organising and Plotting Coordinates, Location Name, and PM 2.5 Reading on Map
mapbox_access_token = 'pk.eyJ1IjoicmFuZHVtYnJpZGVyIiwiYSI6ImNqNndiZHIwdjE5bjIycnBoZzQybjRuMTgifQ.Z_NurQVVPTLKjqC-HBMBLg'
loclist = []
latlist = []
lonlist = []

for loc in data['region_metadata']:
    loclist.append(' Location: ' + loc['name'][0].upper() + loc['name'][1:]+
        '<br> PM 2.5 Reading: '+ str(data['items'][0]['readings']['pm25_one_hourly'][loc['name']]) + " µm/m3")
    latlist.append(loc['label_location']['latitude'])
    lonlist.append(loc['label_location']['longitude'])

plotdata = Data([
    Scattermapbox(
        lat=latlist,
        lon=lonlist,
        mode='markers',
        marker=Marker(
            size=14
        ),
        text=loclist,
    )
])

layout = Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken = mapbox_access_token,
        bearing=0,
        center=dict(
            lat=latlist[2],
            lon=lonlist[2]
        ),
        pitch=0,
        zoom=11
    ),
)

fig = dict(data=plotdata, layout=layout)
plotly.offline.plot(fig, filename = "Heng Teng Yi_PM25.html")

'''
'''
 _______
/////// /|
////// / |
.   . | >/
  [   | /
------|/
~~~~~~

'''
