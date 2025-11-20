# Bitogen Compression Notes (Draft)

## 1. Overview

This document collects notes on using bitogens as a **pre‑processing layer for compression**.

The core idea:
- represent recurring bit‑level structures as bitogens (tokens),
- then apply standard entropy coding (ANS / arithmetic) to the token sequence.

## 2. Pipeline

1. Raw data → bitstream.
2. Bitogenization (Tokenize) → sequence of bitogen IDs.
3. Statistical modeling / AI model over bitogen IDs.
4. Entropy coder (ANS / arithmetic) over predicted distributions.
5. Output compressed bitstream.

Decoding is the reverse process.

## 3. Expected Benefits

- Better exploitation of higher‑order patterns than byte‑level models.
- Improved predictability for AI‑based models.
- Opportunity to share one global bitogen dictionary across many files.

## 4. Experimental Directions

- Compare against zstd, brotli, CMIX, and neural compressors.
- Evaluate on different domains:
  - executable files,
  - protocol traces,
  - logs,
  - scientific binary formats.

