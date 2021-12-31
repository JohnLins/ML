#include <stdio.h>
#include <math.h>

void printList(float *list, int len){
    
    for(int i = 0; i < len; i++){
        
        printf("%f ", list[i]);
    }
    printf("\n");
}

int main()
{
  
  
  //training data
  
  //three examples of a
  float a[3][25] = {
    {0, 1, 0, 0, 0,        0, 1, 0, 0, 0,   ,  0, 1, 0, 0, 0,       0, 1, 0, 0, 0,    0, 1, 0, 0, 0},
    {0, .9, .1, 0, 0,     .1, .8, 0, 0, 0,     0, .9, .1, 0, 0,    .2, .8, 0, 0, 0,   0, 1, 0, 0, 0},
    {0, .7, .2, .1, 0,     0, .9, .3, 0, 0,     .1, 1, .1, 0, 0,    0, .9, 0, 0, 0,   0, 1, 0, 0, 0}
    
  };
    
    //vertical line on left
  
  
  //three examples of b
  float b[3][25] = {
    {0, 0, 0, 1, 0,       0, 0, 0, 1, 0,       0, 0, 0, 1, 0,     0, 0, 0, 1, 0,   0, 0, 0, 1, 0},
    {0, .2, .1, .9, 0,    0, 0, 0, .7, 0,     0, 0, 0, .9, .1,    0, 0, 0, .8, 0,   0, 0, 0, .9, 0},
    {0, 0, .1, .9, 0,     0, 0, 0, 1, .1,     0, 0, .1, 1, 0,     0, 0, 0, 1, 0,    0, 0, .1, .9, .1}
    
  };
    
    //vertical line on right
  
  
  //average a
  float averA[25];
 
  for(int i = 0; i < 25; i++){
    averA[i] = (a[0][i] + a[1][i] + a[2][i])/3;
  }
  
    printList(averA, 25);
  
  //average b
  float averB[25];
  for(int i = 0; i < 25; i++){
    averB[i] = (b[0][i] + b[1][i] + b[2][i])/3;
  }
  
    printList(averB, 25);
  
  
 //test
 float test[25] = {.2, .9, 0, 0, 0,     0, .9, 0, 0, 0,     0, .9, .1, 0, 0,    .1, .9, 0, 0, 0,   0, .9, 0, .1, 0};
 
 //check Euclidean distance
    float tempA = 0;
    float tempB = 0;
 for(int i = 0; i < 25; i++){
    tempA += powf( (test[i] - averA[i]) , 2 );
     
    tempB += powf( (test[i] - averB[i]) , 2 );
 }
    
    float distanceToA = sqrtf(tempA);
    float distanceToB = sqrtf(tempB);
    
    
    //should be closer to A
    printf("A: %f", distanceToA);
    printf("B: %f", distanceToB);
 
  return 0;
}