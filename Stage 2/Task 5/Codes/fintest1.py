import numpy as np
import cv2
import math
import time

## Reads image in HSV format. Accepts filepath as input argument and returns the HSV
## equivalent of the image.
def readImageHSV(filePath):
    mazeImg = cv2.imread(filePath)
    hsvImg = cv2.cvtColor(mazeImg, cv2.COLOR_BGR2HSV)
    return hsvImg

## Reads image in binary format. Accepts filepath as input argument and returns the binary
## equivalent of the image.
def readImageBinary(filePath):
    mazeImg = cv2.imread(filePath)
    grayImg = cv2.cvtColor(mazeImg, cv2.COLOR_BGR2GRAY)
    ret,binaryImage = cv2.threshold(grayImg,100,255,cv2.THRESH_BINARY)
    return binaryImage

##  Returns sine of an angle.
def sine(angle):
    return math.sin(math.radians(angle))

##  Returns cosine of an angle
def cosine(angle):
    return math.cos(math.radians(angle))

##  This function accepts the img, level and cell number of a particular cell and the size of the maze as input
##  arguments and returns the list of cells which are traversable from the specified cell.
def findNeighbours(img, level, cellnum):
    neighbours = []
    ############################# Add your Code Here ################################

    centre = 495
    A1 = 90
    A2 = 36
    A3 = 24
    A4 = 18
    rad1 = 80
    rad2 = 178
    rad3 = 276
    rad4 = 375

    if level == 1:
        #for uppr circle - level 2
        temp = (2,cellnum)
        neighbours.append(temp)
        
    if level == 2:
        angle = 90
        #for neighbours
        if cellnum == 1:
            temp = (2,4)
        else:
            temp = (2,cellnum - 1)
        neighbours.append(temp)
        if cellnum == 4:
            temp = (2,1)
        else:
            temp = (2,cellnum + 1)
        neighbours.append(temp)
        #for lower circle - level 1
        x1 = centre + int((rad1-20)*sine(270 - (cellnum - 1) * angle - angle/2))
        y1 = centre + int((rad1-20)*cosine(270 - (cellnum - 1) * angle - angle/2))
        if img[x1,y1] < 128:
            temp = (level-1,cellnum)
            neighbours.append(temp)
        #for upper circle - level 3
        N1 = float((cellnum-1)*angle)/A2
        N2 = float((cellnum-1)*angle)//A2
        N3 = float(cellnum*angle)/A2
        N4 = float(cellnum*angle)//A2
        if (N1-N2) >= 0.5:
            N1 = int(round(N1))
            N3 = int(N3)
        if (N3-N4) >= 0.5:
            N3 = int(round(N3))
            N1 =int(N1+1)
        arr = range(N1,N3+1)
        for i in arr:
            x1 = centre + int((rad2) * sine( 270 -((i-1) * A2 + A2/2))) #for upper circle
            y1 = centre + int((rad2) * cosine( 270 - ((i-1) * A2 + A2/2)))
            if img[x1,y1] > 128:
                temp = (level+1,i)
                neighbours.append(temp)

    if level == 3:
        angle = 36
        #for lower circle - level 4
        if cellnum == 1:
            temp = (3,10)
        else:
            temp = (3,cellnum - 1)
        neighbours.append(temp)
        if cellnum == 10:
            temp = (3,1)
        else:
            temp = (3,cellnum + 1)
        neighbours.append(temp)
        #for lower circle - level 2
        sweep = angle*(cellnum-1) + angle/2
        sweep2 = sweep//A1
        sweep = float(sweep)/A1
        if(sweep - sweep2)<.5:
            num = int(round(sweep))
            x1 = centre + int((rad2) * sine( 270 -((cellnum-1) * A2 + A2/2)))
            y1 = centre + int((rad2) * cosine( 270 - ((cellnum-1) * A2 + A2/2)))
            if img[x1,y1] > 128:
                temp = (level-1,num+1)
                neighbours.append(temp)
        elif(sweep - sweep2)>.5:
            num = int(round(sweep))
            x1 = centre + int((rad2) * sine( 270 -((cellnum-1) * A2 + A2/2)))
            y1 = centre + int((rad2) * cosine( 270 - ((cellnum-1) * A2 + A2/2)))
            if img[x1,y1] > 128:
                temp = (level-1,num)
                neighbours.append(temp)
        #for upper circle - level 4
        N1 = float((cellnum-1)*angle)/A3
        N2 = float((cellnum-1)*angle)//A3
        N3 = float(cellnum*angle)/A3
        N4 = float(cellnum*angle)//A3
        if (N1-N2) >= 0.5:
            N1 = int(round(N1))
            N3 = int(N3)
        if (N3-N4) >= 0.5:
            N3 = int(round(N3))
            N1 =int(N1+1)
        arr = range(N1,N3+1)
        for i in arr:
            x1 = centre + int((rad3) * sine( 270 -((i-1) * A3 + A3/2))) #for upper circle
            y1 = centre + int((rad3) * cosine( 270 - ((i-1) * A3 + A3/2)))
            if img[x1,y1] > 128:
                temp = (level+1,i)
                neighbours.append(temp)
                
    if level == 4:
        angle = 24
        #for lower circle - level 4
        if cellnum == 1:
            temp = (4,15)
        else:
            temp = (4,cellnum - 1)
        neighbours.append(temp)
        if cellnum == 15:
            temp = (4,1)
        else:
            temp = (4,cellnum + 1)
        neighbours.append(temp)
        #for lower circle
        sweep = angle*(cellnum-1) + angle/2
        sweep2 = sweep//A2
        sweep = float(sweep)/A2
        if(sweep - sweep2)<.5:
            num = int(round(sweep))
            x1 = centre + int((rad3) * sine( 270 -((cellnum-1) * A3 + A3/2)))
            y1 = centre + int((rad3) * cosine( 270 - ((cellnum-1) * A3 + A3/2)))
            if img[x1,y1] > 128:
                temp = (level-1,num+1)
                neighbours.append(temp)
        elif(sweep - sweep2)>.5:
            num = int(round(sweep))
            x1 = centre + int((rad3) * sine( 270 -((cellnum-1) * A3 + A3/2)))
            y1 = centre + int((rad3) * cosine( 270 - ((cellnum-1) * A3 + A3/2)))
            if img[x1,y1] > 128:
                temp = (level-1,num)
                neighbours.append(temp)
        #for upper circle - level 5
        N1 = float((cellnum-1)*angle)/A4
        N2 = float((cellnum-1)*angle)//A4
        N3 = float(cellnum*angle)/A4
        N4 = float(cellnum*angle)//A4
        if (N1-N2) < 0.3:
            N1 = int(round(N1+1))#change
            N3 = int(N3)
            if cellnum==1:
                N1=N1
        elif (N1-N2)>=.6: #change
            N1 = int(round(N1+1))
            N3 = int(N3)
        if (N3-N4) >= 0.3:#change
            N3 = int(round(N3))
            N1 =int(N1+1)
        arr = range(N1,N3+1)
        for i in arr:
            x1 = centre + int((rad4) * sine( 270 -((i-1) * A4 + A4/2))) #for upper circle
            y1 = centre + int((rad4) * cosine( 270 - ((i-1)* A4 + A4/2)))
            if img[x1,y1] > 128:
                temp = (level+1,i)
                neighbours.append(temp)
    if level == 5:
        angle = 18
        #for neighbours
        if cellnum == 1:
            temp = (5,20)
        else:
            temp = (5,cellnum - 1)
        neighbours.append(temp)
        if cellnum == 20:
            temp = (5,1)
        else:
            temp = (5,cellnum + 1)
        neighbours.append(temp)
        #for lower circle - level 4
        sweep = angle*(cellnum-1) + angle/2
        sweep2 = sweep//A3
        sweep = float(sweep)/A3
        if(sweep - sweep2)<.5:
            num = int(round(sweep))
            x1 = centre + int((rad4) * sine( 270 -((cellnum-1) * A4 + A4/2)))
            y1 = centre + int((rad4) * cosine( 270 - ((cellnum-1) * A4 + A4/2)))
            if img[x1,y1] > 128:
                temp = (level-1,num+1)
                neighbours.append(temp)
        elif(sweep - sweep2)>.5:
            num = int(round(sweep))
            x1 = centre + int((rad4) * sine( 270 -((cellnum-1) * A4 + A4/2)))
            y1 = centre + int((rad4) * cosine( 270 - ((cellnum-1) * A4 + A4/2)))
            if img[x1,y1] > 128:
                temp = (level-1,num)
                neighbours.append(temp)
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
def colourCell(img, level, cellnum, colourVal):
    ############################# Add your Code Here ################################

    centre = 495
    
    if level == 1:
        angle = 90
        rad = 0
        rad2 = 80
        array = np.arange(270- cellnum * angle, 270-(cellnum-1) * angle ,.1)   #array for storing angles increasing by 1 degree
    elif level == 2:
        angle = 90
        rad = 80
        rad2 = 178
        array = np.arange(270-(cellnum)* angle,270 - (cellnum-1) * angle ,.1)   #array for storing angles increasing by 1 degree
    elif level == 3:
        angle = 36
        rad = 178
        rad2 = 276
        array = np.arange(270 - cellnum * angle,270 - (cellnum-1) * angle ,.1)  #array for storing angles increasing by 0.5 degree
    elif level == 4:
        angle = 24
        rad = 276
        rad2 = 375
        array = np.arange(270 - cellnum * angle,270 - (cellnum-1) * angle ,.05)  #array for storing angles increasing by 0.5 degree
    elif level == 5:
        angle = 18
        rad = 375
        rad2 = 475
        array = np.arange(270 - cellnum * angle,270 - (cellnum-1) * angle ,.05)  #array for storing angles increasing by 0.5 degree
        
    for i in array:
        for m in range(rad,rad2):
            x1 = centre + int(m*sine(i))
            y1 = centre + int(m*cosine(i))
            if img[x1,y1] > 0:
                img[x1,y1] = colourVal
    #################################################################################  
    return img

