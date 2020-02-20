import numpy as np
import cv2

## Reads image in HSV format. Accepts filepath as input argument and returns the HSV
## equivalent of the image.
def readImageHSV(filePath):
    #############  Add your Code here   ###############
    img = cv2.imread(filePath, cv2.IMREAD_COLOR)
    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    ###################################################
    return hsvImg

## Reads image in binary format. Accepts filepath as input argument and returns the binary
## equivalent of the image.
def readImageBinary(filePath):
    #############  Add your Code here   ###############
    img = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
    ret, binaryImage = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    ###################################################
    return binaryImage

## The findNeighbours function takes a maze image and row and column coordinates of a cell as input arguments
## and returns a stack consisting of all the neighbours of the cell as output.
## Note :- Neighbour refers to all the adjacent cells one can traverse to from that cell provided only horizontal
## and vertical traversal is allowed.
def findNeighbours(img,row,column):
    neighbours = []
    #############  Add your Code here   ###############
    r = (row * 20) + 10
    c = (column * 20) + 10
    maxdim = []
    maxdim = img.shape
    if row == (maxdim[0] / 20) - 1 and column == (maxdim[1] / 20) - 1:
        if img[r - 11, c] == 255:
            temp = (row - 1, column)
            neighbours.append(temp)
        if img[r, c - 11] == 255:
            temp = (row, column - 1)
            neighbours.append(temp)
        
    elif row == 0 and column == (maxdim[1] / 20) - 1:
        if img[r + 11, c] == 255:
            temp = (row + 1, column)
            neighbours.append(temp)
        if img[r, c - 11] == 255:
            temp = (row, column - 1)
            neighbours.append(temp)

    elif row == 0 and column == 0:
        
        if img[r, c + 11] == 255:
            temp = (row, column+1)
            neighbours.append(temp)
        if img[r + 11, c] == 255:
            temp = (row + 1, column)
            neighbours.append(temp)

    elif row == (maxdim[0] / 20) - 1 and column == 0:
        if img[r - 11, c] == 255:
            temp = (row - 1, column)
            neighbours.append(temp)
        if img[r, c + 11] == 255:
            temp = (row, column + 1)
            neighbours.append(temp)

    elif row == 0:
        if img[r, c - 11] == 255:
            temp = (row, column - 1)
            neighbours.append(temp)        
        if img[r, c + 11] == 255:
            temp = (row, column + 1)
            neighbours.append(temp)
        if img[r + 11, c] == 255:
            temp = (row + 1, column)
            neighbours.append(temp)

    elif row == (maxdim[0] / 20) - 1:
        if img[r, c - 11] == 255:
            temp = (row, column - 1)
            neighbours.append(temp)        
        if img[r, c + 11] == 255:
            temp = (row, column + 1)
            neighbours.append(temp)
        if img[r - 11, c] == 255:
            temp = (row - 1, column)
            neighbours.append(temp)

    elif column == 0:
        if img[r - 11, c] == 255:
            temp = (row - 1, column)
            neighbours.append(temp)
        if img[r + 11, c] == 255:
            temp = (row + 1, column)
            neighbours.append(temp)
        if img[r, c + 11] == 255:
            temp = (row, column + 1)
            neighbours.append(temp)

    elif column == (maxdim[1] / 20) - 1:
        if img[r - 11, c] == 255:
            temp = (row - 1, column)
            neighbours.append(temp)
        if img[r + 11, c] == 255:
            temp = (row + 1, column)
            neighbours.append(temp)
        if img[r, c - 11] == 255:
            temp = (row, column - 1)
            neighbours.append(temp)

    else:
        if img[r - 11, c] == 255:
            temp = (row - 1, column)
            neighbours.append(temp)
        if img[r, c - 11] == 255:
            temp = (row, column - 1)
            neighbours.append(temp)
        if img[r, c + 11] == 255:
            temp = (row, column + 1)
            neighbours.append(temp)
        if img[r + 11, c] == 255:
            temp = (row + 1, column)
            neighbours.append(temp)
    ###################################################
    return neighbours

##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the black walls and only paints the empty spaces. This function returns the image
##  with the painted cell.
##  You can change the colourCell() functions used in the previous sections to suit your requirements.

def colourCell( img,row,column,colourVal  ):   ## Add required arguments here.
    #############  Add your Code here   ###############
    r = row * 20
    c = column * 20
    for rcount in range(r, r + 20):
        for ccount in range(c, c + 20):
            if img[rcount, ccount] < 250:
                continue
            img[rcount, ccount] = colourVal
    ###################################################
    return img

##  Function that accepts some arguments from user and returns the graph of the maze image.
def buildGraph(img):  ## You can pass your own arguments in this space.
    graph = {}
    #############  Add your Code here   ###############
    dim = img.shape
    for row in range(0, dim[0] / 20):
        for col in range(0, dim[1] / 20):
            graph[(row, col)] = findNeighbours(img, row, col)
    
    # Printing sorted graph. Uncomment when needed
    """for key in sorted(graph):
        print "%s: %s" % (key, graph[key])"""
    ###################################################
    return graph

