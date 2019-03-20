from index_MPC import MPCdata
from index_WEBCTRL import WebCTRLdata



def main(): 
    wCtrld = WebCTRLdata()
    webdata = wCtrld.getData(2019,1,28)
    
    MPCd = MPCdata()
    mpc_data = MPCd.getData(2019,3,12)
    
    for x in mpc_data:
        min_temp_mpc = x["temperatureMin"]
        max_temp_mpc = x["temperatureMax"]
        date_mpc = x["time"]
        for y in webdata:
            min_temp_web = y["temperatureMin"]
            max_temp_web = y["temperatureMax"]
            date_web = y["time"]
            # print(min_temp_mpc)
            # print(min_temp_web)
            # print(abs(min_temp_mpc - min_temp_web))
            if (abs(min_temp_mpc - min_temp_web) <= 2  and abs(max_temp_mpc - max_temp_web) <= 2 and date_web != date_mpc):
                print("MATCHING DATES")
                print("WEBCTRL")
                print("Date : {} minTemp : {}  maxTemp : {} ".format(date_web,min_temp_web,max_temp_web))
                print("MPC")
                print("Date : {} minTemp : {}  maxTemp : {} ".format(date_mpc,min_temp_mpc,max_temp_mpc))
                print("....")
                print("\n")


if __name__ == "__main__":
    main()


