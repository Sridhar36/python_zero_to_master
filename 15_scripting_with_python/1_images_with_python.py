'''
PIL - Python Imaging Library (expansion of PIL) is the de facto image processing package for Python language.
It incorporates lightweight image processing tools that aids in editing, creating and saving images.
Support for Python Imaging Library got discontinued in 2011, but a project named pillow forked the original PIL project
and added Python3.x support to it. Pillow was announced as a replacement for PIL for future usage. Pillow supports a
large number of image file formats including BMP, PNG, JPEG, and TIFF. The library encourages adding support for newer
formats in the library by creating new file decoders.
This module is not preloaded with Python. So to install it execute the following command in the command-line:
'''

from PIL import Image, ImageFilter

path = 'C:\\Users\\sridh\\PycharmProjects\\pythonProject\\pythonProject\\zero_to_master_complete_python_2022\\pikachu.jpg'
img = Image.open(path)
print(img)
print(img.format)
print(img.size)
print(img.mode)  # RGB - reg green blue
print(dir(img))

# image filters
filterdimage = img.filter(ImageFilter.BLUR)
filterdimage1 = img.filter(ImageFilter.SMOOTH)
filterdimage.save("blur.png", 'png')  # to create new file and name
filterdimage1.save("blurrr.png", 'png')

# convert images
convrtimage = img.convert('L')
convrtimage.save("grey.png", 'png')
# show image
convrtimage.show()
# to rotate
crooked = convrtimage.rotate(90)
crooked.show()
# to resize
resize = convrtimage.resize((300, 300))
resize.save("resized.png", "png")
resize.show()

# thumbnail:
'''
But one thing that I don't know if you can notice is that because the image did not have the same width and height.
What happened was it is actually a little bit compressed, so it lost its aspect ratio. The image looks kind of squished 
in. So how can we fix that? And this is a common problem with images, right? If we make things smaller and smaller or we 
change the aspect ratio, let's say. 400 by 200. So if I save this and go to the image. Well, yeah, look at that.
The image is all squished up. How can we fix it? Well, in this case we can actually use a useful thumbnail method.
So instead of saying resize, if you want to keep the aspect ratio, we can say thumbnail. And this thumbnail will be 
400 by 200. So if I save and run this again, we'll get an error. A non type object has no attribute safe and that is 
because a thumbnail actually doesn't return a new image. It just modifies the current one. So in here we can just say 
image dot thumbnail. And then we'll say image dot save. So if I run this. And we go back to thumbnail, look at that, 
we have a thumbnail, but it keeps the aspect ratio. So even though I said 400 by 200, it's going to try and do its best 
to keep that aspect ratio and maybe not give the exact output that I want. So let's just bring it back to 400 by 400.
Run it again. And there you go. We have our thumbnail and the astronaut is not squished. Very, very useful.
So the thumbnail one is really, really useful. Maybe if you want to create a profile picture for Facebook or Instagram 
or any other social media platform that you might have, and it just gives a tuple of width and height and this is the 
maximum value. So it's never going to go over 404 hundred, but thumbnail is going to automatically do anything within
the range up to 400, but keeping the aspect ratio. So if I actually do here print image dot size. And I run this, you'll
 see that that's exactly what happens.It's intelligently deciding what the best size for the image is.'''

resizedImg = img
resizedImg.thumbnail((400,400))
resizedImg.save('resizedImg.jpg')
resizedImg.show()