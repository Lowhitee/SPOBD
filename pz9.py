from fuzzywuzzy import fuzz
from fuzzywuzzy import process
def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n], 'levenstein'

print(levenstein('arraay', 'arraay'))

def fuzzywuzzi(a, b):
    return fuzz.ratio(a, b) , 'fuzzy'
print(fuzzywuzzi('arraay', 'arraay'))
print(fuzzywuzzi('arraay1', 'arraay'))
print(fuzzywuzzi('arraay1', 'arraay1'))

