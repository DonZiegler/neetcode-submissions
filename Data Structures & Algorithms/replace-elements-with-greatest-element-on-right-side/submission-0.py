class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max=-1
        length=len(arr)
        ans =[0]*length
        for i in range(length-1,-1,-1):
            ans[i]=max
            if arr[i]>max:   
                max=arr[i]

        return ans