__<h1>ATM Machine</h1>__
<hr>
<h4>Description</h4>
The code in this repository provides the basic functionality for an ATM Machine.
`Account` objects can accept parameters for an account holder's first and last names,
The default initial balance is `$0.00`.
There is a daily withdrawal limit of `$300.00` that resets at midnight each day.

To maintain a currency-like format with two decimal places `(0.00)` while avoiding float/currency issues, this code uses Python's `decimal` module which can be read about in the documentation linked [here](https://docs.python.org/3/library/decimal.html).
<hr>

<h4>Class Methods</h4>
Below is a list of the methods associated with the `Account` class:


`__init__()`

 `self.first_name`: The account holder's first name passed in as a parameter.
 `self.last_name`: The account holder's last name passed in as a parameter.
 `self.balance`: The initial balance amount, defaults to `0.00`.
 `self.daily_withdrawal_limit`: Set to 300.00 by default.
 `self.total_withdrawn_today`: Total amount withdrawn today. Cannot exceed `self.daily_withdrawal_limit`.

`get_first_name()`

 Returns the account holder's first name as a string.


`get_last_name()`

 Returns the account holder's last name as a string.


`get_full_name()`


 Returns the account holder's full name as a string.


`get_balance()`

 Returns the account's current balance as a `Decimal` object. This object can be printed, passed into other functions, or have arithmetic operations performed on it with other `Decimal` objects.


`deposit()`

 Accepts a positive "numeric" amount as a string and increases `self.balance` by that amount.
 Will return a message asking for a valid deposit amount for any amount that is equal to or less than zero.
 

`withdraw()`



`_reset_daily_limit()`



`transfer()`



<hr>
<h4>Tests</h4>
Currently using `unittest` to test functionality.
Please look at the provided test suite in `test_atm.py` for more details about what has been tested.
<hr>
