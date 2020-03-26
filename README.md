<h1 align="center">Deep Homography Estimation for Dynamic Scenes</h1>
<p align="center">
<a href="lcmhoang.github.io">Hoang Le</a>, 
<a href="http://web.cecs.pdx.edu/~fliu/">Feng Liu</a>, 
Shu Zhang, 
<a href="http://www.agarwala.org/">Aseem Agarwala</a>,
<br>
Portland State University, Google, Adobe Research
<br>
<i>IEEE Computer Vision and Pattern Recognition  (CVPR) 2020.</i>
</p>

<p align="center" >
  <img src='./mics/fig1.png' width=450 alt="test"/>
</p>

#### Abstract
Homography estimation is an important step in many computer vision problems. Recently, deep neural network methods have shown to be favorable for this problem when compared to traditional methods. However, these new methods do not consider dynamic content in input images. They train neural networks with only image pairs that can be perfectly aligned using homographies. This paper investigates and discusses how to design and train a deep neural network that handles dynamic scenes. We first collect a large video dataset with dynamic content. We then develop a multi-scale neural network and show that when properly trained using our new dataset, this neural network can already handle dynamic scenes to some extent. To estimate homography of a dynamic scene in a more principled way, we need to identify the dynamic content. Since dynamic content detection and homography estimation are two tightly coupled tasks, we follow the multi-task learning principles and augment our multi-scale network such that it jointly estimates the dynamics masks and homography. Our experiments show that our method can robustly estimate homography for challenging scenarios with dynamic scenes, blur artifacts, or lack of textures.

[[Paper]](https://github.com/lcmhoang/hmg-dynamics#deep-homography-estimation-for-dynamic-scenes)

## Dataset 
##### Samples 
<img src='./mics/5vEw60gYNFo.mp4_004027_004052_optimized.gif' width=450 ><img src='./mics/fP5I48j_ang.mp4_007642_007687_optimized.gif' width=450>
<img src='./mics/H3gsjINoZqM.mp4_003840_003871_optimized.gif' width=450><img src='./mics/BYeXtAlu1iM.mp4_003388_003412_optimized.gif' width=450>
*These sample clips are used under Creative Commons license from Youtube users freestylefactory, RealTDragon, Lumnah Acres, and Wild Bill.*

This [VideoID and Frame Index](./video_id_and_frame_idx.txt) contains information about the video id and idx of the extracted frame sequences in our dataset. The file is formatted as following:  
```
[youtube_video_id];[frameIdxStart,frameIdxStartEnd];...;[frameIdxStart,frameIdxStartEnd]  
...  
[youtube_video_id];[frameIdxStart,frameIdxStartEnd];...;[frameIdxStart,frameIdxStartEnd]
```

## License and Citation
The provided implementation is for academic purposes only. Should you be making use of our work, please cite our paper.

```
@inproceedings{Le_CVPR_2020,
     author = {Hoang Le, Feng Liu, Shu Zhang, Aseem Agarwala},
     title = {Deep Homography Estimation for Dynamic Scenes},
     booktitle = {IEEE Conference on Computer Vision and Pattern Recognition},
     year = {2020}
}
```

