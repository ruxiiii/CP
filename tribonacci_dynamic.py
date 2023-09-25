class Solution:
    def Trib(self, n):

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        tribonacci = [0] * n
        tribonacci[0] = 0
        tribonacci[1] = 1
        tribonacci[2] = 1

        for i in range(3, n):
            tribonacci[i] = tribonacci[i-1] + tribonacci[i-2] + tribonacci[i-3]
        return tribonacci
    

sol =  Solution()
sol.Trib(5)
print(sol)
