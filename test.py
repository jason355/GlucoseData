import csv
import datetime





naHol = ['2021/06/14', '2021/09/20','2021/09/21','2021/10/11', 
        '2021/12/31','2022/01/1','2022/02/26','2022/4/5','2022/06/3',
        '2022/09/9','2022/10/10','2022/12/31']
startdates = datetime.datetime(2021, 5, 23)
enddates = datetime.datetime(2021, 8, 29) 
sumVac = []
winVac = []
weekend = []
weekday = []
gluHolD = []
gluHol = [] 
count = 0
dataG = 0
delet = []
send = []


sumVac.append(startdates)
for k in range((enddates - startdates).days):
    sumVac.append((startdates + datetime.timedelta(days=k+1)).strftime('%d/%m/%Y'))
    #print(sumVac[k])


with open("..//Glucose.csv", 'r',encoding="utf-8") as file:
    data = csv.reader(file)
    dataList = list(data)
    lon = len(dataList)
    londate = len(sumVac)
    for j in range(londate):
        for i in range(lon):
            if sumVac[j] == dataList[i][0]:
                if dataList[i][2] != '':
                    gluHolD.append(int(dataList[i][2]))
        longlu = len(gluHolD)
        if longlu !=0:
            avg = sum(gluHolD) / longlu
            send = [sumVac[j], avg]
            #print(send)
            gluHol.append(send)
            #gluHol[j][1].append(send[1])
            gluHolD = []

    lonGlu = len(gluHol)
    print(gluHol)
    for m in range(lonGlu):
        print(gluHol[m]) 

