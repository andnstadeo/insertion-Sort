def perform_insertion_sort(input_list):
    length = len(input_list)

    for i in range(1, length):
        key = input_list[i]
        j = i - 1

        while j >= 0 and key < input_list[j]:
            input_list[j + 1] = input_list[j]
            j -= 1

        input_list[j + 1] = key

if __name__ == "__main__":
    user_input = input("Enter a list of numbers separated by spaces: ")
    unsorted_list = [int(x) for x in user_input.split()]

    print("Unsorted list:", unsorted_list)
    perform_insertion_sort(unsorted_list)

    print("Sorted list:", unsorted_list)
