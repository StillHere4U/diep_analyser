from pydicom import dcmread
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation
import numpy as np
from pydicom.data import get_testdata_file
from os import listdir
from os.path import isfile, join

path1 = "dicom/dicom2/ScalarVolume_15/"
path2 = "dicom/dicom2/ScalarVolume_14/"

onlyfiles1 = [f for f in listdir(path1) if isfile(join(path1, f))]
onlyfiles1.sort()
onlyfiles2 = [f for f in listdir(path2) if isfile(join(path2, f))]
onlyfiles2.sort()

frames1 = []
fig1 = plt.figure()
for file in onlyfiles1 :
    ds = dcmread(path1 + file)
    arr = ds.pixel_array
    frames1.append([plt.imshow(arr,cmap='gray', vmin=-255, vmax=255, animated = True)])

frames2 = []
fig2 = plt.figure()
for file in onlyfiles2 :
    ds = dcmread(path2 + file)
    arr = ds.pixel_array
    frames2.append([plt.imshow(arr,cmap='gray', vmin=-255, vmax=255, animated = True)])

print(len(frames1))
print(len(frames2))
ratio = len(frames2) / len(frames1)
ani1 = animation.ArtistAnimation(fig1, frames1, interval = 10 , blit = True, repeat_delay=1000)

ani2 = animation.ArtistAnimation(fig2, frames2, interval = 10 / ratio, blit = True, repeat_delay=1000)

plt.show()


