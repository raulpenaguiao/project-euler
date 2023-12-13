#ifndef CL_StringManipulator
#define CL_StringManipulator

#include <vector>
#include <string>


static std::string JoinWithSeparator(std::vector<int> lis, std::string sep){
	if(lis.size() == 0) return "";
	std::string ans = std::to_string(lis[0]);
	for(int i = 1; i < lis.size(); i++) ans += sep + std::to_string(lis[i]);
	return ans;
}


static std::string JoinWithSeparator(std::vector<std::string> lis, std::string sep){
	if(lis.size() == 0) return "";
	std::string ans = lis[0];
	for(int i = 1; i < lis.size(); i++) ans += sep + lis[i];
	return ans;
}

#endif