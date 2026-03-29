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
    lined=[
        "Alice,100,Calgary,1",      # suspicious with Edmonton one
        "Alice,200,Edmonton,8",     # suspicious with Calgary one
        "Bob,10000,Toronto,3",      # suspicious because amount >= 10000
        "Bob,50,Toronto,5",         # same city, okay
        "Charlie,500,Vancouver,2",  # okay
        "Charlie,600,Montreal,20"   # different city but outside 10 hours, okay
        ]
   
    results = sorted(findFraudulentTransactions(lined))
    for transaction in results:
        print(transaction)

    
    with open("input.txt", "r") as filename:
        lines = filename.readlines()


if __name__ == "__main__":
    main()