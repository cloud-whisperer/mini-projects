import hashlib

def hash_entry(entry):
    return hashlib.sha256(entry.encode()).hexdigest()

#print("🔐 hash_entry exists:", callable(hash_entry))
