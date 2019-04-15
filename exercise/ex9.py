import math

def simple_benefit(total, rate, year):
	return total * math.pow(1 + rate, year)
	
print(simple_benefit(332500, 0.045, 5))


def year_benefit(per_year, n, rate):
	if n == 1:
		return per_year * (1 + rate)
	else:
		return (year_benefit(per_year, n - 1, rate) + per_year) * (1 + rate)
	
for i in range(1, 11):
	print(i, year_benefit(66500, i, 0.045))