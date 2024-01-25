# 24.01.2024_Qus 1_handshake
# At the annual meeting of Board of Directors of Acme Inc. If everyone attending shakes hands exactly one time with every other attendee, how many handshakes are there?

# Example

# There are  attendees, ,  and .  shakes hands with  and , and  shakes hands with . Now they have all shaken hands after  handshakes.

# Function Description

# Complete the handshakes function in the editor below.

# handshakes has the following parameter:

# int n: the number of attendees
# Returns

# int: the number of handshakes
# Input Format
# The first line contains the number of test cases .
# Each of the following  lines contains an integer, .

# Constraints



# Sample Input

# 2
# 1
# 2
# Sample Output

# 0
# 1
#Logic

def handshakes(n):
    return n * (n - 1) // 2


test_cases = int(input())
for _ in range(test_cases):
    attendees = int(input())
    result = handshakes(attendees)
    print(result)