// Reverse an array arr[]. Reversing an array means rearranging the elements such that the first element becomes the last, 
// the second element becomes second last and so on.

#include<stdio.h>

void main(){
    int arr[] = {1, 2, 5, 1, 2, 21, 7, 2};
    int N = sizeof(arr)/sizeof(arr[0]);

    printf("Exact Array\n");
    for (int i = 0; i < N; i++){
        printf("%d ", arr[i] );
    }

    printf("\nAfter Reverse\n");
    for (int i = N - 1; i >= 0; i--){
        printf("%d ", arr[i] );
    }
}

