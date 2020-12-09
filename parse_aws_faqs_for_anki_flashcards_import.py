#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests as req

# path where to write the files
output_dir = '/home/bkk/Downloads/'

# aws certified database specialty
faqs = ['rds', 'aurora', 'elasticache', 'dynamodb', 'neptune', 'documentdb',
        'elasticsearch-service', 'timestream', 'qldb', 'keyspaces', 'dms', 'redshift']

# separator symbol which divides question and answer
separator = '§'

for faq in faqs:
    f_out = open(output_dir + faq + '.txt', "w")

    resp = req.get('https://aws.amazon.com/' + faq + '/faqs/')
    soup = BeautifulSoup(resp.text, 'html.parser')

    answer = ''
    for tag in soup.find_all('p'):
        if tag.text.startswith('Q:'):
            # new question found. write back previous answer.
            if len(answer) > 1:
                f_out.write(" ".join(answer.strip().split()) + '\n')
            # write question and write separator symbol which distinguishes question and answer
            f_out.write(" ".join(tag.text.strip().split()) + separator)
            answer = ''
        else:
            answer = answer + tag.text.strip() + ' '

    f_out.write(answer)
    f_out.close()
