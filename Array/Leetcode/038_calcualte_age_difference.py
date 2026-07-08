from datetime import datetime
from dateutil.relativedelta import relativedelta
start = datetime.strptime("1998-09-12 00:00:00", "%Y-%m-%d %H:%M:%S")
end = datetime.strptime("2001-05-07 00:00:00", "%Y-%m-%d %H:%M:%S")

diff = relativedelta(end, start)
delta = end - start

years = diff.years
months = years * 12 + diff.months

days = delta.days
hours = int(delta.total_seconds() // 3600)
minutes = int(delta.total_seconds() // 60)
seconds = int(delta.total_seconds())

print(f"{years} years = {months} months = {days} days")
print(f"{months} months = {days} days")
print(f"{days} days = {hours} hours")
print(f"{hours} hours = {minutes} minutes")
print(f"{minutes} minutes = {seconds} seconds")