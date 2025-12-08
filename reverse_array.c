    // Reverse an array arr[]. Reversing an array means rearranging the elements such that the first element becomes the last, 
    // the second element becomes second last and so on.

    #include<stdio.h>

    void reverseingroup(int group[], int k, int N){
        for(int i = 0; i < N; i+=k){
            int left = i;
            int right = left + k - 1;
            if(right >= N)
                right = N - 1;
            
            while(left < right){
                int temp = group[left];
                group[left] = group[right];
                group[right] = temp;
                left++;
                right--;
            }
        }

    }


    int main(){
        int arr[] = {1, 2, 5, 1, 2, 21, 7, 2};
        int N = sizeof(arr)/sizeof(arr[0]);
        int k = 4;

        printf("Exact Array\n");
        for (int i = 0; i < N; i++){
            printf("%d ", arr[i] );
        }

        printf("\nAfter Reverse\n");
        for (int i = N - 1; i >= 0; i--){
            printf("%d ", arr[i] );
        }

        reverseingroup(arr, k, N);      //function call

        printf("\nGroup reverse\n");
        
        for(int i = 0; i < N; i++){
            printf("%d ", arr[i]);
        }
    }

    // Given an array arr[] and an integer k, find the array after reversing every subarray of consecutive k elements in place. 
    // If the last subarray has fewer than k elements, reverse it as it is. Modify the array in place, do not return anything.



