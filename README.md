__<h1>ATM Machine</h1>__
<hr>
<h4>Description</h4>
The code in this repository provides the basic functionality for an ATM Machine.
\`Account\` objects can accept parameters for an account holder's first and last names, and can accept a custom initial balance for the account.
The default initial balance is `$0.00`.
There is a daily withdrawal limit of `$300.00` that resets at midnight each day.
<hr>

<h4>Class Methods</h4>
Below is a list of the methods associated with the `Account` class:


`__init__()`



`get_first_name()`



`get_last_name()`



`get_full_name()`



`get_account_balance()`



`deposit()`



`withdraw()`



`_reset_daily_limit()`



`transfer()`



<hr>
<h4>Tests</h4>
Currently using `unittest` to test functionality.
Please look at the provided test suite in `test_atm.py` for more details about what has been tested.
<hr>
