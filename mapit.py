#! python3

import webbrowser, sys, pyperclip

sys.argv

# Check if command line arguments were passed
if len(sys.argv) > 1:
    #['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.]
    address = ' '.join(sys.argv[1:])
else:
    addresss = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
