//Code writteon on the 12/12/2023
//This sequence can be computed by powering a 2000*2000 matrix 10**18 times
//We use a log complexity algorithm for that matrix power, and make sure all the multiplications are done module 20092010
//There seem to be two imediate impovements ( found on the forums )
// First is to compute twice module the two factors ~10k of 20092010 and use chinese remainder theorem
// The second is to compute A^k for k = 0, 1, ..., 1999 and using Cayley hamilton A^2000 = A+Id
//The forums also invented a great optimization. The matrix A^k can be easily computed only knowing the last column, so we just compute this last column and that's it
// This reduces the complexity to k^2 log n, which allows us to have solutions that run under a minute
//Runs in 67906 seconds



#include <iostream>
#include <ctime>

#define FOR(a, b, c) for(int a = b; a < c; a++)



void PrintMatrix(long long int** mat, int dim){
    FOR(i, 0, dim){
        FOR(j, 0, dim) std::cout << mat[i][j] << " ";
        std::cout << "\n";
    }
}


long long int ProductModule(long long int a, long long int b, long long int MOD){
    long long int m = b;
    long long int n = a;
    long long int ans = 0;
    while(m>0){
        if (m%2 == 1){
            ans += n;
            ans %= MOD;
        }
        n = n << 1;
        n %= MOD;
        m = m >> 1;
    }
    return ans;
}


long long int** ProductMatrix(long long int** mat1, long long int** mat2, long long int MOD, int lag){
    //long long int ans[lag+5][lag+5];
    long long int** ans = 0;
    ans = new long long int*[lag+5];
    FOR(i, 0, lag) ans[i] = new long long int[lag+5];
    FOR(i, 0, lag) FOR(j, 0, lag) ans[i][j] = 0;
    FOR(i, 0, lag) FOR(j, 0, lag) FOR(k, 0, lag){
        ans[i][k] += ProductModule(mat1[i][j], mat2[j][k], MOD);
        ans[i][k] %= MOD;
    }
    return ans;
}

long long int LaggedTerm(int lag, long long int index, long long int MOD){
    clock_t time_req = clock();
    long long int** ans = 0;
    ans = new long long int*[lag+5];
    FOR(i, 0, lag) ans[i] = new long long int[lag+5];
    long long int** mat = 0;
    mat = new long long int*[lag+5];
    FOR(i, 0, lag) mat[i] = new long long int[lag+5];
    //Create the exponent matrix, should start as the identity matrix
    FOR(i, 0, lag) FOR(j, 0, lag) ans[i][j] = 0;
    FOR(i, 0, lag) ans[i][i] = 1;
    //Create original matrix
    FOR(i, 0, lag) FOR(j, 0, lag) mat[i][j] = 0;
    FOR(i, 0, lag-1) mat[i][i+1] = 1;
    mat[lag-1][0] = 1;
    mat[lag-1][1] = 1;
    //PrintMatrix(mat, lag);
    long long int m = index;
    while (m > 0){
        std::cout << m << std::endl;
        std::cout << ((double)(clock() - time_req))/1000 << " seconds" << std::endl;
        if (m%2 == 1) ans = ProductMatrix(ans, mat, MOD, lag);
        m = m >> 1;
        mat = ProductMatrix(mat, mat, MOD, lag);
        //PrintMatrix(mat, lag);
    }
    //PrintMatrix(ans, lag);
    long long int ansValue = 0;
    FOR(i, 0, lag){
        ansValue += ans[0][i];
        ansValue %= MOD;
    } 
    return ansValue;
}



int main(){
    clock_t time_req = clock();
    long long int lag = 2000;
    long long int MOD = 20092010;
    long long int index = 1000000000000000000;

    std::cout << LaggedTerm(lag, index, MOD) << std::endl;
    std::cout << ((double)(clock() - time_req))/1000 << " seconds" << std::endl;
    return 0;
}