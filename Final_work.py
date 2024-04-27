def filter_strings(arr):
    new_arr = []
    for s in arr:
        if len(s) <= 3:
            new_arr.append(s)
    return new_arr

# Пример использования
initial_array = ["apple", "banana", "cat", "dog", "elephant"]
filtered_array = filter_strings(initial_array)
print(filtered_array)
