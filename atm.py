import datetime
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
        self.daily_withdrawal_total = D('0.00')
        self.todays_date = datetime.datetime.today().date()
        self.date_of_latest_withdrawal = None

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
            # Prevent negative balance after deposit
            elif (self.balance + D(amount)) < D('0.00'):
                raise InvalidOperation
            # Increase balance by valid, positive deposit amount
            else:
                self.balance += D(amount)

        except InvalidOperation:
            return 'Please enter a valid deposit amount.'

    def withdraw(self, amount):
        # Acceptable withdrawal denominations and
        # overdraft fee can be dynamically changed here.
        acceptable_denominations = [
            D('5.00'),
            D('10.00'),
            D('20.00'),
            D('50.00')
        ]

        overdraft_fee = D('10.00')

        tomorrows_date = self.todays_date + datetime.timedelta(days=1)

        # Check if the daily withdrawal limit
        # will be exceeded during this transaction
        if D(amount) + self.daily_withdrawal_total > self.daily_withdrawal_limit:
            return f'Daily withdrawal limit reached. Please try again on {tomorrows_date.strftime("%b %d, %Y")}.'

        try:
            # Prevent zero or negative withdrawal amounts
            if D(amount) <= D('0.00'):
                raise InvalidOperation
            # If withdrawal amount is not divisible by any of the acceptable
            # denominations, return a message with the acceptable denominations.
            elif not any(map(lambda x: D(amount) % x == 0, acceptable_denominations)):
                raise InvalidOperation
            # Overdraft fee of $10 applied when withdrawing into negative balance
            elif self.balance - D(amount) < D('0.00'):
                self.balance -= (D(amount) + overdraft_fee)
            # Decrease balance by withdrawal amount, and increment daily total
            else:
                self.balance -= D(amount)
                self.daily_withdrawal_total += D(amount)
                self.date_of_latest_withdrawal = self.todays_date

        except InvalidOperation:
            return f'Withdrawals must be in increments of {", ".join([f"${i}" for i in acceptable_denominations[:-1]])} or ${acceptable_denominations[-1]}.'

    def _reset_daily_limit(self):
        # Update self.todays_date when calling _reset_daily_limit() on a new day.
        self.todays_date = datetime.datetime.today().date()
        # Reset daily withdrawal total
        self.daily_withdrawal_total = D('0.00')

    # Method to transfer custom amount to another account
        # Any denomination -- including cents -- is acceptable for transfers
