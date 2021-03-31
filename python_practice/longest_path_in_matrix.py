



def find_longest_path( mat, rows, cols):
    visited = [[0] * rows]* cols
    longestNode = []
    max_path = []
    longestNode.clear()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            # if(visited[i][j] == False):
                # visited[i][j] == True
            max_path = getNodes(i , j, rows, cols, mat, longestNode, visited)
            if(max_path < longestNode):
                 max_path = longestNode
        print(max_path)



def getNodes(i , j, rows, cols, mat,longestNode, visited):
    neighbours = findValidNeighbours(i , j, rows, cols)
    for neighbour in neighbours:
        if(mat[i][j] - mat[neighbour.rowIndex][neighbour.colIndex] == 1 | mat[i][j] - mat[neighbour.rowIndex][neighbour.colIndex] == -1):
            # if(visited[i][j] == False):
            #     visited[i][j] == True
            if(mat[i][j] not in longestNode):
                longestNode.append(mat[i][j])
                longestNode = getNodes( neighbour.rowIndex, neighbour.colIndex, rows, cols, mat, longestNode, visited)
    return  longestNode

class Neighbour:
    def __init__(self, rowIndex, colIndex ):
        self.rowIndex = rowIndex
        self.colIndex = colIndex


def findValidNeighbours(i , j, rows, cols):
    neighbours = []
    if((i + 1) < rows):
        neighbours.append(Neighbour(i + 1, j))
    if ((i - 1) >= 0):
        neighbours.append(Neighbour(i - 1, j))
    if  ((j + 1) < cols):
        neighbours.append(Neighbour(i, j + 1))
    if ((j - 1) >= 0):
        neighbours.append(Neighbour(i, j - 1))
    return neighbours


if __name__ == '__main__':
    mat = [[1, 2, 9],
           [5, 3, 8],
           [4, 6, 7]]
    find_longest_path(mat, len(mat) , len(mat[0]))