# Bitogen Hybrid Cipher Specification (Draft)

## 1. Scope

This document specifies a **hybrid encryption construction** that uses bitogens
as a *preprocessing layer* before a classical AEAD cipher (AES‑GCM, ChaCha20‑Poly1305, etc.).

The bitogen layer is **not** intended as a standalone cryptographic primitive.  
Security relies on the underlying AEAD. The bitogen layer provides structural obfuscation.

## 2. Preliminaries

- Global bitogen dictionary `D` (public, fixed):  
  `D[i] -> bit-pattern_i`, where each `bit-pattern_i` is a finite bitstring.

- Bitogenization function `Tokenize(bits)`:
  parses a raw bitstring into a sequence of indices `[i1, i2, ..., in]`
  using a longest‑match rule (or a prefix‑free code).

- Inverse `Detokenize([i1, ..., in])`:
  returns the concatenation of `bit-pattern_i`.

## 3. Keys and Subkeys

Given a master symmetric key `K` (e.g. 256 bits), derive:

- `K_perm` – for generating a permutation of bitogen IDs
- `K_stream` – for stream‑like operations on bitogen indices
- `K_aead` – for the classical AEAD cipher

Key derivation can use HKDF:

```text
K_perm   = HKDF(K, "bitogen-permutation")
K_stream = HKDF(K, "bitogen-stream")
K_aead   = HKDF(K, "bitogen-aead")
```

## 4. Encryption Algorithm (High‑Level)

Input:
- `K` : master key
- `P_bits` : plaintext as bitstring
- `AD` : associated data (optional, not encrypted)

Output:
- `nonce || C_final || Tag`

Steps:

1. **Bitogenization**  
   `T = Tokenize(P_bits)`  
   where `T = [i1, i2, ..., in]` are bitogen IDs.

2. **Key Derivation**  
   Compute `(K_perm, K_stream, K_aead)` from `K` as above.

3. **Bitogen Permutation**  
   From `K_perm`, generate a pseudorandom permutation `π` over all bitogen IDs.  
   For each `ik` in `T`, compute:
   `jk = π(ik)`

4. **Stream‑like Mixing (Optional)**  
   Using `K_stream`, generate a pseudo‑random sequence `S_k` over bitogen IDs.  
   For each `jk`, compute e.g.:
   `ck = (jk XOR S_k) mod M`
   where `M` is the bitogen alphabet size.

   This yields the sequence `C_seq = [c1, c2, ..., cn]`.

5. **Packing**  
   Serialize `C_seq` to bytes: `C_bytes`  
   (e.g. fixed‑width encoding for indices).

6. **AEAD Encryption**  
   - Generate a random `nonce`.
   - Compute: `C_final, Tag = AEAD_Encrypt(K_aead, nonce, C_bytes, AD)`

7. **Output**  
   Return `nonce || C_final || Tag`.

## 5. Decryption Algorithm (High‑Level)

Input:
- `K`
- `nonce || C_final || Tag`
- `AD`

Output:
- `P_bits` or error (if authentication fails)

Steps:

1. **Key Derivation**  
   Derive `(K_perm, K_stream, K_aead)` as in encryption.

2. **AEAD Decryption**  
   `C_bytes = AEAD_Decrypt(K_aead, nonce, C_final, Tag, AD)`  
   If authentication fails → abort.

3. **Unpacking**  
   Deserialize `C_bytes` into `C_seq = [c1, ..., cn]`.

4. **Stream‑like Demixing**  
   Regenerate `S_k` from `K_stream`.  
   Recover:
   `jk = (ck XOR S_k) mod M`

5. **Inverse Permutation**  
   Regenerate `π` from `K_perm`, compute its inverse `π⁻¹`.  
   Recover original bitogen IDs:
   `ik = π⁻¹(jk)`

6. **Detokenization**  
   Compute `P_bits = Detokenize([i1, ..., in])`.

## 6. Security Notes

- This construction should be treated as **experimental**.  
- The security goal is at least that of the underlying AEAD.  
- The bitogen layer aims to:
  - obscure structural patterns,
  - introduce symbolic diffusion,
  - complicate traffic analysis.

Any formal security claims require rigorous cryptographic analysis.

