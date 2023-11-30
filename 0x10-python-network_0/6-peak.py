def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""

    # Edge case: Empty list
    if not list_of_integers:
        return None

    # Perform binary search-like approach
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Check if mid is a peak
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
