
def find_peak_1d_while_loop(array):
    start, end = 0, len(array)

    while True:
        mid = (start + end) // 2

        if mid > 0 and array[mid] < array[mid-1]:
            end = mid
        elif mid + 1 < len(array) and array[mid] < array[mid+1]:
            start = mid
        else:
            return array[mid]

def find_peak_1d_recursive(array):
    start, end = 0, len(array)

    def recursion(start, end):
        mid = (start + end) // 2

        if mid > 0 and array[mid] < array[mid-1]:
            return recursion(start, mid)
        elif mid + 1 < len(array) and array[mid] < array[mid+1]:
            return recursion(mid, end)
        else:
            return array[mid]

    return recursion(start, end)
