import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)

print(len(res.text))

print(res.text[:500])

playFile = open('RomeoAndJulia.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
