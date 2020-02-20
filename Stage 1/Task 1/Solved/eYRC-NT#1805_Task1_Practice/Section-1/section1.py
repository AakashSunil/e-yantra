import numpy as np
import cv2

## The readImage function takes a file path as argument and returns image in binary form.
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
def colourCell(img,row,column,colourVal):
    #############  Add your Code here   ###############
    r = row * 20
    c = column * 20
    for rcount in range(r, r+20):
        for ccount in range(c, c+20):
            if img[rcount, ccount] < 127:
                continue
            img[rcount, ccount] = colourVal
    ###################################################
    return img

##  Main function takes the filepath of image as input.
##  You are not allowed to change any code in this function.
def main(filePath):
    img = readImage(filePath)
    coords = [(0,0),(9,9),(3,2),(4,7),(8,6)]
    string = ""
    for coordinate in coords:
        img = colourCell(img, coordinate[0], coordinate[1], 150)
        neighbours = findNeighbours(img, coordinate[0], coordinate[1])
        print neighbours
        string = string + str(neighbours) + "\n"
        for k in neighbours:
            img = colourCell(img, k[0], k[1], 230)
    if __name__ == '__main__':
        return img
    else:
        return string + "\t"
## Specify filepath of image here. The main function is called in this section.
if __name__ == '__main__':
    filePath = 'maze00.jpg'
    img = main(filePath)
    cv2.imshow('canvas', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
