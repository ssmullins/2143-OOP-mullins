"""
Programed by: Samuel Mullins, Carlos Placencia

Program: AsciiCat

Descrition: This program goes out on the internet and downloads a random image containing a cat.
Once an image is obtained it can be manipulated using the defined functions.
    
    * ConvertToAscii - Converts the image into the same image but made up of ascii characters.
    * flip - Takes an input of either Vertical or Horizontal and flips the ascii image respectively.
    * invert - Takes the ascii characters in the image and reverses the shade scale (lightest characters 
               become darkest, and darkest become lightest).
    * printImage - Prints the ascii image to the screen.
"""
import os
import time
import urllib3, uuid
from PIL import Image
import sys

url = 'http://thecatapi.com/api/images/get'

def getCat(directory=None, filename=None, format='png'):
    basename = '%s.%s' % (filename if filename else str(uuid.uuid4()), format)
    savefile =  os.path.sep.join([directory.rstrip(os.path.sep), basename]) if directory else basename
    downloadlink = url + '?type=%s' % format
    http = urllib3.PoolManager()
    r = http.request('GET', downloadlink)
    fp = open(savefile, 'wb')
    fp.write(r.data)
    fp.close()
    return savefile

class RandomCat(object):

    def __init__(self):

        self.name = ''          # name of image
        self.path = '.'         # path on local file system
        self.format = 'png'
        self.width = 0          # width of image
        self.height = 0         # height of image
        self.img = None         # Pillow var to hold image

    """
    @Description:
    - Uses random cat to go get an amazing image from the internet
    - Names the image
    - Saves the image to some location
    @Returns:
    """
    def getImage(self):
        self.name = self.getTimeStamp()
        getCat(directory=self.path, filename=self.name, format=self.format)
        self.img = Image.open(self.name+'.'+self.format)

        self.width, self.heigth = self.img.size

    """
    Saves the image to the local file system given:
    - Names
    - Path
    """
    def saveImage(self):
        pass

    """
    """
    def nameImage(self):
        pass

    """
    Gets time stamp from local system
    """
    def getTimeStamp(self):
        seconds,milli = str(time.time()).split('.')
        return seconds

"""
The ascii character set we use to replace pixels.
The grayscale pixel values are 0-255.
0 - 25 = '#' (darkest character)
250-255 = '.' (lightest character)
"""
class AsciiImage(RandomCat):

    def __init__(self,new_width="not_set"):
        super(AsciiImage, self).__init__()

        self.newWidth = new_width
        self.newHeight = 0

        self.asciiChars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
        self.imageAsAscii = []
        self.matrix = None

    """
    
    """
    def convertToAscii(self):

        if self.newWidth == "not_set":
            self.newWidth = self.width

        self.newHeight = int((self.heigth * self.newWidth) / self.width)

        if self.newWidth == None:
            self.newWidth = self.width
            self.newHeight = self.height

        self.newImage = self.img.resize((self.newWidth, self.newHeight))
        self.newImage = self.newImage.convert("L") # convert to grayscale
        all_pixels = list(self.newImage.getdata())
        self.matrix = listToMatrix(all_pixels,self.newWidth)
        
        for pixel_value in all_pixels: 
             index = pixel_value // 25 # 0 - 10 
             self.imageAsAscii.append(self.asciiChars[index]) 
        
    def printImage(self): 
        self.imageAsAscii = ''.join(ch for ch in self.imageAsAscii) 
        for c in range(0, len(self.imageAsAscii), self.newWidth): 
            print (self.imageAsAscii[c:c+self.newWidth])   
        
