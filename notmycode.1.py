
func = getattr(modulename, funcname, None):
if func:
    func(arg)

>>> def get_name():
...     print('loading...')
...     return 'Anton'
>>> print('Hello, ' + (get_name() or 'Anonymous'))
loading...
Hello, Anton

>>> age = 15
>>> # Conditions are evaluated from left to right
>>> print('kid' if age < 18 else 'adult')
kid
