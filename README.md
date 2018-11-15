## Advanced Lane Finding


In this project, our goal is to write a software pipeline to identify the lane boundaries in a video.


The Project
---

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
<center class="half">
    <img src="readme_images/1.png">
</center>

* Apply a distortion correction to raw images.

  <center class="half">
  <img src="readme_images/2.jpg" >
  </center>

* Use color transforms, gradients, etc., to create a thresholded binary image.

  <center class="half">
      <img src="readme_images/3.jpg">
  </center>

* Apply a perspective transform to rectify binary image ("birds-eye view").

  <center class="half">
      <img src="readme_images/4.jpg">
  </center>

* Detect lane pixels and fit to find the lane boundary.

  <center class="half">
      <img src="readme_images/5.jpg" width="600">
  </center>

* Determine the curvature of the lane and vehicle position with respect to center.

  <center class="third">
      <img src="readme_images/6.png" width="200"><img src="readme_images/7.png" width="200"><img src="readme_images/8.png" width="200">
  </center>

* Warp the detected lane boundaries back onto the original image.

  <center class="center">
      <img src="readme_images/9.jpg" width = 600>
  </center>

* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.


<iframe name="music" src="output_videos/project_video.mp4" marginwidth="1px" marginheight="20px" width=20% height="500px" frameborder=1 　scrolling="yes">
</iframe>

To help the reviewer examine your work, please save examples of the output from each stage of your pipeline in the folder called `output_images`, and include a description in your writeup for the project of what each image shows.    The video called `project_video.mp4` is the video your pipeline should work well on.  

The `challenge_video.mp4` video is an extra (and optional) challenge for you if you want to test your pipeline under somewhat trickier conditions.  The `harder_challenge.mp4` video is another optional challenge and is brutal!

If you're feeling ambitious (again, totally optional though), don't stop there!  We encourage you to go out and take video of your own, calibrate your camera and show us how you would implement this project from scratch!


