#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> rangeAddition(vector<int>& array, vector<vector<int> > &values) {
        // values = [[l1, r1, value1], [l2, r2, value2], ... ]
        vector<int> result(array.size()+2, 0);
        for (int i = 0; i < array.size(); i++) {
            insert(result, i+1, i+1, array[i]);
        }
        for (int i = 0; i < values.size(); i++) {
            insert(result, values[i][0]+1, values[i][1]+1, values[i][2]);
        }
        for (int i = 1; i < result.size(); i++) {
            result[i] += result[i-1];
        }
        return vector<int>{result.begin()+1, result.end()-1};
    }

    void insert(vector<int> &array, int l, int r, int value) {
        array[l] += value;
        array[r+1] -= value;
    }
};