import numpy as np
import cv2

## The readImage function takes a file path as argument and returns image in binary form.
## You can copy the code you wrote for section1.py here.
def readImage(filePath):
    #############  Add your Code here   ###############
    img = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
    ret, binaryImage = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ###################################################
    return binaryImage

## The findNeighbours function takes a maze image and row and column coordinates of a cell as input arguments
## and returns a stack consisting of all the neighbours of the cell as output.
## Note :- Neighbour refers to all the adjacent cells one can traverse to from that cell provided only horizontal
## and vertical traversal is allowed.
## You can copy the code you wrote for section1.py here.
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

##  colourCell function takes 4 arguments:-
##            img - input image
##            row - row coordinates of cell to be coloured
##            column - column coordinates of cell to be coloured
##            colourVal - the intensity of the colour.
##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the black walls and only paints the empty spaces. This function returns the image
##  with the painted cell.
##  You can copy the code you wrote for section1.py here.
def colourCell(img,row,column,colourVal):
    #############  Add your Code here   ###############
    r = row * 20
    c = column * 20
    for rcount in range(r, r + 20):
        for ccount in range(c, c + 20):
            if img[rcount, ccount] < 127:
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
def findPath(init, final, graph): ## You can pass your own arguments in this space.
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
    
    ###################################################
    return all_paths[0]

## This is the mainfunction where all other functions are called. It accepts filepath
## of an image as input. You are not allowed to change any code in this function.
def main(filePath, flag = 0):                 
    img = readImage(filePath)      ## Read image with specified filepath.
    breadth = len(img)/20          ## Breadthwise number of cells
    length = len(img[0])/20           ## Lengthwise number of cells
    if length == 10:
        initial_point = (0,0)      ## Start coordinates for maze solution
        final_point = (9,9)        ## End coordinates for maze solution    
    else:
        initial_point = (0,0)
        final_point = (19,19)
    graph = buildGraph(img)       ## Build graph from maze image. Pass arguments as required.
    shortestPath = findPath(initial_point, final_point, graph)  ## Find shortest path. Pass arguments as required.
    print shortestPath             ## Print shortest path to verify
    string = str(shortestPath) + "\n"
    for i in shortestPath:         ## Loop to paint the solution path.
        img = colourCell(img, i[0], i[1], 200)
    if __name__ == '__main__':     ## Return value for main() function.
        return img
    else:
        if flag == 0:
            return string
        else:
            return graph

## The main() function is called here. Specify the filepath of image in the space given.            
if __name__ == '__main__':
    filePath = 'maze00.jpg'        ## File path for test image
    img = main(filePath)           ## Main function call
    cv2.imshow('canvas', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


