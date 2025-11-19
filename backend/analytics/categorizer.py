from collections import defaultdict

class TransactionCategorizer:
    
    CATEGORY_COLORS = {
        'Food & Drink': '#ef4444',
        'Shopping': '#f59e0b',
        'Gas': '#f97316',
        'Groceries': '#22c55e',
        'Bills & Utilities': '#3b82f6',
        'Entertainment': '#ec4899',
        'Travel': '#8b5cf6',
        'Health': '#06b6d4',
        'Income': '#10b981',
        'Other': '#64748b'
    }
    
    @staticmethod
    def by_category(transactions):
        cats = defaultdict(float)
        for t in transactions:
            if t.is_expense:
                cats[t.category] += abs(t.amount)
        return dict(sorted(cats.items(), key=lambda x: x[1], reverse=True))
    
    @staticmethod
    def monthly(transactions):
        months = defaultdict(lambda: {'spent': 0, 'income': 0})
        for t in transactions:
            key = t.transaction_date.strftime('%Y-%m')
            if t.is_expense:
                months[key]['spent'] += abs(t.amount)
            else:
                months[key]['income'] += t.amount
        return dict(sorted(months.items()))
