import datetime
from datetime import date

now = date(2024, 3, 25)

if now is datetime.date:
    print('yes')
else:
    print('no')

# Date = date(2021, 7, 4)
#
# print("Date is", Date)