import math
from datetime import date, timedelta

def is_prime(number):

    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for divisibility from 2 up to the square root of the number
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False  # If divisible, it's not prime

    return True  # If no divisors found, it's prime

def daterange(start_date: date, end_date: date):
    days = int((end_date - start_date).days)
    for n in range(days):
        yield start_date + timedelta(n)

start_date = date(2000, 1, 1)  #Code start date
end_date = date(2100, 1, 1)    #Code end date


for single_date in daterange(start_date, end_date):
    us=int(single_date.strftime("%m%d%y"))
    eu=int(single_date.strftime("%d%m%y"))
    iso=int(single_date.strftime("%Y%m%d"))
    if is_prime(us) and is_prime(eu) and is_prime(iso):
        print(single_date.strftime("%Y%m%d"))
