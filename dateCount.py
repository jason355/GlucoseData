import csv
import pandas, datetime, os



#Find and count
def findCacu(lon1, lon2, dataList, listf, listtemp, listT):
    for j in range(lon2):
        for i in range(lon1):
            if listf[j] == dataList[i][0]:
                if dataList[i][2] != '':
                    listtemp.append(int(dataList[i][2]))
        longlu = len(listtemp)
        if longlu !=0:
            avg = sum(listtemp) / longlu
            listT.append(avg)
            listtemp = []

#Count date
def countDate(data, start1, end1, start2, end2, start3, end3):
    data.append(start1.strftime("%d/%m/%Y"))
    for k in range((end1 - start1).days):
        data.append((start1 + datetime.timedelta(days=k+1)).strftime("%d/%m/%Y"))

    data.append(start2.strftime("%d/%m/%Y"))
    for k in range((end2 - start2).days):
        data.append((start2 + datetime.timedelta(days=k+1)).strftime("%d/%m/%Y"))
    
    data.append(start3.strftime("%d/%m/%Y"))
    for k in range((end3 - start3).days):
        data.append((start3 + datetime.timedelta(days=k+1)).strftime("%d/%m/%Y"))
    londate = len(Vac)
    return londate

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
    lonedate = countDate(Vac, Sumstart21, Sumend21, Winstart22, Winend22, Sumstart22, Sumend22)
    findCacu(lon, lonedate, dataList, Vac, glutemp, glu)
    print(len(glu))
    print(lonedate) 

    