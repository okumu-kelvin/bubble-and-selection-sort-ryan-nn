def selection_sort(arr):
    n=len(arr)

    for i in range (n):
        min_index=i

        for j in range(i + 1, n):
            if arr[j]< arr[min_index]:
                    min_index= j

            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]

name=input("Enter your name: ")
name=name.lower()

char_list=list(name)

selection_sort(char_list)
sorted_string = ''.join(char_list)

print("Sorted string:", sorted_string)