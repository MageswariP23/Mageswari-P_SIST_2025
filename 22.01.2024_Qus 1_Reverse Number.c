//22.01.2024_Qus 1_Reverse Number

/*Given a number N reverse the number and print it.

Example 1: Input: N = 123 Output: 321 Explanation: The reverse of 123 is 321

Example 2: Input: N = 234 Output: 432 Explanation: The reverse of 234 is 432

Input Format

123

Constraints

N <= 1000

Output Format

321

Sample Input 0

123
Sample Output 0

321
/*

//Logic 1
#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    int rem,rev=0;
     while(n!=0)
    {
        rem=n%10;
        rev=rev*10+rem;
        n/=10;
    }
    printf("%d",rev);
   
       

    
    return 0;
}
