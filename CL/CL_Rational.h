#ifndef CL_Rational
#define CL_Rational

#include <string>
#include "CL_Arithmetics.h"

class Rational{
    long long int numerator, denominator;

    public:
    long long int Numerator(){
        return numerator;
    }
    long long int Denominator(){
        return denominator;
    }

    Rational(long long int n = 0, long long int d = 1){
        numerator = n;
        denominator = d;
    };

    Rational static plus(Rational r, Rational m){
        Rational ans = Rational();
        long long int denom = r.denominator * m.denominator;
        ans.numerator = r.numerator * m.denominator + r.denominator * m.numerator;
        ans.denominator = denom;
        ans.reduce();
        return ans;
    };

    Rational static times(Rational r, Rational m){
        Rational ans = Rational(1, 1);
        ans.numerator = r.numerator * m.numerator;
        ans.denominator = r.denominator * m.denominator;
        ans.reduce();
        return ans;
    };

    operator double()
    {
        double n = numerator;
        return n/denominator; 
    } 

    void reduce(){
        //std::cout << numerator << " / " << denominator << std::endl;
        long long int gcd = GCD(numerator, denominator);
        numerator /= gcd;
        denominator /= gcd;
        //std::cout << numerator << " / " << denominator << std::endl;
    };
};

#endif