class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return

        # If the value to be added is less than or equal to the head
        if self.head.value >= value:
            if self.head.value == value:
                return  # Avoid duplicates
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        # Navigate to the correct insert position
        while current.next and current.next.value < value:
            current = current.next

        # Prevent duplicate in the middle
        if current.next and current.next.value == value:
            return

        # Inserting at the end or in the middle
        new_node.next = current.next
        current.next = new_node


def process_file(input_file_path, output_file_path):
    sorted_list = SortedLinkedList()
    
    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            try:
                num = int(line)
                sorted_list.insert(num)
            except ValueError:
                continue  # Skip non-integer lines

    with open(output_file_path, 'w') as file:
        current = sorted_list.head
        while current:
            file.write(f"{current.value}\n")
            current = current.next


# Path of input and output files
input_file_path = "./input/sample_01.txt"
output_file_path = "./output.txt"
process_file(input_file_path, output_file_path)
