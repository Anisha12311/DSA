from CircularLL import CircularLL

def main():
    # Create a new circular linked list
    circular = CircularLL()
    
    # Insert 3 elements in different ways
    
    # Method 1: Using append to add at the end
    circular.append(10)
    print("After inserting first element (10):")
    circular.traverse()
    
    # Method 2: Using insertAtBegin to add at the beginning
    circular.insertAtBegin(20)
    print("\nAfter inserting second element (20) at beginning:")
    circular.traverse()
    
    # Method 3: Using append to add another element at the end
    circular.append(30)
    print("\nAfter inserting third element (30):")
    circular.traverse()
    
    print("\nFinal circular linked list with 3 elements:")
    circular.traverse()

if __name__ == "__main__":
    main() 