import sys
import csv

csv.field_size_limit(sys.maxsize)

# extract user_id and friend_id and write to separate csv
with open("user.csv","rb") as source:
    rdr= csv.reader( source )
    with open("two-column.csv","wb") as result:
        wtr= csv.writer( result )
        for r in rdr:
            wtr.writerow( (r[0], r[4]) )

#generate edgelist of string
header = True

with open('two-column.csv') as inCSV:
    writer = csv.writer(open('edgelist.csv', 'wb'))
    for line in inCSV.readlines():
        column1, column2 = [_.strip() for _ in line.split(',',1)]
        if header:
            writer.writerow(('source','target'))
            header = False
        else:
            temp=column2.replace("[","]").replace("]"," ").replace('"','').split(",")
            for i in range(len(temp)):
                data=(column1,temp[i])
                writer.writerow(data)

#convert string to int to save space
with open('edgelist.csv') as inCSV1:
    reader=csv.reader(inCSV1)
    writer = csv.writer(open('edgeint.csv', 'wb'))
    for row in reader:
        k=hash(row[0])
        l=hash(row[1])
        writer.writerow((k,l))