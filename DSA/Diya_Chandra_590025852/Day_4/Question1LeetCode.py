class Solution(object):
    def transpose(self,matrix):
        transpose=[]
        for i in range(len(matrix[0])):
            row=[]
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            transpose.append(row)
        return transpose
