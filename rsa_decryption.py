cipher = [17645, 100861, 96754, 160977, 120780, 90338, 130962, 74096,
128123, 25052, 119569, 39404, 6697, 82550, 126667, 151824,
80067, 75272, 72641, 43884, 5579, 29857, 33449, 46274,
59283, 109287, 22623, 84902, 6161, 109039, 75094, 56614,
13649, 120780, 133707, 66992, 128221]

numbers = []
for i in cipher:
  for j in range(1,162991) :
    if (j**13) % 162991 == i:
      numbers.append(j)
    
# numbers = [
#     17509, 24946, 8258, 28514, 11296, 25448, 25955, 27424,
#     29800, 26995, 8303, 30068, 11808, 26740, 29808, 29498,
#     12079, 30583, 30510, 29557, 29302, 25961, 27756, 24942,
#     25445, 30561, 29795, 26670, 26991, 12064, 21349, 25888,
#     31073, 11296, 16748, 26979, 25902
# ]
print(numbers)
for num in numbers:
  print(chr(num), end='')