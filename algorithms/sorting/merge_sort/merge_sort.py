from typing import List, TypeVar, Optional

class MergeSort:

    def sort(self, array):
        start_index = 0
        end_index = len(array)-1
        return self.merge_sort_helper(array, start_index, end_index)
    
    
    def merge_sort_helper(self, array, start_index, end_index):
        if (end_index - start_index + 1) <= 1:
            return
        
        middle_index = (start_index + end_index) // 2

        self.merge_sort_helper(array=array, start_index=start_index, end_index=middle_index)
        self.merge_sort_helper(array=array, start_index=middle_index+1, end_index=end_index)

        self.merge(array, start_index, middle_index, end_index)

        return array
    
    
    def merge(self, array, start_index, middle_index, end_index):
        left_array = array[start_index : middle_index + 1]
        right_array = array[middle_index+1 : end_index+1]

        index = start_index
        right_index = 0
        left_index = 0

        while left_index < len(left_array) and right_index < len(right_array):
            if left_array[left_index] <= right_array[right_index]:
                array[index] = left_array[left_index]
                left_index += 1
            else:
                array[index] = right_array[right_index]
                right_index += 1
            index += 1

        while left_index < len(left_array):
            array[index] = left_array[left_index]
            left_index += 1
            index += 1

        while right_index < len(right_array):
            array[index] = right_array[right_index]
            right_index += 1
            index += 1
        
