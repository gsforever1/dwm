import itertools

# Function to calculate support
def calculate_support(itemsets, transactions):
    support_counts = []
    for itemset in itemsets:
        count = sum(1 for transaction in transactions if all(item in transaction for item in itemset))
        support_counts.append(float(count) / len(transactions))
    return support_counts

# Get user input for minimum support and number of transactions
support_threshold = float(input("Enter the minimum support: "))
items = ['i1', 'i2', 'i3', 'i4', 'i5']  # Items to consider
num_transactions = int(input("Enter number of transactions: "))
transactions = []

# Collect transactions from user
for i in range(num_transactions):
    transaction = input(f"Enter the items bought in transaction {i + 1}, separated by a comma: ").split(',')
    transactions.append([item.strip() for item in transaction])

# Display the transactions
print("\nTransactions are as follows:")
for transaction in transactions:
    print(transaction)

# Candidate set C1 (1-itemsets)
print("\nThe candidate set C1 is:", items)

# Calculate support for all items in candidate set C1
support_c1 = calculate_support([(item,) for item in items], transactions)
for i, item in enumerate(items):
    print(f"Support for {item} is: {support_c1[i]}")

# Generate L1 (frequent 1-itemsets from C1)
l1 = [items[i] for i in range(len(items)) if support_c1[i] >= support_threshold]
print("\nL1 (Frequent 1-itemsets) is:", l1)

# Generate Candidate set C2 (2-itemsets)
c2 = list(itertools.combinations(items, 2))
print("\nCandidate set C2 (2-itemsets) is:", c2)

# Calculate support for all items in C2
support_c2 = calculate_support(c2, transactions)
for i, itemset in enumerate(c2):
    print(f"Support for {itemset} is: {support_c2[i]}")

# Generate L2 (frequent 2-itemsets from C2)
l2 = [c2[i] for i in range(len(c2)) if support_c2[i] >= support_threshold]
print("\nL2 (Frequent 2-itemsets) is:", l2)

# Generate Candidate set C3 (3-itemsets)
c3 = list(itertools.combinations(items, 3))
print("\nCandidate set C3 (3-itemsets) is:", c3)

# Calculate support for all items in C3
support_c3 = calculate_support(c3, transactions)
for i, itemset in enumerate(c3):
    print(f"Support for {itemset} is: {support_c3[i]}")

# Generate L3 (frequent 3-itemsets from C3)
l3 = [c3[i] for i in range(len(c3)) if support_c3[i] >= support_threshold]
print("\nL3 (Frequent 3-itemsets) is:", l3)

# Calculate confidence for L3
confidence = []
for itemset in l3:
    base_item = itemset[0]  # Calculating confidence for the first item in the set
    count_base = sum(1 for transaction in transactions if base_item in transaction)
    count_both = sum(1 for transaction in transactions if all(item in transaction for item in itemset))
    conf = count_both / count_base if count_base > 0 else 0
    confidence.append(conf)

# Print confidence for L3
for i, itemset in enumerate(l3):
    print(f"Confidence for {itemset} is: {confidence[i]}")