# Following code is Binary Searching algorithm
# It uses Divide & Conquer technique to carry out algorithms
"""
Time Complexity ---
Best ==> O(1)
Average/Worst ==> O(log n)

Space Complexity ---
O(1)
"""
def BinarySearch(arr, low, high, sl):
    if high >= low:
        mid = (high+low) // 2
        if arr[mid] == sl:
            return mid
        elif arr[mid] > sl:
            return BinarySearch(arr, low, mid-1, sl)
        else:
            return BinarySearch(arr, mid+1, high, sl)

    else:
        return -1

if __name__ == "__main__":
    array = list(map(int, input("Enter the array elements: ").strip().split()))
    num = int(input("Enter the element to be searched: "))

    result = BinarySearch(array, 0, len(array)-1, num)

    if result == -1:
        print("No match found!")
    else:
        print("Match found @ position -",result+1)
