from bs4 import BeautifulSoup
from datetime import datetime
import sys
inputfile= sys.argv[1]
inputfile=open(inputfile)
soup=BeautifulSoup(inputfile)
for rra in soup.findAll('rra'):
    rows=rra.database.findAll('row')
    for row in rows:
        value=float(row.v.contents[0])
        epoch_time=int(row.previous_sibling.previous_sibling.split('/')[1])
        event_time=datetime.fromtimestamp(epoch_time)
        print("Time= %s Value=%f" % (event_time.strftime("%Y-%m-%d %H:%M:%S"),value))
