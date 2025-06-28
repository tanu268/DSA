# Brute Force Approach
# 1. Traverse and collect all non-zero elements in a new list
# 2. Count number of zeros
# 3. Append that many zeros at the end
# 4. Copy back to original array

def move_zeroes_brute(nums):
    result = []
    count_zeros = 0

    for num in nums:
        if num != 0:
            result.append(num)
        else:
            count_zeros += 1

    result += [0] * count_zeros  # Append required zeros

    # Copy result back to original array
    for i in range(len(nums)):
        nums[i] = result[i]

# Main function for brute
def main():
    nums = [0, 1, 0, 3, 12]
    temp = nums[:]  # create a copy to test
    move_zeroes_brute(temp)
    print("After moving zeroes (brute):", temp)

if __name__ == "__main__":
    main()



"""
Nice one, Tanu! The **"move zeroes"** problem is another gem that shows up both in interviews (DSA world) and in the real world. Let’s break it down for both sides:

---

### 🧠 **DSA Applications** (Interview & Algorithm World)
1. **In-Place Array Rearrangement**  
   Classic problem: move all zeroes to the end while keeping the order of non-zero elements. Solved with two pointers in O(n) time.

2. **Partitioning Arrays**  
   It helps practice element segregation techniques, similar to Dutch National Flag or QuickSort partition logic.

3. **Space Optimization**  
   Encourages solutions without using extra space—great for refining your array manipulation chops.

4. **Streaming Data Structures**  
   Useful in maintaining active (non-zero) elements in memory buffers while "pushing out" inactive ones.

---

### 🌍 **Real-World Applications**
1. **Sparse Data Cleanup**  
   In data analysis or machine learning, zeroes often represent missing or irrelevant values. "Moving them" means filtering out the signal from the noise.

2. **Game Development**  
   Think of grid-based games (like 2048)—you move tiles (non-zeroes) while pushing zeroes away. It’s core logic!

3. **UI & Frontend State Management**  
   Zeros can represent "empty slots" in lists or carousels—shifting them to the end makes the interface more intuitive.

4. **Inventory Systems**  
   Items with quantity zero may need to be pushed to the end when displaying product lists.

5. **Memory & Cache Simulation**  
   Zeroes can signify unused memory slots—organizing arrays helps in simulating memory defragmentation or LRU logic.

---

It’s pretty cool how a small idea like moving zeroes touches everything from games to data pipelines.
"""
