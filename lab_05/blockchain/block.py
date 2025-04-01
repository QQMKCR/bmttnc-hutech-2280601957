import hashlib

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, proof):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Convert all attributes to strings before concatenation
        block_string = (str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.transactions) + str(self.proof))
        return hashlib.sha256(block_string.encode()).hexdigest()