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

ρ = x*cos(θ) + y*sin(θ)

If height of the image is h and the width of the image is w, then for all  0 ≤ θ ≤ 180, the value of ρ varies from -√(h2+w2) to √(h2+w2)
such that

![1](https://user-images.githubusercontent.com/75802971/104766390-7a147400-5790-11eb-9682-b808c6f073d4.JPG)

And let integer (| √(h2+w2) |) be called rmax <br>
Initialise an accumulator matrix with zeros such that first column consists of integer values from - rmax to rmax from row indices 1 through 2* rmax +1 and the first row consists of θ values from 0 to 180 through column indices 1 through 181. This is done to easily map the corresponding ρ and θ.
For example, if rmax is 647. Then the initial accumulator matrix should  look like: <br>

![2](https://user-images.githubusercontent.com/75802971/104766395-7bde3780-5790-11eb-80ee-6e64f8d98dd3.JPG)

4.	Iterate through each pixel that has value 255 and for that particular pixel with indices i, j, we have x = j and y = i.  <br>

For each θi in 0:180°, we calculate ρi as <br>

![3](https://user-images.githubusercontent.com/75802971/104766394-7b45a100-5790-11eb-97e7-8913588d4de8.JPG)

And the value in the accumulator matrix corresponding to this (ρi, θi) the indices of which is given by [ρi+ rmax+1][θ+1] is incremented by 1.
5.	The points with maximum value and more than the threshold indicate a line

<b>Step 4:</b> Based on the threshold passed, get the corresponding (ρ, θ) values of those elements in the accumulator matrix whose value is more than the threshold value. So, the accumulator function returns a list Hough of points (ρi, θi) and each of these points correspond to a line in the image <br>

<b>Step 5:</b> For converting the list obtained into lines, <br>

1.	For every [ρ, θ] in Hough, we have
x0 = ρ*cos(θ)
y0= ρ*sin(θ)
Getting two points based on these values

![4](https://user-images.githubusercontent.com/75802971/104766393-7b45a100-5790-11eb-8be4-35ca8a925e8d.JPG)

The line thus obtained that passes through (x1, y1) and (x2, y2) is basically where a line exists in the image
