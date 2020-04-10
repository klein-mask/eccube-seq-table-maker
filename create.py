import pandas as pd
import sys

def create_sql(file):
    df = pd.read_csv(file, names=('Table', 'Value'))

    with open('./output/create_seq_tables.sql', mode='w') as f:
        data = []
        for row in df.itertuples():
            s = "CREATE TABLE {table} (`sequence` int(11) NOT NULL AUTO_INCREMENT,PRIMARY KEY (`sequence`)) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;\nINSERT INTO {table} VALUES ({value});".format(table=row.Table, value=(row.Value + 1))
            data.append(s)

        print('\n'.join(data), file=f)


if __name__ == "__main__":
    args = sys.argv
    if len(args) >= 2:
        create_sql(args[1])