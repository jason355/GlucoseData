import datetime



#Find and count
def findCacu(lon1, lon2, dataList, listf, listtemp, listT):
    for j in range(lon2):
        for i in range(lon1):
            if listf[j] == dataList[i][0]:
                if dataList[i][2] != '':
                    get = [dataList[i][0], dataList[i][3], int(dataList[i][2])]
                    listtemp.append(get)
        longlu = len(listtemp)
        if longlu != 0:
            for l in range(longlu):
                if listtemp[l+1][0] != listtemp[l][0]:
                    if listtemp[l][1] == listtemp[l+1][1]:
                        listT.append(listtemp)

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
    londate = len(data)
    return londate