import unittest
import decimal
from decimal import Decimal as D
from atm import Account


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.account1 = Account('Sally', 'Smith')
        self.account2 = Account('Sam', 'Jones')

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
        self.assertEqual(self.account1.get_balance(), D('0.00'))
        self.assertEqual(self.account2.get_balance(), D('0.00'))

    def test_atm_account_deposit_positive_amount_passes(self):
        self.account1.deposit('0.01')
        self.assertEqual(self.account1.get_balance(), D('0.01'))
        self.account2.deposit('99999999999999999.95')
        self.assertEqual(self.account2.get_balance(), D('99999999999999999.95'))

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
        self.assertEqual(self.account1.get_balance(), D('1010.00'))

    # test_atm_account_withdraw_results_in_negative_balance_and_charges_overdraft_fee

    # test_atm_account_withdraw_daily_limit_in_one_withdrawal

    # test_atm_account_withdraw_would_exceed_daily_limit_in_one_withdrawal

    # test_atm_account_withdraw_would_exceed_daily_limit_over_multiple_withdrawals

    # test_atm_account_withdraw_daily_limit_resets_after_midnight_tonight

    # test_atm_account_withdraw_zero_dollars_returns_message

    # test_atm_account_withdraw_negative_amount_returns_message

    # test_atm_account_withdraw_custom_amount_with_acceptable_denomination

    # test_atm_account_withdraw_custom_amount_with_unacceptable_denomination_returns_message

    # test_atm_account_withdraw_fifty_dollars_in_fives

    # test_atm_account_withdraw_fifty_dollars_in_tens

    # test_atm_account_withdraw_fifty_dollars_in_fifties

    # test_atm_account_withdraw_one_hundred_dollars_in_fifties

    # test_atm_account_withdraw_twenty_dollars_in_fives

    # test_atm_account_withdraw_twenty_dollars_in_tens

    # test_atm_account_withdraw_twenty_dollars_in_twenties

    # test_atm_account_withdraw_one_hundred_dollars_in_twenties

    # test_atm_account_withdraw_ten_dollars_in_fives

    # test_atm_account_withdraw_ten_dollars_in_tens

    # test_atm_account_withdraw_one_hundred_dollars_in_tens

    # test_atm_account_withdraw_five_dollars_in_fives

    # test_atm_account_withdraw_one_hundred_dollars_in_fives

    # test_atm_account_transfer_to_another_account_with_positive_remaining_balance

    # test_atm_account_transfer_to_another_account_would_result_in_negative_remaining_balance_and_returns_message


if __name__=='__main__':
    unittest.main()
