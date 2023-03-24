import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('proj_0.sqlite')
sql_que = '''SELECT title, year, top_1 FROM top_1_in_20c'''
data = pd.read_sql(sql_que, conn)
x_1 = data.year
y_1 = data.top_1
labels = data.title
plt.bar(x_1, y_1)
plt.xticks(x_1, labels, rotation='vertical')
plt.title('The #1 Rated Movie of Each Year in the 20th Century')
plt.show()