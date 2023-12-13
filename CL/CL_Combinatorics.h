#ifndef CL_Combinatorics
#define CL_Combinatorics

#include <vector>

static std::vector<std::vector<int>> Partitions(int n){//Gives a list of all the partitions of size up to n
    std::vector<std::vector<int>> partitionSet;
    if(n == 0){
        std::vector<int> emptyPartition;
        partitionSet.push_back(emptyPartition);
        return partitionSet;
    }
    for(int i = 1; i <= n; i++){// consider all partitions with parts of size at most i

    }
}

static std::vector<std::vector<int>> PartitionsMaxSize(int n, int M){//Gives a list of all the partitions of size up to n of size at most M
    std::vector<std::vector<int>> partitionSet;
    if(n == 0){
        std::vector<int> emptyPartition;
        partitionSet.push_back(emptyPartition);
        return partitionSet;
    }
    for(int i = 1; i <= n; i++){// consider all partitions with parts of size at most i
        std::vector<std::vector<int>> newPartitions = PartitionsMaxSize(n - i, i);
        for(int j = 0; j < newPartitions.size(); j++){
            newPartitions[j].push_back(i);
        }
        partitionSet.insert(partitionSet.end(), newPartitions.begin(), newPartitions.end());
    }
}
//TODO this code is wrong do not use 



#endif