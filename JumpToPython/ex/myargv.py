import sys

data_list = sys.argv[1:]
result = 0
for data in data_list:
    result += int(data)

print(result)