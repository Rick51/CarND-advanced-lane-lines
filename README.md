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

  The final output video could be watched in the path "output_videos/project_video.mp4". (if below code doesnt work well)

  <iframe
          width="800"
          height="450"
          src="output_videos/project_video.mp4"
          frameborder="0"
          allowfullscreen>
  </iframe>





