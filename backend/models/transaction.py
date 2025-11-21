from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

class NecessityLevel:
    NEEDS = "Needs"
    WANTS = "Wants"
    SAVINGS = "Savings"
    UNKNOWN = "Unknown"

class RecurrenceType:
    SUBSCRIPTION = "Subscription"
    RECURRING = "Recurring"
    ONE_TIME = "One-time"
    UNKNOWN = "Unknown"

@dataclass
class Transaction:
    transaction_date: datetime
    post_date: datetime
    description: str
    amount: float
    category: str
    bank: str
    type: Optional[str] = None
    necessity: str = field(default=NecessityLevel.UNKNOWN)
    recurrence: str = field(default=RecurrenceType.UNKNOWN)
    
    def to_dict(self):
        return {
            'transaction_date': self.transaction_date.strftime('%Y-%m-%d'),
            'description': self.description,
            'amount': self.amount,
            'category': self.category,
            'bank': self.bank,
            'necessity': self.necessity,
            'recurrence': self.recurrence
        }
    
    @property
    def month_year(self):
        return self.transaction_date.strftime('%Y-%m')
    
    @property
    def is_expense(self):
        return self.amount < 0
    
    @property
    def is_income(self):
        return self.amount > 0
