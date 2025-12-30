# Merge Sort

Merge Sort is a divide-and-conquer sorting algorithm. It works by recursively splitting an array into smaller subarrays, sorting each subarray, and then merging them back together in sorted order.

Unlike simpler algorithms such as Bubble Sort, Merge Sort is efficient and performs well on large datasets.

---

## Time Complexity

- Worst case: O(n log n)
- Average case: O(n log n)
- Best case: O(n log n)

Merge Sort provides consistent performance regardless of the initial ordering of elements.

---

## Space Complexity

- Space: O(n)

This implementation uses additional memory during the merge step to store temporary subarrays.

---

## How Merge Sort Works

Given an array of n elements:

1. If the array contains one or zero elements, it is already sorted.
2. Split the array into two halves.
3. Recursively apply Merge Sort to the left half.
4. Recursively apply Merge Sort to the right half.
5. Merge the two sorted halves back into the original array by comparing elements.
6. Repeat until the entire array is sorted.

Each merge operation places elements back into the array in sorted order.

---

## Key Characteristics

- In-place: No (uses temporary subarrays during merging)
- Stable: Yes (maintains the relative order of equal elements)
- Comparison-based: Yes
- Best used for: Large datasets and scenarios requiring predictable performance

---

## Notes on This Implementation

- The algorithm sorts the input array using index-based recursion.
- Temporary arrays are created during each merge step.
- The final sorted array is returned after all recursive calls complete.