##  Function that accepts some arguments from user and returns the graph of the maze image.
def buildGraph(img):      ## You can pass your own arguments in this space.
    graph = {}
    ############################# Add your Code Here ################################
    for cell in range(1, 5):
            graph[(1, cell)] = findNeighbours(img, 1, cell)
    for cell in range(1, 5):
            graph[(2, cell)] = findNeighbours(img, 2, cell)
    for cell in range(1, 11):
            graph[(3, cell)] = findNeighbours(img, 3, cell)
    for cell in range(1, 16):
            graph[(4, cell)] = findNeighbours(img, 4, cell)
    for cell in range(1, 21):
            graph[(5, cell)] = findNeighbours(img, 5, cell)

    # Printing sorted graph. Uncomment when needed
    """for key in sorted(graph):
        print "%s: %s" % (key, graph[key])"""

    #################################################################################
    return graph

##  Function accepts some arguments and returns the Start coordinates of the maze.
def findEndPoint(img):     ## You can pass your own arguments in this space.
    ############################# Add your Code Here ################################
    centre = 495
    angle = 90
    rad = 65
    for cellnum in range(1,5):
        x1 = centre + int( rad * sine(270 - (cellnum - 1) * angle - angle/2)) #next upper level
        y1 = centre + int(rad * cosine(270 - (cellnum - 1) * angle - angle/2))
        if img[x1,y1] < 128 :
            start = (1,cellnum)

    #################################################################################
    return start

