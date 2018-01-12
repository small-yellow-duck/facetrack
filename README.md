# facetrack
In this face-tracking tutorial you will learn to:

- install and run Python with the Anaconda package manager
- create a new Anaconda environment and install packages in it
- use the OpenCV package to do face detection on still images
- use the OpenCV package to do face-tracking with images from a webcam
- build your own SnapChat filters!
- apply some mathematical filters to modify images



# installing Anaconda

Installation instructions for Mac, Windows and Linux: https://conda.io/docs/user-guide/install/index.html

Anaconda is a package manager for Python. Packages (also called modules) are like recipe books - they have instructions for performing a specific task. Imagine you want to bake a pie: you might want to a import package with a recipe for making a crust so that you don't have to write your own instructions for doing that task. The package with the crust recipe would itself refer to other packages with recipes for things like how to churn butter or grow wheat and mill flour. In this way, it's possibile to do some cool stuff with Python without having to understand all the details about how the software is performing every task.

You can run Python and install packages without a package manager, but it's better to use one because it will make your life a lot easier. When you install a new package, Anaconda will make sure that the other packages that your new module relies on are up-to-date. Another advantage is that Anaconda allows you to create a new "environment" for each project you do: that way if an old project uses an old version of a package, you don't have to uninstall and reinstall packages each time you switch between old and new projects.

# creating a new conda environment and installing packages
Create a new Anaconda environment called 'facetrack' and activate that environment
'''
conda create --name facetrack
source activate facetrack
'''

Now you'll want to install some packages that you need:

'''
conda install opencv ipython matplotlib
'''


# getting started with OpenCV

https://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
# trouble-shooting your webcam


# project ideas
- apply snapchat filters to faces in images from your webcam (http://blog.stickpng.com/create-snapchat-filters-png-stickers/)
- write a program that will save a still photo 3 seconds after you wink. Your program might include a numerical countdown on the viewer window as well as some beeps so that the user knows when the photo will be taken.
