from os import name
from re import A
import psycopg2
import threading
import pandas as pd

con = psycopg2.connect(
database = "movies",
user = "postgres",
password="1234",
host = "localhost",
port = "5432"

)


query_1 = '''
          select * from public.func_csv fc limit 1 
          '''


query_2 = '''
          select * from public.func_csv fc limit 10 
          '''

name_1 = 'func_1'

name_2 = 'fun_2'


def select_one(query_string,con,name):
    cur = con.cursor()
    cur.execute(query_string)
    tuples = cur.fetchall()
    df = pd.DataFrame(tuples)
    df.to_csv('{}.csv'.format(name))

    


y = threading.Thread(target=select_one,args=(query_1,con,name_1,))
x = threading.Thread(target=select_one,args=(query_2,con,name_2,))

y.start()
x.start()

x.join()
y.join()

print('Nintendo')