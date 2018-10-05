import numpy as np
import matplotlib.pyplot as plt
from sim import ImageMaker
import yaml

fin = open('config_files/simplest.config','r')
config = yaml.safe_load(fin)
maker = ImageMaker(config)

for i in range(5):
    one_img = maker.get_one()
    scene_img = maker.get_scene()
    print one_img.shape,scene_img.shape
    plt.figure(i+1,figsize=(10,5))
    plt.subplot(1,2,1)
    plt.pcolor(one_img,cmap='jet')
    plt.tight_layout()
    plt.subplot(1,2,2)
    plt.pcolor(scene_img,cmap='jet')
    plt.tight_layout()
    plt.show()
