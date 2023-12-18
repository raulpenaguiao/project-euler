#include <iostream>
#include <vector>
#include <ctime>


#define FOR(a, b, c) for(int a = b; a < c; a++)


int pow2Upperbound(long long int a){
    int counta = 0;
    long long int a1 = a;
    while(a1 > 0){
        a1 = a1 >> 1;
        counta++;
    }
    //std::cout << a << " ,  " << counta << std::endl;
    return counta - 1;
}



long long int xorProduct(long long int a, long long int b){
    if(a < 2){
        if(a == 0) return 0;
        return b;
    }
    long long int ans = xorProduct(a/2, b)*2;
    if(a%2 == 1) ans ^= b;
    return ans;
}

long long int module(long long int a, long long int p){
    //Find largest power if two for a and p;
    int counta = pow2Upperbound(a), countp = pow2Upperbound(p);
    //std::cout << counta << ", " << countp << std::endl;
    //std::cout << a << ", " << p << std::endl;
    if(counta < countp) return a;
    long long int t = p << (counta - countp);
    return module(a^t, p);
}

int main(){
    clock_t time_req = clock();
    int pow = 27;
    int N = 1 << pow, ans, Nsqrt = 1 << ( (pow +1)/ 2 );
    
    std::vector<bool> primeQ;
    FOR(i, 0, N) primeQ.push_back(true);
    //FOR(i ,10 ,20) FOR(j, 10, 20) std::cout << " i = " << i << " and j = " << j << " gives " << xorProduct(i, j) << std::endl;
    //std::cout << module(16, 10);
    //FOR(i ,10 ,20) FOR(j, 10, 20) std::cout << " i = " << i << " and j = " << j << " gives " << module(i, j) << std::endl;
    
    primeQ[0] = false;
    primeQ[1] = false;
    for(int i = 4; i < N; i+=2) primeQ[i] = false;
    for(int i = 3; i < Nsqrt  ; i+= 2) if(primeQ[i]) {
        int LIM = 1 << (pow - pow2Upperbound(i));
        for(int j = i; j < LIM; j+= 2) primeQ[xorProduct(i, j)] = false;
    }
    int count = 0;
    FOR(i, 2, N) if(primeQ[i]){
        count++;
        if(count == 5000000){
            std::cout << i << std::endl;
            std::cout << ((double)(clock() - time_req))/1000 << "seconds" << std::endl;
            return 0;
        } 
    }

    std::cout << "Not found!" << std::endl;
    return 0;
}