# Line-Detection-using-Hough-Transform

### Hough Transform:

#### Description:

Hough transform is a line detection algorithm that uses voting based
mechanisms. It uses the polar m-c plane (ρ, θ plane) instead of the traditional cartesian (x-y)
plane. A line in cartesian coordinates (x-y plane) is represented as a point in the (ρ, θ) or (m,
c) plane In Hough transform,


#### Algorithm:
<b>Step 1:</b> Convert the input image to grayscale <br>
<b>Step 2:</b> Get a binarized image through canny edge detection <br>
<b>Step 3:</b> Implement Hough Transform using the accumulator function <br>

1.	For Hough transform, pass the binarized image and a threshold value to the accumulator function.
2.	The accumulator function takes two parameters, the binarized image and the threshold value
3.	For a pixel (x, y), the ρ value is calculated using 

