import csv
import pandas, datetime
import Csv_process_season as P

#date-time lists and varibles
startdate = datetime.datetime(2021, 5, 3)
enddate = datetime.datetime(2022, 12, 24)


winter = []
spring = []
summer = []
fall = []

#got glucose
index = []
wintemp = []
wintime = [0] * 24
windata = [0] * 24
winterGlu = []
sprtemp = []
springGlu = []
springtime = [0] * 24
sprdata = [0] * 24
sumtemp = []
summerGlu = []
summertime = [0] * 24
sumdata = [0] * 24
falltemp = []
fallGlu = []
falltime = [0] * 24
falldata = [0] * 24
count = 0


with open("..//Glucose.csv", 'r',encoding="utf-8") as file:
    data = csv.reader(file)
    dataList = list(data)
    lon = len(dataList)
    lonS = P.Season(dataList, lon, winter, spring, summer, fall)
    print("First process...")
    P.find(lonS[0], lon, dataList, winter, wintemp)
    P.Caculate(wintemp, wintime, windata, index,winterGlu)
    print(winterGlu)

    print("Second process...")
    P.find(lonS[1], lon, dataList, spring, sprtemp)
    P.Caculate(sprtemp, springtime, sprdata, index,springGlu)
    print(springGlu)
    
    print("Third process...")
    P.find(lonS[2], lon, dataList, summer, sumtemp)
    P.Caculate(sumtemp, summertime, sumdata, index,summerGlu)
    print(summerGlu)
    
    print("Forth process...")
    P.find(lonS[3], lon, dataList, fall, falltemp)
    P.Caculate(falltemp, falltime, falldata, index, fallGlu)
    print(fallGlu)
file.close()


 
with open("..//Glucose outputSea.csv", 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    print("Writing ""Winter"" to file...")
    writer.writerows([index, winterGlu])
    print("Done.")
    writer.writerow(" ")
    print(f"Writing ""Spring"" to file...")
    writer.writerows([index, springGlu])
    print("Done")
    writer.writerow(" ")
    print(f"Writing ""Summer"" to file...")
    writer.writerows([index,summerGlu])
    print("Done")
    writer.writerow(" ")
    print(f"Writing ""Fall"" to file...")
    writer.writerows([index, fallGlu])
    print("Done")
    writer.writerow(" ")
file.close()  