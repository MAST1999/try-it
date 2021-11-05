"""
EXAMINING: A LIST In this lab, the task is to read a set of temperature
data (the monthly high temperatures at Heathrow Airport for 1948 through
2016) from a file and then find some basic information: the highest and lowest temperatures, 
the mean (average) temperature, 
and the median temperature (the temperature in the middle if all the temperatures are sorted).
The temperature data is in the file lab_05.txt in the source code directory for
this chapter. Because I haven’t yet discussed reading files, here’s the code to
read the files into a list:
temperatures = []
with open('lab_05.txt') as infile:
for row in infile:
temperatures.append(int(row.strip())
You should find the highest and lowest temperature, the average, and the
median. You’ll probably want to use the min(), max(), sum(), len(),
and sort() functions/methods.
BONUS Determine how many unique temperatures are in the list.
"""

import os

file = "lab_05.txt"

dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\" + file

temperatures: list[float] = []
with open(dir_path, "r") as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

print("maximum temperatures: ", max(temperatures))
print("minimum temperatures: ", min(temperatures))
print("mean (average) temperatures: ", sum(temperatures) / len(temperatures))

sorted_temp = sorted(temperatures)
x = len(sorted_temp)


median1 = sorted_temp[x // 2]
print("median = ", median1)

unique_temperature = set(sorted_temp)
print(len(unique_temperature))
