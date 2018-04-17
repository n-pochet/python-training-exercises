# Interface Status

Implement the `status` function in `interface_status.py`

It should pretty print, according to a certain formatting, JSON file that is passed to it.

Example:

```
>>> j_if_status = '[{"name": "eth1/1", "status": "UP"}]'
>>> status(j_if_status)
Name:     Status:
-----------------
eth1/1    UP
```

## Run the tests

```
python interface_status_tests.py
```

It should output a positive result:

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```