# Following code is of Linear Searching technique
# It is the direct searching algorithm checks for elements one-by-one

"""
Time complexity ---
Best ==> O(1)
Average/Worst ==> O(n)

Space complexity ---
O(1)

Average Comparisons ---
(N+1)/2
"""

def LinearSearch(arr, sl):
    for i in range(len(arr)):
        if arr[i] == sl:
            return i
    return -1

if __name__ == "__main__":
    arr = list(map(int,input("Enter the array elements: ").strip().split()))
    num = int(input("Enter a number to be searched in the array: "))

    result = LinearSearch(arr, num)

    if result == -1:
        print("Element not found!")
    else:
        print("Element found @",result+1,"position!")
