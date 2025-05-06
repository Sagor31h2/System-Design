import hashlib
import bisect

class ConsistentHashing:
    def __init__(self, servers, replicas=3):
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []
        self.servers = set()
        for server in servers:
            self.add_server(server)

    def hash(self, key):
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16) % (2**32)
    
    def add_server(self, server):
        """Add a server to the hash ring."""
        print(f"Adding server: {server}")
        self.servers.add(server)
        for i in range(self.replicas):
            key = self.hash(f"{server}-{i}")
            self.ring[key] = server
            bisect.insort(self.sorted_keys, key)
    
    def remove_server(self, server):
        """Remove a server from the hash ring."""
        if server in self.servers:
            print(f"Removing server: {server}")
            self.servers.remove(server)
            for i in range(self.replicas):
                key = self.hash(f"{server}-{i}")
                self.ring.pop(key, None)
                self.sorted_keys.remove(key)
    
    def get_server(self, key):
        """Get the server for a given key."""
        if not self.ring:
            return None
        key_hash = self.hash(key)
        idx = bisect.bisect(self.sorted_keys, key_hash) % len(self.sorted_keys)
        return self.ring[self.sorted_keys[idx]]


# Example usage and testing
servers = ["server1", "server2", "server3"]
ch = ConsistentHashing(servers)

# Test keys
keys = ["user1", "user2", "user3", "fileA", "fileB"]
print("\nInitial server mappings:")
for key in keys:
    print(f"{key} -> {ch.get_server(key)}")

# Add a new server
ch.add_server("server4")
print("\nAfter adding server4:")
for key in keys:
    print(f"{key} -> {ch.get_server(key)}")

# Remove a server
ch.remove_server("server2")
print("\nAfter removing server2:")
for key in keys:
    print(f"{key} -> {ch.get_server(key)}")
