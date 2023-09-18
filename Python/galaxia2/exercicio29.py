import datetime

data = input("digite a data: ")
data = datetime.datetime.strptime(data, "%d/%m/%Y")
print(data.date())
print(data.day - 1)
print((data + datetime.timedelta(days=365)))
