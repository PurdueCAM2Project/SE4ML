#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
/*
  remember to add  -lm
  after gcc for adding the math library needed for exp
 */
double sigmoid(double x)
{
  //             1     
  //   ---------------- 
  //    1  + exp (-x)
  
  double expval = exp(-(double) x);
  return (1 / (1 + expval));
}

void printParameters(double weights[2][4][4], double biases[2][4])
{
  int l, j, k;
  for (l = 0; l < 2; l ++)
    {
      for (j = 0; j < 4; j ++)
	{
	  for (k = 0; k < 4; k ++)
	    {
	      printf("weights[%0d][%0d][%0d] = %f\n",
		     l, j, k, weights[l][j][k]);
	    }
	}
    }
  for (l = 0; l < 2; l ++)
    {
      for (j = 0; j < 4; j ++)
	{
	  printf("biases[%0d][%0d] = %f\n",
		 l, j, biases[l][j]);
	}
    }
}

void evaluate(double weights[2][4][4],
	      double biases[2][4],
	      double inputs[4],
	      double outputs[4],
	      double hidden[4])
{
  int  j, k;
  for (j = 0; j < 4; j ++)
    {
      hidden[j] = biases[0][j];
      for (k = 0; k < 4; k ++)
	{
	  hidden[j] += weights[0][k][j] * inputs[k];
	}
      hidden[j] = sigmoid(hidden[j]);
    }

  for (j = 0; j < 4; j ++)
    {
      outputs[j] = biases[1][j];
      for (k = 0; k < 4; k ++)
	{
	  outputs[j] += weights[1][k][j] * hidden[k];
	}
      outputs[j] = sigmoid(outputs[j]);
    }
}

int main(int argc, char * * argv)
{
  double weights[2][4][4] =
    {
      {
	/*
	  The input layer has only 2 neurons. Thus
	  [0][2][*] and [0][3][*] are all zeros.
	*/
	{0.7, 0.8, 0.8, 0.6},
	{0.5, 0.2, 0.35, 0.25},
	{0, 0, 0, 0},
	{0, 0, 0, 0}
      },
      {
	/*
	  The output layer has only 2 neurons. Thus
	  [1][*][2] and [1][*][3] are all zeros.
	*/
	{0.33, 0.28, 0, 0},
	{0.16, 0.76, 0, 0},
	{0.31, 0.48, 0, 0},
	{0.94, 0.23, 0, 0}
      }
    };
  double biases[2][4] =
    {
      /*
	The output layer has only 2 neurons. Thus
	[1][2] and [1][3] are zeros.
      */
      {0.1, 0.3, 0.5, 0.4},
      {0.27, 0.45, 0, 0}
    };
  double inputs[4] = {0.99, 0.01, 0, 0};
  double hidden[4] = {0};
  double outputs[4] = {0};
  printParameters(weights, biases);
  evaluate(weights, biases, inputs, outputs, hidden);
  printf("outputs[0] = %f, outputs[1] = %f\n",
	 outputs[0], outputs[1]);
  // if the desired gate is AND
  double error = outputs[0]  * outputs[0]  +
    (1 - outputs[1]) * (1 - outputs[1]);
  error *= 0.5;
  printf("For AND, the error is %f\n", error);
  return EXIT_SUCCESS;
}