##  Finds shortest path between two coordinates in the maze. Returns a set of coordinates from initial point
##  to final point.
def findPath(img, graph, init, final): ## You can pass your own arguments in this space.
    #############  Add your Code here   ###############
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
    shortest_path = all_paths[0]
    ###################################################
    return shortest_path


## The findMarkers() function returns a list of coloured markers in form of a python dictionaries
## For example if a blue marker is present at (3,6) and red marker is present at (1,5) then the
## dictionary is returned as :-
##          list_of_markers = { 'Blue':(3,6), 'Red':(1,5)}

def findMarkers(img):    ## You can pass your own arguments in this space.
    list_of_markers = {}
    #############  Add your Code here   ###############
    # Red Section #
    red_low_bound0 = np.array([170, 100, 100])
    red_up_bound0 = np.array([180, 255, 255])
    red_low_bound1 = np.array([0, 100, 100])
    red_up_bound1 = np.array([10, 255, 255])

    red_mask1 = cv2.inRange(img, red_low_bound0, red_up_bound0)
    red_mask2 = cv2.inRange(img, red_low_bound1, red_up_bound1)
    red_mask = red_mask1 | red_mask2
    dim = red_mask.shape
    for rows in range(0, dim[0] / 20):
        for cols in range(0, dim[1] / 20):
            if red_mask[(rows * 20) + 10, (cols * 20) + 10] > 127:
                list_of_markers['Red'] = (rows, cols)
    
    # Green Section #
    green_low_bound = np.array([50, 100, 100])
    green_up_bound = np.array([70, 255, 255])
    
    green_mask = cv2.inRange(img, green_low_bound, green_up_bound, )
    dim = green_mask.shape
    for rows in range(0, dim[0] / 20):
        for cols in range(0, dim[1] / 20):
            if green_mask[(rows * 20) + 10, (cols * 20) + 10] > 127:
                list_of_markers['Green'] = (rows, cols)

    # Blue Section #
    blue_low_bound = np.array([110, 100, 100])
    blue_up_bound = np.array([130, 255, 255])
    
    blue_mask = cv2.inRange(img, blue_low_bound, blue_up_bound)
    dim = blue_mask.shape
    for rows in range(0, dim[0] / 20):
        for cols in range(0, dim[1] / 20):
            if blue_mask[(rows * 20) + 10, (cols * 20) + 10] > 127:
                list_of_markers['Blue'] = (rows, cols)

    # Pink Section #
    pink_low_bound = np.array([140, 100, 100])
    pink_up_bound = np.array([160, 255, 255])
    pink_mask = cv2.inRange(img, pink_low_bound, pink_up_bound)
    dim = pink_mask.shape
    for rows in range(0, dim[0] / 20):
        for cols in range(0, dim[1] / 20):
            if pink_mask[(rows * 20) + 10, (cols * 20) + 10] > 127:
                list_of_markers['Pink'] = (rows, cols)

    #Printing list_of_markers. Uncomment when needed
    """for key in sorted(list_of_markers):
        print "%s: %s" % (key, list_of_markers[key])"""
    ###################################################
    return list_of_markers

## The findOptimumPath() function returns a python list which consists of all paths that need to be traversed
## in order to start from the bottom left corner of the maze, collect all the markers by traversing to them and
## then traverse to the top right corner of the maze.

def findOptimumPath(img, init, final, list_of_markers = {}):     ## You can pass your own arguments in this space.
    path_array = []
    #############  Add your Code here   ###############
    # Add all marker co-ordinates to markers list irrespective of colour
    markers = [i for i in list_of_markers.values()]
            
    # Find marker with shortest length from last point reached
    graph = buildGraph(img)
    
    cur_starting_point = (init)
    while (markers):
        shortest_path = [i for i in graph.values()]
        for node in markers:
            temp_path = findPath(img, graph, cur_starting_point, node)
            if len(temp_path) < len(shortest_path):
                shortest_path = temp_path
                #print shortest_path
        cur_starting_point = shortest_path[-1]
        path_array.append(shortest_path)
        markers.remove(shortest_path[-1])
    
    path_array.append(findPath(img, graph, cur_starting_point, final))
    ###################################################
    return path_array
        
## The colourPath() function highlights the whole path that needs to be traversed in the maze image and
## returns the final image.

def colourPath( img, path_array = [] ):      ## You can pass your own arguments in this space. 
    #############  Add your Code here   ###############
    for node in path_array:
        for subnode in node:
            colourCell(img, subnode[0], subnode[1], 150)
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
    listOfMarkers = findMarkers( imgHSV )              ## Acquire the list of markers with their coordinates. 
    test = str(listOfMarkers)
    imgBinary = readImageBinary(filePath)          ## Acquire the binary equivalent of image.
    initial_point = ((len(imgBinary)/20)-1,0)      ## Bottom Left Corner Cell
    final_point = (0, (len(imgBinary[0])/20) - 1)  ## Top Right Corner Cell
    pathArray = findOptimumPath(imgBinary, initial_point, final_point, listOfMarkers) ## Acquire the list of paths for optimum traversal.
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


