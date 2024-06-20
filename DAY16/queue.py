def find_winner(arr, k):
    current_champion = arr[0]
    win_count = 0

    for challenger in arr[1:]:
        if current_champion > challenger:
            win_count += 1
        else:
            current_champion = challenger
            win_count = 1
        
        if win_count == k:
            return current_champion
    
    # If no element wins k times, return the overall largest element
    return current_champion

# Example usage:
arr = [1, 3, 2, 4, 5]
k = 2
print(find_winner(arr, k))  # Output: 4

# Test with larger input size
import random
large_arr = random.sample(range(1, 100001), 100000)
k = 2
print(find_winner(large_arr, k))
