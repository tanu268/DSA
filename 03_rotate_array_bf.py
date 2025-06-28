# Brute Force - Rotate array one step at a time, k times
# Time: O(n * k), Space: O(1)

def rotate(nums,k):
    n = len(nums)
    k = k % n  # In case K > n

    for _ in range(k):
        last = nums[-1]  # Store last element
        #Shift all elements to the right
        for i in range(n - 1, 0, -1):
            nums[i] = nums[i - 1]
        nums[0] = last # Place last at the start


# Example
nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums)  #Output: [5,6,7,1,2,3,4]

""""
🧠 Algorithmic Use Cases (DSA-flavored):
- Circular Buffers – Used in streaming data, sensor readings, or producer-consumer queues. Array rotation helps simulate the "wrap-around."
- Sliding Window Problems – Sometimes shifting windows over cyclic data requires rotation-like behavior.
- Searching in a Rotated Sorted Array – A classic problem where you apply binary search logic to rotated arrays.
- Load Balancing – Round-robin task assignments often rotate arrays of tasks or workers.
- Game Logic – Shuffling cards, rotating turns, Tetris pieces — all involve array rotations at heart.

🌐 Real-World Applications:
- Music/Beat Sequencers – Rotating note patterns changes starting beats and rhythms.
- Time Scheduling – Employee shifts or duty rosters often need to rotate evenly through participants.
- UI Components – Carousel image viewers or slide shows use array rotations to navigate through items.
- Cryptography – Bit or array rotations can be part of encryption schemes.
- Networking – Data packets in round-robin routers may follow rotation-like structure
"""