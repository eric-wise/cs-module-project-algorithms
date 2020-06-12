'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    counts = {}
    for x in arr:
        if x in counts:
            del counts[x]
        else:
            counts[x] = 1

    return list(counts.keys())[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    # arr = [2, 2, 3, 3, 5, 5, 2, 2, 7]
    # arr = [2, 2, 3, 3, 3, 5, 5, 2, 2, 7]

    print(f"The odd-number-out is {single_number(arr)}")
