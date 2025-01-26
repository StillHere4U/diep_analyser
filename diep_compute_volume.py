from pydicom import dcmread
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from os import listdir
from os.path import isfile
import yaml

with open('config_diep_12.yaml', 'r') as file:
    config = yaml.safe_load(file)


# Load the config
path = config["path"]
first_frame = config["first_frame"]
last_frame = config["last_frame"]
xmin = config["xmin"]
xmax = config["xmax"]
ymin = config["ymin"]
ymax = config["ymax"]
threshold = config["threshold"]
# Load files
file_list = [f for f in listdir(path) if isfile(path + "/" + f)]
file_list.sort()
all_files = file_list[first_frame: last_frame]
fig = plt.figure()
frames = []
volumes = []
for file in all_files:
    ds = dcmread(path + file)
    arr = ds.pixel_array[ymax:ymin, xmin:xmax]    
    vein_mask = (arr > threshold).astype(np.uint8)
    
    # Compute surface
    pixel_area = ds.PixelSpacing[0] * ds.PixelSpacing[1]  # mm²
    surface = np.sum(vein_mask) * pixel_area  # mm²
    volumes.append(surface)

    # Generate animation
    frames.append([plt.imshow(vein_mask,cmap='gray',animated = True)])

# Compute total volume
slice_thickness = ds.SliceThickness  # mm
total_volume = np.sum(volumes) * slice_thickness  # mm³
print(f"Volume total de la veine : {total_volume} mm³")

ani1 = animation.ArtistAnimation(fig, frames, interval = 200 , blit = True, repeat_delay=1000)

plt.show()
