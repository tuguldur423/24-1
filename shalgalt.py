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

    # Кодын үүсгэх
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

# Жишээ өгөгдөл
frequencies = {
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45
}

# Хаффман кодыг олох
huffman_codes = huffman_code(frequencies)

# Кодыг хэвлэх
print("Хаффман код:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")