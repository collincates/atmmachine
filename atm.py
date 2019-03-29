class Account(object):

    # Initialize ATM Account object
    def __init__(self, first_name, last_name, balance=0.00):
        # Account holder first name passed as parameter
        self.first_name = first_name
        # Account holder last name passed as parameter
        self.last_name = last_name
        # Initial balance attribute passed as parameter
        self.balance = balance
        # Daily withdrawal limit is $300.00
        self.daily_withdrawal_limit = 300.00

    # Method to return account holder's first name

    # Method to return account holder's last name

    # Method to return account holder's full name

    # Method to return account balance

    # Method to deposit custom amount
        # Any denomination -- including cents -- is acceptable for deposits

    # Method to withdraw a custom amount
        # Denominations are $5, $10, $20, $50. Other denominations are not allowed
        # Overdraft fee of $10 when withdrawing into negative balance

    # Method to reset daily limit
        # Reset limit at 12:01am local time the day after reaching withdrawal limit.

    # Method to transfer custom amount to another account
        # Any denomination -- including cents -- is acceptable for transfers
