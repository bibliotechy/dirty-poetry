import psycopg2
from random import choices

#"select metre, nonsense_percent from lines group by nonsense_percent, metre  having count(*) > 50 ORDER BY nonsense_percent DESC;"


connection = psycopg2.connect("user=postgres password=postgres dbname=dirty_poetry host=127.0.0.1")
cursor = connection.cursor()

# given a rhyme scheme "ABBA BCCB CBBC BAAB"
# find three seperate final phones groups A, B, C
# try to find a matching metre for all lines
# otherwise, just try to find matching 



cursor.execute("select metre, final_phonemes from lines where nonsense_percent BETWEEN .1 and .5  AND length(metre) > 6 GROUP BY final_phonemes, metre HAVING count(*) > 10;")
options = cursor.fetchall()

num_options = len(options)
num_different_rhymes_needed = 8

rhymes = choices(options, k=num_different_rhymes_needed)

lines = {}

for i, rhyme in enumerate(rhymes):
    cursor.execute("select distinct original from lines where metre=%s and final_phonemes=%s::varchar[];", rhyme)
    rhyme_lines = cursor.fetchall()
    lines[chr(65 +i)] = choices(rhyme_lines, k=4)

cursor.execute("select original from lines where original LIKE '%poetry%' OR original LIKE '%poem%'")
title = choices(cursor.fetchall())[0]

rhythm = " ABBA BAAB CDDC DCCD EFFE FEEF GHHG HGGH"

print(title[0])
for char in rhythm:
    if char == " ":
        print("\n")
    else:
        print(lines[char].pop()[0])

cursor.close()
connection.close()
