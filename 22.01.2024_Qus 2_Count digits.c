// 22.01.2024_Qus 2_Count digit
/*Given an integer N, write a program to count the number of digits in N.

Input Format

Example 1: Input0: N = 12345

Example 2: Input1: N = 8394

Constraints

n <= 10000

Output Format

Output0: 5 Explanation: N has 5 digits

Output1: 4 Explanation: N has 4 digits

Sample Input 0

12345
Sample Output 0

5
*/
//logic 1

#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    int count=0;
    while(n!=0)
    {
        n/=10;
        count++;
        
        
    }
    printf("%d",count);

      
    return 0;
}
