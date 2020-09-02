from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv
import io
import numpy as np

inFile = io.open('business1.csv', 'r', encoding='utf-8'
)
reader = csv.reader(inFile, dialect='excel')
header=True

lon = []
lat = []
for row in reader:
    if header:
        pass
    else:
        if float(row[7]) != 0.0 and float(row[8]) != 0.0:
            lon.append(float(row[8])), lat.append(float(row[7]))

m = Basemap(projection='merc', \
            llcrnrlat=-60, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, lat_ts = 20, resolution = 'c')

m = Basemap(projection='ortho', lon_0=-30, lat_0=20, resolution='l')

m.drawcountries()
m.drawcoastlines()
m.drawmapboundary(fill_color='#B7D3E3')
m.fillcontinents(color='white', lake_color='black', zorder=0)

x, y = m(lon, lat)
m.scatter(x, y, 15, marker='o', color='red', alpha=0.3)

parallels = np.arange(-60., 81, 30.)
m.drawparallels(parallels, labels=[0, 1, 1, 0], linewidth=0.5)
meridians = np.arange(10., 351., 30.)
m.drawmeridians(meridians, labels=[1, 0, 0, 1], linewidth=0.5)

plt.show()