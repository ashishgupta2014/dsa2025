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


if __name__ == "__main__":
    arr = [13, 46, 24, 52, 9, 9]
    SelectionSort().sort(arr)
    print(arr)

