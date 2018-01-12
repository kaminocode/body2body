# body2body
Deep learning network to transfer body movements from one individual to another. Eg mimic dance steps. 
First of all, the project has not produced very promising results, all I intend to do is to give you a direction to think. I method used here can be adopted in many situations
For the motivation, let me walk you through some of the priliminary results. 

<a href="https://imgflip.com/gif/223qo6"><img src="https://i.imgflip.com/223qo6.gif" width="400" title="made at imgflip.com"/></a> <a href="https://user-images.githubusercontent.com/8917417/34599694-b5473646-f219-11e7-93dd-bf20136c8230"><img src="https://user-images.githubusercontent.com/8917417/34599694-b5473646-f219-11e7-93dd-bf20136c8230.gif" width="400" title="not made at imgflip.com"/></a> 

I agree the reconstruction is poor, but keep in mind the gan was trained on a 30 second superman animation. The superman video clearly didn't capture most of the required moviements and hence, the above result was expected.

Going into details of the project, I'll start with the basic idea. You just cant train a deep learning network from a given man to superman, because then the solution will be specific to that particular man. So you need something that is same for all people to stand as an intermediate layer. What I used is the pose estimation technique as given in the paper Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields. 

<a href="https://user-images.githubusercontent.com/8917417/34553776-56a15e34-f14f-11e7-8e15-cf2c20612b58"><img src="https://user-images.githubusercontent.com/8917417/34553776-56a15e34-f14f-11e7-8e15-cf2c20612b58.png" width="400" title="sticksuperman1"/></a>

I hence trained a conditional gan to map pose images to superman. Once the gan is trainied, all you need to do is take a video, convert it into frames,then the frames to poses(stick images :P) 
<a href="https://user-images.githubusercontent.com/8917417/34553779-57181b64-f14f-11e7-89f4-56510dcf783c"><img src="https://user-images.githubusercontent.com/8917417/34553779-57181b64-f14f-11e7-89f4-56510dcf783c.png" width="400" title="stickman1"/></a>
and give it to the generator. Make a video from the generated frames and you are done. Sounds very easy right, yeah it is.

### Train 
- Download the dataset and preprocess: 
In our case download a video of your wish. Make sure the video has the same backgroud throughout and full body of the same person. Once this is done preprocess the video to convert it into frames. These frames are the ground truth data. These frames should now be converted to its corresponding poses. Now the frames and corresponding poses should be stitched together. 
<a href="https://user-images.githubusercontent.com/8917417/34605263-f4d48d4c-f230-11e7-9d8f-4cca4c75d5e0"><img src="https://user-images.githubusercontent.com/8917417/34605263-f4d48d4c-f230-11e7-9d8f-4cca4c75d5e0.png" width="400" title="stickspider1"/></a>

- Once this is done you are ready to train your pix2pix network to find a mapping from poses to groundtruth. 
```bash
python train.py --dataroot ./datasets/dance_mimic --name dance_mimic_pix2pix --model pix2pix --which_model_netG unet_256 
```
- To view training results and loss plots, run `python -m visdom.server` and click the URL http://localhost:8096. To see more intermediate results, check out  `./checkpoints/dance_mimic_pix2pix/web/index.html`

- Model will be saved at ./checkpoints/dance_mimic_pix2pix/

### Test (on a given video)
- Download the dataset and preprocess as given above in train. You can make the images aligned(pose frame and actaul frame) or as a single image also. Its better to keep it aligned to visualize how good the results are.

- Once this is done you are ready to test your pix2pix network.
For aligned frames.
```
python test.py --dataroot ./datasets/dance_mimic --name dance_mimic_pix2pix --model pix2pix --which_model_netG unet_256 --which_direction BtoA --dataset_mode aligned --norm batch
```

For single images
```
python test.py --dataroot ./datasets/dance_mimic --name dance_mimic_pix2pix --model pix2pix --which_model_netG unet_256 --which_direction BtoA --dataset_mode single --norm batch
```

The test results will be saved here: `./results/dance_mimic_pix2pix/latest_val/images`.

- From here frames can be joined together to make a complete video. i_fake_B.png has the generated frames. Use take_frames.py to take images and store it in a different folder. There you can run the below command on the terminal to convert frames to video.
```
ffmpeg -r 60 -f image2 -s 256x256 -i %d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p spiderman.mp4
```

- To make two videos side by side use.(Make sure you change the file names appropriately)
```
ffmpeg -i man.mp4 -i spiderman.mp4 -filter_complex '[0:v]pad=iw*2:ih[int];[int][1:v]overlay=W/2:0[vid]' -map [vid] -c:v libx264 -crf 23 -preset veryfast output.mp4
```

- In case you want gif of the video use 
```
ffmpeg -i output.mp4 -pix_fmt rgb24 output.gif
```


### Test (real time webcam)

For testing real time on your webcam
```
python web_spiderman.py
```

### Apply a pre-trained model 

Pretrained model will be made available soon.
