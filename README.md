# Notice
Sample solutions for CU 2110101 Comp Prog course.
You may ask [me](https://www.facebook.com/natchapolsrisang) any questions you have or report bugs if any.

Some problems may have alternative ways to implement. The ones which exceed normal courses are labeled as (Adv: _topic(s) that is used_)

### Please do not copy the codes. You should take these as the examples and write your own codes.

# Common used topics
There are some topics that used frequently as following:

## Inline if-else
Basically if-else with alternative short implementation, as followed:
```python
_something_when_true_ if _condition_ else _something_when_false_
```
which is equivalent to:
```python
if _condition_ :
	_something_when_true_ 
else :
	_something_when_false_
```
Here is an example:
```python
print('More than' if 1 > 2 else 'Less than')
```
#### Note that inline if-else must have `else` in the statement. Otherwise the syntax will be wrong.

## Inline for-loop & List comprehension
Basically for-loop with alternative short implementation, which is usually used with list, set, generator comprehension.

List comprehension is a way to express a list using short syntax, which usually combined with inline for-loop

The syntax of inline for-loop is:
```python
_command_ for _variable_ in _iterable_
```
which is equivalent to:
```python
for _variable_ in _iterable_ :
	_command_
```

The list comprehension syntax is:
```python
ls = [_expression_ for _var_ in _iterable_]
```
which is equivalent to:
```python
ls = []
for _var_ in _iterable_ :
	ls.append(_expression_)
```
Here is an example:
```python
ls = [x for x in range(5)]	# [0, 1, 2, 3, 4]
```

Inline if-else can also be used in for-loop as followed:
```python
_something_when_true_ if _condition_ else _something_when_false_ for _variable_ in _iterable_
# Again, else is needed.
```
or
```python
_command_ for _variable_ in _iterable_ if _condition_
```

Here are some examples:
```python
ls = [x for x in range(5) if x % 2 == 0]			# [0, 2, 4]
ls = [x if x % 2 == 0 else -x for x in range(5)]		# [0, -1, 2, -3, 4]
```

## Function
Function is a block of reusable codes, which provides an easier way to implement reputative commands.

The implementation is:
```python
def function_name( [paramaters] ) :
	command_1
	command_2
	.
	.
	.
```
Here is an example:
```python
def double(x) :
	return 2*x
double(5)	# 10
```

## Lambda Function
Lambda Function is an anonymous function, which is usually needed when it has been created. It is usually used with other functions i.e. `map()`, `filter()`
The implementation is:
```python
lambda [parameters] : expression
```
Here is an example:
```python
sum = lambda x, y : x + y
```
which is equivalent to:
```python
def sum(x, y) :
	return x + y
```

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
- `zip()`: zip lists to tuples.
- `map()`: map a list to another with a function.
- Iterator & Generator
