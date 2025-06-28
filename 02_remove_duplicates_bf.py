#brute force 
#step 1: Traverse and store unique elements in a new list
#step 2: Copy the result back to the original array(if required)
def remove_duplicates(nums):
    result = []
    for num in nums:
        if num not in result:
            result.append(num)

#copy unique elements back to original list (in place style)
    for i in range(len(result)):
        nums[i] = result[i]
    return len(result)

# Main function to test the brute approach
def main():
    nums = [1, 1, 2, 2, 2]
    length = remove_duplicates(nums)
    print("After removing duplicates (brute):", nums[:length])
    print("Length:", length)

if __name__ == "__main__":
    main()


    """"
    Removing duplicates from data might seem like a tidy-up task, but it has some seriously valuable real-world applications. Here’s where it makes a big impact:

1. **Data Cleaning in Analytics**  
   When analyzing customer behavior, survey results, or any large dataset, duplicates can skew results. Cleaning them ensures that every data point counts equally.

2. **Improved Performance**  
   In systems that manage huge amounts of information—like search engines or recommendation systems—removing repeated entries can reduce memory usage and speed things up.

3. **Database Integrity**  
   Databases often use constraints to avoid duplicates (like unique email addresses or IDs). Still, during migrations or merges, deduplication ensures consistency and avoids conflicts.

4. **Email & Notification Systems**  
   You don’t want to email the same user multiple times because their address appears more than once in your list. Deduplication prevents annoyance and reduces costs.

5. **E-commerce and Inventory**  
   Say a product is accidentally listed multiple times—it confuses customers and can lead to over-ordering. Removing duplicates keeps inventory accurate and the catalog clean.

6. **Security and Access Control**  
   Repeated permission entries can cause unpredictable behavior or security risks. Deduplicating user roles or access lists helps maintain clarity and control.

7. **Machine Learning & AI**  
   Training models on duplicate-heavy data can result in biased or overfit models. Clean, unique datasets lead to better generalization and performance.

8. **Social Media & Content Platforms**  
   Deduplicating posts or comments helps stop spam, filter noise, and improve user experience.

It’s like digital decluttering—less noise, better insight. 
"""