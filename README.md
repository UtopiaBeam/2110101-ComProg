# Notice
Sample solutions for CU 2110101 Comp Prog course.
You may ask [me](https://www.facebook.com/natchapolsrisang) any questions you have or report bugs if any.

Some problems may have alternative ways to implement. The ones which exceed normal courses are labeled as (Adv: _topic(s) that is used_)

### Please do not copy the codes. You should take these as the examples and write your own codes.

# Common used topics
## sorted()
Return sorted list from the given iterable.
The syntax is:
```python
sorted(iterable[, key][, reverse])
```
- iterable - sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any iterator 
- reverse (Optional) - If true, the sorted list is reversed (or sorted in Descending order)
- key (Optional) - function that serves as a key for the sort comparison
Here is the examples:
```python
sorted([3, 2, 4, 1])					# [1, 2, 3, 4]
sorted(['a', 'B', 'C'])					# ['B', 'C', 'a']
sorted(['a', 'B', 'C'], key = str.swapcase)		# ['a', 'B', 'C']
sorted([3, 2, 4, 1], reverse = True)			# [4, 3, 2, 1]
```

# TBA
- `math` functions i.e. `sqrt()`, `ceil()`, `floor()`, `pow()`
- `format()`: set the format of strings.
- `zip()`: zip lists to tuples.
- `map()`: map a list to another with a function.
- `sum()`: sum all elements in the list.
- Inline if/else & for-loop
- Function & Lambda functions
- Iterator & Generator