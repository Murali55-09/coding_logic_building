// The cost of stock on each day is given in an array price[]. 
// Each day you may decide to either buy or sell the stock i at price[i],
// you can even buy and sell the stock on the same day. Find the maximum profit that you can get.

// approach 1: take two variables localmin and localmax assign them  with array[0] initially, then iterate through array to find the 
// localmin's and localmax's in the array if it finded then calculate profit = localmin - localmax

#include<stdio.h>

void maxprof(int arr[], int n){
    int localmin = arr[0];
    int localmax = arr[0];
    int profit = 0;
    int i = 0;
    
    while (i < n -1){

        while (i < n && arr[i] >= arr[i + 1])
            i++;
        localmin = arr[i];

        while (i < n && arr[i] <= arr[i + 1])
            i++;
        localmax = arr[i];

        profit += (localmax - localmin);
    }

    printf("Profit : %d ", profit);
}


int main(){
    int array[] = {100, 120, 210, 80, 50, 90, 250};
    int  n = sizeof(array)/sizeof(array[0]);
    maxprof(array, n);
}