# -*- coding: utf-8 -*-
"""PR1(1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ef-ZpJFIrOE_ZqQjeBCiJxxG_FVGTOge

<div>
<img src="./sharif.png"
alt="SUT logo" width=150 height=150 align=left class="saturate">
<br>
<font face="Times New Roman">
<div dir=ltr align=center>
<!-- <font color=0F5298 size=7> -->
<font color=0F5298 size=6>
    Linear Algebra <br> <br>
<!-- <font color=2565AE size=5> -->
<font size=5>
    Computer Engineering Department <br>
    Winter 2024 <br> <br>


    
____

**bold text**<div>
<font face="Times New Roman">
<div dir=ltr align=left>
<font color=686880 size=4>
    Name: mobina kochaknia

Welcome to your first practical homework assignment for the Linear Algebra course! Congratulations on embarking on this mathematical journey. In this course, you will explore the fundamental concepts and techniques that underpin a vast array of mathematical and real-world applications.

As you delve into your first set of practical exercises, remember that every problem presents an opportunity for growth and understanding. Approach each question with curiosity and enthusiasm, and don't be afraid to make mistakes—they're an essential part of the learning process.

This assignment serves as an introduction to NumPy, <b> emphasizing the exclusion of iterative operations such as 'for' loops for processing NumPy arrays, with the exception of obtaining inputs, which is permissible.
"""

# Imports
import cv2
# for google colab
from google.colab.patches import cv2_imshow
import numpy as np
import matplotlib.pyplot as plt
import timeit
import matplotlib.image as mpimg
from PIL import Image
import imageio
from google.colab import files
import imageio

"""# Image Processing

In this section, First you should load an image and convert it to a gray scaled image then we'll process it by some operations using numpy.
"""

# read and show the image
image = imageio.imread('ski_ca__283_29.jpg')
np_img = np.array(image)
plt.imshow(np_img)
plt.show()

"""<b> From now on, you must work with the grayscale image in each cell.

In gray scaled 0 means black and 255 is white and each number between these two shows a color in range of black to white. Now for this task, Make pixels brighter than 150, 100 degree darker.
"""

# TODO: don't use loop or anything like that and try to code by numpy where
image = Image.open('/content/ski_ca__283_29.jpg')
np_img = np.array(image).copy()
np_img[np_img > 150] -= 100
plt.imshow(np_img)
plt.show()

"""In grayscale images, pixel values typically range from 0 to 255, where 0 represents black and 255 represents white. subtracting each pixel value from 255 effectively produces the negative of the grayscale image. Now we want to create negative grayscale version of our image."""

# TODO: Create negative grayscale image

gray_image = np.dot(np_img[...,:3], [0.2989, 0.5870, 0.1140])
negative_image = 255 - gray_image
plt.imshow(negative_image, cmap='gray')
plt.show()

# TODO: Split the image horizontally into two equal parts using NumPy's split function.

# Calculate the middle index
middle_index = np_img.shape[0] // 2

# Split the image array into two equal parts horizontally using numpy's split function
upper_half, lower_half = np.split(np_img, [middle_index])

# Display the upper half of the image
plt.imshow(upper_half)
plt.title('Upper Half')
plt.show()

# Display the lower half of the image
plt.imshow(lower_half)
plt.title('Lower Half')
plt.show()

# TODO: Split the image vertically into two equal parts using indexes and slicing.
middle_index = np_img.shape[0] // 2

# Split the image array into two equal parts horizontally
upper_half = np_img[:middle_index]
lower_half = np_img[middle_index:]

# Display the upper half of the image
plt.imshow(upper_half)
plt.title('Upper Half')
plt.show()

# Display the lower half of the image
plt.imshow(lower_half)
plt.title('Lower Half')
plt.show()

"""now i need 4 vertical split (vsplit) from image. write code in a way that could be used for each image (not hard code size)."""

# TODO: Split the image vertically into four equal parts using numpy vsplit function.
if np_img.shape[0] % 4 != 0:
    # Crop the image to make it divisible by 4
    np_img = np_img[:np_img.shape[0] - np_img.shape[0] % 4]

