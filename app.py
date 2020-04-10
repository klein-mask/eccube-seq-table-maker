import pandas as pd
import sys


class SqlMaker:
    
    def __init__(self, input_file):
        self.input_file = input_file
        self.output_path = './output/'
        self.df = pd.read_csv(input_file, names=('Table', 'Value'))
    
    def exec(self, *args):
        print(args)
        for arg in args:
            if arg == 'create':
                self.create()
            elif arg == 'input':
                self.input()
            elif arg == 'alter':
                self.alter()
    
    def create(self):
        query = []
        for row in self.df.itertuples():
            s = "CREATE TABLE {table} (`sequence` int(11) NOT NULL AUTO_INCREMENT,PRIMARY KEY (`sequence`)) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;".format(table=row.Table)
            query.append(s)
        query = '\n'.join(query)

        self.output(query, self.output_path + 'create.sql')

    def input(self):
        query = []
        for row in self.df.itertuples():
            s = "INSERT INTO {table} VALUES ({value});".format(table=row.Table, value=(row.Value + 1))
            query.append(s)
        query = '\n'.join(query)

        self.output(query, self.output_path + 'input.sql')

    def alter(self):
        query = []
        for row in self.df.itertuples():
            s = "ALTER TABLE {table} AUTO_INCREMENT={value};".format(table=row.Table, value=(row.Value + 1))
            query.append(s)
        query = '\n'.join(query)

        self.output(query, self.output_path + 'alter.sql')

    def output(self, query, file):
        with open(file, mode='w') as f:
            print(query, file=f)

if __name__ == '__main__':
    args = sys.argv
    if len(args) >= 3:
        input = args[1]
        queries = args[2:]

        SM = SqlMaker(input)
        SM.exec(*queries)
