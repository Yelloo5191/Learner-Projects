import pyinputplus as pyip


response = pyip.inputNum(prompt='Number: ')
print(response)

response = pyip.inputNum(prompt='Blank: ', blank=True)
print(response)

response = pyip.inputNum(prompt='Limit: ', limit=2)
print(response)

response = pyip.inputNum(prompt='Timeout: ', timeout=5)
print(response)

response = pyip.inputNum(prompt='Regex Roman Numeral: ', allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
print(response)
