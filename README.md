# Notice
Sample solutions for CU 2110101 Comp Prog course.
You may ask [me](https://www.facebook.com/natchapolsrisang) any questions you have or report bugs if any.

Some problems may have alternative ways to implement. The ones which follow normal courses are labeled by number (if there are multiple ways of implementation), and the ones which exceed normal courses are labeled as (Adv: _topic(s) that is used_)

### Please do not copy the codes. You should take these as the examples and write your own codes.

# Progressing solutions
_None_

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
and is also equivalent to:
```python
[_something_when_false_,  _something_when_true_](_condition_)
```
Here is an example:
```python
print('More than' if 1 > 2 else 'Less than')
# which is equivalent to
print(['Less than', 'More than'](1 > 2))
```
#### Note that inline if-else must have `else` in the statement. Otherwise the syntax will be wrong.

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
## `map()`, `filter()`, and List Comprehension
Map is a way to map a list to another list with a functon.
List Comprehension implementation using map is:
```python
ls = [func(_args_) for _args_ in _iterable_]
```
- `func()` is a map function.
- `_args_` is a list of arguments.
- `_iterable_` is an iterable.

which is equivalent to:
```python
ls = list(map(func, _iterable_))
```
Here is an example:
```python
ls = [x**2 for x in [1, 2, 3]]			# ls = [1, 4, 9]
ls = list(map(lambda x : x**2, [1, 2, 3]))	# ls = [1, 4, 9]
```

Filter is a way to filter elements in list using a condition.
List Comprehension implementation using filter is:
```python
ls = [_args_ for _args_ in _iterable_ if _condition_]
```
- `func()` is a map function.
- `_args_` is a list of arguments.
- `_iterable_` is an iterable.
- `_condition_` is a filter condition.

which is equivalent to:
```python
ls = list(filter(_condition_, _iterable_))
```
Here is an example:
```python
ls = [x for x in [1, 2, 3] if x % 2 != 0]		# ls = [1, 3]
ls = list(filter(lambda x : x % 2 != 0, [1, 2, 3]))	# ls = [1, 3]
```

## `zip()`
`zip()` is a function that zip two or more lists into a list of tuples.
The implementation is:
```python
zip(_list of lists_)
```
Here are some examples:
```python
zip([1, 2, 3], [4, 5, 6])			# [(1, 4), (2, 5), (3, 6)]
zip(['a', 'b', 'c'], [1, 2, 3], [3, 2, 1])	# [('a', 1, 3), ('b', 2, 2), ('c', 3, 1)]
```
Here is an illustration:
```
ls1:	[1, 	 2, 	 3]
ls2:	[4, 	 5, 	 6]
	 ^  	 ^  	 ^
	 |  	 |  	 |
zip:  [(1, 4), (2, 5), (3, 6)]
```

# TBA ?
- Iterator & Generator
