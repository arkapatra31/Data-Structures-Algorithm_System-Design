# Python Dictionaries & Hash Collisions

A deep dive into how Python's most important data structure works under the hood — from hashing to probing to resizing.

---

## Table of Contents

1. [How Dictionaries Work Internally](#1-how-dictionaries-work-internally)
2. [What is a Hash Collision?](#2-what-is-a-hash-collision)
3. [Collision Resolution: Open Addressing & Probing](#3-collision-resolution-open-addressing--probing)
4. [The hash() Function and \_\_hash\_\_ / \_\_eq\_\_](#4-the-hash-function-and-__hash__--__eq__)
5. [Table Resizing & Load Factor](#5-table-resizing--load-factor)
6. [The Compact Dict (Python 3.6+)](#6-the-compact-dict-python-36)
7. [Practical Implications & Edge Cases](#7-practical-implications--edge-cases)
8. [Code Examples](#8-code-examples)

---

## 1. How Dictionaries Work Internally

A Python `dict` is a **hash table** — an array of slots (called "buckets") where key-value pairs are stored. When you write `d[key] = value`, Python performs three steps:

```
┌──────────┐      ┌───────────────┐      ┌──────────────┐      ┌───────┐
│  "apple"  │ ──▶ │ hash("apple") │ ──▶  │ hash % 8 = 3 │ ──▶  │ [ 3 ] │
│   (key)   │      │ (hash func)   │      │  (index calc) │      │(slot) │
└──────────┘      └───────────────┘      └──────────────┘      └───────┘
```

1. **Hash the key** — compute `hash(key)` to get an integer.
2. **Compute the index** — calculate `hash(key) % table_size` to find which slot to use.
3. **Store the pair** — place the key-value pair at (or near) that slot.

Looking up a key follows the same process: hash it, compute the index, then check that slot. This is why dict operations are O(1) on average — you jump directly to the right location instead of scanning.

### Visualizing the hash table

```
Index │ Key       │ Value
──────┼───────────┼──────
  0   │  (empty)  │  —
  1   │ "banana"  │  12
  2   │  (empty)  │  —
  3   │ "apple"   │  5     ◀── hash("apple") % 8 = 3
  4   │  (empty)  │  —
  5   │ "cherry"  │  7
  6   │  (empty)  │  —
  7   │  (empty)  │  —
```

---

## 2. What is a Hash Collision?

A **collision** occurs when two different keys produce the **same table index**. For example, if both `hash("apple") % 8` and `hash("mango") % 8` equal `3`, they both want slot 3 — but only one can go there directly.

> **Why collisions are inevitable:** There are infinitely many possible keys but only a finite number of table slots. By the *pigeonhole principle*, collisions must happen. The question is how to handle them efficiently.

---

## 3. Collision Resolution: Open Addressing & Probing

Python does **not** use chaining (linked lists at each slot), which is the textbook approach. Instead, it uses **open addressing** — when a collision occurs, Python searches for the next available slot using a deterministic **probing sequence**.

### The probing formula

```python
j = ((5 * j) + 1 + perturb) % table_size
perturb >>= 5   # shifts right by 5 bits each iteration
```

This formula has two components:

| Component | Purpose |
|-----------|---------|
| `5 * j + 1` | Linear congruential generator — visits every slot exactly once (mod 2ⁿ). Guarantees full table coverage. |
| `+ perturb` | Mixes in **higher-order bits** of the full hash value. Keys with the same low bits don't all follow the same probe sequence. |

### How probing works (visual)

```
Slot: │ 0 │ 1      │ 2 │ 3      │ 4 │ 5      │ 6 │ 7 │
      │   │ banana │   │ apple  │   │ cherry │   │   │
                         ▲
                         │
        "mango" hashes to index 3 ──▶ OCCUPIED!
                                      │
                         probe next ──▶ slot 4 is empty ✓
                                       "mango" stored here
```

Unlike simple linear probing (`j+1, j+2, j+3...`) which creates **clustering** (runs of occupied slots that slow future probes), Python's formula scatters probes across the table. The `perturb` variable decays to zero over iterations, at which point the formula becomes a pure linear congruential generator that guarantees visiting every slot.

---

## 4. The `hash()` Function and `__hash__` / `__eq__`

For an object to be used as a dictionary key, it must implement two methods:

| Method | Purpose | Rule |
|--------|---------|------|
| `__hash__()` | Returns an integer used to find the slot | If `a == b`, then `hash(a) == hash(b)` |
| `__eq__()` | Confirms identity during collision resolution | Must be consistent with `__hash__` |

### The hash/eq contract

- If `a == b` → `hash(a)` **must** equal `hash(b)`
- If `hash(a) == hash(b)` → `a` and `b` are **not** necessarily equal (that's a collision)
- Violating the first rule **silently corrupts** the dictionary

### Hashable vs unhashable types

| Hashable ✅ | Unhashable ❌ | Why |
|-------------|--------------|-----|
| `str`, `int`, `float` | `list` | Mutable — contents can change after hashing |
| `tuple` (of immutables) | `dict` | Mutable |
| `frozenset` | `set` | Mutable |
| Custom classes (by default) | — | Use `id()` as hash by default |

---

## 5. Table Resizing & Load Factor

Python monitors the **load factor** — the ratio of used slots (including tombstones) to total slots. When it exceeds roughly **2/3 (~66%)**, the table resizes.

```
BEFORE: 6/8 slots used (75%) — over threshold!
┌───┬───┬───┬───┬───┬───┬───┬───┐
│ ■ │ ■ │   │ ■ │ ■ │   │ ■ │ ■ │   (8 slots)
└───┴───┴───┴───┴───┴───┴───┴───┘
 Load: ████████████████░░░░ 75%
                       ▲ 2/3 threshold

          ──── resize ────▶

AFTER: 6/16 slots used (37.5%)
┌──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┐
│■ │  │  │■ │  │■ │  │  │  │■ │  │  │■ │  │  │■ │ (16 slots)
└──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┘
 Load: ████████░░░░░░░░░░░░ 37.5%
```

Key facts about resizing:

- **Table size is always a power of 2** — 8 → 16 → 32 → 64 → ...
- **Every key is rehashed** — `new_index = hash(key) % new_size`, so keys move to new positions.
- **O(n) cost per resize** — but resizes are infrequent, so inserts remain **amortized O(1)**.

---

## 6. The Compact Dict (Python 3.6+)

Since Python 3.6 (guaranteed in 3.7+), dictionaries use a **split design** with two arrays:

| Array | Contents | Density |
|-------|----------|---------|
| **Indices array** | Small integers (1–8 bytes each) pointing into entries | Sparse (has empty slots) |
| **Entries array** | Triples of `(hash, key, value)` in insertion order | Dense (no gaps) |

### Benefits

- **Insertion order preserved** — a structural consequence, not a separate mechanism
- **~20-25% less memory** — the sparse array uses tiny integers instead of full pointer triples
- **Better cache performance** — the dense entries array is iterated sequentially

---

## 7. Practical Implications & Edge Cases

### Hash randomization (security)

Since Python 3.3, string hashes are **randomized per process** via `PYTHONHASHSEED`. This defends against **hash-flooding attacks** where an attacker crafts keys that all collide, degrading dict operations from O(1) to O(n).

- Integer hashes are still deterministic: `hash(42) == 42` for small ints
- Set `PYTHONHASHSEED=0` to disable for debugging

### Deletion uses tombstones

When you `del d[key]`, Python marks the slot as a **"dummy" entry (tombstone)** rather than leaving it truly empty. A real empty slot would break the probe chain — subsequent lookups might terminate too early, making existing keys unfindable.

### Time complexity summary

| Operation | Average | Worst Case |
|-----------|---------|------------|
| `d[key]` (get) | O(1) | O(n) |
| `d[key] = val` (set) | O(1) | O(n) |
| `del d[key]` | O(1) | O(n) |
| Resize | — | O(n) |
| Iteration | O(n) | O(n) |

> The O(n) worst case is effectively impossible under normal conditions thanks to the probing formula, resize policy, and hash randomization.

### Hash flooding attacks

Before hash randomization, an attacker could send thousands of HTTP POST parameters (or JSON keys) specifically chosen to collide in Python's hash table. This turned each dict insertion into O(n) work, creating a denial-of-service with relatively small payloads. `PYTHONHASHSEED` makes this impractical because the hash function changes every time the process starts.

### ⚠️ Never violate the hash/eq contract

If you implement a custom `__hash__` that returns different values for equal objects, dict lookups **silently fail** — the key is stored at one slot, but lookups compute a different slot. No error is raised.

---

## 8. Code Examples

### Basic hash mechanics

```python
# Hash values for different types
print(hash('apple'))   # large integer, randomized per process
print(hash(42))        # 42 — small ints hash to themselves
print(hash(42.0))      # same as hash(42), because 42 == 42.0
print(hash((1, 2)))    # tuples are hashable

# These raise TypeError (mutable → unhashable):
# hash([1, 2])
# hash({'a': 1})
```

### Simulating Python's probe sequence

```python
def probe_sequence(key, table_size=8, steps=5):
    """Show where Python would look for a key."""
    h = hash(key)
    idx = h % table_size
    perturb = h

    print(f"Key: {key!r}, hash: {h}, initial slot: {idx}")
    for i in range(steps):
        print(f"  Probe {i}: slot {idx}")
        idx = ((5 * idx) + 1 + perturb) % table_size
        perturb >>= 5

probe_sequence("apple")
probe_sequence("mango")
```

### Correct vs broken `__hash__`/`__eq__`

```python
class GoodKey:
    """Correctly implements the hash/eq contract."""
    def __init__(self, val):
        self.val = val
    def __hash__(self):
        return hash(self.val)
    def __eq__(self, other):
        return isinstance(other, GoodKey) and self.val == other.val

class BadKey:
    """BROKEN: equal objects can have different hashes."""
    def __init__(self, val):
        self.val = val
    def __hash__(self):
        return id(self)  # different object → different hash!
    def __eq__(self, other):
        return isinstance(other, BadKey) and self.val == other.val

# Good key works:
d = {GoodKey("x"): 100}
print(d[GoodKey("x")])  # → 100

# Bad key fails silently:
d2 = {BadKey("x"): 100}
# d2[BadKey("x")]  → KeyError! Can't find it.
```

### Forcing collisions — performance impact

```python
import time

class CollidingKey:
    """Every instance hashes to 42 — maximum collisions."""
    def __init__(self, val):
        self.val = val
    def __hash__(self):
        return 42
    def __eq__(self, other):
        return isinstance(other, CollidingKey) and self.val == other.val

# Normal keys: O(1) per insert
t0 = time.perf_counter()
normal = {f"key_{i}": i for i in range(10_000)}
print(f"Normal:    {(time.perf_counter()-t0)*1000:.1f} ms")

# Colliding keys: O(n) per insert
t0 = time.perf_counter()
colliding = {CollidingKey(i): i for i in range(10_000)}
print(f"Colliding: {(time.perf_counter()-t0)*1000:.1f} ms")
# Colliding will be dramatically slower!
```

### Observing resize thresholds

```python
import sys

d = {}
prev = sys.getsizeof(d)
print(f"Empty dict: {prev} bytes")

for i in range(20):
    d[i] = i
    size = sys.getsizeof(d)
    if size != prev:
        print(f"After {i+1} inserts: {size} bytes (resized!)")
        prev = size
```

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────┐
│              PYTHON DICT INTERNALS CHEAT SHEET          │
├─────────────────────────────────────────────────────────┤
│ Structure:   Hash table (open addressing)               │
│ Probe:       j = ((5*j) + 1 + perturb) % size          │
│ Load factor: Resizes at ~2/3 full                       │
│ Table size:  Always 2ⁿ  (8, 16, 32, 64, ...)           │
│ Deletion:    Tombstones (dummy entries)                  │
│ Order:       Insertion order preserved (3.7+)            │
│ Layout:      Compact split-table (indices + entries)     │
│ Security:    PYTHONHASHSEED randomizes string hashes     │
│ Complexity:  O(1) avg for get/set/del, O(n) worst       │
│ Contract:    a == b  ⟹  hash(a) == hash(b)  (ALWAYS)   │
└─────────────────────────────────────────────────────────┘
```

---

*Generated from a conversation with Claude (Anthropic).*
