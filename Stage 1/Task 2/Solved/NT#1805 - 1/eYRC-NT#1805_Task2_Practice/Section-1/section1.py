"""
**
* Team ID           : eYRC-NT#1805
* Author List       : A. Peter Hudson, Aakash Sunil, Abhishek BR, Aniketh M
* Filename          : section1.py
* Theme             : NT-eYRC
* Functions         : sine(angle), cosine(angle), readImage(filePath),
                      findNeighbours(), colourCell(), buildGraph(),
                      findStartPoint(), findPath(), main()
* Global Variables  : NONE
**
"""
import numpy as np
import cv2
import math
import time

"""
*
* Function Name : sine(angle)
* Input         : angle -> the angle of each cell arc
* Output        : Returns sine of an angle in radians.
* Logic         : sine angle
* Example Call  : sine(angle)
*
"""

def sine(angle):
    return math.sin(math.radians(angle))

"""
*
* Function Name : cosine(angle)
* Input         : angle -> the angle of each cell arc
* Output        : Returns cosine of an angle in radians.
* Logic         : cosine angle
* Example Call  : cosine(angle)
*
"""

def cosine(angle):
    return math.cos(math.radians(angle))

"""
*
* Function Name : readImage(filePath)
* Input         : an image in the the path specified
* Output        : Returns the image in Grayscale Value
* Logic         : Reads an image from the specified filepath and converts
                  it to Grayscale. Then applies binary thresholding to the image.
* Example Call  : readImage(filePath)
*                  
"""

def readImage(filePath):
    mazeImg = cv2.imread(filePath)
    grayImg = cv2.cvtColor(mazeImg, cv2.COLOR_BGR2GRAY)
    ret,binaryImage = cv2.threshold(grayImg,127,255,cv2.THRESH_BINARY)
    return binaryImage

"""
* Function Name : findNeighbours(image, level, cellnum, size)
* Input         : image, level, cellnum, size
                  image - input image
                  level - level of cell to be searched for neighbours
                  cellnum - cell number of cell whose neighbours are to be found
                  size - size of maze
* Output        : Returns a set of neighbours in form of a dictionary.
* Logic         : Accepting the Inputs of a cell, it checks for neighbours
                  traversable from a specified cell.
