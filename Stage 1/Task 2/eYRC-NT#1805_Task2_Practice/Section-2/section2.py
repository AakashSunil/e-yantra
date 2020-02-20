"""
* Team ID           : eYRC-NT#1805
* Author List       : A. Peter Hudson, Aakash Sunil, Abhishek BR, Aniketh M
* Filename          : section2.py
* Theme             : NT-eYRC
* Functions         :
* Global Variables  :
"""
import numpy as np
import cv2
import math
import time
"""
## Reads image in HSV format. Accepts filepath as input argument and returns the HSV
## equivalent of the image.
"""
def readImageHSV(filePath):
    mazeImg = cv2.imread(filePath)
    hsvImg = cv2.cvtColor(mazeImg, cv2.COLOR_BGR2HSV)
    return hsvImg
"""
## Reads image in binary format. Accepts filepath as input argument and returns the binary
## equivalent of the image.
"""
def readImageBinary(filePath):
    mazeImg = cv2.imread(filePath)
    grayImg = cv2.cvtColor(mazeImg, cv2.COLOR_BGR2GRAY)
    ret,binaryImage = cv2.threshold(grayImg,200,255,cv2.THRESH_BINARY)
    return binaryImage
"""
##  Returns sine of an angle.
"""
def sine(angle):
    return math.sin(math.radians(angle))
"""
##  Returns cosine of an angle
"""
def cosine(angle):
    return math.cos(math.radians(angle))
