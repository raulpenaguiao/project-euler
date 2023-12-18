#include <iostream>
#include <math.h>
#include <cmath>
#include <ctime>
#include <tuple>
#include <iomanip>
#include "CL_Arithmetics.h"

#define FOR(a, b, c) for(int a = b; a < c; a++)

long long int sum_b(int N, double K){//This gives the smallest number of steps so that all elements in the list are above e^2^K
    long long int ans = 0;
    FOR(a, 2, N+1) ans += ceil(K - log2(log(a)));
    return ans;
}


long double tiro(int N, long long int M){//This gives log2(log(min({2, ..., N}^M)) where {2, ..., N}^M is the set resulting after M operations
    long double uBound = N, lBound = N, mPoint, PREC = .000001;
    while(sum_b(N, uBound) < M ) uBound *= 2; 
    while(sum_b(N, lBound) > M) lBound /= 2;
    while(abs(uBound - lBound) > PREC){
        mPoint = (uBound + lBound ) / 2;
        std::cout << std::setprecision(std::numeric_limits<long double>::max_digits10) << "bounds: " << mPoint << " :: " << sum_b(N, mPoint) << " -- " << lBound << " :: " << sum_b(N, lBound) << " - " << uBound  << " :: " << sum_b(N, uBound) << std::endl;
        if(sum_b(N, mPoint) < M) lBound = mPoint;
        else uBound = mPoint;
    }
    return lBound;
}



int main(){
    clock_t time_req = clock();
    int N = 1;
    FOR(i, 0, 1) N *= 10;
    long long int M = 1;
    FOR(i, 0, 2) M *= 10;
    std::cout << M << ", " << N << std::endl;
    long double x = tiro(N, M);
    //std::cout << sum_b(N, 102.20312910620184) << " :: "  << sum_b(N, 102.20312910620294) << std::endl;
    long long int F = sum_b(N, x);
    std::cout << std::setprecision(std::numeric_limits<long double>::max_digits10) << x << " is reached after " << F << " steps, now we try to reach " << M << std::endl;
    long long int sum = 0, MOD = 1234567891;
    FOR(a, 2, N+1){
        int pow = PowerMod(a, PowerMod(2, ceil(x - log2(log(a))), MOD-1), MOD);
        sum += pow;
        sum %= MOD;
    }
    std::cout << "Current sum is " << sum << std::endl;

    //Find smallest element of the list after F steps
    long double min = x+1.0001;
    int argmin = 1;
    FOR(a, 2, N+1) if(min > log2(log(a)) + ceil(x - log2(log(a)))) {
        min = ceil(x - log2(log(a))) + log2(log(a));
        argmin = a;
    }
    std::cout << argmin << " is the smallest with power " << ceil(x - log2(log(argmin))) << std::endl;

    long long int smallest_power = PowerMod(argmin, PowerMod(2, ceil(x - log2(log(argmin))), MOD-1), MOD);
    std::cout << smallest_power << " is the power " << (smallest_power*smallest_power)%MOD << " the square." << std::endl;
    sum += ((M - F + MOD)%MOD)*(((smallest_power*smallest_power)%MOD - smallest_power + MOD)%MOD);
    sum %= MOD;

    std::cout << "Total sum = " << sum << std::endl;
    std::cout << ((double)(clock() - time_req))/1000 << " seconds" << std::endl;
    return 0;
}