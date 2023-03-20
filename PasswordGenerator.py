import secrets
import string
import json
from itertools import product


class PasswordGenerator(object):
    def GenerateHexAllCombinations(self, numDigits):
        dataFile = 'data{0}.json'.format(numDigits)
        print(
            "Generating all Hex combinations for {0} bytes".format(numDigits))
        retArr = []
        li = ['a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C',
              'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for comb in product(li, repeat=numDigits):
            val = ''.join(comb)
            retArr.append(val)
        with open(dataFile, 'w') as json_file:
            json.dump(retArr, json_file,
                      indent=4,
                      separators=(',', ': '))

    def GenerateRandomPassword(self, numDigits):
        return ''.join(secrets.choice(string.ascii_uppercase[:5] +
                                      string.ascii_lowercase[:5] + string.digits) for i in range(numDigits))
