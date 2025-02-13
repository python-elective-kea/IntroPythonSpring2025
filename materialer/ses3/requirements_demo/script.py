import requests

req = requests.get('https://github.com/python-elective-kea/IntroPythonSpring2025/blob/main/lessons/ses3.md')
# print(req.text)

f = open('index.html', 'w')
f.write(req.text)



