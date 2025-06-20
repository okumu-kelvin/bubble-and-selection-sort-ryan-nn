def bubble_sort(unsorted_list):
    n=len(unsorted_list)

    for i in range(n):

        for index in range(n-i-1):

            if unsorted_list[index]> unsorted_list[index + 1]:

                unsorted_list[index], unsorted_list[index + 1] = unsorted_list[index + 1], unsorted_list[index]

name= input("Enter your name : ")
name=name.lower()
#converts the name inputed to lowercase for accuracy in sorting because the Unicode for lowercase and uppercase vary

char_list=list(name)
#the name inputed is converted into a list of individual characters and stored

bubble_sort(char_list)
#the function is called to run the loop

sorted_list=''.join(char_list)
#here the sorted_list is turned back into a string

print("Sorted string:", sorted_list)