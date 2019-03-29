import datetime
from decimal import InvalidOperation, Decimal as D


class Account(object):
    """
    Object representing a bank account with basic ATM functionality
    like deposit, withdraw, and account transfers.
    The daily withdrawal limit can be reset by calling
    '_reset_daily_limit()' on any day following the day
    on which the limit was reached.
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = D('0.00')
        self.daily_withdrawal_limit = D('300.00')
        self.daily_withdrawal_total = D('0.00')
        self.todays_date = datetime.datetime.today().date()
        self.date_of_latest_withdrawal = None
        self.overdraft_fee = D('10.00')

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_balance(self):
        return f'Your balance is ${self.balance}.'

    def deposit(self, amount):
        """
        Any positive numeric amount--including cents--is acceptable for deposit.
        Decimal object automatically catches 'non-numeric' strings
        and raises an InvalidOperation error.
        """

        try:
            # Prevent zero or negative deposit amounts
            if D(amount) <= D('0.00'):
                raise InvalidOperation
            # Increase balance by valid, positive deposit amount
            else:
                self.balance += D(amount)
                return f'Your balance is ${self.balance}.'

        except InvalidOperation:
            return 'Please enter a valid deposit amount.'

    def withdraw(self, amount):
        """
        Any positive numeric amount--including cents--can be withdrawn.
        Decimal object automatically catches 'non-numeric' strings
        and raises an InvalidOperation error.
        """

        # Acceptable withdrawal denominations can be dynamically changed here.
        acceptable_denominations = [
            D('5.00'),
            D('10.00'),
            D('20.00'),
            D('50.00')
        ]

        tomorrows_date = self.todays_date + datetime.timedelta(days=1)

        # Check if the daily withdrawal limit
        # will be exceeded during this transaction
        if D(amount) + self.daily_withdrawal_total > self.daily_withdrawal_limit:
            return (
                f'Daily withdrawal limit reached. '
                f'Please try again on {tomorrows_date.strftime("%b %d, %Y")}.'
            )

        try:
            # Prevent zero or negative withdrawal amounts
            if D(amount) <= D('0.00'):
                raise InvalidOperation
            # If withdrawal amount is not divisible by any of the acceptable
            # denominations, return a message with the acceptable denominations.
            elif not any(
                map(lambda x: D(amount) % x == 0, acceptable_denominations)
            ):
                raise InvalidOperation
            # Overdraft fee of $10 applied when withdrawing to negative balance
            elif self.balance - D(amount) < D('0.00'):
                self.balance -= (D(amount) + self.overdraft_fee)
                return (
                    f'You have been charged an overdraft fee of '
                    f'${self.overdraft_fee}. Your balance is ${self.balance}.'
                )
            # Decrease balance by withdrawal amount, increment daily total
            # and set date_of_latest_withdrawal to today.
            else:
                self.balance -= D(amount)
                self.daily_withdrawal_total += D(amount)
                self.date_of_latest_withdrawal = self.todays_date
                return f'Your balance is ${self.balance}.'

        except InvalidOperation:
            return (
                f'Withdrawals must be in increments of '
                f'{", ".join([f"${i}" for i in acceptable_denominations[:-1]])}'
                f' or ${acceptable_denominations[-1]}.'
            )
    def transfer(self, to_account, amount):
        # Ensure that to_account value is an Account() instance
        if isinstance(to_account, type(Account('first_name', 'last_name'))):
            # Prevent zero or negative transfer amounts
            if D(amount) <= D('0.00'):
                    return 'Transfer amount must be larger than $0.00.'
            # Transfer amount is a positive value
            else:
                # Resulting balance after transfer cannot be a negative value
                if self.balance - D(amount) < D('0.00'):
                    return (
                        f'You can transfer a maximum amount '
                        f'of ${self.balance}.'
                    )
                # Transfer valid, positive amount to_account
                else:
                    self.balance -= D(amount)
                    to_account.balance += D(amount)
                    return (
                        f'{self.get_full_name()}\'s balance is: '
                        f'${self.balance}. '
                        f'{to_account.get_full_name()}\'s balance is: '
                        f'${to_account.balance}.'
                    )

        # If to_account value is not an instance of Account()
        else:
            return 'Receiving account must be an instance of class Account().'

    def _reset_daily_limit(self):
        # Update self.todays_date when _reset_daily_limit() called on a new day.
        if self.todays_date != datetime.datetime.today().date():
            self.todays_date = datetime.datetime.today().date()
            # Reset daily withdrawal total
            self.daily_withdrawal_total = D('0.00')
            return (
                f'The daily limit for {self.get_full_name}\'s '
                f'account has been reset.'
            )
        else:
            return (
                f'Please reset the daily withdrawal limit on '
                f'{(self.todays_date + datetime.timedelta(days=1)).strftime("%b %d, %Y")}.'
            )
