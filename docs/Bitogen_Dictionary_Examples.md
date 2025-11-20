# Bitogen Dictionary Examples (Draft)

## 1. Simple Toy Dictionary

```text
ID   Pattern (bits)   Comment
-----------------------------------------------
0    0                Single 0
1    1                Single 1
2    01               Common transition
3    10               Common transition
4    001              Example multi‑bit pattern
5    111              Example multi‑bit pattern
```

## 2. Text‑Oriented Example (ASCII Fragments)

Longer bitogens might correspond to frequent byte sequences.

```text
ID   Pattern (hex)   Meaning
-----------------------------------------------
10   20              ' ' (space)
11   0A              newline
12   2C              ','
13   2E              '.'
14   2020            double space
15   0D0A            CRLF
16   7468            'th'
17   6865            'he'
18   20 74           ' t'
```

In practice, dictionaries could be:

- hand‑crafted for specific domains, or
- learned automatically (e.g. via BPE‑like algorithms over bitstrings).

