import time
import os
from options.test_options import TestOptions
from data.data_loader import CreateDataLoader
from models.models import create_model
from util.visualizer import Visualizer
from util import html
import cv2

opt = TestOptions().parse()
opt.nThreads = 1   # test code only supports nThreads = 1
opt.batchSize = 1  # test code only supports batchSize = 1
opt.serial_batches = True  # no shuffle
opt.no_flip = True  # no flip

data_loader = CreateDataLoader(opt)
dataset = data_loader.load_data()
model = create_model(opt)
visualizer = Visualizer(opt)
i=0
data1={}
for i, data in enumerate(dataset):
    data1=data
    if i>0:
        break;
# create website
web_dir = os.path.join(opt.results_dir, opt.name, '%s_%s' % (opt.phase, opt.which_epoch))
webpage = html.HTML(web_dir, 'Experiment = %s, Phase = %s, Epoch = %s' % (opt.name, opt.phase, opt.which_epoch))
# test
for i, data in enumerate(dataset):
    #if i >= opt.how_many:
    #    break
    #print(str(data))
    #print(str(dataset))

    model.set_input(data)
    #print (iter(dataset))
    #print (data)
    #print (data1)
    #print (data['3'].shape)
    model.test()
    visuals = model.get_current_visuals()
    img_path = model.get_image_paths()
    cv2.imwrite("2.png", visuals['fake_B'])
    #print(len(visuals))
    print('%04d: process image... %s' % (i, img_path))
    visualizer.save_images(webpage, visuals, img_path)

webpage.save()
