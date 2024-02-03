Super explanation ng code:

perform_insertion_sort(input_list) function:
 -> Takes an unsorted list input_list as input.
 -> Sorts the list using the insertion sort algorithm.

Outer loop (for i in range(1, length)):
 -> Iterates through the list, starting from the second element (i = 1) because the first element is considered sorted.

Inner loop (while j >= 0 and key < input_list[j]):
 -> Shifts elements in the sorted portion of the list to the right to make space for the current element (key).
 -> Continues shifting as long as key is smaller than the element to its left and the index j is within bounds.

Inserting the element:
 -> Once the correct position is found, inserts key at input_list[j + 1].

User Input and Execution:
 -> Prompts the user to enter a list of numbers.
 -> Prints the unsorted list.
 -> Calls the perform_insertion_sort function to sort the list.
 -> Prints the sorted list.


Big O Complexity
Time Complexity:
 -> Worst-case: O(n^2) - When the list is in reverse order, the inner loop runs for almost every element, leading to a quadratic time complexity.
 -> Average-case: O(n^2) - The average time complexity is also quadratic, as it involves nested loops.
 -> Best-case: O(n) - When the list is already sorted, the inner loop doesn't run, resulting in a linear time complexity.

Space Complexity:
 -> O(1) - Insertion sort is an in-place algorithm, meaning it doesn't require additional memory for sorting, making it space-efficient.