* Example Call  : findNeighbours(image, level, cellnum, size)
*
##  This function accepts the img, level and cell number of a particular cell and the size of the maze as input
##  arguments and returns the list of cells which are traversable from the specified cell.
"""

def findNeighbours(img, level, cellnum, size):
    neighbours = []

    ############################# Add your Code Here ################################

    if size == 1:
        centre=220
    else:
        centre=300
    
    if level == 1:

        angle = 60
        #for upper cell
        x1 = centre + int((level*40 + 20)*sine((cellnum - 1) * angle)) 
        y1 = centre + int((level*40 + 20)*cosine((cellnum - 1) * angle))
        if img[x1,y1] == 255:
            if cellnum == 1:
                temp = (1,6)
            else:
                temp = (1,cellnum - 1)
            neighbours.append(temp)

        #for lower cell    
        x1 = centre + int((level*40 + 20) * sine(cellnum * angle))
        y1 = centre + int((level*40 + 20) * cosine(cellnum * angle))
        if img[x1,y1] == 255:
            if cellnum == 6:
                temp = (1,1)
            else:
                temp = (1,cellnum + 1)
            neighbours.append(temp)

        #next upper level
        x1 = centre + int(((level + 1)*40) * sine((cellnum - 1) * angle + angle/4)) 
        y1 = centre + int(((level + 1)*40) * cosine((cellnum - 1) * angle + angle/4))
        if img[x1,y1] == 255:
            temp = (level + 1,cellnum*2 - 1)
            neighbours.append(temp)

        #next upper level
        x1 = centre + int(((level + 1)*40) * sine(cellnum * angle - angle/4 )) 
        y1 = centre + int(((level + 1)*40) * cosine(cellnum * angle - angle/4))
        if img[x1,y1] == 255:
            temp = (level + 1,cellnum * 2)
            neighbours.append(temp)

        #next lower level
        x1 = centre + int((level * 40) * sine((cellnum - 1) * angle + angle/2)) 
        y1 = centre + int((level * 40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255:
            temp = (0,0)
            neighbours.append(temp)
            
    elif level == 2:
        angle = 30

        #for upper cell
        x1 = centre + int((level*40 + 20)*sine((cellnum - 1) * angle)) 
        y1 = centre + int((level*40 + 20)*cosine((cellnum - 1) * angle))
        if img[x1,y1] == 255:
            if cellnum == 1:
                temp = (2,12)
            else:
                temp = (2,cellnum - 1)
            neighbours.append(temp)

        #for lower cell
        x1 = centre + int((level*40 + 20) * sine(cellnum * angle)) 
        y1 = centre + int((level*40 + 20) * cosine(cellnum * angle))
        if img[x1,y1] == 255:
            if cellnum == 12:
                temp = (2,1)
            else:
                temp = (2,cellnum + 1)
            neighbours.append(temp)

        #next upper level
        x1 = centre + int(((level + 1)*40) * sine((cellnum - 1) * angle + angle/4)) 
        y1 = centre + int(((level + 1)*40) * cosine((cellnum - 1) * angle + angle/4))
        if img[x1,y1] == 255:
            temp = (level + 1,cellnum*2 - 1)
            neighbours.append(temp)

        #next upper level
        x1 = centre + int(((level + 1)*40) * sine(cellnum * angle - angle/4 )) 
        y1 = centre + int(((level + 1)*40) * cosine(cellnum * angle - angle/4))
        if img[x1,y1] == 255:
            temp = (level + 1,cellnum * 2)
            neighbours.append(temp)

        #next lower level
        x1 = centre + int((level * 40) * sine((cellnum - 1) * angle + angle/2)) 
        y1 = centre + int((level * 40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255 and cellnum%2==1:
            temp = (level - 1,(cellnum+1)/2)
            neighbours.append(temp)
        elif img[x1,y1] == 255:
            temp = (level - 1,(cellnum)/2)
            neighbours.append(temp)


    elif level == 3:
        angle = 15

        #for upper cell
        x1 = centre + int((level*40 + 20)*sine((cellnum - 1) * angle)) 
        y1 = centre + int((level*40 + 20)*cosine((cellnum - 1) * angle))
        if img[x1,y1] == 255:
            if cellnum == 1:
                temp = (3,24)
            else:
                temp = (3,cellnum - 1)
            neighbours.append(temp)

        #for lower cell
        x1 = centre + int((level*40 + 20) * sine(cellnum * angle)) 
        y1 = centre + int((level*40 + 20) * cosine(cellnum * angle))
        if img[x1,y1] == 255:
            if cellnum == 24:
                temp = (3,1)
            else:
                temp = (3,cellnum + 1)
            neighbours.append(temp)

        #next upper level            
        x1 = centre + int(((level + 1)*40) * sine((cellnum - 1) * angle + angle/2)) 
        y1 = centre + int(((level + 1)*40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255:
            temp = (level + 1,cellnum)
            neighbours.append(temp)

        #next lower level    
        x1 = centre + int((level * 40) * sine((cellnum - 1) * angle + angle/2)) 
        y1 = centre + int((level * 40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255 and cellnum%2==1:
            temp = (level - 1,(cellnum+1)/2)
            neighbours.append(temp)
        elif img[x1,y1] == 255:
            temp = (level - 1,(cellnum)/2)
            neighbours.append(temp)
        
    elif level == 4 :
        angle = 15

        #for upper cell
        x1 = centre + int((level*40 + 20)*sine((cellnum - 1) * angle)) 
        y1 = centre + int((level*40 + 20)*cosine((cellnum - 1) * angle))
        if img[x1,y1] == 255:
            if cellnum == 1:
                temp = (level,24)
            else:
                temp = (level,cellnum - 1)
            neighbours.append(temp)

        #for lower cell    
        x1 = centre + int((level*40 + 20) * sine(cellnum * angle)) 
        y1 = centre + int((level*40 + 20) * cosine(cellnum * angle))
        if img[x1,y1] == 255:
            if cellnum == 24:
                temp = (level,1)
            else:
                temp = (level,cellnum + 1)
            neighbours.append(temp)

        if size == 2 and (level == 4 or level == 3 or level == 5):
            #next upper level
            x1 = centre + int(((level + 1)*40) * sine((cellnum - 1) * angle + angle/2)) 
            y1 = centre + int(((level + 1)*40) * cosine((cellnum - 1) * angle + angle/2))
            if img[x1,y1] == 255:
                temp = (level + 1,cellnum)
                neighbours.append(temp)

        #next lower level
        x1 = centre + int((level * 40) * sine((cellnum - 1) * angle + angle/2)) 
        y1 = centre + int((level * 40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255:
            temp = (level - 1,cellnum)
            neighbours.append(temp)

    elif level == 5 :
        angle = 15

        #for upper cell
        x1 = centre + int((level*40 + 20)*sine((cellnum - 1) * angle)) 
        y1 = centre + int((level*40 + 20)*cosine((cellnum - 1) * angle))
        if img[x1,y1] == 255:
            if cellnum == 1:
                temp = (level,24)
            else:
                temp = (level,cellnum - 1)
            neighbours.append(temp)

        #for lower cell    
        x1 = centre + int((level*40 + 20) * sine(cellnum * angle)) 
        y1 = centre + int((level*40 + 20) * cosine(cellnum * angle))
        if img[x1,y1] == 255:
            if cellnum == 24:
                temp = (level,1)
            else:
                temp = (level,cellnum + 1)
            neighbours.append(temp)

        #next upper level
        x1 = centre + int(((level + 1)*40) * sine((cellnum - 1) * angle + angle/4)) 
        y1 = centre + int(((level + 1)*40) * cosine((cellnum - 1) * angle + angle/4))
        if img[x1,y1] == 255:
            temp = (level + 1,cellnum*2 - 1)
            neighbours.append(temp)

        #next upper level
        x1 = centre + int(((level + 1)*40) * sine(cellnum * angle - angle/4 )) 
        y1 = centre + int(((level + 1)*40) * cosine(cellnum * angle - angle/4))
        if img[x1,y1] == 255:
            temp = (level + 1,cellnum * 2)
            neighbours.append(temp)

        #next lower level
        x1 = centre + int((level * 40) * sine((cellnum - 1) * angle + angle/2)) 
        y1 = centre + int((level * 40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255:
            temp = (level - 1,cellnum)
            neighbours.append(temp)
            
    else:
        angle = 7.5

        #for upper cell
        x1 = centre + int((level*40 + 20)*sine((cellnum - 1) * angle)) 
        y1 = centre + int((level*40 + 20)*cosine((cellnum - 1) * angle))
        if img[x1,y1] == 255:
            if cellnum == 1:
                temp = (level,48)
            else:
                temp = (level,cellnum - 1)
            neighbours.append(temp)

        #for lower cell    
        x1 = centre + int((level*40 + 20) * sine(cellnum * angle)) 
        y1 = centre + int((level*40 + 20) * cosine(cellnum * angle))
        if img[x1,y1] == 255:
            if cellnum == 48:
                temp = (level,1)
            else:
                temp = (level,cellnum + 1)
            neighbours.append(temp)

        #next lower level    
        x1 = centre + int((level * 40) * sine((cellnum - 1) * angle + angle/2)) 
        y1 = centre + int((level * 40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255 and cellnum%2==1:
            temp = (level - 1,(cellnum+1)/2)
            neighbours.append(temp)
        elif img[x1,y1] == 255:
            temp = (level - 1,(cellnum)/2)
            neighbours.append(temp)

    #################################################################################

    return neighbours

"""
*
* Function Name : colourCell(img, level, cellnum, size, colourVal)
* Input         : img - input image
                  level - level of cell to be coloured
                  cellnum - cell number of cell to be coloured
                  size - size of maze
                  colourVal - the intensity of the colour.
