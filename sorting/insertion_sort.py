class InsertionSort:

    @staticmethod
    def sort(array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key


if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    InsertionSort().sort(arr)
    print(arr)
    """
    [13, 46, 24, 52, 20, 9] 
    """
