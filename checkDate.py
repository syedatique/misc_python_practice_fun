import datetime, pdb
delta = datetime.timedelta(days=30)
now = datetime.datetime.now()
# now = datetime.datetime(2016, 12, 29)
newDate = now + delta

newDay=newDate.strftime("%A")

# pdb.set_trace()
if newDay == "Saturday":
    expDate = newDate - datetime.timedelta(days=1)
elif newDay == "Sunday":
    expDate = newDate + datetime.timedelta(days=1)
else:
    expDate = newDate

expDate = expDate.strftime("%Y-%m-%d")

print expDate, type(expDate)