
//IT'S NOT BEHAVING QUITE RIGHT


#include <stdio.h>
//#include <supporting.h>

#define n 8
int main(void) {
  //hyperparameter
  const float dx = 4.5;


  //MUST BE SORTED
  //THERE IS A WAY TO GET AROUND HAVING TO SORT IT THOUGH
  float t_x[n] = {0, 1, 2, 5, 4.1, 5.8, 6.2, 9};
  float t_y[n] = {1, 6, 5.5, 8, 4, 3.3, 3.2, 2};

  float min_x = 0;
  float max_x = 9;
  float range = max_x - min_x; 

  //Each element of the slope set is represented by 1 dx, where index 0 = 1 * dx
  int num_of_slopes = (int)(range/dx + 0.5);
  printf("%i\n", num_of_slopes);
  float slopes[num_of_slopes];


  //train
  int index_left_off = 0;
 for(int i = 1; i <= num_of_slopes; i++){

   float total_slope = 0;
   int number_of_points = 0;
   while(t_x[index_left_off] <= dx * i){
     
      float slope;
     if(index_left_off != n){
        slope = (t_y[index_left_off+1] - t_y[index_left_off]) / (t_x[index_left_off+1] - t_x[index_left_off]);
     } 

     total_slope += slope;

      index_left_off++;
     number_of_points++;
   }

   slopes[i] = total_slope / number_of_points; //average

 }
printf("%i\n", index_left_off);

  for(int i = 0; i < num_of_slopes; i++){
    printf("%f,", slopes[i]);
  }

  
  return 0;
}