"""
@Class: AsciiShop
@Usage: manipCat = AsciiShop(50)

@Description:
    AsciiShop class is used to manipulate an ascii image.
        * Flip the image horizontally or vertically.
        * Invert the pixles value of the ascii image (darkest to lightest and lightest to darkest).
        * Print the manipulated image
@Params:
    param1 - (object) RandomCat - Instance of the class RandomCat so we have access to its data members.
@Methods:
    convertToAscii - Converts an image to grayscale with self.newImage.convert('L'),
        stores the grayscaled in a list self.all_pixels[], stores self.all_pixels in
        another list self.matrix, assigns each grayscale value in self.matrix to an 
        ascii character.
        Usage: manipCat = AsciiShop(50)
    flip - Takes a string parameter (Vertical, Horizontal), Vertical will reverse the self.matrix list
        so if it were printed it would be flipped Vertically, Horizontal will reverse each individual
        row in self.matrix so when printed the image will be flipped Horizontally.
        Usage: manipCat.flip('Vertical')
    invert - Reverses the ascii character value that is assigned to the values in self.matrix so that
        when the image is printed the dark characters are now lighter and the lighter characters are 
        now darker.
        Usage: manipCat.invert()
    printImage - Smashes all the characters in self.matrix together so there is no empty space, prints
        the compacted image to the screen.
        Usage: manipCat.printImage()
"""

class AsciiShop(RandomCat):
        
    def __init__(self,new_width="not_set"):
        super(AsciiShop, self).__init__()

        self.newWidth = new_width
        self.newHeight = 0

        self.asciiChars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
        self.imageAsAscii = []
        self.matrix = None
        self.all_pixels = []

    """
    @Descrition: Converts an image to grayscale with self.newImage.convert('L'),
        stores the grayscaled in a list self.all_pixels[], stores self.all_pixels in
        another list self.matrix, assigns each grayscale value in self.matrix to an 
        ascii character.
    @Params: None
    @Returns: Image converted to ascii
    """
    def convertToAscii(self):

        if self.newWidth == "not_set":
            self.newWidth = self.width

        self.newHeight = int((self.heigth * self.newWidth) / self.width)

        if self.newWidth == None:
            self.newWidth = self.width
            self.newHeight = self.height

        self.newImage = self.img.resize((self.newWidth, self.newHeight))
        self.newImage = self.newImage.convert("L") # convert to grayscale
        self.all_pixels = list(self.newImage.getdata())
        self.matrix = listToMatrix(self.all_pixels,self.newWidth)
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = self.asciiChars[self.matrix[i][j] // 25]
 
    """
    @Descrition: Takes a string parameter (Vertical, Horizontal), Vertical will reverse the self.matrix list
       so if it were printed it would be flipped Vertically, Horizontal will reverse each individual
       row in self.matrix so when printed the image will be flipped Horizontally.
    @Params: String (Vertical, Horizontal).
    @Returns: String in the form of manipulated ascii image.
    """  
    def flip(self, str):
        
        dir = str
        
        if dir == 'Vertical':
            self.matrix.reverse()
        elif dir == 'Horizontal':
            for i in range(len(self.matrix)):
                    self.matrix[i].reverse()
        else:
            print('Invalid Input')
    
    """
    @Description: Reverses the ascii character value that is assigned to the values in self.matrix so that
        when the image is printed the dark characters are now lighter and the lighter characters are 
        now darker.
    @Params: None
    @Returns: Inverted ascii image.
    """    
    def invert(self):
        
        self.asciiChars.reverse()
        self.all_pixels = list(self.newImage.getdata())
        self.matrix = listToMatrix(self.all_pixels,self.newWidth)
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = self.asciiChars[self.matrix[i][j] // 25]
   
    """ 
    @Description: Smashes all the characters in self.matrix together so there is no empty space, prints
        the compacted image to the screen.
    @Params: None
    @Returns: Nothing
    """ 
    def printImage(self):
        for i in self.matrix:
            print(''.join(i))

"""
Convert to 2D list of lists to help with manipulating the ascii image.
Example:
    L = [0,1,2,3,4,5,6,7,8]
    L = to_matrix(L,3)
    L becomes:
    [[0,1,2],
    [3,4,5],
    [6,7,8]]
"""
def listToMatrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

if __name__=='__main__':

    # awesomeCat = AsciiImage(50)
    # awesomeCat.getImage()
    # awesomeCat.convertToAscii()
    # awesomeCat.printImage()
    
    flipCat = AsciiShop(50)
    flipCat.getImage()
    flipCat.convertToAscii()
    flipCat.printImage()
    print('.')
    flipCat.flip('Vertical')
    flipCat.printImage()
    print('.')
    flipCat.flip('Horizontal')
    flipCat.printImage()
    print('.')
    flipCat.invert()
    flipCat.printImage()
    
    
