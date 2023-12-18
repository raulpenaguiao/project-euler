#include <iostream>
#include <ctime>
#include <cmath>
#include <vector>
#include <iomanip>

#define FOR(a, b, c) for(int a = b; a < c; a++)
#define LIM 1000000




bool primeQ[1000010];

int indexAbove(std::vector<int> lst, double target){//Assumes list is ordered in an increasing manner
    int l = 0, h = lst.size();
    if(lst[l] > target) return 0;
    while(l < h - 1){
        int s = (l+h)/2;
        if(lst[s] <= target){
            l = s;
        }
        else{
            h = s;
        }
    }
    return l + 1;
}


int main(){
    clock_t time_req = clock();
    bool verbose = false;
    if(verbose) std::cout << "Primes to be computed!" << std::endl;
    int lim = floor(sqrt(LIM))+1;
    //Sieve primes
    primeQ[0] = false;
    primeQ[1] = false;
    primeQ[2] = true;
    FOR(i, 3, LIM+1) primeQ[i] = (i%2 == 1);
    if(verbose) std::cout << "Primes initialized!" << std::endl;
    for(int i = 3; i * i <= LIM; i+=2) {
        if(verbose) std::cout << "Multiples of " << i << std::endl;
        if(primeQ[i]) for(int k = i*i; k <= LIM; k += 2*i) primeQ[k] = false;
    }

    if(verbose) std::cout << "Primes computed!" << std::endl;
    //Find smallest prime p > lim with p%10 = 7
    int lim7 = lim;
    while(!primeQ[lim7] || lim7%10 != 7) lim7++;
    if(verbose) std::cout << lim7 << std::endl;
    //Find smallest prime p > lim with p%10 = 9
    int lim9 = lim;
    while(!primeQ[lim9] || lim9%10 != 9) lim9++;
    if(verbose) std::cout << lim9 << std::endl;
    
    std::vector<int> primes7, primes9;
    std::vector<double> primes7ACCLOG, primes9ACCLOG;
    double log7 = 0, log9 = 0;
    FOR(i, 3, LIM+1) if(primeQ[i]){
        if(i%10 == 7){
            primes7.push_back(i);
            log7 += log(i);
            primes7ACCLOG.push_back(log7);
        }
        if(i%10 == 9){
            primes9.push_back(i);
            log9 += log(i);
            primes9ACCLOG.push_back(log9);
        }
    }

    double log79 = 0;
    //initialize log79 as the one contaning as few primes 7 as possible
    lim7 = 0;
    while(lim7 < primes7.size() && primes7[lim7]*primes7[lim7]*primes7[lim7] < LIM)  lim7++;
    //Now lim7 is the position of the first prime7 that is not strictly needed
    //We compute the score with this configuration on prime7, plus all the necessary prime9
    double d = LIM;
    if(lim7 > 0){
        d /= primes7[lim7 - 1];
        log79 = primes7ACCLOG[lim7 - 1];
    } else{
        lim7++;
    }
    log79 += primes9ACCLOG[indexAbove(primes9, d + 0.01) - 1];
    // Comparing a double and an int may cause issues with rounding of double, so we give some leeway
    if(verbose) std::cout << std::setprecision(std::numeric_limits<double>::max_digits10) << log79 << std::endl;
    //For each prime7, see how many prime9 are needed to accomplish the condition
    FOR(i, lim7, primes7.size()) {
        double d = LIM;
        d /= primes7[i];
        double newGuess = primes9ACCLOG[indexAbove(primes9, d + 0.01) - 1] + primes7ACCLOG[i - 1];
        if(newGuess < log79) log79 = newGuess;
    }

    //Add the primes3
    FOR(i, 3, LIM+1) if(primeQ[i] && i%10 == 3) log79 += log(i);
    
    std::cout << "Answer = " << std::setprecision(std::numeric_limits<double>::max_digits10) << log79 << std::endl;
    std::cout << ((double)(clock() - time_req))/1000 << " seconds" << std::endl;
    return 0;
}