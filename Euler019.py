import datetime

sd = datetime.date(1901,1,1).toordinal()
ed = datetime.date(2000,12,13).toordinal()

A = [datetime.date.fromordinal(i) for i in range(sd,ed+1)]
B = [a for a in A if a.isoweekday() == 7 and a.day == 1]
print len(B)