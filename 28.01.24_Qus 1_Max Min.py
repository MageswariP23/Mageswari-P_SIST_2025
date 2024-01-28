#28.01.2024_Qus 1_Max Min

# You will be given a list of integers, , and a single integer . You must create an array of length  from elements of  such that its unfairness is minimized. Call that array . Unfairness of an array is calculated as

# Where:
# - max denotes the largest integer in 
# - min denotes the smallest integer in 

# Example



# Pick any two elements, say .

# Testing for all pairs, the solution  provides the minimum unfairness.

# Function Description

# Complete the maxMin function in the editor below.
# maxMin has the following parameter(s):

# int k: the number of elements to select
# int arr[n]:: an array of integers
# Returns

# int: the minimum possible unfairness
# The first line contains an integer , the number of elements in array .
# The second line contains an integer .
# Each of the next  lines contains an integer  where .

# Constraints




# Sample Input 0

# 7
# 3
# 10
# 100
# 300
# 200
# 1000
# 20
# 30
# Sample Output 0

# 20
# Explanation 0

# Here ; selecting the  integers , unfairness equals

# max(10,20,30) - min(10,20,30) = 30 - 10 = 20

#logic
def maxMin(k, arr):
    arr.sort()
    min_unfairness = float('inf')
    for i in range(len(arr) - k + 1):
        unfairness = arr[i + k - 1] - arr[i]
        min_unfairness = min(min_unfairness, unfairness)

    return min_unfairness

n1 = 7
k1 = 3
arr1 = [10, 100, 300, 200, 1000, 20, 30]

result1 = maxMin(k1, arr1)
print(result1)  

n2 = 10
k2 = 4
arr2 = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]

result2 = maxMin(k2, arr2)
print(result2) 

n3 = 5
k3 = 2
arr3 = [1, 2, 1, 2, 1]

result3 = maxMin(k3, arr3)
print(result3)  


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()