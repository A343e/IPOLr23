import random
import datetime

def bubble_sort_descending(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def measure_time(elements):
    lst = random.sample(range(1, elements+1), elements)
    start_time = datetime.datetime.now()
    bubble_sort_descending(lst)
    end_time = datetime.datetime.now()
    return (end_time - start_time).total_seconds()

elements = [10,100,1000,10000,100000]
times = [measure_time(e) for e in elements]

print("Elements\tTime")
for e, t in zip(elements, times):
    print(f"{e}\t{t}")