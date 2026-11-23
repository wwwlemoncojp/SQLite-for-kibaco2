import sqlite3
import pandas as pd

# pandasでカレントディレクトリにあるcsvファイルを読み込む
# csvには、1列目にID, 2列目にname, 3列目にaddressが入っているとする。
df = pd.read_csv('enrollList.csv', encoding="cp932")

# カラム名（列ラベル）を作成。csv file内にcolumn名がある場合は、下記は不要
# pandasが自動で1行目をカラム名として認識してくれる。
df.columns = ['teacherID', 'lessonID', 'year', 'grade']

dbname = 'kibaco2.sqlite3'

conn = sqlite3.connect(dbname)
cur = conn.cursor()

# dbのnameをstudentとし、読み込んだcsvファイルをsqlに書き込む
# if_existsで、もしすでにstudentが存在していたら、書き換えるように指示
df.to_sql('lesson', conn, if_exists='replace')

# 作成したデータベースを1行ずつ見る
select_sql = 'SELECT * FROM lesson'
for row in cur.execute(select_sql):
    print(row)

cur.close()
conn.close()