import utils

transactions = utils.unpack_json()

transactions_executed = [transaction for transaction in transactions if 'EXECUTED' in transaction.values()]
transaction_dates = [transaction['date'] for transaction in transactions_executed]
transaction_dates.sort(reverse=True)

for i in range(5):
    for item in transactions_executed:
        if item['date'] == transaction_dates[i]:
            print(utils.form_transaction(item))
            print()
            break