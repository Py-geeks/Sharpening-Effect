# Sharpening-Effect
Sharpening an image is a very basic method of image processing. In principle, image sharpening consists<br>
of adding to the original image a signal that is proportional to a high-pass filtered version of the original image

## Tools and Languages:
<img align="left" alt="OpenCV" width="26px" src="opencv.png" >
<img align="left" alt="VS Code" width="26px" src="visual-studio-code.png" >
<img align="left" alt="pip" width="26px" height="34px" src="pip.png" >
<img align="left" alt="Python" width="26px" src="python.png" >
<br>

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cv2 and numpy.


```bash
pip install cv2
pip install numpy
```

## Import
Use [import](https://www.w3schools.com/python/ref_keyword_import.asp) keyword to import modules.
```python
import cv2
import numpy as np
```

## Reading image from file

```python
img = cv2.imread("cat.png")
```


## Negative conversion
Image negative is produced by subtracting each pixel from the maximum intensity value.<br>
This is a very easy method rather than manipulating individual color channels.<br> 
```python
kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1, 9,-1],
                              [-1,-1,-1]])
sharpened = cv2.filter2D(img,-1,kernel_sharpening)
```

## Completion message

```python
print('Image Sharpened.')
```

## comparing original vs resized

```python
cv2.imshow('ORIGINAL',img)
cv2.imshow('SHARPEN',sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Images
<p align="center">
	<img src="cat.png" alt="Logo", height=250px,width=350px>
	<img src="sharpened.PNG" alt="SHARP", height=250px,width=350px>
</p>

### Developed by
 [Ashish ku. Behera](https://github.com/ashish-max "Github Id")
