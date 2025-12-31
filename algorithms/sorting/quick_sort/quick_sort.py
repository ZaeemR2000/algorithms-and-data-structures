class QuickSort:

    def sort(self, array):
        self.quick_sort_helper(array, 0, len(array)-1)
        return array


    def quick_sort_helper(self, arr, start_index, end_index):
        if (end_index - start_index + 1) <= 1:
            return
        
        pivot = arr[end_index]
        index = start_index

        for i in range(start_index, end_index):
            if arr[i] < pivot:
                arr[index], arr[i] = arr[i], arr[index]
                index += 1
        arr[end_index] = arr[index]
        arr[index] = pivot

        self.quick_sort_helper(arr, start_index, index-1)
        self.quick_sort_helper(arr, index+1, end_index)
