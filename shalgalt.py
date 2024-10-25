class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_code(frequencies):

    heap = []
    
    for char, freq in frequencies.items():
        heap.heappush(heap, Node(char, freq))

    while len(heap) > 1:
        left = heap.heappop(heap)
        right = heap.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heap.heappush(heap, merged)

    root = heap[0]
    huffman_codes = {}
    
    def generate_codes(node, current_code=""):
        if node is not None:
            if node.char is not None:
                huffman_codes[node.char] = current_code
            generate_codes(node.left, current_code + "0")
            generate_codes(node.right, current_code + "1")

    generate_codes(root)

    return huffman_codes

frequencies = {
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45
}

huffman_codes = huffman_code(frequencies)

# Кодыг хэвлэх
print("Хаффман код:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = [64,34,25,12,22,11,90]
bubble_sort(arr)
print("Sorted array:", arr)



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr = [64,34,25,12,22,11,90]
insertion_sort(arr)
print("Sort", arr)

# 1=b
# 2=b
# 3=c
# 4=a
# 5=c
# 6=a
# 7=c
# 7-1=c
# 8=c
# 9=a
# 10=d
# 11=b
# 12=b
# 13=
# 14=
# 15=c
# 16=a
# 17=b
# 18=c
# asuult2=b
# algoritminguitsetgel=b
# punkts butsaah=b

# Кодыг хэвлэх
print("Хаффман код:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")
