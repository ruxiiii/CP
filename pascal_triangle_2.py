class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        value=0
        for i in range(numRows):
            row=[]
            for j in range(i+1):
                if j==0 or j ==i:
                    row.append(1)
                else:
                    value = triangle[i-1][j-1] + triangle[i-1][j]
                    row.append(value)

            triangle.append(row)
        return triangle
