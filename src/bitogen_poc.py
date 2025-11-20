import random
import math
from collections import Counter

class BitogenSystem:
    def __init__(self):
        """
        Initializes the fixed 'Genetic Map' of Bitogens.
        In a real scenario, this map would be trained on massive datasets (like LLM tokenizers).
        """
        self.base_map = {
            # High-level semantic Bitogens (Words/Patterns)
            "THE": 1001, "AND": 1002, "TION": 1003,
            "BITOGEN": 1004, "DATA": 1005, "ENCRYPTION": 1006,
            "SEMANTIC": 1007, "COMPRESSION": 1008, " ": 2000,
            "101010": 3001, "000000": 3002 # Binary patterns
        }
        # Fallback: ASCII/Byte level mapping
        self.vocab_size = 100000
        for i in range(256):
            char = chr(i)
            if char not in self.base_map:
                self.base_map[char] = i
        
        self.id_to_pattern = {v: k for k, v in self.base_map.items()}
        self.all_valid_ids = list(self.base_map.values())

    def tokenize(self, text):
        """
        Converts raw data into Bitogen IDs using 'Greedy Longest Match'.
        """
        tokens = []
        i = 0
        n = len(text)
        while i < n:
            match_found = False
            # Search for longest pattern first (simulated up to 12 chars)
            for length in range(12, 0, -1):
                if i + length <= n:
                    chunk = text[i:i+length]
                    # Case-insensitive check for demo purposes
                    keys = [chunk, chunk.upper()]
                    for k in keys:
                        if k in self.base_map:
                            tokens.append(self.base_map[k])
                            i += length
                            match_found = True
                            break
                    if match_found: break
            if not match_found:
                # Fallback to single char
                tokens.append(self.base_map.get(text[i], ord(text[i])))
                i += 1
        return tokens

    def calculate_entropy(self, tokens):
        if not tokens: return 0
        counts = Counter(tokens)
        total = len(tokens)
        entropy = 0
        for count in counts.values():
            p = count / total
            entropy -= p * math.log2(p)
        return entropy * total

    def encrypt_sequence(self, tokens, password):
        """
        Permutes the Bitogen Map based on the password (Dynamic S-Box).
        """
        # Seed random for deterministic shuffle (simulating a KDF)
        random.seed(password)
        
        # Create permutation map
        targets = self.all_valid_ids.copy()
        random.shuffle(targets)
        
        perm_map = {}
        # Add salt/offset to values
        offset = random.randint(10000, 900000)
        
        for original, scrambled in zip(self.all_valid_ids, targets):
            perm_map[original] = scrambled + offset
            
        encrypted = [perm_map.get(t, t) for t in tokens]
        return encrypted

# --- DEMONSTRATION ---

def main():
    system = BitogenSystem()
    
    input_text = "The Bitogen data encryption uses semantic compression and Bitogen mapping."
    print(f"Original Text: '{input_text}'")
    print(f"Raw Size: {len(input_text) * 8} bits\n")

    # 1. Tokenization
    tokens = system.tokenize(input_text)
    print(f"[1] Tokenized Sequence (Bitogens): {tokens}")
    print(f"    Token Count: {len(tokens)} (Reduced from {len(input_text)} chars)")
    
    # 2. Entropy Analysis
    entropy_bits = system.calculate_entropy(tokens)
    print(f"    Theoretical Entropy Size: {entropy_bits:.2f} bits")
    print(f"    Estimated Compression: {100 - (entropy_bits/(len(input_text)*8))*100:.1f}%\n")

    # 3. Encryption
    password = "StrongPassword2025"
    encrypted = system.encrypt_sequence(tokens, password)
    print(f"[2] Encrypted Sequence (Permuted Map): {encrypted}")
    
    # 4. Different Key Test
    encrypted_wrong = system.encrypt_sequence(tokens, "WrongKey")
    print(f"[3] Encrypted Sequence (Wrong Key):    {encrypted_wrong}")
    print("    Note: The numerical values are completely disjoint.")

if __name__ == "__main__":
    main()
