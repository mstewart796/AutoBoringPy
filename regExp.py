import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Call me 415-555-1234 today, or 415-555-4321 on my office line tomorrow'))
