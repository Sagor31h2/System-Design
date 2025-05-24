#source https://blog.algomaster.io/p/bloom-filters
import hashlib

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def build_hashes(self, item):
        hashes = []
        for i in range(self.hash_count):
            hash_input = (item + str(i)).encode('utf-8')
            hash_digest = hashlib.sha256(hash_input).hexdigest()
            hash_value = int(hash_digest, 16) % self.size
            hashes.append(hash_value)
        return hashes

    def add(self, item):
        for hash_value in self.build_hashes(item):
            self.bit_array[hash_value] = 1

    def check(self, item):
        return all(self.bit_array[hash_value] == 1 for hash_value in self.build_hashes(item))  

# Usage
bloom_fill = BloomFilter(1000, 5)

bloom_fill.add("sagor")
bloom_fill.add("tusher")

print(bloom_fill.check("sagor"))   # True
print(bloom_fill.check("tusher"))  # True
print(bloom_fill.check("sohal"))   # False (probably)
