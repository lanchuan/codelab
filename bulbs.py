class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        a=0
        l=len(A)
        if l==0:
            return 0
        if l==1 and A[0]==0:
            return 1
        for i in range(l-1):
            if A[l-i-1]==1 and A[l-i-2]==0:
                a+=1
            elif A[l-i-1]==0 and A[l-i-2]==1:
                a+=1
        if A[0]==0:
                a+=1
        return a

