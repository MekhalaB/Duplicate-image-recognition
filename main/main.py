from PIL import Image
import numpy as np

def get_image(image_path):
    # """Get a numpy array of an image so that one can access values[x][y]."""
    image = Image.open(image_path, "r")
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == "RGB":
        channels = 3
    elif image.mode == "L":
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    pixel_values = np.array(pixel_values).reshape((width, height, channels))
    return pixel_values


#main()
im1=r"\sherbrooke_frames\sherbrooke_frames\00001033.jpg"
#im2=r"\atrium_frames\atrium_frames\00003779.jpg"
#im2=r"\atrium_frames\atrium_frames\00000139.jpg"
im2=r"\sherbrooke_frames\sherbrooke_frames\1.jpg"
p1=get_image(im1) #3D array
p2=get_image(im2) #3D array

flat1=p1.flatten() #flatten the 3d array to a 1d array
n1=flat1.shape[0] #to get the size of array in a integer format
a1=flat1
b1=np.array(np.zeros((n1))) #converting each number to binary
for i in range(n1):
    b1[i]=bin(int(a1[i]))[2:].zfill(8) #to take out the b added by bin function

flat2=p2.flatten()  #same process for second array
n2=flat2.shape[0] 
a2=flat2
b2=np.array(np.zeros((n2)))
for i in range(n2): 
    b2[i]=bin(int(a2[i]))[2:].zfill(8)

r=np.corrcoef(b1,b2)  #getting the Pearson coefficients
mean=np.mean(r)       #taking the avg of the values
print(mean*100)       #printing the mean * 100 so that it comes like a percentage




