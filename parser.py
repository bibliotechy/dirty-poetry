import asyncio
import psycopg2
import os
from psycopg2.sql import Identifier, SQL
import time
from dirty_poetry.utils import get_final_phonemes, nonsense_metre, nonsense_percent, tokenizer
from aiofile import AIOFile, LineReader
import logging



 # CREATE TABLE lines (line_id serial PRIMARY KEY, original text, metre varchar(255), last_word varchar(255), final_phonemes varchar(10)[]);

nonsense_tokenizer = tokenizer()

logging.basicConfig(filename='parser.log', encoding='utf-8', level=logging.DEBUG)
with open("./words_alpha.txt") as f:
    real_words = f.read().split("\n")

connection = psycopg2.connect("user=postgres password=postgres dbname=dirty_poetry host=127.0.0.1")
cursor = connection.cursor()

#files = [os.path.join(path, name) for path, subdirs, files in os.walk("/Users/cbn/projects/chronam_ocr_pairtree/") for name in files]
files = ["/Users/cbn/projects/chronam_ocr_pairtree/punctuated-nonsense.txt"]

def main():
    #semaphore = asyncio.Semaphore(50)
    for file in files:
        with open(file) as f:
            for line_with_newline in f.readlines():
                start = time.time()            
                line = line_with_newline.rstrip()
                tokens = nonsense_tokenizer(line)
                line_metre = nonsense_metre(tokens, real_words)
                if "w" in line_metre: # if the are any real words found in the meter
                    line_hash = hash(line)
                    last_word = tokens[-1].text
                    last_metre = line_metre[-1]
                    final_phonemes = get_final_phonemes(last_word, last_metre)
                    np = nonsense_percent(line_metre)
                    # import pdb
                    # pdb.set_trace()
                    transforms_done = time.time()

                    cursor.execute("INSERT INTO lines (hash, original, metre, last_word, final_phonemes, nonsense_percent) VALUES (%s, %s, %s, %s, %s, %s);", (line_hash, line, line_metre, last_word, final_phonemes, np))
                    connection.commit()
                    sent_to_db = time.time()
                    logging.debug(f"Line processing took {transforms_done - start} seconds")
                    logging.debug(f"DB commit took {sent_to_db - transforms_done}")



# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

main()

cursor.close()
connection.close()
