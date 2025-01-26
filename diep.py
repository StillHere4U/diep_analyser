from pydicom import dcmread
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation
import numpy as np
from pydicom.data import get_testdata_file
from os import listdir
from os.path import isfile, join

path1 = "ScalarVolume_14/"
path2 = "ScalarVolume_12/"

xmin = 250
xmax = 280
ymin = 186
ymax = 160

pxmin = -80
pxmax = -50

xmin2 = 240
xmax2 = 255
ymin2 = 146
ymax2 = 107

imgages1 = [74,75,76,77]

onlyfiles1 = [f for f in listdir(path1) if isfile(join(path1, f))]
onlyfiles1.sort()
onlyfiles2 = [f for f in listdir(path2) if isfile(join(path2, f))]
onlyfiles2.sort()

selected1 = onlyfiles1[74]
selected2 = onlyfiles2[290]


fig = plt.figure()
ds = dcmread(path1 + selected1)
print(ds.PixelData[:2])
arr = ds.pixel_array
#arr_crop = arr[ymax2:ymin2,xmin2:xmax2].copy()
arr_crop = arr[ymax:ymin,xmin:xmax].copy()
print(np.sum(arr_crop > -68))
print(np.amin(arr))

print(np.amax(arr))
#arr[arr<150] = 0
#plt.imshow(arr,cmap='gray', vmin=-255, vmax=255, animated = True)

#plt.show()
#plt.imshow(arr_crop,cmap='gray', vmin=pxmin, vmax=pxmax, animated = True)
plt.imshow(arr_crop,cmap='gray', vmin=pxmin, vmax=pxmax, animated = True)

plt.show()

