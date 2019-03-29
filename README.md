__<h1>ATM Machine</h1>__
<hr>
<h4>Description</h4>
The code in this repository provides the basic functionality for an ATM Machine.
`Account` objects can accept parameters for an account holder's first and last names.
The default initial balance for a new `Account` is `$0.00`.
Acceptable withdrawals are in increments of `$5.00`, `$10.00`, `$20.00`, and `$50.00`.
There is a daily withdrawal limit of `$300.00` can be reset by calling the "private" method `_reset_daily_limit()` on any day following the day on which the daily withdrawal limit was reached.

To maintain a currency-like format with two decimal places `(0.00)` while avoiding float/currency issues, this code uses Python's `decimal` module which can be read about in the documentation linked [here](https://docs.python.org/3/library/decimal.html).
<hr>

<h4>Example Usage</h4>

```
>>> from atm import Account

# Make a new account for Bob Smith
>>> bob_smith = Account('Bob', 'Smith')

>>> bob_smith.get_balance()
'Your balance is $0.00.'

>>> bob_smith.deposit('99.99')
'Your balance is $99.99.'

>>> bob_smith.withdraw('20.00')
'Your balance is $79.99.'

>>> bob_smith.withdraw('0.99')
'Withdrawals must be in increments of $5.00, $10.00, $20.00 or $50.00.'

>>> bob_smith.withdraw('5.00')
'Your balance is $74.99.'

# Withdrawing more than current balance triggers an overdraft fee
>>> bob_smith.withdraw('100.00')
'You have been charged an overdraft fee of $10.00. Your balance is $-35.01.'

>>> bob_smith.deposit('100.00')
'Your balance is $64.99.'

# Set up a new account for Mary Clark
>>> mary_clark = Account('Mary', 'Clark')

>>> mary_clark.get_balance()
'Your balance is $0.00.'

# Bob Smith attempts to transfer more than he has to Mary Clark
>>> bob_smith.transfer(mary_clark, '1000000.00')
'You can transfer a maximum amount of $64.99.'

# Bob transfers the maximum amount to Mary
>>> bob_smith.transfer(mary_clark, '64.99')
"Bob Smith's balance is: $0.00. Mary Clark's balance is: $64.99."

# Mary gives some of it back to Bob
>>> mary_clark.transfer(bob_smith, '20.99')
"Mary Clark's balance is: $44.00. Bob Smith's balance is: $20.99."
```
<hr>

<h4>Class Methods</h4>
Below is a list of the methods associated with the `Account` class:


`__init__()`

   `self.first_name`: The account holder's first name passed in as a parameter.
   `self.last_name`: The account holder's last name passed in as a parameter.
   `self.balance`: The initial balance amount, defaults to `0.00`.
   `self.daily_withdrawal_limit`: Set to 300.00 by default.
   `self.daily_withdrawal_total`: Total amount withdrawn today. Cannot exceed `self.daily_withdrawal_limit` in a single day.
   `self.todays_date`: Stores the current date as a `datetime.date` object.
   `self.date_of_latest_withdrawal`: Defaults to `None`. Is set to today's date whenever the `withdraw()` method is called. This attribute is used in conjunction with `_reset_daily_limit()` to enforce the daily withdrawal limit until tomorrow at midnight.
   `self.overdraft_fee`: Amount of fee to be charged when withdrawing into a negative account balance.

`get_first_name()`

   Returns the account holder's first name as a string.


`get_last_name()`

   Returns the account holder's last name as a string.


`get_full_name()`


   Returns the account holder's full name as a string.


`get_balance()`

   Returns the account's current balance as a `Decimal` object. This object can be printed, passed into other functions, or have arithmetic operations performed on it with other `Decimal` objects.


`deposit(amount)`

    `amount`: Accepts a positive "numeric" value as a string and increases `self.balance` by that amount.
   Will return a message asking for a valid deposit amount for any deposit amount that is equal to or less than zero.


`withdraw(amount)`

   `amount`: Accepts a positive "numeric" value as a string and decreases `self.balance` by that amount.
   Will return a message displaying the acceptable withdrawal denominations if the amount provided is not divisible by any of the acceptable denominations. This includes any withdrawals less than or equal to zero.
   When the daily withdrawal limit has been reached ($300 by default)--or would be reached at the end of the current transaction--withdrawals are made unavailable until the next day starting at midnight.
   An overdraft fee is applied when withdrawing into a negative account balance.

`transfer(to_account, amount)`

   `to_account`: The account to which you want to transfer the `amount`. This must be an instance of `Account()` or a message will be returned.
   `amount`: Accepts a positive "numeric" value as a string and decreases `self.balance` by that amount, and increased `to_account.balance` by that amount. Zero, negative, or amounts that exceed the originating account's max balance are not allowed and return warning messages.


`_reset_daily_limit()`

   "Private" method that can be called in order to reset the daily withdrawal limit. This only works if called on a day other than the value stored in `self.todays_date`. If this method is called on the same day that the daily limit has been reached, a message will be displayed indicating to call the method on a day other than today.



<hr>
<h4>Tests</h4>
Test coverage is 100%.
Currently using `unittest` to test functionality.
Please look at the provided test suite in `test_atm.py` for more details about what has been tested.
<hr>
