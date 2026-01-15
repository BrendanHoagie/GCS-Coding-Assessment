"""
My implementation of sort_and_find_median

I opted to implement quicksort as my sorting algorithm because of it's speed and ease of implementation.
Quicksort runs in O(n log n) with a space complexity of O(log n) stack frames with my recursive implementation.

Some considerations:
- Given more time, I would have used a testing library like pytest to write thorough test cases for this code.
- If I knew this code would be used on exclusively very long lists of fixed size integers or fixed size floats,
  I might have thought to implement radix sort, which performs better than quicksort under those conditions.
  However, my soulution is very generalizable and done under a time crunch, so I am very happy with this 
"""

def sort_and_find_median(numbers: list[float]) -> float:
    """
    Finds the median of a list of numbers by sorting via quicksort
    
    Args:
        numbers - a list of floats to find the median of
        
    Returns:
        a float represneting the median value of the range
        
    Raises:
        ValueError if the input array has no items in it
    """
    n = len(numbers)
    if n == 0:
        raise ValueError("Error: Cannot find the median of an empty list")
    brendan_quicksort(numbers, 0, len(numbers) - 1)
    if n % 2 == 0:
        return (numbers[(n // 2) - 1] + numbers[n // 2]) / 2
    else:
        return numbers[(n // 2)]
    
def brendan_partition(arr: list[float], low: float, high: float) -> int:
    """
    Helper for brendan_quicksort, partitions a subarray around a pivot element, modifying array in place
    
    Args:
        arr - a list of floats being sorted in place
        low - the starting index of the subarray
        high - the ending index of the subarray
        
    Returns:
        The final index position of the pivot after partitioning
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def brendan_quicksort(arr: list[float], low: float, high: float) -> None:
    """
    Implementation of quicksort done in place
    
    Args:
        arr - a list of floats to be sorted
        low - the starting index of the subarray to sort
        high - the ending index of the subarray to sort
        
    Returns:
        None. Modifies input arr in place
    """
    if low < high:
        part = brendan_partition(arr, low, high)
        brendan_quicksort(arr, low, part - 1)
        brendan_quicksort(arr, part + 1, high)
        
if __name__ == "__main__":
    nums = []
    while True:
        input_as_str = input("Enter a number. Enter 'done' to run the test: ")
        try:
            choice = float(input_as_str)
            nums.append(choice)
            print(f"Nums: {nums}")
        except ValueError as e:
            if input_as_str == "done":
                try:
                    median = sort_and_find_median(nums)
                    print(f"The median value is {median}\n")
                    break
                except ValueError as e:
                    print(e)
                    break             
            else:
                print(f"'{input_as_str}' is not a number, please try again")
