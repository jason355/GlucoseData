import datetime


#Find
def find(lon1, lon2, dataList, listf, listtemp):
    for j in range(lon1):
        for i in range(lon2):
            if listf[j] == dataList[i][0]:
                if dataList[i][2] != '':
                    get = [dataList[i][0], dataList[i][3], int(dataList[i][2])]
                    listtemp.append(get)
    print("Find done.")

#Caculate    
def Caculate(listtemp, gluTime, gluData, index,finallist):
    index.clear()
    longlu = len(listtemp)
    if longlu != 0:
        for m in range(longlu):
            glu = listtemp[m][2]
            Hr = int(listtemp[m][1][0:2])
            #print(Hr)
            gluTime[Hr] = gluTime[Hr] + 1
            gluData[Hr] = gluData[Hr]+ glu
        for n in range(24):
            finallist.append(gluData[n] / gluTime[n])
        for o in range(len(gluTime)):
            index.append(gluData.index(gluData[o]))
    print("Caculate done.")


""" #Count date
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
    #print(data)
    # londate = len(data)
    # return londate

"""  


def Season(dateList, lon, winter, spring, summer, fall):          # lon1
    print("...")
    for i in range(lon):
        #print(i)
        #print(dateList[i][0][3:5])
        if dateList[i][0][3:5] in ["12", "01", "02"]:
            winter.append(dateList[i][0])
        elif dateList[i][0][3:5] in ["03", "04", "05"]:
            spring.append(dateList[i][0])
        elif dateList[i][0][3:5] in ["06", "07", "08"]:
            summer.append(dateList[i][0])
        elif dateList[i][0][3:5] in ['09', '10', '11']:
            fall.append(dateList[i][0])
    print("All season are in the list.")
    return len(winter), len(spring), len(summer), len(fall)
    