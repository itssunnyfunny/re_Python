# Real Numbers -> floating = decimal
import sys
from decimal import Decimal
from fractions import Fraction as fraction

ideal_temp = 98.23
current_temp = 98.499999

print(f"Ideal temp { ideal_temp}")
print(f"Current temp {current_temp}")
print(f"DIfference temp {ideal_temp - current_temp}")
print(sys.float_info)
