
import pandas as pd
import datetime
 
##Cataloguing marks
subs = {}
 
for i in range(int(input("Number of subjects: "))):
    subs[input("Enter Subject "+str(i+1)+ ": ")] = {}
 
print("")
print("List of subjects",list((subs.keys())))
 
exams = []
for i in range(int(input("Number of exams written till now: "))):
    exams.append(input("Enter exam "+ str(i+1)+ " (eg: ut1,sa1,tee1): "))
 
print("")
print("MARKS ENTRY")
print("")
print("Entry Format: Marks obtained/Total marks")
for exam in exams:
    print("Enter", exam, "marks: ")
    for sub in subs.keys():
        m = input(sub+" :").split('/')
        subs[sub][exam] = float(m[0])*100.0//float(m[1]) #normalizing
 
print("")
print("Your marks so far: \n")
df = pd.DataFrame(subs)
df.loc["avg"] = df.mean()
print(df)
print("Your lowest grades are in", df.loc["avg"].idxmin(),"\n\n")
print("Enter upcoming exam dates")
exams = {}
for sub in subs:
    exams[datetime.datetime.strptime(input("Enter date(dd/mm/yy) for "+str(sub)+": "), '%d/%m/%y')] = sub
 
exam_dates = list(exams.keys())
exam_dates.sort()
 
prep_days = int(input("No. of days to prepare for the exam: "))
 
calendar = {}
 
day_1 = datetime.timedelta(days=1)
i = exam_dates[-1] - day_1
sub = exams[exam_dates[-1]]
while i>= exam_dates[0]:
    calendar[i] = sub
    i -= day_1
    if i+day_1 in exam_dates:
        sub = exams[i+day_1]
 
calendar[i] = exams[i+day_1]
calendar[i - day_1] = exams[i+day_1]
prep_days -= 2
i = i - day_1 - day_1
 
lowest = min(df.loc["avg"])
study_drist = []
for m in list(df.loc["avg"]):
    study_drist.append(lowest/m)
s = sum(study_drist)
for j in range(len(study_drist)):
    study_drist[j] = round(study_drist[j]*prep_days/s)
 
study = {}
for j in range(len(df.columns)):
 study[df.columns[j]] = study_drist[j]
 
exam_dates.reverse()
 
for exam_d in exam_dates:
    sub = exams[exam_d]
    for j in range(study[sub]):
        calendar[i] = sub
        i = i- day_1
 
print("Creating ur exam time table...")
 
dates = list(calendar.keys())
dates.sort()
print("\n DATE  || SUBJECT")
for date in dates:
    if date.day>9:
        print(" "+str(date.day) + "-"+str(date.month)+ "  || " +calendar[date])
    else:
        print(" "+str(date.day) + "-"+str(date.month)+ "   || " +calendar[date])
