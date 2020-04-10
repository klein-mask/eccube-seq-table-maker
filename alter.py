import pandas as pd
import sys

def alter_sql(file):
    df = pd.read_csv(file, names=('Table', 'Value'))

    with open('./output/alter_seq_tables.sql', mode='w') as f:
        data = []
        for row in df.itertuples():
            s = "ALTER TABLE {table} AUTO_INCREMENT={value};".format(table=row.Table, value=(row.Value + 1))
            data.append(s)

        print('\n'.join(data), file=f)


if __name__ == "__main__":
    args = sys.argv
    if len(args) >= 2:
        alter_sql(args[1])