"""
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
        
        #for upper cell - level 1
        x1 = centre + int((level*40 + 20)*sine((cellnum - 1) * angle)) 
        y1 = centre + int((level*40 + 20)*cosine((cellnum - 1) * angle))
        if img[x1,y1] == 255:
            if cellnum == 1:
                temp = (1,6)
            else:
                temp = (1,cellnum - 1)
            neighbours.append(temp)

        #for lower cell - level 1
        x1 = centre + int((level*40 + 20) * sine(cellnum * angle)) 
        y1 = centre + int((level*40 + 20) * cosine(cellnum * angle))
        if img[x1,y1] == 255:
            if cellnum == 6:
                temp = (1,1)
            else:
                temp = (1,cellnum + 1)
            neighbours.append(temp)

        #next upper level - level 2 odd cell(first half of level 2 cell)
        x1 = centre + int(((level + 1)*40) * sine((cellnum - 1) * angle + angle/4)) 
        y1 = centre + int(((level + 1)*40) * cosine((cellnum - 1) * angle + angle/4))
        if img[x1,y1] == 255:
            temp = (level + 1,cellnum*2 - 1)
            neighbours.append(temp)
            
        #next upper level - level 2 even cell(second half of level 2 cell)
        x1 = centre + int(((level + 1)*40) * sine(cellnum * angle - angle/4 )) 
        y1 = centre + int(((level + 1)*40) * cosine(cellnum * angle - angle/4))
        if img[x1,y1] == 255:
            temp = (level + 1,cellnum * 2)
            neighbours.append(temp)
            
        #next lower level - level 0
        x1 = centre + int((level * 40) * sine((cellnum - 1) * angle + angle/2)) 
        y1 = centre + int((level * 40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255:
            temp = (0,0)
            neighbours.append(temp)
            
    elif level == 2:
        angle = 30

        #for upper cell - level 2
        x1 = centre + int((level*40 + 20)*sine((cellnum - 1) * angle))
        y1 = centre + int((level*40 + 20)*cosine((cellnum - 1) * angle))
        if img[x1,y1] == 255:
            if cellnum == 1:
                temp = (2,12)
            else:
                temp = (2,cellnum - 1)
            neighbours.append(temp)

        #for lower cell - level 2
        x1 = centre + int((level*40 + 20) * sine(cellnum * angle)) 
        y1 = centre + int((level*40 + 20) * cosine(cellnum * angle))
        if img[x1,y1] == 255:
            if cellnum == 12:
                temp = (2,1)
            else:
                temp = (2,cellnum + 1)
            neighbours.append(temp)

        #next upper level - level 3 odd cell(first half of level 3 cell)
        x1 = centre + int(((level + 1)*40) * sine((cellnum - 1) * angle + angle/4)) 
        y1 = centre + int(((level + 1)*40) * cosine((cellnum - 1) * angle + angle/4))
        if img[x1,y1] == 255:
            temp = (level + 1,cellnum*2 - 1)
            neighbours.append(temp)
            
        #next upper level - level 3 even cell(second half of level 3 cell)
        x1 = centre + int(((level + 1)*40) * sine(cellnum * angle - angle/4 )) 
        y1 = centre + int(((level + 1)*40) * cosine(cellnum * angle - angle/4))
        if img[x1,y1] == 255:
            temp = (level + 1,cellnum * 2)
            neighbours.append(temp)

        #next lower level - level 1
        x1 = centre + int((level * 40) * sine((cellnum - 1) * angle + angle/2))
        y1 = centre + int((level * 40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255 and cellnum%2==1:  #level 2 odd cell
            temp = (level - 1,(cellnum+1)/2)
            neighbours.append(temp)
        elif img[x1,y1] == 255:                 #level 2 even cell
            temp = (level - 1,(cellnum)/2)
            neighbours.append(temp)


    elif level == 3:
        angle = 15

        #for upper cell - level 3
        x1 = centre + int((level*40 + 20)*sine((cellnum - 1) * angle))
        y1 = centre + int((level*40 + 20)*cosine((cellnum - 1) * angle))
        if img[x1,y1] == 255:
            if cellnum == 1:
                temp = (3,24)
            else:
                temp = (3,cellnum - 1)
            neighbours.append(temp)

        #for lower cell - level 3
        x1 = centre + int((level*40 + 20) * sine(cellnum * angle)) 
        y1 = centre + int((level*40 + 20) * cosine(cellnum * angle))
        if img[x1,y1] == 255:
            if cellnum == 24:
                temp = (3,1)
            else:
                temp = (3,cellnum + 1)
            neighbours.append(temp)

        #next upper level- level 4 same cell number
        x1 = centre + int(((level + 1)*40) * sine((cellnum - 1) * angle + angle/2)) 
        y1 = centre + int(((level + 1)*40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255:
            temp = (level + 1,cellnum)
            neighbours.append(temp)

        #next lower level- level 2
        x1 = centre + int((level * 40) * sine((cellnum - 1) * angle + angle/2))
        y1 = centre + int((level * 40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255 and cellnum%2==1:  #level 3 odd cell
            temp = (level - 1,(cellnum+1)/2)
            neighbours.append(temp)
        elif img[x1,y1] == 255:                 #level 3 even cell
            temp = (level - 1,(cellnum)/2)
            neighbours.append(temp)
        
    elif level == 4 :
        angle = 15

        #for upper cell - level 4
        x1 = centre + int((level*40 + 20)*sine((cellnum - 1) * angle)) 
        y1 = centre + int((level*40 + 20)*cosine((cellnum - 1) * angle))
        if img[x1,y1] == 255:
            if cellnum == 1:
                temp = (level,24)
            else:
                temp = (level,cellnum - 1)
            neighbours.append(temp)

        #for lower cell - level 4        
        x1 = centre + int((level*40 + 20) * sine(cellnum * angle)) 
        y1 = centre + int((level*40 + 20) * cosine(cellnum * angle))
        if img[x1,y1] == 255:
            if cellnum == 24:
                temp = (level,1)
            else:
                temp = (level,cellnum + 1)
            neighbours.append(temp)

        #next upper level- level 5 same cell number only when size == 2 
        if size == 2 :
            x1 = centre + int(((level + 1)*40) * sine((cellnum - 1) * angle + angle/2)) 
            y1 = centre + int(((level + 1)*40) * cosine((cellnum - 1) * angle + angle/2))
            if img[x1,y1] == 255:
                temp = (level + 1,cellnum)
                neighbours.append(temp)

        #next lower level- level 3 same cell number
        x1 = centre + int((level * 40) * sine((cellnum - 1) * angle + angle/2)) #next lower level
        y1 = centre + int((level * 40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255:
            temp = (level - 1,cellnum)
            neighbours.append(temp)

    elif level == 5 :
        angle = 15

        #for upper cell - level 5
        x1 = centre + int((level*40 + 20)*sine((cellnum - 1) * angle)) 
        y1 = centre + int((level*40 + 20)*cosine((cellnum - 1) * angle))
        if img[x1,y1] == 255:
            if cellnum == 1:
                temp = (level,24)
            else:
                temp = (level,cellnum - 1)
            neighbours.append(temp)

        #for lower cell - level 5  
        x1 = centre + int((level*40 + 20) * sine(cellnum * angle))
        y1 = centre + int((level*40 + 20) * cosine(cellnum * angle))
        if img[x1,y1] == 255:
            if cellnum == 24:
                temp = (level,1)
            else:
                temp = (level,cellnum + 1)
            neighbours.append(temp)
            
        #next upper level - level 6 odd cell
        x1 = centre + int(((level + 1)*40) * sine((cellnum - 1) * angle + angle/4)) #next upper level
        y1 = centre + int(((level + 1)*40) * cosine((cellnum - 1) * angle + angle/4))
        if img[x1,y1] == 255:
            temp = (level + 1,cellnum*2 - 1)
            neighbours.append(temp)

        #next upper level - level 6 even cell
        x1 = centre + int(((level + 1)*40) * sine(cellnum * angle - angle/4 )) 
        y1 = centre + int(((level + 1)*40) * cosine(cellnum * angle - angle/4))
        if img[x1,y1] == 255:
            temp = (level + 1,cellnum * 2)
            neighbours.append(temp)

        #next lower level - level 4 same cell number
        x1 = centre + int((level * 40) * sine((cellnum - 1) * angle + angle/2)) 
        y1 = centre + int((level * 40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255:
            temp = (level - 1,cellnum)
            neighbours.append(temp)
            
    else:
        angle = 7.5

        #for upper cell - level 6
        x1 = centre + int((level*40 + 20)*sine((cellnum - 1) * angle))
        y1 = centre + int((level*40 + 20)*cosine((cellnum - 1) * angle))
        if img[x1,y1] == 255:
            if cellnum == 1:
                temp = (level,48)
            else:
                temp = (level,cellnum - 1)
            neighbours.append(temp)

        #for lower cell - level 6
        x1 = centre + int((level*40 + 20) * sine(cellnum * angle)) 
        y1 = centre + int((level*40 + 20) * cosine(cellnum * angle))
        if img[x1,y1] == 255:
            if cellnum == 48:
                temp = (level,1)
            else:
                temp = (level,cellnum + 1)
            neighbours.append(temp)

        #next lower level - level 5
        x1 = centre + int((level * 40) * sine((cellnum - 1) * angle + angle/2)) 
        y1 = centre + int((level * 40) * cosine((cellnum - 1) * angle + angle/2))
        if img[x1,y1] == 255 and cellnum%2==1:  # odd cell
            temp = (level - 1,(cellnum+1)/2)
            neighbours.append(temp)
        elif img[x1,y1] == 255:                 # even cell
            temp = (level - 1,(cellnum)/2)
            neighbours.append(temp)
            
    #################################################################################
    return neighbours
"""
##  colourCell function takes 5 arguments:-
##            img - input image
##            level - level of cell to be coloured
##            cellnum - cell number of cell to be coloured
##            size - size of maze
##            colourVal - the intensity of the colour.
##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the black walls and only paints the empty spaces. This function returns the image
##  with the painted cell.
"""
def colourCell(img, level, cellnum, size, colourVal):
    ############################# Add your Code Here ################################
    if size == 1:
        centre=220
    else:
        centre=300
    def colorneighbourpixel(img,x,y):   #colouring neighbours of a pixel as position calculation is based on angles
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
        array = np.arange((cellnum-1)* angle, cellnum * angle ,1)   #array for storing angles increasing by 1 degree
    elif level == 1:
        angle = 60
        array = np.arange((cellnum-1)* angle, cellnum * angle ,1)   #array for storing angles increasing by 1 degree
    elif level == 2:
        angle = 30
        array = np.arange((cellnum-1)* angle, cellnum * angle ,1)   #array for storing angles increasing by 1 degree
    elif (level == 3 or level == 4 or level == 5):
        angle = 15
        array = np.arange((cellnum-1)* angle, cellnum * angle ,.5)  #array for storing angles increasing by 0.5 degree
    else:
        angle = 7.5
        array = np.arange((cellnum-1)* angle, cellnum * angle ,.5)  #array for storing angles increasing by 0.5 degree

    for i in array:
        for m in range(level*40,(level + 1)*40):
            x1 = centre + int(m*sine(i))
            y1 = centre + int(m*cosine(i))
            colorneighbourpixel(img,x1,y1)
        
    #################################################################################  
    return img
"""
##  Function that accepts some arguments from user and returns the graph of the maze image.
"""
def buildGraph(img, size):      ## You can pass your own arguments in this space.
    graph = {}
    ############################# Add your Code Here ################################
    if size == 1:
        level = 4
        centre=220
    else:
        level = 6
        centre=300

    for cell in range(1, 7):    # neighbours for level 1 cells
            graph[(1, cell)] = findNeighbours(img, 1, cell, size)
    for cell in range(1, 13):   # neighbours for level 2 cells
            graph[(2, cell)] = findNeighbours(img, 2, cell, size)
    for lvl in range(3, 5):     # neighbours for level 3 and level 4 cells
        for cell in range(1, 25):
            graph[(lvl, cell)] = findNeighbours(img, lvl, cell, size)
            
    if(size == 2):
        for cell in range(1, 25):   # neighbours for level 5 cells
            graph[(5, cell)] = findNeighbours(img, 5, cell, size)
        for cell in range(1, 49):   # neighbours for level 6 cells
            graph[(6, cell)] = findNeighbours(img, 6, cell, size)

    # neighbours for (0,0) - level 0
    angle=60
    arr = []
    for cellnum in range(1,7):
        x1 = centre + int((40) * sine((cellnum - 1) * angle + angle/2)) #next upper level
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
##  Finds shortest path between two coordinates in the maze. Returns a set of coordinates from initial point
##  to final point.
"""
def findPath(init, final, graph):             ## You can pass your own arguments in this space.
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
## The findMarkers() function returns a list of coloured markers in form of a python dictionaries
## For example if a blue marker is present at (3,6) and red marker is present at (1,5) then the
## dictionary is returned as :-
##          list_of_markers = { 'Blue':(3,6), 'Red':(1,5)}
"""
def findMarkers(img,size):             ## You can pass your own arguments in this space.
    list_of_markers = {}
    ############################# Add your Code Here ################################
    # Red Section #
    def findcell(img,centre):
        array = []
        #level 0
        x1 = centre 
        y1 = centre
        if img[x1, y1] > 127:
            temp = (0, 0)
            array.append(temp)
        #level 1
        level = 1
        angle = 60
        for cellnum in range(1, 7):
            x1 = centre + int((level * 40 + 20) * sine((cellnum - 1) * angle + angle/2)) #centre of the cell
            y1 = centre + int((level * 40 + 20) * cosine((cellnum - 1) * angle + angle/2))
            if img[x1, y1] > 127:
                temp = (1, cellnum)
                array.append(temp)
        #level 2
        level = 2
        angle = 30
        for cellnum in range(1, 13):
            x1 = centre + int((level * 40 + 20) * sine((cellnum - 1) * angle + angle/2)) #centre of the cell
            y1 = centre + int((level * 40 + 20) * cosine((cellnum - 1) * angle + angle/2))
            if img[x1, y1] > 127:
                temp = (level, cellnum)
                array.append(temp)
        #level 3 and 4
        angle = 15
        for level in range(3,5):
            for cellnum in range(1, 25):
                x1 = centre + int((level * 40 + 20) * sine((cellnum - 1) * angle + angle/2)) #centre of the cell
                y1 = centre + int((level * 40 + 20) * cosine((cellnum - 1) * angle + angle/2))
                if img[x1, y1] > 127:
                    temp = (level, cellnum)
                    array.append(temp)
                    
        if size == 2:
                #level 5
                level = 5
                angle = 15
                for cellnum in range(1, 25):
                    x1 = centre + int((level * 40 + 20) * sine((cellnum - 1) * angle + angle/2)) #centre of the cell
                    y1 = centre + int((level * 40 + 20) * cosine((cellnum - 1) * angle + angle/2))
                    if img[x1, y1] > 127:
                        temp = (level, cellnum)
                        array.append(temp)
                #level 6
                level = 6
                angle = 7.5
                for cellnum in range(1, 49):
                    x1 = centre + int((level * 40 + 20) * sine((cellnum - 1) * angle + angle/2)) #centre of the cell
                    y1 = centre + int((level * 40 + 20) * cosine((cellnum - 1) * angle + angle/2))
                    if img[x1, y1] > 127:
                        temp = (level, cellnum)
                        array.append(temp)
        return array
    
    if size == 1:
        centre = 220
    else:
        centre = 300

    # red marker         
    red_low_bound0 = np.array([170, 100, 100])
    red_up_bound0 = np.array([180, 255, 255])
    red_low_bound1 = np.array([0, 100, 100])
    red_up_bound1 = np.array([10, 255, 255])

    red_mask1 = cv2.inRange(img, red_low_bound0, red_up_bound0)
    red_mask2 = cv2.inRange(img, red_low_bound1, red_up_bound1)
    red_mask = red_mask1 | red_mask2

    list_of_markers['Red'] = findcell(red_mask, centre)

    # blue marker
    blue_low_bound = np.array([110, 100, 100])
    blue_up_bound = np.array([130, 255, 255])

    blue_mask = cv2.inRange(img, blue_low_bound, blue_up_bound)

    list_of_markers['Blue'] = findcell(blue_mask, centre)
    
    #################################################################################
    return list_of_markers
"""
## The findOptimumPath() function returns a python list which consists of all paths that need to be traversed
## in order to start from the START cell and traverse to any one of the markers ( either blue or red ) and then
## traverse to FINISH. The length of path should be shortest ( most optimal solution).
"""
def findOptimumPath( img, list_of_markers , size):     ## You can pass your own arguments in this space.
    ############################# Add your Code Here ################################
    graph = {}
    graph = buildGraph(img, size)
    shortest = [ ]
    start = findStartPoint(img, size)
    markers = [i for i in list_of_markers.values()]

    cell = markers[0]
    blue_marker = cell[0]
    cell = markers[1]
    red_marker = cell[0]
    path_blue = findPath(start, blue_marker, graph)
    path_red = findPath(start, red_marker, graph)
    pathb = []
    pathr = []
    pathArray = []
    end = (0,0)
    len_blue = len(path_blue)
    len_red = len(path_red)
    endcell = []
    endcell =  findPath(blue_marker, end, graph)
    lenb = len_blue + len(endcell)
    pathb.append(path_blue)
    pathb.append(endcell)
    endcell = []
    endcell = findPath(red_marker, end, graph)
    lenr = len_red + len(endcell)
    pathr.append(path_red)
    pathr.append(endcell)
    if lenr == lenb:
        if len_blue < len_red:
            pathArray = pathb
        else:
            pathArray = pathr
    elif lenr <  lenb:
        pathArray = pathr
    else:
        pathArray = pathb

    #################################################################################
    return pathArray
"""
## The colourPath() function highlights the whole path that needs to be traversed in the maze image and
## returns the final image.
"""
def colourPath( img, path_array , size ):   ## You can pass your own arguments in this space. 
    ############################# Add your Code Here ################################
    for node in path_array:
        for subnode in node:
            colourCell(img, subnode[0], subnode[1], size, 180)

    #################################################################################
    return img

#####################################    Add Utility Functions Here   ###################################
##                                                                                                     ##
##                   You are free to define any functions you want in this space.                      ##
##                             The functions should be properly explained.                             ##




##                                                                                                     ##
##                                                                                                     ##
#########################################################################################################
"""
## This is the main() function for the code, you are not allowed to change any statements in this part of
## the code. You are only allowed to change the arguments supplied in the findMarkers(), findOptimumPath()
## and colourPath() functions.
"""
def main(filePath, flag = 0):
    img = readImageHSV(filePath)
    imgBinary = readImageBinary(filePath)
    if len(img) == 440:
        size = 1
    else:
        size = 2
    listofMarkers = findMarkers(img,size)
    path = findOptimumPath(imgBinary, listofMarkers, size)
    img = colourPath(imgBinary, path, size)
    print path
    print listofMarkers
    if __name__ == "__main__":                    
        return img
    else:
        if flag == 0:
            return path
        elif flag == 1:
            return str(listofMarkers) + "\n"
        else:
            return img
"""
## The main() function is called here. Specify the filepath of image in the space given.
"""
if __name__ == "__main__":
    filePath = "image_09.jpg"     ## File path for test image
    img = main(filePath)           ## Main function call
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
