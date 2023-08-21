class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle= []

        for i in range(rowIndex+1):
            row = []
            for  j in range(i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    value = triangle[i-1][j-1] + triangle[i-1][j]
                    row.append(value)
            triangle.append(row)
        return row
