import pandas as pd
from datetime import datetime
from backend.models.transaction import Transaction

class ChaseParser:
    @staticmethod
    def parse(filepath):
        df = pd.read_csv(filepath)
        transactions = []
        
        # Check which format
        if 'Transaction Date' in df.columns:
            # Credit card format
            for _, row in df.iterrows():
                try:
                    t = Transaction(
                        transaction_date=datetime.strptime(row['Transaction Date'], '%m/%d/%Y'),
                        description=str(row['Description']).strip(),
                        amount=float(row['Amount']),
                        category=str(row.get('Category', 'Other')),
                        bank='Chase'
                    )
                    transactions.append(t)
                except Exception as e:
                    continue
        
        elif 'Posting Date' in df.columns:
            # Checking/debit format
            for _, row in df.iterrows():
                try:
                    date = datetime.strptime(str(row['Posting Date']).strip(), '%m/%d/%Y')
                    amt = float(str(row['Amount']).replace(',', ''))
                    t = Transaction(
                        transaction_date=date,
                        description=str(row['Description']).strip(),
                        amount=amt,
                        category='Other',
                        bank='Chase'
                    )
                    transactions.append(t)
                except:
                    continue
        
        return transactions
