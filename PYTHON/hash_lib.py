# SHA-256 algorithm for hashing
import hashlib
content = "Codebase"
hash = hashlib.sha256()
hash.update(content.encode('utf-8'))
print(hash.hexdigest()) # prints a 64 characters hash
