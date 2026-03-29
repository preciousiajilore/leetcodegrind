from collections import defaultdict

def findFraudulentTransactions(lines):
    transactions_by_name = defaultdict(list)
     #instantiate where to store the suspicious transactions
    sus = set()

    for idx, line in enumerate(lines):
        #parse by line and then group
        name, amount, city, time = line.strip().split(",")
        amount = float(amount)
        time = int(time)

        if amount >= 10000:
            sus.add(line.strip())
        
        #store them by name
        transactions_by_name[name].append((time, amount, city, idx, line.strip()))

   

    #for each name, look at their transactions and then check
    for name, transactions in transactions_by_name.items():
        transactions.sort(key=lambda x:x[0]) #this way we sort by time

        n = len(transactions)

        for i in range(n):
            time_i, amount_i, city_i, idx_i, line_i = transactions[i]

            for j in range(i+1, n):
                time_j, amount_j, city_j, idx_j, line_j = transactions[j]

                if time_j - time_i > 10:
                    break
                
                if city_i != city_j:
                    sus.add(line_i)
                    sus.add(line_j)
    
    return list(sus)

def main():
    lines=[
        "Alice,12000,New York,100",
        "Alice,8000,Los Angeles,105",
        "Bob,5000,Chicago,110",
        "Bob,15000,Chicago,115",
        "Charlie,7000,Miami,120",
        "Charlie,7000,Miami,125",
        "Charlie,7000,Miami,130",
        "Charlie,7000,Miami,135",
        "Charlie,7000,Miami,140",
    ]
    result = findFraudulentTransactions(lines)
    for transaction in result:
        print(transaction)

if __name__ == "__main__":
    main()