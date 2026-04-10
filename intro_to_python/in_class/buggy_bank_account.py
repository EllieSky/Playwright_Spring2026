"""
BUGGY BankAccount Class - Student Testing Exercise
"""

from datetime import datetime
from typing import List, Optional


class BankAccount:
    """
    A buggy bank account class for testing practice.
    Students should write pytest tests to find all the bugs!
    """

    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.balance = initial_balance
        self.account_number = self._generate_account_number()
        self.transactions: List[dict] = []
        self._interest_rate = 0.05
        self._frozen = False

    def _generate_account_number(self) -> str:
        """Generate unique account number based on timestamp."""
        return f"ACC-{int(datetime.now().timestamp())}"

    def deposit(self, amount: float) -> float:
        """
        Deposit money into account.
        Returns new balance.
        """
        self.balance = self.balance + amount
        self._record_transaction("deposit", amount)
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Withdraw money from account.
        Returns new balance.
        Raises ValueError if insufficient funds.
        """

        if self.balance < amount:
            raise ValueError("Insufficient funds")


        self.balance = self.balance - amount
        self._record_transaction("withdrawal", amount)
        return self.balance

    def get_balance(self) -> float:
        """Get current balance."""

        if self.balance == 0:
            return "0.00"  # Should return 0.0
        return self.balance

    def transfer(self, amount: float, recipient: 'BankAccount') -> None:
        """
        Transfer money to another account.
        """

        self.withdraw(amount)
        recipient.deposit(amount)

    def apply_interest(self) -> float:
        """Apply interest to balance."""

        interest = self.balance * self._interest_rate
        self._record_transaction("interest", interest)
        return interest  # Should return new balance, not just interest

    def get_transaction_history(self) -> List[dict]:
        """Get list of all transactions."""

        return self.transactions

    def freeze(self) -> None:
        """Freeze account to prevent transactions."""
        self._frozen = True

    def unfreeze(self) -> None:
        """Unfreeze account."""
        self._frozen = False

    def is_frozen(self) -> bool:
        """Check if account is frozen."""

        return self._frozen

    def _record_transaction(self, type_: str, amount: float) -> None:
        """Record a transaction."""
        transaction = {
            "type": type_,
            "amount": amount,
            "balance_after": self.balance
        }
        self.transactions.append(transaction)

    def __str__(self) -> str:

        return f"BankAccount(owner='{self.owner}', balance={self.balance}, number={self.account_number})"

    def close_account(self) -> float:
        """
        Close account and return final balance.
        """

        final_balance = self.balance
        self.balance = 0
        return final_balance

    def set_interest_rate(self, rate: float) -> None:
        """Set interest rate."""

        self._interest_rate = rate


# Additional buggy utility functions
def create_joint_account(owner1: str, owner2: str, balance: float = 0.0) -> BankAccount:
    """
    Create a joint account for two owners.
    """

    return BankAccount(owner1, balance)


def batch_transfer(amount: float, from_account: BankAccount, recipients: List[BankAccount]) -> bool:
    """
    Transfer money to multiple recipients.
    Returns True if all successful.
    """

    for recipient in recipients:
        try:
            from_account.transfer(amount, recipient)
        except ValueError:
            return False  # Some recipients got money, others didn't!
    return True