* Output        : Returns image with neighbours coloured
* Logic         : Traverse to the cell and colour the neighbouring cells
                  colourCell function basically highlights the given cell by painting it with the given colourVal.
                  Care should be taken that the function doesn't paint over the black walls and only paints the empty spaces.
                  This function returns the image with the painted cell.
* Example Call  : colourCell(img, level, cellnum, size, colourVal)
*
"""

def colourCell(img, level, cellnum, size, colourVal):

    ############################# Add your Code Here ################################

    if size == 1:
        centre=220
    else:
        centre=300
    def colorneighbourpixel(img,x,y):
         if img[x1,y1] == 255:
            img[x1,y1] = colourVal
         if img[x1,y1+1] == 255:
            img[x1,y1+1] = colourVal
         if img[x1,y1-1] == 255:
            img[x1,y1-1] = colourVal
         if img[x1+1,y1] == 255:
            img[x1+1,y1] = colourVal
         if img[x1-1,y1] == 255:
            img[x1-1,y1] = colourVal
         if img[x1+1,y1+1] == 255:
            img[x1+1,y1+1] = colourVal
         if img[x1+1,y1-1] == 255:
            img[x1+1,y1-1] = colourVal
         if img[x1-1,y1+1] == 255:
            img[x1-1,y1+1] = colourVal
         if img[x1-1,y1-1] == 255:
            img[x1-1,y1-1] = colourVal

    if level == 0:
        angle = 360
    elif level == 1:
        angle = 60
    elif level == 2:
        angle = 30
    elif (level == 3 or level == 4 or level == 5):
        angle = 15
    else:
        angle = 7.5

    array=np.arange((cellnum-1)*angle,cellnum*angle,0.5)

    for i in array:
        for m in range(level*40,(level + 1)*40):
            x1 = centre + int(m*sine(i))
            y1 = centre + int(m*cosine(i))
            colorneighbourpixel(img,x1,y1)

    #################################################################################

    return img

"""
*
* Function Name : buildGraph(img, size)
* Input         : img - input image
                  size - size of maze
