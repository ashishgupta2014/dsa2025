class SelectionSort:

    @staticmethod
    def sort(array):
        for i in range(0, len(array) - 1):
            k = i+1
            min_num = array[i]
            for j in range(k, len(array)):
                if min_num > array[j]:
                    k = j
                    min_num = array[j]
            array[i], array[k] = array[k], array[i]

    def recursion(self, array, i=0):
        n = len(array)
        if i >= n - 1:
            return
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        self.recursion(array, i + 1)


if __name__ == "__main__":
    arr = [13, 46, 24, 52, 9, 9]
    SelectionSort().sort(arr)
    print(arr)
    arr = [13, 46, 24, 52, 9, 9]
    SelectionSort().recursion(arr)
    print(arr)

