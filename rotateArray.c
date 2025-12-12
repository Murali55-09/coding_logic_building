//Given an array of integers arr[] of size n, the task is to rotate the array elements to the left by d positions
//ex: Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
// Output: {3, 4, 5, 6, 1, 2}
// Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and after the second rotation, arr[] becomes {3, 4, 5, 6, 1, 2}

// method 1: rotate one by one suppose d=2 --> [2,3,4,53,2] ==> [3,4,53,2,2] ==> [4,53,2,2,3] rotate one by one o(n*d), o(1)

//method 2: using temp array: put the array n-d elements from last of ariginal arr in temp and, d elements from first in the original in the temp ,
// then copy the temp to original o(n), o(n)

//method 3: reverse the first d elements and then reverse the n-d elements from the last 

// d = d % n --> for checking d > n then do modulus

#include<stdio.h>

void reverse(int arr[], int start, int end){
    while(start < end){
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}


int main(){
    int arr[] = {1, 4, 2, 5, 7, 8, 9};
    int n = sizeof(arr)/sizeof(arr[0]);
    int d = 3;

    //reversing the first d elements
    reverse(arr, 0, d-1);  // we are passing the refernce of the array to the function not a copy

    //reversing the last n-d elements
    reverse(arr, d, n-1);

    //reversing the whole array
    reverse(arr, 0, n-1);

    //printing the elements
    for(int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    
    return 0;

}



