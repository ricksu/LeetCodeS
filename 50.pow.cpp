// normal solution, will be time exceeded for large numbers

class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;
        double rt = 1;
        int N = n < 0 ? -n : n; 
        for (int i = 0; i < N; i++) {
            rt *= x;
        }
        if (n < 0) {
            rt = 1 /(double) rt;
        }
        return rt;
    }
};


//Better solution
class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0 || x == 1) return 1;
        if (n > 0) {
            if (n % 2 == 0) {
                double temp = myPow(x, n / 2);
                return n > 0 ? (temp * temp) : 1/(temp*temp);
            } else {
                return x * myPow(x, n-1);
            }
            
        } else {
            return myPow(1/x, -(n+1))/x;
        }

    }
};
