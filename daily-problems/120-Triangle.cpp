#include <bits/stdc++.h>
using namespace std;

// Nothing crazy, normal bottoms up dp
// f(i, j) = triange[i][j] , if last row 
//           triangle[i][j] + min{f(i + 1, j), f(r + 1, j + 1)}

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int N = triangle.size();
        
        vector<vector<int>> dp;
        for (int r = 0; r < N; r++) {
            dp.push_back(vector<int>(r + 1, INT_MAX));
        }

        for (int i = 0; i < N; i++) {
            dp[N - 1][i] = triangle[N - 1][i];
        }
        for (int j = 1; j < N; j++) {
            int r = N - j - 1;
            for (int i = 0; i < N - j; i++) {
                dp[r][i] = triangle[r][i] + min(dp[r + 1][i], dp[r + 1][i + 1]);
            }
        }
        return dp[0][0];
    } 
};



