docker run -p 8502:8501 --name=fafa -v YOUR_PATH/image-classification-web-app/saved_model/:/models/horse-vs-human/1 -e MODEL_NAME=horse-vs-human tensorflow/serving


# Create a CNN

Convolution and Pooling are used to improve our image recognition performance.

## - Convolution
Technique to **isolate features** in images.

By passing filters over an image to reduce the amount of information, they then allowed the neural network to effectively extract features that can distinguish one class of image from another. 

**Output shape:** After passing a 3x3 filter over a 28x28 image, the output will be 26x26.

## - Pooling 
Technique to reduce the information in an image while maintaining features.

Pooling **compresses the information** to make it more manageable. 

**Output shape:** After max pooling a 26x26 image with a 2x2 filter, the output will be 13x13.