##  Finds shortest path between two coordinates in the maze. Returns a set of coordinates from initial point
##  to final point.
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

## The findMarkers() function returns a list of coloured markers in form of a python dictionaries
## For example if a blue marker is present at (3,6) and red marker is present at (1,5) then the
## dictionary is returned as :-
##          list_of_markers = { 'Blue':(3,6), 'Red':(1,5)}
def findMarkers(img):             ## You can pass your own arguments in this space.
    list_of_markers = {}
    ############################# Add your Code Here ################################
    # Red Section #
    def findcell(img):
        centre = 495
        array = []
        
        #level 2
        level = 2
        angle = 90
        rad = 82
        rad2 = 176
        k=0
        for cellnum in range(1, 5):
            arr = np.arange(270 - cellnum * angle,270 - (cellnum-1) * angle ,1)  #array for storing angles increasing by 0.5 degree
            for i in arr:
                for m in range(rad+20,rad2,5):
                    x1 = centre + int(m*sine(i))
                    y1 = centre + int(m*cosine(i))
                    if img[x1,y1] > 127:
                        temp = (level, cellnum)
                        array.append(temp)
                        k=1
                        break
                if k==1:
                    break
            if k==1:
                break
        #level 3
        level = 3
        angle = 36
        rad = 180
        rad2 = 274
        k=0
        for cellnum in range(1, 11):
            arr = np.arange(270 - cellnum * angle,270 - (cellnum-1) * angle ,1)  #array for storing angles increasing by 0.5 degree
            for i in arr:
                for m in range(rad+20,rad2,5):
                    x1 = centre + int(m*sine(i))
                    y1 = centre + int(m*cosine(i))
                    if img[x1,y1] > 127:
                        temp = (level, cellnum)
                        array.append(temp)
                        k=1
                        break
                if k==1:
                    break
            if k==1:
                break
        #level 4
        level = 4
        angle = 24
        rad = 278
        rad2 = 372
        k=0
        for cellnum in range(1, 16):
            arr = np.arange(270 - cellnum * angle,270 - (cellnum-1) * angle ,1)  #array for storing angles increasing by 0.5 degree
            for i in arr:
                for m in range(rad+20,rad2,5):
                    x1 = centre + int(m*sine(i))
                    y1 = centre + int(m*cosine(i))
                    if img[x1,y1] > 127:
                        temp = (level, cellnum)
                        array.append(temp)
                        k=1
                        break
                if k==1:
                    break
            if k==1:
                break

        #level 5
        level = 5
        angle = 18
        rad = 380
        rad2 = 470
        k=0
        for cellnum in range(2, 20):
            arr = np.arange(270 - cellnum * angle,270 - (cellnum-1) * angle ,1)  #array for storing angles increasing by 0.5 degree
            for i in arr:
                for m in range(rad+20,rad2,5):
                    x1 = centre + int(m*sine(i))
                    y1 = centre + int(m*cosine(i))
                    if img[x1,y1] > 127:
                        temp = (level, cellnum)
                        array.append(temp)
                        k=1
                        break
                if k==1:
                    break
            if k==1:
                break
        
        return temp
        
    
    # red marker         
    red_low_bound0 = np.array([175, 100, 100])
    red_up_bound0 = np.array([180, 255, 255])
    red_low_bound1 = np.array([0, 100, 100])
    red_up_bound1 = np.array([10, 255, 255])

    red_mask1 = cv2.inRange(img, red_low_bound0, red_up_bound0)
    red_mask2 = cv2.inRange(img, red_low_bound1, red_up_bound1)
    red_mask = red_mask1 | red_mask2

    list_of_markers['Red'] = findcell(red_mask)

    # blue marker
    blue_low_bound = np.array([110, 100, 100])
    blue_up_bound = np.array([130, 255, 255])

    blue_mask = cv2.inRange(img, blue_low_bound, blue_up_bound)

    list_of_markers['Blue'] = findcell(blue_mask)

    # sky blue marker
    sblue_low_bound = np.array([90, 100, 100])
    sblue_up_bound = np.array([110, 255, 255])

    sblue_mask = cv2.inRange(img, sblue_low_bound, sblue_up_bound)

    list_of_markers['Sky-Blue'] = findcell(sblue_mask)
    
    # pink marker
    pink_low_bound = np.array([145, 100, 100])
    pink_up_bound = np.array([170, 255, 255])
    
    pink_mask = cv2.inRange(img, pink_low_bound, pink_up_bound)

    list_of_markers['Pink'] = findcell(pink_mask)

    # green marker
    green_low_bound = np.array([50, 100, 100])
    green_up_bound = np.array([70, 255, 255])
    
    green_mask = cv2.inRange(img, green_low_bound, green_up_bound)

    list_of_markers['Green'] = findcell(green_mask)

    # yellow marker
    yellow_low_bound = np.array([25, 100, 100])
    yellow_up_bound = np.array([35, 255, 255])
    
    yellow_mask = cv2.inRange(img, yellow_low_bound, yellow_up_bound)

    list_of_markers['Yellow'] = findcell(yellow_mask)

    # white marker
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,white_mask = cv2.threshold(grayImg,50,255,cv2.THRESH_BINARY_INV)

    list_of_markers['White'] = findcell(white_mask)
    #cv2.imshow("white",white_mask)
    #################################################################################
    return list_of_markers