* Output        : Returns graph (path to be followed in the maze) in a dictionary
* Logic         : Find the neighbours at every level of the maze and add to an array
                  Finally assign the array to the graph.
* Example Call  : buildGraph(img, size)
*
"""

def buildGraph(img, size):   ## You can pass your own arguments in this space.
    graph = {}
    ############################# Add your Code Here ################################
    if size == 1:
        level = 4
        centre=220
    else:
        level = 6
        centre=300

    for cell in range(1, 7):
            graph[(1, cell)] = findNeighbours(img, 1, cell, size)
    for cell in range(1, 13):
            graph[(2, cell)] = findNeighbours(img, 2, cell, size)
    for lvl in range(3, 5):
        for cell in range(1, 25):
            graph[(lvl, cell)] = findNeighbours(img, lvl, cell, size)
            
    if(size == 2):
        for cell in range(1, 25):
            graph[(5, cell)] = findNeighbours(img, 5, cell, size)
        for cell in range(1, 49):
            graph[(6, cell)] = findNeighbours(img, 6, cell, size)

    # neighbours for (0,0)
    angle=60
    arr = []
    for cellnum in range(1,7):
        #next upper level
        x1 = centre + int((40) * sine((cellnum - 1) * angle + angle/2)) 
        y1 = centre + int((40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255:
            temp = (1,cellnum)
            arr.append(temp)

    graph[(0,0)]=arr
    # Printing sorted graph. Uncomment when needed
    """for key in sorted(graph):
        print "%s: %s" % (key, graph[key])"""

    #################################################################################

    return graph

"""
*
* Function Name : findStartPoint(img, size)
* Input         : img - Image read
                  size - Maze size
