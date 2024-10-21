import datetime


#Find
def find(lon1, lon2, dataList, listf, listtemp):
    for j in range(lon1):
        for i in range(lon2):
            if listf[j] == dataList[i][0]:
                if dataList[i][2] != '':
                    get = [dataList[i][0], dataList[i][3], int(dataList[i][2])]
                    listtemp.append(get)


#Caculate
def Caculate(listtemp, gluTime, gluData, finallist):    
    longlu = len(listtemp)
    if longlu != 0:
        for m in range(longlu):
            glu = listtemp[m][2]
            Hr = int(listtemp[m][1][0:2])
            gluTime[Hr] = gluTime[Hr] + 1
            gluData[Hr] = gluData[Hr]+ glu
        for n in range(24):
            finallist.append(gluData[n] / gluTime[n])
        #print(Hr, gluTime, gluData)
#Count date
def countDate(data, start1, end1):
    data.append(start1.strftime("%d/%m/%Y"))
    for k in range((end1 - start1).days):
        data.append((start1 + datetime.timedelta(days=k+1)).strftime("%d/%m/%Y"))


def WeekDaEn(startD, endD, dateList, weekday, weekend, exceptdate):          # lon1
    print("...")
    for i in range((endD - startD).days):
        if dateList[i] not in exceptdate:
            if int(dateList[i][1]) in range(1, 6):
                weekday.append(dateList[i][0])
            elif int(dateList[i][1]) in range(6, 8):
                weekend.append(dateList[i][0])
    print("All weedays and weekends were in the list.")