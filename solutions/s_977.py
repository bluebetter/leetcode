class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n, j = len(A), 0
        while j < n and A[j] < 0:
            j += 1
        i = j - 1
        ret = []
        while i >= 0 and j < n:
            a = A[i] * A[i]
            b = A[j] * A[j]
            if a < b:
                ret.append(a)
                i -= 1
            else:
                ret.append(b)
                j += 1
        while i >= 0:
            ret.append(A[i] * A[i])
            i -= 1
        while j < n:
            ret.append(A[j] * A[j])
            j += 1
        return ret
