# Brute Force Solution - Check all rotations
# Time: O(n^2), Space: O(n)

def check(nums):
    n = len(nums)

    # Try every possible rotation
    for i in range(n):
        # Rotate the array by i positions
        rotated = nums[i:] + nums[:i]   # for left rotation
        '''rotated = nums[-i:] + nums[:-i]   --for right
'''

        if all(rotated[j] <= rotated[j + 1] for j in range(n - 1)):
            return True  # This rotation is sorted!
    return False  # None of the rotations resulted in a sorted array

# Example Test Cases
print(check([3, 4, 5, 1, 2]))  # True
print(check([1, 2, 3]))        # True
print(check([2, 1, 3, 4]))     # False



"""
Array rotation might sound like a niche operation, but it's surprisingly useful across a bunch of real-world scenarios! Here are a few places where it shines:

1. **Data Structures**  
   In circular buffers or queues (used in audio/video streaming, scheduling, etc.), rotation helps efficiently manage the "wrap-around" behavior when the structure reaches its capacity.

2. **Cryptography**  
   Some encryption algorithms use array or bit rotation as part of their encoding techniques to obfuscate data.

3. **Image Processing**  
   Pixels or color channels might be rotated to apply filters or transformations, especially in operations like image rotation or scanning line shifts.

4. **Game Development**  
   Think of games like Tetris or Rubik’s Cube simulators—rotating arrays helps represent moving pieces or shifting rows and columns.

5. **Simulating Rotating Systems**  
   For time-based simulations (like rotating duty rosters or seating arrangements), array rotation can shift elements without rebuilding the entire structure.

6. **Load Balancing & Scheduling**  
   When distributing tasks or resources in a round-robin fashion, rotating the array of servers or people ensures fairness and efficiency.

7. **Music & Rhythm Software**  
   In beat sequencing or pattern loops, rotating arrays can change the starting point of rhythms or alter musical timing.


"""
