// Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.

#include<stdio.h>


void main(){
    int arr[] = {1, 3, 4, 1, 6, 8, 3, 1, 6};
    int N  = sizeof(arr)/sizeof(arr[0]);
    int large = arr[0];
    int second_large = -1;

    for(int i = 1 ; i < N; i++){
        if(arr[i] > large){
            second_large = large;
            large = arr[i];
        }

        else if(arr[i] < large  && arr[i] > second_large){
            second_large = arr[i];
        }
    }

    if(second_large == -1){
        printf("No Numbers");
    }
    else{
        printf("%d is the second Largest Number", second_large);
    }
}