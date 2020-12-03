# -*- coding: utf-8 -*-

import pandas as pd
import csv
from xml.etree import ElementTree as ET
import os

cols = ['id','author', 'title', 'genre', 'price','publish_date','description']
rows = []

# Parse XML file
tree = ET.parse('book.xml')
root = tree.getroot()
for elem in root:
    id = elem.attrib.get('id')
    author = elem.find("author").text
    title = elem.find("title").text
    genre = elem.find("genre").text
    price = elem.find("price").text
    publish_date = elem.find("publish_date").text
    description = elem.find("description").text

    rows.append({"id": id,
                 "author": author,
                 "title": title,
                 "genre": genre,
                 "price": price,
                 "publish_date": publish_date,
                 "description": description
                 })

df = pd.DataFrame(rows, columns=cols)

# write dataframe to csv
df.to_csv('123.csv')


