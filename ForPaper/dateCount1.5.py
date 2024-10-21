import csv
import pandas, datetime
import CSV_process_time as P

#date-time lists and varibles
startdate = datetime.datetime(2021, 5, 3)
enddate = datetime.datetime(2023, 2, 24)


naHol = ['14/06/2021', '20/09/2021','21/09/2021','11/10/2021', 
        '31/12/2021','01/01/2022','26/02/2022','05/04/2022','03/06/2022',
        '09/09/2022','10/10/2022','31/12/2022','02/01/2023']

Sumstart21 = datetime.datetime(2021, 7, 3) 
Sumend21 = datetime.datetime(2021, 8, 30)  


Sumstart22 = datetime.datetime(2022, 5, 23)
Sumend22 = datetime.datetime(2022, 8, 29) 

Winstart22 = datetime.datetime(2022, 1, 21)
Winend22 = datetime.datetime(2022, 2, 12)

Winstart23 = datetime.datetime(2023, 1, 20)
Winend23 = datetime.datetime(2023, 2, 13)

Vac = []
weekend = []
weekday = []


#got glucose
glutemp = []
gluHolidaytimes = [0] * 24
gluHolidayData = [0] * 24
gluweekdaytimes = [0] * 24
gluweekdayData = [0] * 24
index = [] 
Holiday = []
finalWeekday = []
count = 0


with open("Glucose.csv", 'r',encoding="utf-8") as file:
    data = csv.reader(file)
    dataList = list(data)
    lon = len(dataList)
    
    P.countDate(Vac, Sumstart21, Sumend21, Winstart22, Winend22, Sumstart22, Sumend22, Winstart23, Winend23)
    for j in range(len(naHol)):
        Vac.append(naHol[j])
    P.WeekDaEn(startdate, enddate, dataList, weekday, weekend, Vac)
    for j in range(len(weekend)):
        Vac.append(weekend[j])
    #print(weekend)
    #lonedate = len(Vac)
    #P.find(lonedate, lon, dataList, Vac, glutemp)
    #P.Caculate(glutemp, gluHolidaytimes, gluHolidayData, index, Holiday)
    #print(f"Your holiday hourly glucose avg > {index}\n{Holiday}")
"""     
    lonedate = len(weekday)
    P.find(lonedate, lon, dataList, weekday, glutemp)
    P.Caculate(glutemp, gluweekdaytimes, gluweekdayData, index, finalWeekday)
    print(f"Your weekday hourly glucose avg > {index}\n{finalWeekday} ") """
file.close()



with open("Glucose output4.0.csv", 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    print(f"Writing ""Holoday"" to file...")
    writer.writerows([index, Holiday])
    print(f"Writing ""finalWeekday"" to file...")
    writer.writerows([index, finalWeekday])
file.close() 