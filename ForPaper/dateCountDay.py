import csv
import pandas, datetime
import CSV_process_timeday as P

#date-time lists and varibles
startdate = ['01/11/2022']
enddate = datetime.datetime(2022, 11, 1)

#got glucose
glutemp = []
gluTime = [0] * 24
gluData = [0] * 24
listGlu = []
finallGlu = []
count = 0


with open("..//Glucose.csv", 'r',encoding="utf-8") as file:
    data = csv.reader(file)
    dataList = list(data)
    lon = len(dataList)
    P.find(1, lon, dataList, startdate, glutemp)
    P.Caculate(glutemp, gluTime, gluData,listGlu, count, finallGlu)
    print(finallGlu)

file.close()



with open("..//Glucose outputDay.csv", 'r+', encoding="utf-8") as file:
    writer = csv.writer(file)
    print(f"Writing ""11/1"" to file...")
    writer.writerows(glutemp)
file.close() 