def linear_search(data, target):
    n = len(data)

    for i in range(n):
        if data[i] == target:
            return i

    return -1


data = [12, 7, 25, 18, 30, 9, 21]

print (linear_search(data, 18))
#2
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


# Data yang akan diurutkan
data = [5, 2, 4, 6, 1, 3]

# Menjalankan insertion sort
hasil = insertion_sort(data)

print("Data awal  : [5, 2, 4, 6, 1, 3]")
print("Data akhir :", hasil)