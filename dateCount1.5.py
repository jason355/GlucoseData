import csv
import pandas, datetime
import CSV_process_time as P


naHol = ['2021/06/14', '2021/09/20','2021/09/21','2021/10/11', 
        '2021/12/31','2022/01/1','2022/02/26','2022/4/5','2022/06/3',
        '2022/09/9','2022/10/10','2022/12/31']

Sumstart21 = datetime.datetime(2021, 7, 3) 
Sumend21 = datetime.datetime(2021, 8, 30)  


Sumstart22 = datetime.datetime(2022, 5, 23)
Sumend22 = datetime.datetime(2022, 8, 29) 

Winstart22 = datetime.datetime(2022, 1, 21)
Winend22 = datetime.datetime(2022, 2, 12)
Vac = []

weekend = []
weekday = []

glutemp = []
glu = [] 




with open("..//Glucose.csv", 'r',encoding="utf-8") as file:
    data = csv.reader(file)
    dataList = list(data)
    lon = len(dataList)
    lonedate = P.countDate(Vac, Sumstart21, Sumend21, Winstart22, Winend22, Sumstart22, Sumend22)
    P.findCacu(lon, lonedate, dataList, Vac, glutemp, glu)
file.close()



"""    
with open("..//Glucose output.csv", 'r+', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(glu)
    print(glu)
file.close() """