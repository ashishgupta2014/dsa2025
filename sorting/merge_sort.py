class MergeSort:

    def sort(self, array):
        self.divide(array, 0, len(array))

    @staticmethod
    def merge(array, start, mid, end):
        left = array[start:mid]
        right = array[mid:end]
        i = j = 0
        k = start

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    def divide(self, array, start, end):
        if end - start > 1:
            mid = (start + end) // 2
            self.divide(array, start, mid)
            self.divide(array, mid, end)
            self.merge(array, start, mid, end)


if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    MergeSort().sort(arr)
    print(arr)