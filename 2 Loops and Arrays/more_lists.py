# More Lists and Loops
# By: Shane Matsushima
# Date: 2025-03-10
#
# CODING CHALLENGE: Complete the functions
#
# Complete the TODO aspects of the code while progressing through each section of lectures

# ======== DO NOT TOUCH =================
num = [2, 4, 3, 8]
# =======================================

# Function sums the integers in the list
# Output should be 17
def sum_list():
    sum = 0
    # ========== START CODING HERE ==========
    # TODO loop through the list and add each element to the variable sum
    for i in range(len(num)):
        sum += num[i]

    # =======================================
    return sum


# Function adds 1 to each element of the list
# Output should be [3, 5, 4, 9]
def add_to_list(lst:list) -> list:
    # ========== START CODING HERE ==========
    # TODO add 1 to each element in the list
    for i in range(len(lst)):
        lst[i] += 1
    # =======================================
    return lst

if __name__ == "__main__":
    print(f"Sum of list is {sum_list()}")
    print(f"List after adding 1 to each element is {add_to_list(num)}")