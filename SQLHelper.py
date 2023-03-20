import sqlite3
import json


class SQLUtilities(object):
    def LoadDb(self, fileName, tableName):
        dictionaryFile = 'dictionary{}.json'.format(fileName)
        p = open(dictionaryFile)
        dictData = json.load(p)
        print("Loaded Data from {}".format(dictionaryFile))

        conn = sqlite3.connect('TMTO.db')
        c = conn.cursor()
        table = """CREATE TABLE IF NOT EXISTS {}(KEY VARCHAR(6), VAL VARCHAR(6));""".format(
            tableName)
        c.execute(table)

        print("Creating Params for {}".format(tableName))
        params = [tuple(i) for i in dictData.items()]
        c.executemany(
            'INSERT INTO {} VALUES (?,?)'.format(tableName), params)

        print("Data Inserted into {0}".format(tableName))
        # Commit your changes in the database
        conn.commit()

        # Closing the connection
        conn.close()

    def QueryDB(self, tableName, targetVal):
        retVal = []
        conn = sqlite3.connect('TMTO.db')
        c = conn.cursor()
        data = c.execute(
            '''SELECT Key, Val FROM {} WHERE Val = '{}' '''.format(tableName, targetVal))
        for row in data:
            retVal.append(row[0])  # Selects Key
        return retVal

    def DeleteTable(self, tableName):
        conn = sqlite3.connect('TMTO.db')
        c = conn.cursor()
        c.execute("DELETE FROM {}".format(tableName))
        c.execute("Drop TABLE {}".format(tableName))
