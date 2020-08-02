import re

pattern = re.compile(r'[\w.-]+@[\w.]+')
r = pattern.findall('Please come to the counter and show the invitation letter send to nrdev10@gmail.com . Please don\'t forget it. You can send a request to send the invitation again at this email niloy.mail@gmail.com or niloy.connect@outlook.com')
print(r)
