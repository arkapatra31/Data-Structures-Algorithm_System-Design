"""
Exploring Python dictionary internals, hashing, and collisions.
"""
import sys

# =============================================================
# 1. How hash() works for different types
# =============================================================
print("=== Hash values ===")
print(f"hash('apple')  = {hash('apple')}")
print(f"hash('banana') = {hash('banana')}")
print(f"hash(42)       = {hash(42)}")      # small ints hash to themselves
print(f"hash(42.0)     = {hash(42.0)}")    # 42 == 42.0, so hashes must match
print(f"hash((1, 2))   = {hash((1, 2))}")  # tuples are hashable

# This would raise TypeError:
# hash([1, 2])   # lists are mutable → not hashable
# hash({1: 2})   # dicts are mutable → not hashable


# =============================================================
# 2. Simulating how Python finds a slot (simplified)
# =============================================================
def find_slot(key, table_size=8):
    """Simulate Python's open-addressing probe sequence."""
    h = hash(key)
    idx = h % table_size
    perturb = h

    print(f"\nProbing for key={key!r}, hash={h}")
    print(f"  Initial index: {h} % {table_size} = {idx}")

    # Show first 5 probe positions
    for i in range(5):
        print(f"  Probe {i}: slot {idx}")
        # Python's actual formula from dictobject.c
        idx = ((5 * idx) + 1 + perturb) % table_size
        perturb >>= 5  # shift right by 5 bits each round

print("=== Probe sequences ===")
find_slot("apple")
find_slot("mango")


# =============================================================
# 3. Demonstrating the __hash__ / __eq__ contract
# =============================================================
class GoodKey:
    """Correctly implements hash/eq contract."""
    def __init__(self, val):
        self.val = val

    def __hash__(self):
        return hash(self.val)

    def __eq__(self, other):
        return isinstance(other, GoodKey) and self.val == other.val

    def __repr__(self):
        return f"GoodKey({self.val!r})"


class BadKey:
    """BROKEN: equal objects have different hashes!"""
    def __init__(self, val):
        self.val = val

    def __hash__(self):
        return id(self)  # different object → different hash, even if val matches

    def __eq__(self, other):
        return isinstance(other, BadKey) and self.val == other.val

    def __repr__(self):
        return f"BadKey({self.val!r})"


print("\n=== Good vs Bad key contract ===")

# Good keys work correctly
d = {}
d[GoodKey("x")] = 100
print(f"GoodKey lookup: {d[GoodKey('x')]}")  # 100 — finds it!

# Bad keys are broken
d2 = {}
d2[BadKey("x")] = 100
try:
    val = d2[BadKey("x")]  # KeyError! Different hash, can't find it
    print(f"BadKey lookup: {val}")
except KeyError:
    print("BadKey lookup: KeyError! (hash contract violated)")


# =============================================================
# 4. Forcing collisions to observe behavior
# =============================================================
class CollidingKey:
    """All instances hash to the same value — maximum collisions."""
    def __init__(self, val):
        self.val = val

    def __hash__(self):
        return 42  # every key collides!

    def __eq__(self, other):
        return isinstance(other, CollidingKey) and self.val == other.val

    def __repr__(self):
        return f"CK({self.val!r})"


print("\n=== Forced collision performance ===")
import time

# Normal dict: O(1) per insert
normal = {}
t0 = time.perf_counter()
for i in range(10_000):
    normal[f"key_{i}"] = i
t1 = time.perf_counter()
print(f"Normal keys (10k inserts): {(t1-t0)*1000:.1f} ms")

# Colliding dict: O(n) per insert due to all-same hash
colliding = {}
t0 = time.perf_counter()
for i in range(10_000):
    colliding[CollidingKey(i)] = i
t1 = time.perf_counter()
print(f"Colliding keys (10k inserts): {(t1-t0)*1000:.1f} ms")
print("  ^ Much slower due to O(n) probing per insert!")


# =============================================================
# 5. Dict memory and resize thresholds
# =============================================================
print("\n=== Dict size growth ===")
d = {}
prev_size = sys.getsizeof(d)
print(f"Empty dict: {prev_size} bytes")

for i in range(20):
    d[i] = i
    new_size = sys.getsizeof(d)
    if new_size != prev_size:
        print(f"After {i+1} inserts: {new_size} bytes (resized!)")
        prev_size = new_size


# =============================================================
# 6. Hash randomization (PYTHONHASHSEED)
# =============================================================
print("\n=== Hash randomization ===")
print(f"hash('hello') = {hash('hello')}")
print("Run this script twice — string hashes will differ each time!")
print("Integer hashes are stable: hash(100) =", hash(100))
print("Set PYTHONHASHSEED=0 to disable randomization for debugging.")