# Bubble Sort

Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. Larger elements "bubble up" toward the end of the list with each pass.

---

## Time Complexity

- **Worst case:** O(n²)
- **Average case:** O(n²)
- **Best case:** O(n) (when the array is already sorted and if early-exit optimization is used)

Bubble Sort is inefficient for large datasets, but it is useful for learning basic sorting concepts.

---

## How Bubble Sort Works

Given an array of `n` elements:

1. Start at index `0` and compare the current element with the next element.
2. If the elements are in the wrong order (greater than for ascending order), swap them.
3. Move to the next index and repeat the comparison.
4. Once the end of the array is reached, the largest element will be in its correct position.
5. Repeat the process for the remaining unsorted portion of the array.
6. Continue until no swaps are needed or until the array is fully sorted.

Each pass places one element in its final position.

---

## Key Characteristics

- **In-place:** Yes (does not require extra memory)
- **Stable:** Yes (does not change the order of equal elements)
- **Comparison-based:** Yes
- **Best used for:** Learning and small datasets