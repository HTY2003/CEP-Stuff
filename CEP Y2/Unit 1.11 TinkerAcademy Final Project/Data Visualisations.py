import urllib.request as req
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def data_retrieve(channel_id, read_api_key):
    conn = req.urlopen("http://api.thingspeak.com/channels/%s/feeds.csv?api_key=%s" \
                           % (channel_id,read_api_key))
    response = pd.read_csv(conn)
    #Reads csv files directly from Thingspeak URL
    conn.close()
    return response

#Data Retrieval
dht = data_retrieve(311611, "IU84FZDLGICE1DO9")
anemo = data_retrieve(340307, "I2I69J7MDBNNDQ6X")

'''As of now, while the above request code works, running this code would
result in empty graphs as the channel data was deleted due to the demo
in class adding extra data and ruining the channel feeds.

Hence, the csv files will be included to use for our submitted visualisations.'''

dht = pd.read_csv("dht.csv")
anemo = pd.read_csv("anemo.csv")

#Graph Labels
dhtdict = {1:"Rec. Temp", 2:"Mean Temp",
             3:"Rec. Humidity", 4:"Mean Humidity"}
anemodict = {1: "Rec. RPM", 2:"Mean RPM"}

#Datetime Values
dhtdt = pd.to_datetime(dht["created_at"]).values
anemodt = pd.to_datetime(anemo["created_at"]).values

#Graph Settings 
plt.style.use('fivethirtyeight')
plt.figure(figsize=(25,15))

#-------Temperature Graph Plotting----------
plt.title("Temparatures Measured / °C", fontsize=20)

for i in range(1,3):
    x = dht["field"+str(i)].values
    if len(x) > 0:
        y_pos = x[-1]
        plt.text(dhtdt[-1], y_pos, dhtdict[i], fontsize=15)    
        plt.plot(dhtdt, x, lw=1.5)
    plt.savefig("Heng Teng Yi_Temp.png")

plt.clf()

#----------Humidity Graph Plotting-----------
plt.title("Humidity Measured / %", fontsize=20)
for i in range(3,5):
    x = dht["field"+str(i)].values
    if len(x) > 0: #Can plot empty graphs if needed
        y_pos = x[-1]
        plt.text(dhtdt[-1], y_pos, dhtdict[i], fontsize=15)    
        plt.plot(dhtdt, x, lw=1.5)
    plt.savefig("Heng Teng Yi_Humid.png")
    
plt.clf()

#-------Wind Speed Graph Plotting----------
plt.title("Wind Speed Measured / RPM", fontsize=20)
for i in range(1,3):
    x = anemo["field"+str(i)].values
    if len(x) > 0:
        y_pos = x[-1]
        plt.text(anemodt[-1], y_pos, anemodict[i], fontsize=15)    
        plt.plot(anemodt, x, lw=1.5)
    plt.savefig("Heng Teng Yi_WS.png")
    
plt.clf()