## The findOptimumPath() function returns a python list which consists of all paths that need to be traversed
## in order to start from the START cell and traverse to any one of the markers ( either blue or red ) and then
## traverse to FINISH. The length of path should be shortest ( most optimal solution).
def findOptimumPath(img, init, final, list_of_markers = {}):     ## You can pass your own arguments in this space.
    ############################# Add your Code Here ################################
    graph = {}
    graph = buildGraph(img)
    shortest = [ ]
    path_array = []
    markers = [i for i in list_of_markers.values()]
    cur_starting_point = init
    while (markers):
        shortest_path = [i for i in graph.values()]
        for node in markers:
            #print node
            temp_path = findPath(cur_starting_point, node,graph)
            if len(temp_path) < len(shortest_path):
                shortest_path = temp_path
                #print shortest_path
        cur_starting_point = shortest_path[-1]
        path_array.append(shortest_path)
        markers.remove(shortest_path[-1])
    
    path_array.append(findPath(cur_starting_point, final,graph))
    #################################################################################
    return path_array

## The colourPath() function highlights the whole path that needs to be traversed in the maze image and
## returns the final image.
def colourPath( img, path_array ):   ## You can pass your own arguments in this space. 
    ############################# Add your Code Here ################################
    print path_array
    for node in path_array:
        for subnode in node:
            colourCell(img, subnode[0], subnode[1], 180)
    """for node in path_array:
            colourCell(img, node[0], node[1], 180)"""

    #################################################################################
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
    img = readImageHSV(filePath)
    cimg = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
    ret, timg = cv2.threshold(cimg, 225, 255, cv2.THRESH_BINARY)
    imgBinary = readImageBinary(filePath)
    listofMarkers = findMarkers(img)
    start = (5,1)
    end = findEndPoint(imgBinary)
    print end
    #end = listofMarkers.values()
    #print end[0]
    path = findOptimumPath(imgBinary, start, end, listofMarkers)
    #graph = buildGraph(imgBinary)
    #path = findPath(start,end,graph)
    #for key in sorted(graph):
    #print "%s: %s" % (key, graph[key])
    print path
    cimg = colourPath(timg, path)
    print listofMarkers
    if __name__ == "__main__":                    
        return timg #imgBinary
    else:
        if flag == 0:
            return path
        elif flag == 1:
            return str(listofMarkers) + "\n"
        else:
            return timg
    
## The main() function is called here. Specify the filepath of image in the space given.
if __name__ == "__main__":
    filePath = "MAP - 102.jpg"     ## File path for test image
    img = main(filePath)           ## Main function call
    #cv2.imshow("image",img)
    simg = cv2.resize(img,None,fx=.5, fy=.5, interpolation = cv2.INTER_CUBIC)
    cv2.imshow("image",simg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
