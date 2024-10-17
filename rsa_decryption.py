cipher = [17645, 100861, 96754, 160977, 120780, 90338, 130962, 74096,
128123, 25052, 119569, 39404, 6697, 82550, 126667, 151824,
80067, 75272, 72641, 43884, 5579, 29857, 33449, 46274,
59283, 109287, 22623, 84902, 6161, 109039, 75094, 56614,
13649, 120780, 133707, 66992, 128221]

asciis = []

#convert to asciis using this formular: {\text{Cipher}} = (\text{ASCII})^{e_{\text{Bob}}} \mod n_{\text{Bob}}
for i in cipher:
  for j in range(1,162991) :
    if (j**13) % 162991 == i:
      asciis.append(j)

print(asciis, end='\n')
    
# asciis = [
#     17509, 24946, 8258, 28514, 11296, 25448, 25955, 27424,
#     29800, 26995, 8303, 30068, 11808, 26740, 29808, 29498,
#     12079, 30583, 30510, 29557, 29302, 25961, 27756, 24942,
#     25445, 30561, 29795, 26670, 26991, 12064, 21349, 25888,
#     31073, 11296, 16748, 26979, 25902
# ]

#convert ASCII Numbers to Readable Text
for num in asciis:
  print(chr(num), end='')
  
#ASCII Numbers to Hexadecimal
hex_values = []
for value in asciis:
  hex_values.append(hex(value))

print(hex_values, end='\n')

#hexadecimal numbers into one string and covert each consecutive pair to a character
hex_string = ''.join(hex_values).replace('0x', '')
print(hex_string, end='\n')
# 4465617220426f622c20636865636b2074686973206f75742e2068747470733a2f2f7777772e7375727665696c6c616e636577617463682e696f2f205365652079612c20416c6963652e

ascii_chars = ''
for i in range(0, len(hex_string), 2):
    ascii_chars += chr(int(hex_string[i:i+2], 16))

print(ascii_chars, end='\n')
# Dear Bob, check this out. https://www.surveillancewatch.io/ See ya, Alice.