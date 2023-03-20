import json
import hashlib


class TableGenerator(object):
    def Generate(self, numDigits, lenChains):
        dataFile = 'data{0}.json'.format(numDigits)
        dictionaryFile = 'dictionary{0}.json'.format(numDigits)

        f = open(dataFile)
        data = json.load(f)

        p = open(dictionaryFile)
        alreadyComputed = json.load(p)

        dictionary = {}
        print("Generating chains")

        for i in range(len(data)):  # Number of chains
            if (data[i] not in alreadyComputed.keys()):
                t = hashlib.sha256(data[i].encode('utf-8')).hexdigest()
                for j in range(lenChains - 1):  # Length of chains
                    t = t[:numDigits]
                    t = hashlib.sha256(t.encode('utf-8')).hexdigest()
                t = t[:numDigits]
                dictionary.update({"{0}".format(data[i]): "{0}".format(t)})

        with open(dictionaryFile) as fp:
            dictObj = json.load(fp)
            dictObj.update(dictionary)

        with open(dictionaryFile, 'w') as outfile:
            json.dump(dictObj, outfile,
                      indent=4,
                      separators=(',', ': '))
        f.close()
        print("Finished generating chain")

    def GenerateLarge(self, numDigits, lenChains, fileNumber, start, end):
        dataFile = 'data{0}.json'.format(numDigits)
        dictionaryFile = 'dictionary{0}.json'.format(fileNumber)
        f = open(dataFile)
        data = json.load(f)

        # p = open(dictionaryFile)
        # alreadyComputed = json.load(p)

        dictionary = {}
        print("Generating chains")

        # for i in range(len(data)):  # Number of chains
        for i in range(start, end):
            # if (data[i] not in alreadyComputed.keys()):
            t = hashlib.sha256(data[i].encode('utf-8')).hexdigest()
            for j in range(lenChains - 1):  # Length of chains
                t = t[:numDigits]
                # t = json.dumps(t).encode('utf-8')
                # t = hashlib.sha256(t).hexdigest()
                t = hashlib.sha256(t.encode('utf-8')).hexdigest()
            t = t[:numDigits]
            dictionary.update({"{0}".format(data[i]): "{0}".format(t)})

        with open(dictionaryFile) as fp:
            dictObj = json.load(fp)
            dictObj.update(dictionary)

        with open(dictionaryFile, 'w') as outfile:
            json.dump(dictObj, outfile,
                      indent=4,
                      separators=(',', ': '))
        f.close()
        print("Finished generating chain")
