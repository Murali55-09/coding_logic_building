// Given an array of integers arr[] representing a permutation (i.e., all elements are unique and arranged in some order), 
// find the next lexicographically greater permutation by rearranging the elements of the array.
// If such a permutation does not exist (i.e., the array is the last possible permutation), 
// rearrange the elements to form the lowest possible order (i.e., sorted in ascending order).

//method : 1. find the index of  samllest number right to the number from right scan <-- [2, 3, 5, 6, 3, 2] --> here 5 is smallest right to 6,
// return index  call it pivot
// 2. find the smallest number right to pivot ,then swap it ==> [2, 3, 5, 6, 3, 2] ==> [2, 3, 2, 6, 3, 5] 
// 3. then reverse the elements right to the pivot ==> [2, 3, 2, 5, 3, 6] this is finall

//1.find index of smallest
//2.swap with smallest number to the right of pivot
//3.reverse the elements to the right of the pivot,    everyhting except from right

#include<stdio.h>

void reverse(int arr[], int start, int end){
    while (start < end){
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }  
}

int smallestind(int arr[], int size){
    for(int i = size - 2; i >= 0; i--){
        if(arr[i] < arr[i + 1])
            return i;
    }

    return -1;
}

void swapelem(int arr[], int pivot, int n){
    int index = -1;

    // find element just larger than pivot
    for(int i = n - 1; i > pivot; i--){
        if(arr[i] > arr[pivot]){
            index = i;
            break;
        }
    }

    // swap pivot with that element
    int temp = arr[pivot];
    arr[pivot] = arr[index];
    arr[index] = temp;
}

int main(){
    int arr[] = {2, 4, 5, 9, 8, 7};
    int n = sizeof(arr)/sizeof(arr[0]);
    
    int pivot = smallestind(arr, n);

    swapelem(arr, pivot, n);

    reverse(arr, pivot + 1 , n - 1);

    int i = 0;
    while(i < n){
        printf("%d ", arr[i]);
        i++;
    }

}