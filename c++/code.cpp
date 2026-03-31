#include <bits/stdc++.h>
using namespace std;


int main() {
    int n, W;
    cin >> n >> W;

    vector<int> w(n+1), v(n+1);
    
    for (int i = 1; i <= n; i++) cin >> w[i] >> v[i];


    vector<int> dp(W+1, 0);
    for (int i = 1; i <= n; i++)
        for (int j = W; j >= w[i]; j--)  // duyệt NGƯỢC
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);


    cout << "dp[W]: " << dp[W] << endl;
    return 0;
}
