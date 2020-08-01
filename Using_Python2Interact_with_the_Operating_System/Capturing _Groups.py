''' Fix the regular expression used in the rearrange_name function so that it can match middle names, middle initials, as well as double surnames. '''

import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*) (\w?\.)$", name)
    #print(result)
    if result == None:
        return name
    return "{} {} {}".format(result[2], result[3], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)
