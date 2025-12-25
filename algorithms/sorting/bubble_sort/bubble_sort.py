from typing import Union, List

class BubbleSort:

    def sort(
        self, 
        list: List[Union[int, float]], 
        reverse: bool = False
    ) -> List[Union[int, float]]:
        
        n = len(list)
        for i in range(n - 1, 0, -1):
            for j in range(i):
                if reverse:
                    if list[j] < list[j+1]:
                        list[j], list[j+1] = list[j+1], list[j]
                else:
                    if list[j] > list[j+1]:
                        list[j], list[j+1] = list[j+1], list[j]
        return list