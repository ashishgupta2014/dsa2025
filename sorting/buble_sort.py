class BubleSort:

    @staticmethod
    def sort(array):
        for i in range(0, len(array)):
            for j in range(0, len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]


if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    BubleSort().sort(arr)
    print(arr)
