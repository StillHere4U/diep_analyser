from pydicom import dcmread

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile
import yaml

configs = []
with open('pre_config.yaml', 'r') as file:
    configs.append(yaml.safe_load(file))
with open('post_config.yaml', 'r') as file:
    configs.append(yaml.safe_load(file))
anims = []
volumes = []
# Load files
for config in configs:
    file_list = [f for f in listdir(config["path"]) if isfile(config["path"] + "/" + f)]
    file_list.sort()
    all_files = file_list[config["first_frame"]: config["last_frame"]]
    fig = plt.figure()
    frames = []
    volumes = []
    for file in all_files:
        ds = dcmread(config["path"] + file)
        arr = ds.pixel_array[config["ymax"]:config["ymin"], config["xmin"]:config["xmax"]]    
        vein_mask = (arr > config["threshold"]).astype(np.uint8)
        
        # Compute surface
        pixel_area = ds.PixelSpacing[0] * ds.PixelSpacing[1]  # mm²
        surface = np.sum(vein_mask) * pixel_area  # mm²
        volumes.append(surface)

        # Generate animation
        frames.append([plt.imshow(vein_mask,cmap='gray',animated = True)])

    # Compute total volume
    slice_thickness = ds.SliceThickness  # mm
    total_volume = np.sum(volumes) * slice_thickness  # mm³
    volumes.append(total_volume)
    print(f"Volume total de la veine : {total_volume} mm³")

    anims.append(animation.ArtistAnimation(fig, frames, interval = 200 , blit = True, repeat_delay=1000))

print(f"The volume of the vein has increased by: {np.round((volumes[1]/volumes[0 ] - 1)* 100,2)}%")
plt.show()
