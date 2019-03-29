import unittest
import datetime
import decimal
from decimal import Decimal as D
from atm import Account


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.account1 = Account('Sally', 'Smith')
        self.account2 = Account('Sam', 'Jones')

        self.tomorrows_date = (
            datetime.datetime.today()
            + datetime.timedelta(days=1)
            ).date().strftime("%b %d, %Y")

    def test_atm_account_return_account_holders_first_name(self):
        self.assertEqual(self.account1.get_first_name(), 'Sally')
        self.assertEqual(self.account2.get_first_name(), 'Sam')

    def test_atm_account_return_account_holders_last_name(self):
        self.assertEqual(self.account1.get_last_name(), 'Smith')
        self.assertEqual(self.account2.get_last_name(), 'Jones')

    def test_atm_account_return_account_holders_full_name(self):
        self.assertEqual(self.account1.get_full_name(), 'Sally Smith')
        self.assertEqual(self.account2.get_full_name(), 'Sam Jones')

    def test_atm_account_initial_balance_default_of_zero_dollars(self):
        self.assertEqual(
            self.account1.get_balance(),
            'Your balance is $0.00.'
        )
        self.assertEqual(
            self.account2.get_balance(),
            'Your balance is $0.00.'
        )

    def test_atm_account_deposit_positive_amount_passes(self):
        self.account1.deposit('0.01')
        self.assertEqual(
            self.account1.get_balance(),
            'Your balance is $0.01.'
        )
        self.account2.deposit('99999999999999999.95')
        self.assertEqual(
            self.account2.get_balance(),
            'Your balance is $99999999999999999.95.'
        )

    def test_atm_account_deposit_negative_amount_returns_message(self):
        self.assertEqual(
            self.account1.deposit('-1234.56'),
            'Please enter a valid deposit amount.'
        )

    def test_atm_account_deposit_zero_amount_returns_message(self):
        self.assertEqual(
            self.account2.deposit('0.00'),
            'Please enter a valid deposit amount.'
        )

    def test_atm_account_return_accurate_balance_after_multiple_deposits(self):
        self.account1.deposit('1000')
        self.account1.deposit('5.00')
        self.account1.deposit('4.99')
        self.account1.deposit('0.01')
        self.assertEqual(
            self.account1.get_balance(),
            'Your balance is $1010.00.'
        )

    def test_atm_account_withdraw_zero_dollars_returns_message(self):
        self.account1.deposit('5.00')
        self.assertEqual(
            self.account1.withdraw('0.00'),
            'Withdrawals must be in increments of $5.00, $10.00, $20.00 or $50.00.'
        )

    def test_atm_account_withdraw_negative_amount_returns_message(self):
        self.account2.deposit('5.00')
        self.assertEqual(
            self.account2.withdraw('-10.00'),
            'Withdrawals must be in increments of $5.00, $10.00, $20.00 or $50.00.'
        )

    def test_atm_account_withdraw_amount_using_acceptable_denomination(self):
        self.account1.deposit('500.00')
        self.account1.withdraw('120.00')
        self.assertEqual(
            self.account1.get_balance(),
            'Your balance is $380.00.'
        )

    def test_atm_account_withdraw_amount_using_unacceptable_denomination_returns_message(self):
        self.account2.deposit('35.99')
        self.assertEqual(
            self.account2.withdraw('5.01'),
            'Withdrawals must be in increments of $5.00, $10.00, $20.00 or $50.00.'
        )

    def test_atm_account_withdraw_results_in_zero_balance(self):
        self.account1.deposit('200.00')
        self.account1.withdraw('100.00')
        self.account1.withdraw('100.00')
        self.assertEqual(
            self.account1.get_balance(),
            'Your balance is $0.00.'
        )

    def test_atm_account_withdraw_results_in_negative_balance_and_charges_ten_dollar_overdraft_fee(self):
        self.account2.deposit('100.00')
        self.assertEqual(
            self.account2.get_balance(),
            'Your balance is $100.00.'
        )
        # Withdraw $200, trigger overdraft charge of $10
        self.account2.withdraw('200.00')
        self.assertEqual(
            self.account2.get_balance(),
            'Your balance is $-110.00.'
        )

    def test_atm_account_withdraw_daily_limit_in_one_withdrawal(self):
        self.account1.deposit('500.00')
        self.account1.withdraw('300.00')
        self.assertEqual(
            self.account1.get_balance(),
            'Your balance is $200.00.'
        )

    def test_atm_account_withdraw_would_exceed_daily_limit_in_one_withdrawal(self):
        self.account2.deposit('1000.00')
        self.assertEqual(
            self.account2.withdraw('300.01'),
            (
                f'Daily withdrawal limit reached. '
                f'Please try again on {self.tomorrows_date}.'
            )
        )

    def test_atm_account_withdraw_would_exceed_daily_limit_over_multiple_withdrawals(self):
        self.account1.deposit('500.00')
        self.account1.withdraw('100.00')
        self.account1.withdraw('100.00')
        self.account1.withdraw('100.00')
        # Daily limit has been reached, so anything more will exceed the limit
        self.assertEqual(
            self.account1.withdraw('5.00'),
            (
                f'Daily withdrawal limit reached. '
                f'Please try again on {self.tomorrows_date}.'
            )
        )

    def test_atm_account_date_of_latest_withdrawal_defaults_to_none(self):
        self.account2.deposit('5000.00')
        self.assertIsNone(self.account2.date_of_latest_withdrawal)

    def test_atm_account_withdraw_sets_date_of_latest_withdrawal_as_today(self):
        self.account2.deposit('1000.00')
        self.account2.withdraw('100.00')
        self.account2.withdraw('100.00')
        self.assertEqual(
            self.account2.date_of_latest_withdrawal,
            datetime.datetime.today().date()
        )

    def test_atm_account_transfer_to_another_account_with_incorrect_account_type(self):
        self.account1.deposit('100.00')
        self.assertEqual(
            self.account1.transfer('Not an Account(), but a string', '123.45'),
            'Receiving account must be an instance of class Account().'
        )

    def test_atm_account_transfer_to_another_account_zero_amount(self):
        self.account1.deposit('100.00')
        self.assertEqual(
            self.account1.transfer(self.account2, '0.00'),
            'Transfer amount must be larger than $0.00.'
        )
    def test_atm_account_transfer_to_another_account_negative_amount(self):
        self.account1.deposit('100.00')
        self.assertEqual(
            self.account1.transfer(self.account2, '-50.00'),
            'Transfer amount must be larger than $0.00.'
        )

    def test_atm_account_transfer_to_another_account_with_positive_remaining_balance_in_both_accounts(self):
        self.account1.deposit('500.00')
        # self.account2's balance is zero by default
        self.account1.transfer(self.account2, '123.45')
        self.assertEqual(
            self.account1.get_balance(),
            'Your balance is $376.55.'
        )
        self.assertEqual(
            self.account2.get_balance(),
            'Your balance is $123.45.'
        )

    def test_atm_account_transfer_to_another_account_results_in_zero_remaining_balance_in_originating_account(self):
        self.account1.deposit('100.00')
        # Transfer the maximum current balance
        self.account1.transfer(self.account2, '100.00')
        # Assert that transfer completed successfully
        self.assertEqual(
            self.account1.get_balance(),
            'Your balance is $0.00.'
        )
        self.assertEqual(
            self.account2.get_balance(),
            'Your balance is $100.00.'
        )

    def test_atm_account_transfer_to_another_account_would_result_in_negative_remaining_balance_and_returns_message(self):
        self.account1.deposit('100.00')
        self.account2.deposit('100.00')
        # Attempt to transfer more than current balance, return warning message
        self.assertEqual(
            self.account1.transfer(self.account2, '200.99'),
            f'You can transfer a maximum amount of ${self.account1.balance}.'
        )
        # Assert that transfer did not complete
        self.assertEqual(
            self.account1.get_balance(),
            'Your balance is $100.00.'
        )
        self.assertEqual(
            self.account2.get_balance(),
            'Your balance is $100.00.'
        )

    def test_atm_account_withdraw_daily_limit_resets_at_midnight_tonight(self):
        # Make a deposit, then max out today's daily withdrawal limit
        self.account1.deposit('500.00')
        self.account1.withdraw('150.00')
        self.account1.withdraw('150.00')
        # Confirm that today's daily withdrawal limit has been reached
        self.assertEqual(
            self.account1.withdraw('5.00'),
            (
                f'Daily withdrawal limit reached. '
                f'Please try again on {self.tomorrows_date}.'
            )
        )
        # Failed attempt to _reset_daily_limit before midnight
        self.assertEqual(
            self.account1._reset_daily_limit(),
            (
                f'Please reset the daily withdrawal limit on '
                f'{(self.account1.todays_date + datetime.timedelta(days=1)).strftime("%b %d, %Y")}.'
            )
        )
        # Mock the date as tomorrow, calling _reset_daily_limit() on a new day.
        self.account1.todays_date += datetime.timedelta(days=1)
        self.account1._reset_daily_limit()
        # Make a withdrawal on a new day
        self.account1.withdraw('5.00')
        # Assert that transfer completed successfully
        self.assertEqual(
            self.account1.get_balance(),
            'Your balance is $195.00.'
        )


if __name__=='__main__':
    unittest.main()
