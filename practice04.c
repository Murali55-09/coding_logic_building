// Reverse a Array

#include<stdio.h>
#define N 10

void main(){
    int array[N] = {1, 3, 4, 5, 2, 5, 7, 6, 9, 4};
    for(int i = N - 1; i >= 0; i--){
        printf("%d ", array[i]);
    }

    // Duplicate Number printing
    

    int number = 0;
    int duplicate[N] = {0};

    printf("Enter the Number\n");
    scanf("%d", &number);           //3453

    int rem = 0;

    while(number>0){
        rem = number % 10;      //3, 5, 4, 3
        if(duplicate[rem] == 1 )        //duplicate[3] == 1(F),  [5] == 1(F), [4] == 1(F), [3] == 1(T)[break out of loop]
            break;
        
        duplicate[rem] = 1;         //duplicate[3] = 1 assigned, [5] = 1, [4] = 1 

        number = number / 10;       // number = 345 then, this goes to  next iteration, 34, 3

    }

    if(number > 0)          //if it contains duplicates, number = 3
        printf("yes");
    else
        printf("No");
}