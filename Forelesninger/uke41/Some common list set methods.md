# Common list, set, and dictionary methods in Python

This note covers a selection of useful functions and methods for lists, sequences, sets, and dictionaries. Python provides more methods than the ones included here; consult the Python documentation when you need more.

## Lists

List methods that modify a list generally return `None`. Methods that return a new value generally leave the original list unchanged.

| Method | What it does | Example |
|---|---|---|
| `list.append(value)` | Adds `value` to the end of the list. | `[1, 2, 3].append(7)` changes the list to `[1, 2, 3, 7]`. |
| `list.clear()` | Removes all items from the list. | `[1, 2, 3].clear()` leaves an empty list. |
| `list.copy()` | Returns a shallow copy of the list. | `new_list = my_list.copy()` |
| `list.count(value)` | Returns the number of occurrences of `value`. | `[1, 2, 4, 1, 1].count(1)` returns `3`. |
| `list.extend(iterable)` | Adds each item from an iterable to the end of the list. | `my_list.extend([7, 8])` |
| `list.index(value)` | Returns the index of the first occurrence of `value`. Raises `ValueError` if it is not found. | `[1, 2, 4, 1].index(1)` returns `0`. |
| `list.insert(index, value)` | Inserts `value` before `index`, shifting later items to the right. | `[5, 4, 3].insert(1, 7)` changes the list to `[5, 7, 4, 3]`. |
| `list.pop(index)` | Removes and returns the item at `index`. With no index, removes and returns the last item. Raises `IndexError` if the index is out of range. | `[5, 7, 4].pop(1)` returns `7` and leaves `[5, 4]`. |
| `list.remove(value)` | Removes the first occurrence of `value`. Raises `ValueError` if it is not found. | `[5, 7, 4, 7].remove(7)` leaves `[5, 4, 7]`. |
| `list.reverse()` | Reverses the list in place. | `[5, 7, 4].reverse()` leaves `[4, 7, 5]`. |
| `list.sort()` | Sorts the list in place. Supports `reverse=True` and `key=...`. | `[5, 7, 4].sort()` leaves `[4, 5, 7]`. |

### `extend` versus `append`

`extend` adds the items of an iterable individually. `append` adds its argument as one item:

```python
numbers = [1, 2, 3]
numbers.extend([7, 8])
# numbers is [1, 2, 3, 7, 8]

numbers = [1, 2, 3]
numbers.append([7, 8])
# numbers is [1, 2, 3, [7, 8]]
```

When extending a list with a set, the items are added, but their order is not guaranteed:

```python
numbers = [1, 2, 3]
numbers.extend({7, 8})
```

### Inserting at an index

If the index passed to `insert` is beyond the end of the list, the value is added at the end. An excessively negative index inserts at the beginning.

### Sorting with `key`

The `key` argument specifies a function used to determine the sort order. For example, sort names by length:

```python
names = ["Ada", "Jo", "Ruby", "Pascal"]
names.sort(key=len)                 # shortest first
names.sort(reverse=True, key=len)   # longest first
```

Values being compared must be mutually orderable. For example, sorting a list that mixes strings and numbers raises `TypeError` in Python 3.

## Sequence functions

These built-in functions work with sequences such as lists and tuples.

| Function | What it does | Example |
|---|---|---|
| `sorted(iterable)` | Returns a new list containing the items in sorted order. Does not modify the original iterable. Supports `reverse` and `key`. | `sorted((3, 1, 2))` returns `[1, 2, 3]`. |
| `reversed(sequence)` | Returns an iterator that yields the items in reverse order. Does not modify the sequence. | `list(reversed((1, 2, 3)))` returns `[3, 2, 1]`. |
| `len(collection)` | Returns the number of items. | `len([1, 2, 3])` returns `3`. |

`sorted` always returns a list. To get a sorted tuple, convert the result:

```python
values = (3, 1, 2)
sorted_tuple = tuple(sorted(values))
```

`reversed` returns an iterator. Convert it to a list or tuple if you need that concrete type:

```python
values = (1, 2, 3)
reversed_list = list(reversed(values))    # [3, 2, 1]
reversed_tuple = tuple(reversed(values))  # (3, 2, 1)
```

## Sets

A set is an unordered collection of distinct, hashable items. It is useful for removing duplicates, membership tests, and set operations.

### Creating sets

`set(iterable)` creates a set from an iterable, discarding duplicate values:

```python
set([1, 2, 3, 1, 2])  # {1, 2, 3}
set("xyzzy")          # {'x', 'y', 'z'}
set()                 # an empty set
```

