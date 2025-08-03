class BubleSort:

    @staticmethod
    def sort(array):
        for i in range(0, len(array)):
            for j in range(0, len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]

    def recursive_sort(self, array, n=None):
        if n is None:
            n = len(array)
        if n == 1:
            return

        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        # Recursive call for remaining array
        self.recursive_sort(array, n - 1)


if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    BubleSort().sort(arr)
    print(arr)
    arr = [13, 46, 24, 52, 20, 9]
    BubleSort().recursive_sort(arr)
    print(arr)

