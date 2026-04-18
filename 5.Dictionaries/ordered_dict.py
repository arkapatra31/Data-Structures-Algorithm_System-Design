from collections import OrderedDict

# =============================================================
# 1. Equality: order matters for OrderedDict, not for dict
# =============================================================
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"c": 3, "a": 1, "b": 2}
print(f"dict == dict (different order):        {d1 == d2}")  # True

od1 = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
od2 = OrderedDict([("c", 3), ("a", 1), ("b", 2)])
print(f"OrderedDict == OrderedDict (diff order): {od1 == od2}")  # False!

# But OrderedDict vs dict comparison ignores order:
print(f"OrderedDict == dict:                     {od1 == d1}")  # True


# =============================================================
# 2. move_to_end — reposition without delete + reinsert
# =============================================================
od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
print(f"\nBefore move_to_end: {list(od.keys())}")  # ['a', 'b', 'c']

od.move_to_end("a")  # move "a" to the end
print(f"After move_to_end('a'):  {list(od.keys())}")  # ['b', 'c', 'a']

od.move_to_end("c", last=False)  # move "c" to the front
print(f"After move_to_end('c', last=False): {list(od.keys())}")  # ['c', 'b', 'a']


# =============================================================
# 3. popitem — LIFO or FIFO
# =============================================================
od = OrderedDict([("first", 1), ("second", 2), ("third", 3)])

print(f"\npopitem(last=True):  {od.popitem(last=True)}")   # ('third', 3) — LIFO
print(f"popitem(last=False): {od.popitem(last=False)}")     # ('first', 1) — FIFO
print(f"Remaining: {dict(od)}")  # {'second': 2}


# =============================================================
# 4. Practical use: simple LRU cache with OrderedDict
# =============================================================
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)  # mark as recently used
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # evict oldest

lru = LRUCache(3)
lru.put("a", 1)
lru.put("b", 2)
lru.put("c", 3)
print(f"\nLRU state: {list(lru.cache.keys())}")  # ['a', 'b', 'c']

lru.get("a")  # access "a" — moves to end
print(f"After accessing 'a': {list(lru.cache.keys())}")  # ['b', 'c', 'a']

lru.put("d", 4)  # exceeds capacity — evicts "b" (oldest)
print(f"After adding 'd':    {list(lru.cache.keys())}")  # ['c', 'a', 'd']