The order in which set items are displayed or iterated over is not guaranteed. Use `set()` for an empty set: `{}` creates an empty dictionary.

Set items must be hashable. Immutable values such as integers, strings, and tuples containing only hashable values can be set items. Mutable values such as lists, dictionaries, and sets cannot.

```python
coordinates = {(1, 2), (0, 4)}  # valid: tuples are hashable here
# {[1, 2], [0, 4]}              # TypeError: lists are unhashable
```

### Set methods

| Method | What it does | Example |
|---|---|---|
| `set.add(value)` | Adds an item to the set. | `{1, 2, 3}.add(4)` adds `4` to the set. |
| `set.clear()` | Removes all items from the set. | `my_set.clear()` |
| `set.copy()` | Returns a shallow copy of the set. | `new_set = my_set.copy()` |
| `set.difference(other)` | Returns items that are in this set but not in `other`. | `{1, 2, 3, 4}.difference({2, 4})` returns `{1, 3}`. |
| `set.intersection(other)` | Returns items that occur in both sets. | `{1, 2, 3, 4}.intersection({3, 4, 5})` returns `{3, 4}`. |
| `set.issubset(other)` | Returns `True` if every item in this set is also in `other`. | `{1, 2}.issubset({1, 2, 3})` returns `True`. |
| `set.issuperset(other)` | Returns `True` if this set contains every item in `other`. | `{1, 2, 3}.issuperset({1, 2})` returns `True`. |
| `set.remove(value)` | Removes `value`. Raises `KeyError` if it is not present. | `my_set.remove(2)` |
| `set.symmetric_difference(other)` | Returns items that are in either set, but not in both. | `{1, 2, 3, 4}.symmetric_difference({3, 4, 5, 6})` returns `{1, 2, 5, 6}`. |
| `set.union(other)` | Returns a set containing items from either set. | `{1, 2, 3}.union({3, 4, 5})` returns `{1, 2, 3, 4, 5}`. |

The original set is not changed by `difference`, `intersection`, `symmetric_difference`, or `union`; these methods return a new set.

## Dictionaries

A dictionary stores key-value pairs. Keys must be hashable; values can be of any type, including mutable types such as lists.

```python
scores = {"Ada": 2, "Bob": 2, "Cher": 1}
```

Here, names are keys and scores are values. For example, `scores["Ada"]` returns `2`. A tuple can be a key if all its items are hashable:

```python
data = {("A", "B"): [1, 2, 3]}  # valid: tuple key, list value
```

### Dictionary methods

| Method | What it does | Example |
|---|---|---|
| `dict()` | Creates a dictionary, optionally from key-value pairs. | `dict([("A", 0), ("B", 5)])` |
| `dict.clear()` | Removes all key-value pairs. | `my_dict.clear()` |
| `dict.copy()` | Returns a shallow copy of the dictionary. | `new_dict = my_dict.copy()` |
| `dict.fromkeys(keys, value)` | Creates a dictionary with the given keys, all associated with `value`. | `dict.fromkeys(["A", "B", "C"], 0)` returns `{"A": 0, "B": 0, "C": 0}`. |
| `dict.get(key, default)` | Returns the value for `key`, or `default` if the key is missing. The default is `None`. | `my_dict.get("X", -1)` |
| `dict.items()` | Returns a view of the dictionary's key-value pairs. | `list(my_dict.items())` |
| `dict.keys()` | Returns a view of the dictionary's keys. | `list(my_dict.keys())` |
| `dict.pop(key)` | Removes `key` and returns its value. Raises `KeyError` if it is missing and no default is supplied. | `my_dict.pop("C")` |
| `dict.values()` | Returns a view of the dictionary's values. | `list(my_dict.values())` |

For example:

```python
my_dict = {"A": 0, "B": 5, "C": 3}

my_dict.get("B")        # 5
my_dict.get("X")        # None
my_dict.get("X", -1)    # -1
list(my_dict.items())   # [('A', 0), ('B', 5), ('C', 3)]
list(my_dict.keys())    # ['A', 'B', 'C']
list(my_dict.values())  # [0, 5, 3]
my_dict.pop("C")        # returns 3 and removes the key "C"
```

`items()`, `keys()`, and `values()` return dynamic views, not lists. Convert them with `list(...)` when you specifically need a list.

**Note:** If the value passed to `dict.fromkeys` is mutable, every key refers to that same object. For separate mutable values, use a dictionary comprehension instead:

```python
lists = {key: [] for key in ["A", "B", "C"]}
```
