# Create class for ATM Account object

    # Initialize ATM Account object
        # Account holder first name passed as parameter
        # Account holder last name passed as parameter
        # Initial balance attribute passed as parameter
            # Initial balance defaults to $0.00
        # Daily withdrawal limit is $300.00

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
