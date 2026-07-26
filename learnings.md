<details>
<summary>Decorators in python</summary>

I felt the need to learn it when i saw the weird `@app.get` decorator being used

decorators are nothing but functions that take another function as an argument and return a wrapper function adding some extra functionality.

```python
def my_decorator(func):
	def wrapper():
		print("before executing the function")
		func()
		print("after executing the function")
	return wrapper

@my_decorator
def greet():
	print("inside the greet function: ")

# the above code is equivalent to greet = my_decorator(greet)
```

decorators with arguments
```python
# passing arguments to the function
def my_decorator_with_args(func):
	def wrapper(*args, **kwargs):
		print("before executing the function")
		func(*args, **kwargs)
		print("after executing the function")
	return wrapper

@my_decorator_with_args
def greet_with_args(name):
	print(f"inside the greet function: {name}")

greet_with_args("Hello")  # Output: before executing the function
```
</details>

