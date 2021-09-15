
class BinarySearch:

    def __init__(self):
        pass

    def vanilla_binary_search(self, sorted_input: list, key: int) -> bool:
        if not sorted_input:
            sorted_input = self.sorted_input

        left, right = 0, len(sorted_input)-1

        while left <= right:
            m = (right + left) // 2
            if sorted_input[m] == key:
                return True
            elif key < sorted_input[m]:
                right = m-1
            else:
                left = m+1

        return False

bs = BinarySearch()
print(bs.vanilla_binary_search([1,2,3,4,5,6,7,8,9], 1))