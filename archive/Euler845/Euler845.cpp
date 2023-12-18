#include <iostream>
#include <math.h>
#include <cmath>
#include <vector>
#include <ctime>
#include "CL_BigInt.h"


#define FOR(i, a, b) for(int i = a; i < b; i++)
#define sLIM 100000

BigInt binom[100][100];
bool primeQ[sLIM];

int sign(BigInt a){
    if(a%2 == 0) return 1;
    return -1;
}

BigInt Binom(BigInt a, BigInt b){
    if(a < 0 || b > a) return 0;
    return binom[a][b];
}

BigInt G(int N, BigInt k){// numbers < 10^N that have digit sum = k
    if(k <= 0 || N <= 0){
        if( k == 0 && N >= 0) return 1;
        return 0;
    }
    BigInt ans = 0;
    FOR(i, 0, N+1) ans += sign(i)*Binom(N, i) * Binom(N+k-10*i-1, N - 1);
    return ans;
}


std::vector<BigInt> digits(BigInt n, int base = 10){
    if (n < base){
        std::vector<BigInt> digs;
        digs.push_back(n);
        return digs;
    }
    std::vector<BigInt> digs = digits(n/base);
    digs.push_back(n%10);
    return digs;
}

BigInt F(BigInt M, BigInt a){//number of integers n < M such that d(n) == a
    std::vector<int> digs = digits(M);
    int l = digs.size();
    BigInt ans("0");
    int currsum = 0;
    FOR(i, 0, l) FOR(j, 0, digs[i]){
        ans += G(l-i-1, a - currsum);
        currsum++;
    }
    return ans;
}


int sumList(std::vector<int>  lst){
    int ans = 0;
    FOR(i, 0, lst.size()) ans += lst[i];
    return ans;
}

int f(int N, int k){
    int ans = 0;
    FOR(i, 1, N) if(sumList(digits(i)) == k) ans++;
    return ans;
}

BigInt pdsBelow(BigInt input, bool verbose = false){ // gives the number of integers below input that have a prime digit sum
    BigInt ans("0");
    int nDigs = digits(input).size();
    FOR(i, 1, 9*nDigs+1) {
        if(primeQ[i]){
            ans += F(input, i);
            //if(verbose) std::cout << "Updated with dig sum = " << i << " yielding " << ans << std::endl;
        }
    }
    return ans;
}


int main(){
    clock_t time_req = clock();
    FOR(i, 0, 100)  binom[i][0] = 1;
    FOR(i, 1, 100)  binom[i][i] = 1;
    FOR(i, 2, 100) FOR(j, 1, i) binom[i][j] = binom[i-1][j] + binom[i-1][j-1];
    for(int i = 3; i < sLIM; i+=2) primeQ[i] = true;
    for(int i = 4; i < sLIM; i+=2) primeQ[i] = false;
    primeQ[2] = true;
    for(int i = 3; i*i < sLIM; i +=2 ) if(primeQ[i]) for(int j = i*i; j < sLIM; j += i) primeQ[j] = false;

    //binary search
    BigInt target = 1;
    FOR(i, 0, 8) target *= 10;
    BigInt ubound = target*2, lbound = target, mbound;
    while(pdsBelow(ubound) < target) ubound *=2;
    while(ubound - lbound > 2){
        mbound = (ubound+lbound)/2;
        if(pdsBelow(mbound) < target) lbound = mbound;
        else ubound = mbound;
    }
    //std::cout << lbound << std::endl;
    pdsBelow(lbound, true);
    std::cout << F(BigInt("45009328011709397"), 53) << std::endl;
    //FOR(i, 2, 170) std::cout << i << " - " << sumList(digits(i)) << " - " << pdsBelow(i) << " - " << primeQ[sumList(digits(i))] << std::endl;
    //FOR(i, 2, 170) std::cout << pdsBelow(i) << " + " << primeQ[sumList(digits(i))] << " = ";
    //FOR(i, 2, 40) if(primeQ[sumList(digits(i))]) std::cout << i << " - " ;
    //std::cout << std::endl;
    //FOR(i, 2, 80) if(primeQ[sumList(digits(i))]) std::cout << pdsBelow(i+1) << " - " ;
    //std::cout << std::endl;
    //std::cout << pdsBelow(30, true) << std::endl;

    //FOR(i, 1, 40) FOR(j, 2, 20) std::cout << " (" << i << ", " << j << " ) -> " << F(i, j) << std::endl;
    std::cout << ((double)(clock() - time_req))/1000 << " seconds" << std::endl;
    return 0;
}