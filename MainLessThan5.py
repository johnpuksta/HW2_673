from TableGenerator import TableGenerator
from PasswordGenerator import PasswordGenerator
from CheckTable import TableCheck
import hashlib

# Number of digits being cracked, 2 digits = 1 byte = 8 bits
# Only use Digits 1..5, use other file for greater than 5
numDigits = 3
# Length of each chain generated in dictionary
lenChains = 10

# Run once to generate all passwords and chains for specified num bytes, uncomment if numDigits changes
PG = PasswordGenerator()
# PG.GenerateHexAllCombinations(numDigits)
# TG = TableGenerator()
# TG.Generate(numDigits, lenChains)

# Generate random password to crack
testPass = PG.GenerateRandomPassword(numDigits)
testHash = hashlib.sha256(testPass.encode('utf-8')).hexdigest()
testHash = testHash[:numDigits]
print("Randomly generated password is: {0} and it's given hash is: {1}".format(
    testPass, testHash))

CT = TableCheck()
checkedHashes = []
collision = []


def checkHashes(testHash, numDigits, lenChains, checkedHashes, collisions):
    solvedInput = [False, 0]
    while (solvedInput[0] == False):
        solvedInput = CT.CheckTable(
            testHash, numDigits, checkedHashes, lenChains, collisions)
        checkedHashes.append(solvedInput[1])
    verifiedRes = hashlib.sha256(
        solvedInput[1].encode('utf-8')).hexdigest()
    verifiedRes = verifiedRes[:numDigits]
    return verifiedRes, checkedHashes, solvedInput


verifiedRes, checkedHashes, solvedInput = checkHashes(
    testHash, numDigits, lenChains, checkedHashes, collision)

loop = False
while (loop == False):
    if (verifiedRes == testHash and solvedInput[1] == testPass):
        print("X: {0} is the inverse of the hash of Y: {1} ".format(
            solvedInput[1], testHash))
        loop = True
    elif (verifiedRes == testHash):
        print("X: {0} is the inverse of the hash of Y: {1} but does is not equal to testPass: {2}".format(
            solvedInput[1], testHash, testPass))
        collision.append(solvedInput[1])
        verifiedRes, checkedHashes, solvedInput = checkHashes(
            testHash, numDigits, lenChains, checkedHashes, collision)
    else:
        print("Could not find inverse of the hash Y: {0}".format(testHash))
        loop = True