# Split the image array into four equal parts vertically using numpy's vsplit function
quarter_1, quarter_2, quarter_3, quarter_4 = np.vsplit(np_img, 4)

# Display the first quarter of the image
plt.imshow(quarter_1)
plt.title('First Quarter')
plt.show()

# Display the second quarter of the image
plt.imshow(quarter_2)
plt.title('Second Quarter')
plt.show()

# Display the third quarter of the image
plt.imshow(quarter_3)
plt.title('Third Quarter')
plt.show()

# Display the fourth quarter of the image
plt.imshow(quarter_4)
plt.title('Fourth Quarter')
plt.show()

"""In this section first split the original image horizontally calling them left and right images"""

middle_index = np_img.shape[1] // 2

# Split the image array into two equal parts vertically
left_half, right_half = np.hsplit(np_img, [middle_index])

plt.imshow(left_half)
plt.title('Left Half')
plt.show()

plt.imshow(right_half)
plt.title('Right Half')
plt.show()

"""Now, using  invert the left image."""

#TODO: invert left
middle_index = np_img.shape[1] // 2

# Split the image array into two equal parts vertically
left_half, right_half = np.hsplit(np_img, [middle_index])

# Invert the left half of the image
left_half = 255 - left_half

# Display the inverted left half of the image
plt.imshow(left_half)
plt.title('Inverted Left Half')
plt.show()

# Display the right half of the image
plt.imshow(right_half)
plt.title('Right Half')
plt.show()

"""Now, mirror both the inverted left image and the right image."""

#TODO: flip inverted left image
left_half = np.fliplr(left_half)



# Display the mirrored and inverted left half of the image
plt.imshow(left_half)
plt.title('Mirrored and Inverted Left Half')
plt.show()

#TODO: flip right image
# Display the mirrored right half of the image
# Mirror the right half of the image
right_half = np.fliplr(right_half)
plt.imshow(right_half)
plt.title('Mirrored Right Half')
plt.show()

"""In the next step we want to concat the two images horizontally."""

#TODO: concat mirrored_left and mirrored_right
# Concatenate the two images horizontally
concatenated_image = np.concatenate((left_half, right_half), axis=1)

# Display the concatenated image
plt.imshow(concatenated_image)
plt.title('Concatenated Image')
plt.show()

"""For the final step invert the concated image."""

#TODO: invert final_image
# Invert the concatenated image
inverted_concatenated_image = 255 - concatenated_image

# Display the inverted concatenated image
plt.imshow(inverted_concatenated_image)
plt.title('Inverted Concatenated Image')
plt.show()

"""###Broadcasting###

In this question, we have several vectors. From them, we want to find a vector that is most similar to a specific vector.

In order to compare how "similar" two vectors are, we define the D parameter like below (a and b are the two vectors we want to compare, with n indices). the smaller the value of D for 2 vectors is, the more similar those two vectors are.

$D=\sqrt{\Sigma_{i=1}^n(a_i-b_i)^2}$

Inputs: in the first line the users gives the value m, which is the number of vectors. In each of the next m lines, the user will give a vector as the input. In the next line, the users gives the vector v.

You are expected to find the closest vector to v.
"""

#in this cell, you should only get the inputs

m = int(input("Enter the number of vectors: "))
vectors = np.array([list(map(int, input("Enter a vector: ").split())) for _ in range(m)])
v = np.array(list(map(int, input("Enter the vector v: ").split())))

#in this cell you should find the expected output. you are not allowed to use loops in this cell.
distances = np.sqrt(np.sum((vectors - v)**2, axis=1))
closest_index = np.argmin(distances)
closest_vector = vectors[closest_index]
print("The closest vector to v is:", closest_vector)

"""# Shear Images and find similarity"""

!wget https://img.freepik.com/free-photo/cat-sneaking-look-from-white-screen_60438-3711.jpg -O image.jpg

# Load the image
image = mpimg.imread('/content/ski_ca__283_29.jpg')

