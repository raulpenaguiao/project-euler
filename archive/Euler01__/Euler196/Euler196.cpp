//Code written on 2023/11/20
//Possible memory optimisation by sweeping the grid instead of generating it
//Runs in 505.325 seconds



#include <iostream>
#include <ctime>
#include <vector>
#include "CL_Primes.h"

#define FOR(a, b, c) for(long long int a = b; a < c; a++)


long long int f(long long int N){
    //std::cout << " f = " <<  N*(N-1)/2+1 << std::endl;
    return N*(N-1)/2+1;
}


long long int S(long long int N){
    if( N < 5 ){
        if( N == 1 ) return 0;
        if( N == 2 || N == 3) return 5;
        if( N == 3 ) return 7;
        if( N == 4 ) return 24;
    }
    long long int tot = 0;
    std::vector<long long int> rowVecNum;
    FOR(i, 0, N+2) rowVecNum.push_back(0);
    std::vector<std::vector<long long int>> vecNum;
    FOR(i, 0, 5) vecNum.push_back(rowVecNum);

    std::vector<bool> rowPrimeQ;
    FOR(i, 0, N+4) rowPrimeQ.push_back(false);
    std::vector<std::vector<bool>> vecPrimeQ;
    FOR(i, 0, 5) vecPrimeQ.push_back(rowPrimeQ);
    std::vector<std::vector<bool>> vecCenterPrimeQ;
    FOR(i, 0, 5) vecCenterPrimeQ.push_back(rowPrimeQ);
    std::vector<std::vector<bool>> vecBelongsPrimeQ;
    FOR(i, 0, 5) vecBelongsPrimeQ.push_back(rowPrimeQ);

    FOR(i, 0, 5){
        long long int bg =  f(N-2+i), fg = f(N-2+i+1);
        FOR(j, bg, fg){
            vecPrimeQ[i][j-bg+1] = MillerRabin(j);
            vecNum[i][j-bg+1] = j;
        }
    }

    //std::cout << "A";
    FOR(i, 1, 4){
        long long int bg = f(N-2+i), fg = f(N-2+i+1);
        FOR(j, bg, fg) if(vecPrimeQ[i][j-bg+1]){
            int primesAround = 0;
            if(vecPrimeQ[i-1][j-bg+1-1]) primesAround++;
            if(vecPrimeQ[i-1][j-bg+1]) primesAround++;
            if(vecPrimeQ[i-1][j-bg+1+1]) primesAround++;
            if(vecPrimeQ[i][j-bg+1-1]) primesAround++;
            if(vecPrimeQ[i][j-bg+1+1]) primesAround++;
            if(vecPrimeQ[i+1][j-bg+1-1]) primesAround++;
            if(vecPrimeQ[i+1][j-bg+1]) primesAround++;
            if(vecPrimeQ[i+1][j-bg+1+1]) primesAround++;
            if(primesAround > 1) vecCenterPrimeQ[i][j-bg+1] = true;
        }
    }
    //std::cout << "A";
    long long int bg = f(N), fg = f(N+1);
    FOR(j, bg, fg)if(vecPrimeQ[2][j-bg+1]){
        if(vecCenterPrimeQ[1][j-bg+1-1]||vecCenterPrimeQ[1][j-bg+1]||vecCenterPrimeQ[1][j-bg+1+1]||
        vecCenterPrimeQ[2][j-bg+1-1]||vecCenterPrimeQ[2][j-bg+1]||vecCenterPrimeQ[2][j-bg+1+1]||
        vecCenterPrimeQ[3][j-bg+1-1]||vecCenterPrimeQ[3][j-bg+1]||vecCenterPrimeQ[3][j-bg+1+1]){
            tot+= vecNum[2][j-bg+1];
            vecBelongsPrimeQ[2][j-bg+1] = true;
            //std::cout << vecNum[2][j-bg+1] << ", ";
        }
    }
    /*
    FOR(i, 0, 5){
        int count = 0;
        FOR(j, bg, fg) if(vecPrimeQ[i][j-bg+1]) count++;
        std::cout << count << ", ";
        count = 0;
        FOR(j, bg, fg) if(vecCenterPrimeQ[i][j-bg+1]) count++;
        std::cout << count << ", ";
        count = 0;
        FOR(j, bg, fg) if(vecBelongsPrimeQ[i][j-bg+1]) count++;
        std::cout << count << ", ";
        std::cout << std::endl;
    }*/

    return tot;
}



int main(){
    long long int N;
    /*
    while(true){
        std::cin >> N;
        if(MillerRabin(N)){
            std::cout << "Is prime!"<< std::endl;
        }
        else{
            std::cout << "Is not prime."<< std::endl;
        }
    }*/
    clock_t time_req = clock();
    long long int ans = 0;
    ans = S(5678027) + S(7208785) ;
    std::cout << "Answer = " << ans << std::endl;
    std::cout << ((double)(clock() - time_req))/1000 << " seconds" << std::endl;
    /*while(true){
        std::cin >> N;
        clock_t time_req = clock();
        int ans = S(N);
        std::cout << "Answer = " <<  ans << std::endl;
        std::cout << ((double)(clock() - time_req))/1000 << " seconds" << std::endl;
    }*/
    return 0;
}