#include<stdio.h>

int majorityele(int arr[], int size){
    // int size = sizeof(arr)/sizeof(arr[0]);          // it cant be done here because we passed reference of arr only, not copy of it
    int ele = 0;
    int ele1 = -1, ele2 = -1;
    int cnt1 = 0, cnt2 = 0;

    while(ele < size){
        if(ele1 == arr[ele])
            cnt1 ++;
        
        else if(ele2 == arr[ele])
            cnt2 ++;
        
        else if(cnt1 == 0){
            ele1 = arr[ele];
            cnt1 ++;
        }

        else if(cnt2 == 0){
            ele2 = arr[ele];
            cnt2 ++;
        }

        else{
            cnt1-- , cnt2 -- ;
        }
        ele++;
    }

    int res[2] = {0};
    cnt1 = 0, cnt2 = 0;
    int i = 0;

    while( i < size){
        if(arr[i] == ele1)
            cnt1++;
        
        if(arr[i] == ele2)
            cnt2++;
        i++;
    }

    if(cnt1 > size/3)
        res[0] = ele1;
    
    if(cnt2 > size/3 && ele1 != ele2)
        res[1] = ele2;
    
    int m = sizeof(res)/sizeof(res[0]);

    if(m == 2 && res[0] > res[1]){
        int temp =res[0];
        res[0] = res[1];
        res[1] = temp;
    }

    for( int i =0; i < m; i++){
        printf("%d ", res[i]);
    }
}
int main(){
    int arr[] = {2, 4, 4, 2, 5, 2, 4, 2, 4, 6};
    int size = sizeof(arr)/sizeof(arr[0]);
    majorityele(arr, size);
}