# Get the dimensions of the image
rows, cols, _ = image.shape

# Calculate the sheared image dimensions
shear_factor = 0.5
sheared_cols = int(cols + abs(shear_factor) * rows)

# Define the shear matrix
shear_matrix = np.array([[1, shear_factor, 0],
                          [0, 1, 0],
                          [0, 0, 1]])

# Create a grid of indices
x, y = np.meshgrid(np.arange(sheared_cols), np.arange(rows))
ones = np.ones_like(x)

# Flatten the grid of indices
indices = np.vstack((x.flatten(), y.flatten(), ones.flatten()))

# TODO: Apply the shear matrix to the indices using dot product
sheared_indices = np.dot(shear_matrix, indices)


# Reshape the indices back to their original grid shape
sheared_indices = sheared_indices[:2, :].reshape(2, rows, sheared_cols)


# TODO: Clip indices to stay within image bounds and Map the sheared indices to the original image
sheared_indices[0, :] = np.clip(sheared_indices[0, :], 0, cols - 1)
sheared_indices[1, :] = np.clip(sheared_indices[1, :], 0, rows - 1)
sheared_image = image[sheared_indices[1, :].astype(np.int32), sheared_indices[0, :].astype(np.int32), :]


# Display the original and sheared images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(sheared_image)
plt.title('Sheared Image')
plt.axis('off')

plt.show()

from google.colab import drive
drive.mount('/content/drive')

"""Find the similarity between the 2 images by dot product. Why isn't the similarity high?"""

# Flatten the original and resized sheared images into vectors
from skimage.transform import resize
sheared_image_resized = resize(sheared_image, (rows, cols))
original_vector = image.flatten()
sheared_vector = sheared_image_resized.flatten()

# Calculate the dot product between the two vectors
dot_product = np.dot(original_vector, sheared_vector)

# Calculate the magnitude (length) of each vector
original_magnitude = np.linalg.norm(original_vector)
sheared_magnitude = np.linalg.norm(sheared_vector)

# Normalize the dot product by dividing it by the product of the magnitudes
similarity = dot_product / (original_magnitude * sheared_magnitude)

print(f"Similarity between the original and sheared images: {similarity}")

