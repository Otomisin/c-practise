#include <stdio.h>
// https://www.youtube.com/watch?v=Bz4MxDeEM6k&list=PL_c9BZzLwBRKKqOc9TJz1pP0ASrxLMtp2&ab_channel=CalebCurry

int main()
{
    int const col = 3;
    int const row = 2;
    int grades [row][col] = {
        {2, 4, 7},
        {7, 3, 5}
    };

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col ; j++)  
        {
            printf("%d ", grades[i][j]);
        }
    }
    return (0);
}