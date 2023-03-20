import json
import hashlib
from SQLHelper import SQLUtilities


class TableCheck(object):
    def CheckTable(self, testHash, numDigits, checkHashes, chainLen, collisions):
        dictionaryFile = 'dictionary{0}.json'.format(numDigits)
        with open(dictionaryFile) as json_file:
            data = json.load(json_file)
            loop = False
            testHash2 = testHash
            while (loop == False):
                if testHash2 in data.values() and testHash2 not in checkHashes:
                    key = list(filter(lambda x: data[x] == testHash2, data))
                    loop = True
                else:
                    testHash2 = hashlib.sha256(
                        testHash2.encode('utf-8')).hexdigest()
                    testHash2 = testHash2[:numDigits]
        json_file.close()
        for k in key:
            t = hashlib.sha256(
                k.encode('utf-8')).hexdigest()
            t = t[:numDigits]
            # Check first Val
            if (t == testHash and k not in collisions):
                return True, k
            # If not first val
            for j in range(chainLen - 1):
                inputX = t
                t = hashlib.sha256(
                    t.encode('utf-8')).hexdigest()
                t = t[:numDigits]
                if (t == testHash and inputX not in collisions):
                    return True, inputX
        return False, testHash2

    def CheckSQLTable(self, testHash, numDigits, checkedHashes, chainLen, collisions, tableName):
        loop = False
        SQ = SQLUtilities()
        testHash2 = testHash
        while (loop == False):
            key = SQ.QueryDB(tableName, testHash2)
            if len(key) > 0 and testHash2 not in checkedHashes:
                loop = True
            else:
                testHash2 = hashlib.sha256(
                    testHash2.encode('utf-8')).hexdigest()
                testHash2 = testHash2[:numDigits]
        for k in key:
            t = hashlib.sha256(
                k.encode('utf-8')).hexdigest()
            t = t[:numDigits]
            # Check first Val
            if (t == testHash and k not in collisions):
                return True, k
            # If not first val
            for j in range(chainLen - 1):
                inputX = t
                t = hashlib.sha256(
                    t.encode('utf-8')).hexdigest()
                t = t[:numDigits]
                if (t == testHash and inputX not in collisions):
                    return True, inputX
        return False, testHash2
