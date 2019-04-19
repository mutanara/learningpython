import datetime

#1
today = datetime.date.today()
text1 = '{today.month}/{today.day}/{today.year}'.format(today=today)
print(text1)

#2
text2 = today.strftime('%-m/%-d/%y')
print(text2)

#3
now = datetime.datetime.utcnow() #utc time
text3 = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print(text3)

#4
now = datetime.datetime.now() #local time
date_text = now.strftime('%Y/%m/%d %H:%M:%S.%f') #[:-3]
text4 = "Time is: %s" %(date_text)
print(text4)

#5
now = datetime.datetime.now()
date_text = now.strftime('%B %d, %Y %H:%M:%S.%f %p')
text5 = "Time is %s" %(date_text)
print(text5)

#6
now = datetime.datetime.now()
date_text = now.strftime('%x')
text6 = "Time is %s" %(date_text)
print(text6)