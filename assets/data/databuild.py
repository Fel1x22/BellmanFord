from bellmanFord import bellmanFord
from matrixCreator import create_matrix

fileName = "output.txt"
fileObj = open(fileName,'w')

for i in range(10, 510, 10):
    for j in range(5):
      matrix = create_matrix(i, mode="no_negatives_complete") 
      fileObj.write(f'{bellmanFord(matrix, i)[1]:.20f}' + "\n")