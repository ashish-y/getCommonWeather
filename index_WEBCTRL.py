import datetime
import pandas as pd
import forecastio
import matplotlib.pyplot as plt

# Enter your API here
api_key = ("44f3ab263e33924cb610febb6e2cc3c7")
lat = 37.374222
lng = -120.577530
plt.close()
# date = datetime.datetime(2019,3,19)

# forecast = forecastio.load_forecast(api_key, lat, lng, time=date, units="us")
# hourly = forecast.hourly()

class WebCTRLdata:
    # print(hourly.data[0].d)

    def __init__(self):
        
        self.data = {}
        #attributes = ["temperature", "humidity"]
        self.attributes = ["temperature"]

        for attr in self.attributes:
            self.data[attr] = []
    
    def getData(self,year=2019,month=3,day=12):
        result =[]
        start = datetime.datetime(year, month, day)
        for offset in range(1, 30):
            forecast = forecastio.load_forecast(api_key, lat, lng, time=start+datetime.timedelta(offset), units="us")
            h = forecast.daily()
            d = h.data
            for p in d:
                json = {"temperatureMin":p.d["temperatureMin"],"temperatureMax":p.d["temperatureMax"],"time":(p.time).strftime('%Y-%m-%d')}
                result.append(json)
        return result

    def plot(self,time):
        start = datetime.datetime(2019, 3, 12)
        for offset in range(1, 2):
            forecast = forecastio.load_forecast(api_key, lat, lng, time=start+datetime.timedelta(offset), units="us")
            h = forecast.hourly()
            d = h.data
            for p in d:
                times.append(p.time)
                for attr in self.attributes:
                    self.data[attr].append(p.d[attr])
        return self.data



def main(): 
    times = []   
    webd = WebCTRLdata().getData(times)
    df = pd.DataFrame(webd, index=times)

    #df = df.tz_localize("Asia/Kolkata").tz_convert("US/Central")

    df.head()
    df.to_csv("weather-WEBCTRL.csv")
    print("PLOTTTING.")
    print("PLOTTTING..")
    print("PLOTTTING...")
    plt.style.use('ggplot')

    df.plot()
    plt.show()


if __name__ == "__main__":
    main()