* Output        : Returns the Start Point on the maze.
* Logic         : 
* Example Call  : findStartPoint(img, size)
*
##  Function accepts some arguments and returns the Start coordinates of the maze.
"""

def findStartPoint(img, size):     ## You can pass your own arguments in this space.

    ############################# Add your Code Here ################################

    if size == 1:
        centre = 220
        level = 4
        limit = 24
        angle = 15
    else:
        centre=300
        level = 6
        limit = 48
        angle = 7.5

    for cellnum in range(1,limit + 1):
        x1 = centre + int(((level + 1)*40) * sine((cellnum - 1) * angle + angle/2)) #next upper level
        y1 = centre + int(((level + 1)*40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255:
            start = (level,cellnum)

    #################################################################################

    return start

"""
*
* Function Name : findPath(init, final, graph)
* Input         : init - Initial state (start)
                  final - Final state (end)
                  graph - Graph of the Maze
* Output        : Returns the Shortest Path from the graphs in buildGraph on the maze.
* Logic         : Using Breadth First Search Algorithm---find the shortest Path
* Example Call  : findPath(init, final, graph)
*
##  Finds shortest path between two coordinates in the maze. Returns a set of coordinates from initial point
##  to final point.
"""

def findPath(init, final, graph):      ## You can pass your own arguments in this space.

    ############################# Add your Code Here ################################

    node_storage = []
    all_paths = []
    def breadth_first(init, final, graph, node_storage = [], all_paths = []):
        cur_way = [init]
        node_storage.append(cur_way)
        while (len(node_storage) != 0):
            cur_way = node_storage.pop(0)
            if cur_way[-1] == final:
                all_paths.append(cur_way)
            
            for neighbour in graph[cur_way[-1]]:
                if neighbour not in cur_way:
                    other_way = []
                    other_way = cur_way + [neighbour]
                    node_storage.append(other_way)
    
    breadth_first(init, final, graph, node_storage, all_paths)
    shortest = all_paths[0]
    
    #################################################################################

    return shortest

"""
*
* Function Name : main()
* Input         : NONE
* Output        : NONE
* Logic         : Read the Image and check the size of the maze.
                  Call all Functions one by one
                  buildGraph-->findStartPoint-->findPath-->shortestPath-->colourCell
* Example Call  : main()
*
"""
##  This is the main function where all other functions are called. It accepts filepath
##  of an image as input. You are not allowed to change any code in this function. You are
##  You are only allowed to change the parameters of the buildGraph, findStartPoint and findPath functions

def main(filePath, flag = 0):
    img = readImage(filePath)                           ## Read image with specified filepath
    if len(img) == 440:                                 ## Dimensions of smaller maze image are 440x440
        size = 1
    else:
        size = 2
    maze_graph = buildGraph(img,size)                   ## Build graph from maze image. Pass arguments as required
    start = findStartPoint(img,size)                    ## Returns the coordinates of the start of the maze
    shortestPath = findPath(start, (0,0), maze_graph)   ## Find shortest path. Pass arguments as required.
    print shortestPath
    string = str(shortestPath) + "\n"
    for i in shortestPath:                              ## Loop to paint the solution path.
        img = colourCell(img, i[0], i[1], size, 230)
    if __name__ == '__main__':                          ## Return value for main() function.
        return img
    else:
        if flag == 0:
            return string
        else:
            return graph
## The main() function is called here. Specify the filepath of image in the space given.
if __name__ == "__main__":
    filepath = "image_09.jpg"                           ## File path for test image
    img = main(filepath)                                ## Main function call
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
