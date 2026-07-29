def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
       
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
    return -1

def main():
    try:
        
        size = int(input("Enter the size of the array: "))
        if size <= 0:
            print("Array size must be greater than 0.")
            return

    
        print(f"Enter {size} elements one by one:")
        arr = []
        for i in range(size):
            element = int(input(f"Element {i+1}: "))
            arr.append(element)

        print(f"\nOriginal Array: {arr}")
        arr.sort()
        print(f"Sorted Array: {arr}")

        target = int(input("\nEnter the element you want to search for: "))

        result = binary_search(arr, target)

        if result != -1:
            print(f" Element {target} found at index {result} in the sorted array.")
        else:
            print(f"Element {target} is not present in the array.")

    except ValueError:
        print("Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()
