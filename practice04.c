// Reverse a Array

#include<stdio.h>
#define N 10

void main(){
    int array[N] = {1, 3, 4, 5, 2, 5, 7, 6, 9, 4};
    for(int i = N - 1; i >= 0; i--){
        printf("%d ", array[i]);
    }
}