# Bitogen

**Bitogen** is a conceptual framework and experimental toolkit for adding a *symbolic layer* on top of raw binary data.

Instead of working directly on bits or bytes, Bitogen introduces **bitogens**:
stable symbolic tokens that map to predefined bit patterns. This enables:

- more structured **compression** (symbolic modeling + entropy coding),
- **cryptographic preprocessing** (keyed permutations on symbolic sequences),
- AI‑friendly **tokenization of arbitrary binary data**,
- a unified view on data representation, compression and security.

> This repository is intended as a *research starting point* for cryptographers, compression researchers and systems engineers.

---

## Highlights

- **Bitogen dictionary** – global, fixed map from bitogen IDs to bit patterns.  
- **Bitogenization** – longest‑match tokenization of raw bitstreams into bitogens.  
- **Compression layer** – bitogen sequences + ANS / arithmetic coding.  
- **Hybrid cipher** – bitogen preprocessing + key‑dependent permutation + AEAD (AES‑GCM / ChaCha20‑Poly1305).  
- **Research‑oriented design** – meant to be analyzed, broken, extended and improved.

---

## Documentation

Core concept overview (recommended starting point):

- `docs/Bitogen_Overview_Documentation.md`

More detailed / scientific materials:

- `docs/bitogen_whitepaper_scientific.pdf` – research‑style whitepaper (EN)
- `docs/bitogen_concept_en.pdf` – concise concept PDF (EN)
- `docs/bitogen_koncepcja_pl.pdf` – Polish conceptual overview
- `docs/bitogen_conversation_fragment.pdf` – selected conversation fragment that seeded the idea

Technical notes:

- `docs/Bitogen_Cipher_Spec.md` – hybrid cipher specification
- `docs/Bitogen_Compression_Notes.md` – compression‑focused notes
- `docs/Bitogen_Dictionary_Examples.md` – example bitogen maps

Roadmap:

- `roadmap/ROADMAP.md`

Logo / visual identity (simple SVG):

- `logo/bitogen_logo.svg`

---

## Status

> **Early‑stage research idea. Not production‑ready.**  
> Use for experiments, academic work, or conceptual exploration.

There are *no* security guarantees beyond those of the underlying AEAD primitives.  
Any cryptographic usage should be treated as experimental only.

---

## License

Recommended for the repository: **MIT License**  
(so that researchers and engineers can freely use and extend the ideas.)

