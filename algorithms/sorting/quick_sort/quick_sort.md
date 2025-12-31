# QuickSort Implementation (Python)
QuickSort is a divide-and-conquer sorting algorithm that works by selecting a pivot element, partitioning the array around the pivot, and recursively sorting the subarrays.

---

## How It Works

1. Choose the **last element** of the array as the pivot.
2. Reorder the array so that:
   - All elements smaller than the pivot come before it
   - All elements greater than or equal to the pivot come after it
3. Place the pivot in its correct sorted position.
4. Recursively apply the same process to the left and right subarrays.

This implementation performs the sorting **in-place**, meaning no extra arrays are created.

---

## Algorithm Characteristics

- **Time Complexity**
  - Best Case: `O(n log n)`
  - Average Case: `O(n log n)`
  - Worst Case: `O(n²)` (when the array is already sorted or nearly sorted)

- **Space Complexity**
  - `O(log n)` due to recursion stack (in-place sorting)

---

## Example Usage

```python
from quick_sort import QuickSort

arr = [5, 3, 8, 4, 2, 7, 1, 10]
sorter = QuickSort()
sorted_arr = sorter.sort(arr)

print(sorted_arr)