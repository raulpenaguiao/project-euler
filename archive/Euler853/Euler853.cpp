#include <iostream>
#include "CL_Primes.h"
#include "CL_StringManipulator.h"
#include <vector>
#include <string>
#include <bits/stdc++.h>

#define FOR(a, b) for(int a = 0; a < b; a++)

std::vector<int> ListIntersection(std::vector<int> l1, std::vector<int> l2){//Assumes given lists are sorted
	std::vector<int> ans;
	int index = 0;
	FOR(i, l2.size()){
		bool skip = true;
		while(skip){
			if(l1[index] == l2[i]){
				index++;
				skip = false;
				ans.push_back(l1[index]);
			}
			else{
				if(l1[index] < l2[i]){
					index++;
					if (index == l1.size()) return ans;
				}
				else{
					skip = false;
				}
			}
		}
	}
	return ans;
}

std::vector<int> RemoveFromList(std::vector<int> l1, std::vector<int> l2){//Assumes given lists are sorted
	std::vector<int> ans;
	int index = 0;
	FOR(i, l1.size()){
		bool skip = true;
		while(skip){
			if(l1[i] == l2[index]){
				index++;
				skip = false;
				if(index == l2.size()){
					for(int j = i+1; j < l1.size(); j++) ans.push_back(l1[j]);
					return ans;
				}
			}
			else{
				if(l1[i] < l2[index]){
					ans.push_back(l1[i]);
					skip = false;
				}
				else{
					index++;
					if(index == l2.size()){
						for(int j = i; j < l1.size(); j++) ans.push_back(l1[j]);
						return ans;
					}
				}
			}
		}
	}
	return ans;
}


int main() {
	long long int fibbs[100000];
	fibbs[0] = 0;
	fibbs[1] = 1;
	int NUM = 120;
	FOR(i, NUM+2) fibbs[i+2] = fibbs[i+1] + fibbs[i];

	FOR(i, 20) std::cout << " / " << fibbs[i];
	std::cout << std::endl;
	FOR(i, 20) std::cout << " / " << GCD(fibbs[i], fibbs[i+1]  - 1 );
	std::cout << std::endl;
	std::vector<int> dofNUM = Divisors(NUM);
	std::cout << fibbs[NUM] << " - " << fibbs[NUM+1] - 1 << " - " <<  GCD(fibbs[NUM], fibbs[NUM+1]-1) << std::endl;
	std::vector<int> divs = Divisors(GCD(fibbs[NUM], fibbs[NUM+1]-1));
	sort(divs.begin(), divs.end());	
	sort(dofNUM.begin(), dofNUM.end());	
	std::cout << NUM << " ::: " <<  JoinWithSeparator(divs, " - ") << std::endl;
	for(int n = 0; n < dofNUM.size() - 1; n ++) {
		std::vector<int> newDivs = Divisors(GCD(fibbs[dofNUM[n]], fibbs[dofNUM[n]+1]-1));
		sort(newDivs.begin(), newDivs.end());
		std::cout << dofNUM[n] << " ::: " <<  JoinWithSeparator(newDivs, " - ") << std::endl;
		divs = RemoveFromList(divs, newDivs);
		std::cout << dofNUM[n] << " ::: " <<  JoinWithSeparator(divs, " - ") << std::endl;
	}
}