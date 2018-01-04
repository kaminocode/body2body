# body2body
Deep learning network to transfer body movements from one individual to another. Eg mimic dance steps. 
First of all, the project has not produced very promising results, all I intend to do is to give you a direction to think. I method used here can be adopted in many situations
For the motivation, let me walk you through some of the priliminary results. 

<a href="https://imgflip.com/gif/223qo6"><img src="https://i.imgflip.com/223qo6.gif" width="800" title="made at imgflip.com"/></a> . I agree the reconstruction is poor, but keep in mind the gan was trained on a 30 second superman animation. The superman video clearly didn't capture most of the required moviements and hence, the above result was expected.

Going into technical details of the project, I'll start with the basic idea. You just cant train a deep learning network from a given man to superman, because then the solution will be specific to that particular man. So you need something that is same for all people to stand as an intermediate layer. What I used is the pose estimation technique as given in the paper Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields. 

<a href="https://user-images.githubusercontent.com/8917417/34553776-56a15e34-f14f-11e7-8e15-cf2c20612b58"><img src="https://user-images.githubusercontent.com/8917417/34553776-56a15e34-f14f-11e7-8e15-cf2c20612b58.png" title="sticksuperman1"/></a>

I hence trained a conditional gan to map pose images to superman. Once the gan is trainied, all you need to do is take a video, convert it into frames,then the frames to poses(stick images :P) 
<a href="https://user-images.githubusercontent.com/8917417/34553779-57181b64-f14f-11e7-89f4-56510dcf783c"><img src="https://user-images.githubusercontent.com/8917417/34553779-57181b64-f14f-11e7-89f4-56510dcf783c.png" title="stickman1"/></a>
and give it to the generator. Make a video from the generated frames and you are done. Sounds very easy right, yeah it is.




