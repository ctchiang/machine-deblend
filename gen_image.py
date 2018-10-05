import numpy as np
import matplotlib.pyplot as plt
from sim import ImageMaker
import yaml

fin = open('simplest.config','r')
config = yaml.safe_load(fin)
maker = ImageMaker(config)

for i in range(5):
    one_img = maker.get_one()
    scene_img = maker.get_scene()
    print one_img.shape,scene_img.shape
    plt.figure(i+1,figsize=(5.5,5))
    plt.pcolor(one_img,cmap='jet')
    plt.tight_layout()
    plt.show()
