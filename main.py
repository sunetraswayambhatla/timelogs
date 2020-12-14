from datetime import datetime,timedelta
import re

                                                      #converting time to 24H Format
def timeconvert(st1):
      if st1[1:2]==':':                               #changing Single digit Hour to two digits hours(i.e. 2:00 -> 02:00)
           st1='0'+st1
      if st1[-2:] == "am" and st1[:2] == "12":
         return "00" + st1[2:-2]
      elif st1[-2:] == "am":
         return st1[:-2]
      elif st1[-2:] == "pm" and st1[:2] == "12":
         return st1[:-2]
      else:
           return str(int(st1[:2]) + 12) + st1[2:5]
    

fname= input("Enter file name")
                                                      #regular expression used to extract time values of format "HH:MM(am/pm) - HH:MM(am/pm)"
regx='([0-1]?[0-9]:[0-5][0-9][ap]m - [0-1]?[0-9]:[0-5][0-9][ap]m)'
thours=timedelta()
fhand = open(fname)
for line in fhand:
    times=re.findall(regx,line)                       #times now stores all the 'from - to' time values of the file
    for t in times:
        hrs=t.split(' - ')
        starttime=timeconvert(hrs[0])
        endtime=timeconvert(hrs[1])
        t1=datetime.strptime(starttime,"%H:%M")
        t2=datetime.strptime(endtime,"%H:%M")
        tdelt=(t2-t1)
        ch=str(tdelt)
                                                     # correcting negative value time differences by adding 1 day if hours less than 12 ; 12 hours if hours more that 12 hrs
        if ch[0:1]=='-' and ch[9:10]==':':
             tdelt=tdelt+timedelta(days=1)
        elif ch[0:1]=='-' and ch[9:10]!=':':
             tdelt=tdelt+timedelta(hours=12)     
        #print(tdelt)
        thours+=tdelt
            

print('time spent: ', thours)
