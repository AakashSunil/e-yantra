import numpy as np
import cv2
import math
import time
##  Returns sine of an angle.
def sine(angle):
    return math.sin(math.radians(angle))

##  Returns cosine of an angle
def cosine(angle):
    return math.cos(math.radians(angle))

##  Reads an image from the specified filepath and converts it to Grayscale. Then applies binary thresholding
##  to the image.
def readImage(filePath):
    mazeImg = cv2.imread(filePath)
    grayImg = cv2.cvtColor(mazeImg, cv2.COLOR_BGR2GRAY)
    ret,binaryImage = cv2.threshold(grayImg,127,255,cv2.THRESH_BINARY)
    return binaryImage

##  This function accepts the img, level and cell number of a particular cell and the size of the maze as input
##  arguments and returns the list of cells which are traversable from the specified cell.
def findNeighbours(img, level, cellnum, size):
    neighbours = []
    ############################# Add your Code Here ################################


    #################################################################################
    return neighbours

##  colourCell function takes 5 arguments:-
##            img - input image
##            level - level of cell to be coloured
##            cellnum - cell number of cell to be coloured
##            size - size of maze
##            colourVal - the intensity of the colour.
##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the black walls and only paints the empty spaces. This function returns the image
##  with the painted cell.
def colourCell(img, level, cellnum, size, colourVal):
    ############################# Add your Code Here ################################


    #################################################################################
    return img

##  Function that accepts some arguments from user and returns the graph of the maze image.
def buildGraph(  ):   ## You can pass your own arguments in this space.
    graph = {}
    ############################# Add your Code Here ################################


    #################################################################################
    return graph


##  Function accepts some arguments and returns the Start coordinates of the maze.
def findStartPoint(   ):     ## You can pass your own arguments in this space.
    ############################# Add your Code Here ################################


    #################################################################################
    return start

##  Finds shortest path between two coordinates in the maze. Returns a set of coordinates from initial point
##  to final point.
def findPath(    ):      ## You can pass your own arguments in this space.
    ############################# Add your Code Here ################################


    #################################################################################
    return shortest

##  This is the main function where all other functions are called. It accepts filepath
##  of an image as input. You are not allowed to change any code in this function. You are
##  You are only allowed to change the parameters of the buildGraph, findStartPoint and findPath functions
def main(filePath, flag = 0):
    img = readImage(filePath)     ## Read image with specified filepath
    if len(img) == 440:           ## Dimensions of smaller maze image are 440x440
        size = 1
    else:
        size = 2
    maze_graph = buildGraph(   )   ## Build graph from maze image. Pass arguments as required
    start = findStartPoint(  )  ## Returns the coordinates of the start of the maze
    shortestPath = findPath(   )  ## Find shortest path. Pass arguments as required.
    print shortestPath
    string = str(shortestPath) + "\n"
    for i in shortestPath:               ## Loop to paint the solution path.
        img = colourCell(img, i[0], i[1], size, 230)
    if __name__ == '__main__':     ## Return value for main() function.
        return img
    else:
        if flag == 0:
            return string
        else:
            return graph
## The main() function is called here. Specify the filepath of image in the space given.
if __name__ == "__main__":
    filepath = "image_06.jpg"     ## File path for test image
    img = main(filepath)          ## Main function call
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
