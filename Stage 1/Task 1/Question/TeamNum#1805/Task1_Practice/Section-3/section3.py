import numpy as np
import cv2

## Reads image in HSV format. Accepts filepath as input argument and returns the HSV
## equivalent of the image.
def readImageHSV(filePath):
    #############  Add your Code here   ###############


    ###################################################
    return hsvImg

## Reads image in binary format. Accepts filepath as input argument and returns the binary
## equivalent of the image.
def readImageBinary(filePath):
    #############  Add your Code here   ###############


    ###################################################
    return binaryImage

## The findNeighbours function takes a maze image and row and column coordinates of a cell as input arguments
## and returns a stack consisting of all the neighbours of the cell as output.
## Note :- Neighbour refers to all the adjacent cells one can traverse to from that cell provided only horizontal
## and vertical traversal is allowed.
def findNeighbours(img,row,column):
    neighbours = []
    #############  Add your Code here   ###############


    ###################################################
    return neighbours

##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the black walls and only paints the empty spaces. This function returns the image
##  with the painted cell.
##  You can change the colourCell() functions used in the previous sections to suit your requirements.

def colourCell(   ):   ## Add required arguments here.
    
    #############  Add your Code here   ###############


    ###################################################
    return img

##  Function that accepts some arguments from user and returns the graph of the maze image.
def buildGraph():  ## You can pass your own arguments in this space.
    graph = {}
    #############  Add your Code here   ###############


    ###################################################

    return graph

##  Finds shortest path between two coordinates in the maze. Returns a set of coordinates from initial point
##  to final point.
def findPath(): ## You can pass your own arguments in this space.
    #############  Add your Code here   ###############


    ###################################################
    return shortest     

## The findMarkers() function returns a list of coloured markers in form of a python dictionaries
## For example if a blue marker is present at (3,6) and red marker is present at (1,5) then the
## dictionary is returned as :-
##          list_of_markers = { 'Blue':(3,6), 'Red':(1,5)}

def findMarkers(img,   ):    ## You can pass your own arguments in this space.
    list_of_markers = {}
    #############  Add your Code here   ###############


    ###################################################
    return list_of_markers

## The findOptimumPath() function returns a python list which consists of all paths that need to be traversed
## in order to start from the bottom left corner of the maze, collect all the markers by traversing to them and
## then traverse to the top right corner of the maze.

def findOptimumPath(    ):     ## You can pass your own arguments in this space.
    path_array = []
    #############  Add your Code here   ###############


    ###################################################
    return path_array
        
## The colourPath() function highlights the whole path that needs to be traversed in the maze image and
## returns the final image.

def colourPath(    ):      ## You can pass your own arguments in this space. 
    #############  Add your Code here   ###############


    ###################################################
    return img

#####################################    Add Utility Functions Here   ###################################
##                                                                                                     ##
##                   You are free to define any functions you want in this space.                      ##
##                             The functions should be properly explained.                             ##




##                                                                                                     ##
##                                                                                                     ##
#########################################################################################################

## This is the main() function for the code, you are not allowed to change any statements in this part of
## the code. You are only allowed to change the arguments supplied in the findMarkers(), findOptimumPath()
## and colourPath() functions.

def main(filePath, flag = 0):
    imgHSV = readImageHSV(filePath)                ## Acquire HSV equivalent of image.
    listOfMarkers = findMarkers(    )              ## Acquire the list of markers with their coordinates. 
    test = str(listOfMarkers)
    imgBinary = readImageBinary(filePath)          ## Acquire the binary equivalent of image.
    initial_point = ((len(imgBinary)/20)-1,0)      ## Bottom Left Corner Cell
    final_point = (0, (len(imgBinary[0])/20) - 1)  ## Top Right Corner Cell
    pathArray = findOptimumPath(    ) ## Acquire the list of paths for optimum traversal.
    print pathArray
    img = colourPath(imgBinary, pathArray)         ## Highlight the whole optimum path in the maze image
    if __name__ == "__main__":                    
        return img
    else:
        if flag == 0:
            return pathArray
        elif flag == 1:
            return test + "\n"
        else:
            return img
## Modify the filepath in this section to test your solution for different maze images.           
if __name__ == "__main__":
    filePath = "maze00.jpg"                        ## Insert filepath of image here
    img = main(filePath)                 
    cv2.imshow("canvas", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


