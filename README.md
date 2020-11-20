# Sharpening-Effect
Sharpening an image is a very basic method of image processing <br> 

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
inv = 255-img
```

## Completion message

```python
print('Negative Image created.')
```

## Comparing original vs grayscale

```python
cv2.imshow('ORIGINAL',img)
cv2.imshow('INVERSE',inv)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Images
<p align="center">
	<img src="cat.png" alt="Logo", height=250px,width=350px>
	<img src="inversecat.PNG" alt="Gray", height=250px,width=350px>
</p>

### Developed by
 [Ashish ku. Behera](https://github.com/ashish-max "Github Id")
