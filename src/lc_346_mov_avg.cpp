#include <iostream>
#include <queue>

#include <iomanip>

using std::cout;
using std::queue;

class MovingAverage {

    int win_size;
    int numerator;
    int denominator;
    double mov_avg;
    queue<int> q;
    

public:
    MovingAverage(int size) {
        win_size    = size;
        numerator   = 0;
        denominator = 0;
        mov_avg     = 0.0;
        
    }
    
    double next(int val) {
        if( denominator < win_size){
            
            numerator   += val;
            denominator += 1;

            q.push(val);
            
            mov_avg = ( static_cast<double>(numerator) / denominator);

            cout << "Denominator: " << denominator << std::endl;

            return mov_avg;
        }
        else{
            //
            q.push(val);

            mov_avg = mov_avg - ( static_cast<double>(q.front()) / win_size) + ( static_cast<double>(val) / win_size);

            q.pop();

            return mov_avg;
        }
        
        return 1.0;
    }
};
