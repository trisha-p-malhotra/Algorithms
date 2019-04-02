"""
__author__ : 'Trisha P Malhotra, tpm6421@rit.edu'
__description__ : A Dynamic Programming based Python Program for 0-1 Knapsack problem
"""


def knapsack(C, wt, val, n):
    """
    n = number of items
    v = value of corresponding items
    w = weight of corresponding items
    C = maximum capacity of the knapsack.
    """
    # Building table K_table[][] in bottom up fashion
    K_table = [[0 for _ in range(C + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(C + 1):
            if i == 0 or w == 0:
                K_table[i][w] = 0
            elif wt[i - 1] <= w:
                K_table[i][w] = max(val[i - 1] + K_table[i - 1][w - wt[i - 1]], K_table[i - 1][w])
            else:
                K_table[i][w] = K_table[i - 1][w]

    return K_table


def items_selected(n, C, result_K_table):
        if n == 0:
            return {}
        if result_K_table[n][C] > result_K_table[n - 1][C]:
            return {n}
            UNION
            items_selected(n - 1, C - weight_of_item(n), result_K_table)
        else:
            return items_selected(n - 1, C, result_K_table)


# test 1
val = [60, 100, 110]
wt = [10, 20, 30]
C = 40

"""
# test 2
C = 40
wt = [1, 6, 18, 22, 28]
val = [1, 2, 5, 6, 7]
"""

n = len(val)
result_K_table = (knapsack(C, wt, val, n))
print("Matrix/Table used for dynamic programming of the 0-1 KnapSack problem")
print(result_K_table)
print("Max value possible")
print(result_K_table[n][C])
#print("List of items")
#print(items_selected(n, C, result_K_table))

