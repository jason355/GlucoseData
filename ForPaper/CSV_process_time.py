import datetime


#Find
def find(lon1, lon2, dataList, listf, listtemp):
    for j in range(lon1):
        for i in range(lon2):
            if listf[j] == dataList[i][0]:
                print(f"{listf[j]}")
                try:
                    get = [dataList[i][1], dataList[i][3], int(dataList[i][4])]
                    listtemp.append(get)
                except ValueError:
                    print("The data can't turn to int.")

#Caculate
def Caculate(listtemp, gluTime, gluData, index,finallist):
    index.clear()
    longlu = len(listtemp)
    if longlu != 0:
        for m in range(longlu):
            glu = listtemp[m][2]
            Hr = int(listtemp[m][1][0:2])
            gluTime[Hr] = gluTime[Hr] + 1
            gluData[Hr] = gluData[Hr]+ glu
        for n in range(24):
            finallist.append(gluData[n] / gluTime[n])
        for o in range(len(gluTime)):
            index.append(gluData.index(gluData[o]))
#Count date
def countDate(data, start1, end1, start2, end2, start3, end3, start4, end4):
    data.append(start1.strftime("%d/%m/%Y"))
    for k in range((end1 - start1).days):
        data.append((start1 + datetime.timedelta(days=k+1)).strftime("%d/%m/%Y"))

    data.append(start2.strftime("%d/%m/%Y"))
    for k in range((end2 - start2).days):
        data.append((start2 + datetime.timedelta(days=k+1)).strftime("%d/%m/%Y"))
    
    data.append(start3.strftime("%d/%m/%Y"))
    for k in range((end3 - start3).days):
        data.append((start3 + datetime.timedelta(days=k+1)).strftime("%d/%m/%Y"))
    data.append(start3.strftime("%d/%m/%Y"))
    for k in range((end4 - start4).days):
        data.append((start4 + datetime.timedelta(days=k+1)).strftime("%d/%m/%Y"))
    #print(data)
    # londate = len(data)
    # return londate



def WeekDaEn(startD, endD, dateList, weekday, weekend, exceptdate):          # lon1
    for i in range((endD - startD).days):
        if dateList[i] not in exceptdate:
            if int(dateList[i][5]) in range(1, 6):
                weekday.append(dateList[i][0])
            elif int(dateList[i][5]) in range(6, 8):
                weekend.append(dateList[i][0])
    print(len(weekday) + len(weekend))
    print("All weedays and weekends were in the list.")