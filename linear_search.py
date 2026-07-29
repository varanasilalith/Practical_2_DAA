def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1  
def main():
    try:
        size = int(input("Enter the size of the array: "))
        
        if size <= 0:
            print("Array size must be a positive integer.")
            return
        elements = []
        print(f"Enter {size} elements one by one:")
        for _ in range(size):
            item = int(input(" "))
            elements.append(item)
        elements.sort()
        print(f"\nSorted Array: {elements}")

        target = int(input("\nEnter the element you want to search for: "))
        index = linear_search(elements, target)

        if index != -1:
            print(f"Element {target} found at index {index} in the sorted array.")
        else:
            print(f"Element {target} was not found in the array.")
    except ValueError:
        print("Invalid input. Please enter integers only.")
if __name__ == "__main__":
    main()
