

uid="armygo"
pw1="1q2w3e4r!!"
pw2="1q2w3e4r!!"

import re

def validity_test(id,pass1,pass2):
    id_array=list(id)
    pass_array=list(pass1)

    if len(id_array)<3 or len(id_array)>20:
        return False
    if not re.match("^[a-z0-9]*$", id):
        return False


    if len(pass_array)<8 or len(pass_array)>20:
        return False
    if not re.match("^[A-Za-z0-9!@#$]+$", pass1):
        return False
    if not re.match(".*[A-Za-z]+.*", pass1):
        return False
    if not re.match(".*[0-9]+.*", pass1):
        return False
    if not re.match(".*[!@#$]+.*", pass1):
        return False

    if pass1 != pass2:
        return False



    return True
if validity_test(uid,pw1,pw2):
    print("pass")
else:
    print("fail")