"""# Graph Theory

In graph theory, a matrix is associated with each graph, which is called the adjacency matrix of that graph.
The definition of the adjacency matrix of a graph is that if our graph is given with a set of vertices
$V=\{v_1, ..., v_n\}$,
then the corresponding matrix
$A_{n\times n} = [a_{ij}]$
will be such that
$a_{ij} = 1$
if and only if vertices
$v_i$
and
$v_j$
are connected by an edge, otherwise
$a_{ij} = 0$.
Now, we want to define some types of multiplication for two graphs and ask you to find the adjacency matrix product of two arbitrary graphs using your knowledge of
$numpy$
and the adjacency matrices of the graphs.

The first type of multiplication is the tensor or Category product of two graphs. Its definition is as follows: if we consider two graphs
$G$
and
$H$
in such a way that
$V(G) = \{x_1, ..., x_n\}$
and
$V(H) = \{y_1, ..., y_m\}$,
then the category product of these two graphs, denoted by
$G\times H$,
has a vertex set defined as
$V(G\times H) = V(G) \times V(H)$,
and we connect two vertices
$(x_i, y_j)$
and
$(x_{i'}, y_{j'})$
if and only if
$y_jy_{j'} \in E(H)$
or
$x_ix_{i'} \in E(G)$.

Now, we ask you to obtain the adjacency matrix of the Cartesian product of two graphs by taking the adjacency matrices of those graphs and applying the defined connections.
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Create example graphs
# You can test your code by edit this section
graph_A = nx.Graph([(1, 2), (2, 3)])
graph_B = nx.Graph([(4, 5), (5, 6)])

# Get adjacency matrices
matrix_A = nx.linalg.graphmatrix.adjacency_matrix(graph_A).todense()
matrix_B = nx.linalg.graphmatrix.adjacency_matrix(graph_B).todense()

print("Adjacency Matrix A:")
print(matrix_A)
print("\nAdjacency Matrix B:")
print(matrix_B)

def category_product(matrix_A, matrix_B):
  result_matrix = np.kron(matrix_A, matrix_B)
  return result_matrix
  pass


result_matrix = category_product(matrix_A, matrix_B)
print("Adjacency matrix of category product of A and B:")
print(result_matrix)

"""To better understand this matter, we illustrate the graphs:"""

# Create graphs from matrices
graph_result = nx.Graph(result_matrix)

# Visualize original graphs and the resulting graph
plt.figure(figsize=(12, 4))

plt.subplot(131)
nx.draw(graph_A, with_labels=True, font_weight='bold')
plt.title('Graph A')

plt.subplot(132)
nx.draw(graph_B, with_labels=True, font_weight='bold')
plt.title('Graph B')

plt.subplot(133)
nx.draw(graph_result, with_labels=True, font_weight='bold')
plt.title('Resulting category Product of Graphs ')

plt.show()

"""The second type of multiplication is the Cartesian product of two graphs, denoted as $G\square H$. If we consider two graphs $G$ and $H$ with vertex sets $V(G) = \{x_1, ..., x_n\}$ and $V(H) = \{y_1, ..., y_m\}$, then the Cartesian product of these two graphs is represented by $G\square H$, and its vertex set is defined as $V(G\square H) = V(G) \times V(H)$. We connect two vertices $(x_i, y_j)$ and $(x_{i'}, y_{j'})$ if and only if $y_jy_{j'} \in E(H)$ and $i = i'$ or $x_ix_i' \in E(G)$ and $j = j'$.

Now, we ask you to obtain the adjacency matrix of the Cartesian product of two graphs by taking the adjacency matrices of those graphs and applying the defined connections.
"""

def cartesian_product(matrix_A, matrix_B):
  result_matrix = np.outer(matrix_A, matrix_B)
  return result_matrix
  pass

result_matrix = cartesian_product(matrix_A, matrix_B)
print("Adjacency matrix of cartesian product of G and H:")
print(result_matrix)

"""To better understand this matter, we illustrate the graphs:"""

# Create graphs from matrices
graph_result = nx.Graph(result_matrix)

# Visualize original graphs and the resulting graph
plt.figure(figsize=(12, 4))

plt.subplot(131)
nx.draw(graph_A, with_labels=True, font_weight='bold')
plt.title('Graph A')

plt.subplot(132)
nx.draw(graph_B, with_labels=True, font_weight='bold')
plt.title('Graph B')

plt.subplot(133)
nx.draw(graph_result, with_labels=True, font_weight='bold')
plt.title('Resulting Cartesian Product of Graphs ')

plt.show()

"""# Vectorization, Rotation and Introduction to pandas
Face Data
"""

Face1 = np.array([[-64.0, 39.0], [-63.0, 21.0], [-60.0, 3.0], [-57.0, -14.0], [-51.0, -31.0],
                  [-42.0, -47.0], [-30.0, -60.0], [-16.0, -70.0], [-1.0, -73.0], [15.0, -71.0],
                  [29.0, -60.0], [42.0, -48.0], [52.0, -32.0], [58.0, -16.0], [62.0, 2.0],
                  [64.0, 20.0], [64.0, 38.0], [-53.0, 47.0], [-45.0, 57.0], [-33.0, 60.0],
                  [-19.0, 60.0], [-7.0, 56.0], [8.0, 57.0], [20.0, 60.0], [33.0, 61.0],
                  [46.0, 56.0], [53.0, 47.0], [1.0, 42.0], [1.0, 28.0], [1.0, 14.0], [2.0, 0.0],
                  [-14.0, -7.0], [-7.0, -10.0], [1.0, -12.0], [9.0, -10.0], [16.0, -7.0],
                  [-39.0, 38.0], [-32.0, 41.0], [-24.0, 42.0], [-17.0, 37.0], [-24.0, 36.0],
                  [-32.0, 36.0], [17.0, 37.0], [24.0, 42.0], [32.0, 41.0], [40.0, 38.0],
                  [33.0, 35.0], [24.0, 35.0], [-25.0, -31.0], [-15.0, -28.0], [-6.0, -26.0],
                  [-0.0, -28.0], [7.0, -26.0], [15.0, -28.0], [25.0, -30.0], [16.0, -38.0],
                  [7.0, -42.0], [-0.0, -43.0], [-7.0, -43.0], [-16.0, -39.0], [-20.0, -32.0],
                  [-6.0, -32.0], [-0.0, -33.0], [7.0, -32.0], [20.0, -31.0], [7.0, -34.0],
                  [1.0, -35.0], [-6.0, -34.0]])

Face2 = np.array([[-64.0, 41.0], [-64.0, 23.0], [-62.0, 5.0], [-60.0, -13.0], [-53.0, -31.0],
                  [-43.0, -48.0], [-31.0, -62.0], [-17.0, -74.0], [-1.0, -77.0], [16.0, -74.0],
                  [30.0, -62.0], [42.0, -47.0], [53.0, -31.0], [59.0, -14.0], [63.0, 4.0],
                  [64.0, 21.0], [65.0, 39.0], [-53.0, 46.0], [-46.0, 55.0], [-34.0, 59.0],
                  [-21.0, 59.0], [-9.0, 55.0], [9.0, 55.0], [21.0, 58.0], [34.0, 58.0],
                  [46.0, 53.0], [53.0, 43.0], [1.0, 40.0], [1.0, 25.0], [1.0, 11.0],
                  [1.0, -3.0], [-18.0, -5.0], [-9.0, -9.0], [0.0, -13.0], [10.0, -9.0],
                  [18.0, -5.0], [-40.0, 36.0], [-32.0, 38.0], [-25.0, 38.0], [-18.0, 36.0],
                  [-25.0, 35.0], [-33.0, 35.0], [18.0, 35.0], [26.0, 37.0], [33.0, 36.0],
                  [41.0, 34.0], [33.0, 33.0], [26.0, 34.0], [-35.0, -20.0], [-23.0, -20.0],
                  [-11.0, -20.0], [-1.0, -22.0], [9.0, -21.0], [20.0, -20.0], [32.0, -20.0],
                  [21.0, -38.0], [9.0, -46.0], [-1.0, -48.0], [-12.0, -46.0], [-25.0, -38.0],
                  [-31.0, -22.0], [-11.0, -24.0], [-1.0, -26.0], [9.0, -24.0], [28.0, -22.0],
                  [9.0, -37.0], [-1.0, -39.0], [-11.0, -38.0]])

Face3 = np.array([[-66.0, 36.0], [-65.0, 17.0], [-63.0, -1.0], [-59.0, -19.0], [-52.0, -37.0],
                  [-44.0, -54.0], [-33.0, -68.0], [-19.0, -78.0], [-3.0, -81.0], [13.0, -78.0],
                  [27.0, -68.0], [40.0, -56.0], [50.0, -40.0], [57.0, -23.0], [62.0, -5.0],
                  [64.0, 13.0], [65.0, 32.0], [-51.0, 58.0], [-44.0, 69.0], [-32.0, 73.0],
                  [-19.0, 73.0], [-8.0, 68.0], [12.0, 68.0], [23.0, 73.0], [36.0, 74.0],
                  [47.0, 69.0], [54.0, 58.0], [2.0, 47.0], [2.0, 34.0], [2.0, 23.0],
                  [2.0, 10.0], [-13.0, -2.0], [-6.0, -4.0], [1.0, -6.0], [7.0, -5.0],
                  [14.0, -2.0], [-39.0, 41.0], [-32.0, 46.0], [-23.0, 46.0], [-16.0, 41.0],
                  [-24.0, 39.0], [-32.0, 38.0], [18.0, 40.0], [25.0, 46.0], [34.0, 45.0],
                  [41.0, 40.0], [34.0, 37.0], [25.0, 38.0], [-20.0, -36.0], [-14.0, -27.0],
                  [-6.0, -22.0], [-1.0, -24.0], [5.0, -22.0], [12.0, -28.0], [18.0, -38.0],
                  [12.0, -48.0], [4.0, -53.0], [-2.0, -54.0], [-8.0, -53.0], [-15.0, -47.0],
                  [-16.0, -36.0], [-6.0, -29.0], [-1.0, -29.0], [4.0, -29.0], [14.0, -37.0],
                  [4.0, -43.0], [-1.0, -44.0], [-7.0, -43.0]])



TargetFace1 = np.array([[-65.2, 37.6], [-64.4, 19.0], [-62.2, 1.0], [-58.8, -16.8], [-52.0, -34.6], [-43.4, -51.4], [-32.0, -65.2], [-18.0, -75.6], [-2.2, -78.6], [14.0, -75.8], [28.0, -65.2], [40.8, -52.6], [51.0, -36.6], [57.6, -19.8], [62.2, -1.8], [64.0, 16.0], [64.8, 34.6], [-51.8, 53.4], [-44.6, 63.8], [-32.6, 67.6], [-19.4, 67.6], [-8.0, 63.0], [10.6, 63.2], [22.0, 67.4], [35.0, 68.2], [46.6, 63.2], [53.6, 52.8], [1.6, 44.6], [1.6, 31.0], [1.6, 18.8], [1.8, 5.4], [-14.2, -3.6], [-6.8, -6.2], [0.8, -8.6], [8.0, -6.8], [15.2, -3.6], [-39.2, 39.4], [-32.0, 43.4], [-23.6, 43.6], [-16.6, 39.2], [-24.2, 37.6], [-32.2, 37.0], [17.8, 38.4], [25.0, 43.4], [33.4, 42.4], [40.8, 38.4], [33.6, 35.8], [25.0, 36.6], [-24.0, -31.8], [-16.0, -25.8], [-7.0, -22.4], [-0.8, -24.4], [6.2, -22.6], [14.2, -26.4], [22.2, -32.8], [14.6, -44.0], [5.6, -49.4], [-1.4, -50.6], [-8.6, -49.6], [-17.2, -43.6], [-19.8, -32.4], [-7.0, -28.6], [-0.8, -29.2], [5.6, -28.6], [18.0, -32.8], [5.6, -40.0], [-0.6, -41.2], [-7.6, -40.2]])

TargetFace2 = np.array([[-77.6, 46.6], [-76.9, 24.6], [-74.2, 3.0], [-70.7, -18.3], [-62.6, -39.6], [-51.7, -59.7], [-37.7, -76.2], [-20.9, -89.2], [-2.0, -92.8], [17.7, -89.5], [34.5, -76.2], [49.6, -60.3], [62.1, -41.1], [69.7, -21.0], [74.9, 0.6], [76.8, 21.7], [77.7, 43.7], [-62.8, 60.3], [-54.1, 72.2], [-39.7, 76.7], [-23.8, 76.7], [-9.8, 71.5], [11.7, 71.8], [25.7, 76.2], [41.3, 76.9], [55.6, 70.9], [64.0, 58.8], [1.6, 51.4], [1.6, 34.5], [1.6, 18.9], [1.9, 2.5], [-18.4, -5.4], [-9.0, -9.1], [0.7, -12.5], [10.5, -9.5], [19.4, -5.4], [-47.3, 45.8], [-38.4, 49.7], [-28.9, 50.0], [-20.5, 45.5], [-29.3, 43.9], [-38.9, 43.5], [21.3, 44.6], [30.2, 49.5], [39.7, 48.3], [48.9, 44.4], [40.0, 41.8], [30.2, 42.7], [-33.0, -33.7], [-21.6, -29.2], [-9.7, -26.6], [-0.9, -29.0], [8.6, -27.1], [19.3, -29.6], [30.7, -34.2], [20.1, -49.6], [8.2, -56.8], [-1.3, -58.5], [-11.3, -57.1], [-23.3, -49.5], [-27.9, -35.0], [-9.7, -33.2], [-0.9, -34.5], [8.2, -33.2], [25.6, -35.1], [8.2, -45.9], [-0.6, -47.6], [-10.1, -46.4]])



edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8),
         (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16),
         (17, 18), (18, 19), (19, 20), (20, 21),
         (22, 23), (23, 24), (24, 25), (25, 26),
         (27, 28), (28, 29), (29, 30), (30, 33), (31, 32), (32, 33), (33, 34), (34, 35),
         (36, 37), (37, 38), (38, 39), (39, 40), (40, 41), (41, 36),
         (42, 43), (43, 44), (44, 45), (45, 46), (46, 47), (47, 42),
         (48, 49), (49, 50), (50, 51), (51, 52), (52, 53), (53, 54),
         (54, 55), (55, 56), (56, 57), (57, 58), (58, 59), (59, 48),
         (60, 61), (61, 62), (62, 63), (63, 64), (64, 65), (65, 66), (66, 67), (67,60)]

"""----------------------------------------------------------------------
use the face data and perform the rotation by multiplying the rotation matrix and plot the final result, you can use the plot function provided below (select your favorite angle for rotation).
"""

def plot_face(plt,X,edges,color='b'):
    "plots a face"
    plt.plot(X[:,0], X[:,1], 'o', color=color)
    for i,j in edges:
        xi,yi = X[i]
        xj,yj = X[j]
        plt.plot((xi,xj), (yi,yj), '-', color=color)
        plt.axis('square')
        plt.xlim(-100,100)
        plt.ylim(-100,100)

"""Example of ploting face data using plot_face function"""

plot_face(plt, Face1, edges, color='b')
plt.show()

"""complete the code below"""

def rotaion_matrix(x):
  angle_degrees = x
  angle_radians = np.deg2rad(angle_degrees)

  R_x = np.array([[np.cos(angle_radians), -np.sin(angle_radians)],
                  [np.sin(angle_radians), np.cos(angle_radians)]])
  return R_x

x = 30
rotation_matrix = np.array( rotaion_matrix(x))

X = np.dot(Face1, rotation_matrix)

plot_face(plt, X, edges, color='b')
plt.show()

"""<b> Vectorization: </b>
Replace For loop with a single line comand and compare excutation time
"""

import numpy as np
import timeit

m,n,p = 100,50, 2000

A = np.random.rand(m,n,p)
s = np.random.rand(p)

def op1(A, s, p):
    for i in range(p):
        A[:,:,i] *= s[i]
    return A

def op2(A, s):
    A *= s[None, None, :]
    return A

t1 = timeit.timeit(lambda: op1(A, s, p), number=1)
t2 = timeit.timeit(lambda: op2(A, s), number=1)
if t1>t2:
    print("t2 is shorter")
elif t1<t2:
    print("t1 is shorter")

"""in the code below you can see how to calculate excutation time in python, craete op2() and compare the time excutation"""

m,n,p = 100,50, 2000

A = np.random.rand(m,n,p)
s = np.random.rand(p)
def op1():
    for i in range(p):
        A[:,:,i] *= s[i]
t1 = timeit.timeit(op1,number=1)
print(t1)

"""Use the pandas dataframe to load the grades.csv file and calculate average of each student and sort them by average and save in the sorted_gardes.csv file"""

import pandas as pd

# Load the CSV file into a pandas dataframe
grades_df = pd.read_csv('grades.csv')

# Calculate the average for each person across Test1, Test2, Test3, and Test4
grades_df['Average'] = grades_df[['Test1', 'Test2', 'Test3', 'Test4']].mean(axis=1)

# Sort the students by average
sorted_grades_df = grades_df.sort_values(by='Average', ascending=False)

# Save the sorted data to a new CSV file named 'sorted_grades.csv'
sorted_grades_df.to_csv('sorted_grades.csv', index=False)

print("Sorted grades saved to 'sorted_grades.csv'.")