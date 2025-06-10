import timeit
import random

# --- 1. Insertion Sort ---
def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# --- 2. Merge Sort ---
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# --- 3. Timsort (built-in) ---
def timsort(arr):
    return sorted(arr)

# --- Генерація даних ---
def generate_data(size):
    return [random.randint(1, 10000) for _ in range(size)]

# --- Вимірювання часу ---
def measure_time(func, data, repeats=3):
    return timeit.timeit(lambda: func(data), number=repeats) / repeats

# --- Основна логіка ---
def main():
    sizes = [100, 500, 1000, 5000]
    print("{:<10} {:<15} {:<15} {:<15}".format("Size", "Insertion (s)", "Merge (s)", "Timsort (s)"))
    print("-" * 60)
    for size in sizes:
        data = generate_data(size)

        t_insert = measure_time(insertion_sort, data) if size <= 1000 else float('inf')
        t_merge = measure_time(merge_sort, data)
        t_timsort = measure_time(timsort, data)

        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f}".format(size, t_insert, t_merge, t_timsort))

if __name__ == "__main__":
    main()