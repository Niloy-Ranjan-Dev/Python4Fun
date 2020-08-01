''' Return true if the vowels a, e and i are seen sequenciallly with a consonent between them'''

import re
def check_aei (text):
    pattern = re.compile(r"[^aei]?[aei]?[^aei]+[aei]?[^aei]")
    result = re.search(pattern, text)
    return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True
