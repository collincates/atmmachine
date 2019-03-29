from decimal import InvalidOperation, Decimal as D


class Account(object):
    """
    Object representing a bank account with basic ATM functionality
    like deposit, withdraw, and account transfers.
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = D('0.00')
        self.daily_withdrawal_limit = D('300.00')
        self.total_withdrawn_today = D('0.00')

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        """
        Any positive numeric amount--including cents--is acceptable for deposit.
        Decimal object automatically catches 'non-numeric' strings and raises
        an InvalidOperation error.
        """

        try:
            # Prevent zero or negative deposit amounts
            if D(amount) <= D('0.00'):
                raise InvalidOperation
            # Prevent zero or negative balance after deposit
            elif (self.balance + D(amount)) <= D('0.00'):
                raise InvalidOperation
            # Increase balance by valid, positive deposit amount
            else:
                self.balance += D(amount)

        except InvalidOperation:
            return 'Please enter a valid deposit amount.'

    # Method to withdraw a custom amount
        # Denominations are $5, $10, $20, $50. Other denominations are not allowed
        # Overdraft fee of $10 when withdrawing into negative balance

    # Method to reset daily limit
        # Reset limit at 12:01am local time the day after reaching withdrawal limit.

    # Method to transfer custom amount to another account
        # Any denomination -- including cents -- is acceptable for transfers
