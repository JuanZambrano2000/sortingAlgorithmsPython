class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        for i in range(n):
            for j in range(0, n-1-i):
                if arr[j] > arr[j+1]:
                    aux = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = aux                   
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends