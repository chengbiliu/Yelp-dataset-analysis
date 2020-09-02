import sys
import csv
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D
import numpy as np

csv.field_size_limit(sys.maxsize)

# with open("business.csv","rb") as source:
#     rdr= csv.reader( source )
#     with open("busSim.csv","wb") as result:
#         wtr= csv.writer( result )
#         for r in rdr:
#             wtr.writerow( (r[0], r[9], r[10],r[13]) )
#
# #generate edgelist of string
# header = True
#
# with open('busSim.csv') as inCSV:
#     writer = csv.writer(open('BusUnique.csv', 'wb'))
#     for line in inCSV.readlines():
#         column1, column2, column3, column4= [_.strip() for _ in line.split(',',3)]
#         if header:
#             writer.writerow(('ID','Stars','Count','Label'))
#             header = False
#         else:
#             temp=column4.replace("[","]").replace("]","").replace('"','').split(",")
#             for i in range(len(temp)):
#                 data=(column1,column2,column3,temp[i])
#                 writer.writerow(data)

# with open('BusUnique.csv') as inCSV:
#     writer = csv.writer(open('BusUnique.csv', 'wb'))
#     for line in inCSV.readlines():
#         print line[3]

df=pd.read_csv("BusUnique1.csv",sep=",")
df2 = df.groupby('Label').size()
toplist = df2.nlargest(10).index.to_series().tolist()
# toplist = ['Chinese','Korean','Mexican','French','German','Italian','Japanese','African','American (Traditional)','American (New)']

star=[]
reviewcount=[]
popular=[]
for item in toplist:
    topSeries = df[df['Label']==item]
    StarWeighted = np.average(topSeries["Stars"],weights=topSeries["Count"])
    star.append(StarWeighted)
    reviewcount.append(topSeries['Count'].sum())
    popular.append(topSeries['Count'].mean(axis=0))
    # color = [str(item / 255.) for item in y]
    # plt.scatter(x, y, s=500, c=color)
print star
print reviewcount
print popular
print np.average(popular)
labelcount = [int(a/b) for a,b in zip(reviewcount,popular)]

agg = pd.DataFrame({'ID':toplist,'star': star, 'reviewcount': reviewcount, 'popular':popular,'labelcount':labelcount})
print agg.sort(columns='popular')['star']

colorvariable = agg.sort(columns='star')['star']
norm = [float(i)/sum(colorvariable) for i in colorvariable]
norm = [float((i-3)*4.5)/5 for i in colorvariable]
color = [str(item) for item in norm]
print color

plt.bar(range(len(star)), agg.sort(columns='star')['popular'], align='center', color=color, edgecolor="black")
# plt.bar(range(len(popular)), popular, align='center', color=color, edgecolor="black")
# plt.bar(range(len(reviewcount)), agg.sort(columns='labelcount',ascending=False)['labelcount'], align='center', edgecolor="black")
# plt.bar(range(len(reviewcount)), agg.sort(columns='labelcount',ascending=False)['reviewcount'], align='center', edgecolor="black")
plt.xticks(range(len(reviewcount)), agg.sort(columns='star',ascending=True)['ID'], size='small',rotation=45)

for i, v in enumerate(sorted(star)):
    plt.text(i-.3, v, str("%.2f" % v), color='blue')

plt.savefig("image.png")
plt.title("Yelp Food Genres Rating and Popularity")
plt.ylabel("Number of Reviews Per Restaurant")
plt.xlabel("Genres")
plt.show()

