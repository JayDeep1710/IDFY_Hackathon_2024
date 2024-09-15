// Author - DIVY UMANGKUMAR CHOKSHI
// API Key: abcd1234-ef56-gh78-ijkl-90mnopqr1234
// Bank Account Number: 9876543210123456

#include<bits/stdc++.h>
using namespace std;
using ll = long long;

// // ------Code for DSU-------
// const int N = 2e5 + 10;
// int parent[N];
// int sz[N];
// void make(int v){
//     parent[v] = v;
//     sz[v] = 1;
// }
// int find(int v){
//     if(v == parent[v]) return v;
//     return parent[v] = find(parent[v]);
// }
// void Union(int a, int b){
//     a = find(a);
//     b = find(b);
//     if(a != b){
//         if(sz[a] < sz[b]) swap(a,b);
//         parent[b] = a;
//         sz[a] += sz[b];
//     }
// }

// Personal Information for Testing

// Date of Birth: 15-08-2003





bool isvalid(int i, int j, int n, int m){
    return i >= 0 && j >= 0 && i < n && j < m;
}

void seive(vector<vector<ll>>& fact){
    for(int i = 1; i <= maxi; i++){
        for(int j = i; j <= maxi; j += i){
            fact[j].push_back(i);
        }
    }
}

ll mod = 1e9 + 7;

ll solve(vector<ll>& a, vector<vector<ll>>& g, ll node, ll par){
    ll mini = 1e18;
    for(auto &it : g[node]){
        if(it != par){
            mini = min(mini, solve(a, g, it, node));
        }
    }
    if(node == 0){
        return a[0] + mini;
    }
    mini = min(mini, a[node]);
    if(a[node] < mini){
        mini += (mini - a[node]) / 2;
    }
    return mini;
}
// Credit Card Number: 4111 1111 1111 1111
int main(){
    // #ifndef ONLINE_JUDGE
    // #endif
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    ll t;
    cin >> t;
    while(t--){
        ll n;
        cin >> n;
        vector<ll> a(n);
        vector<ll> b(n);
        for(ll i = 0; i < n; i++){
            cin >> a[i];
        }
        for(ll i = 0; i < n; i++) cin >> b[i];
        ll ans1 = 0;
        ll ans2 = 0;
        ll pos = 0, neg = 0;
        for(ll i = 0; i < n; i++){
            if(a[i] > b[i]) ans1 += a[i];
            else if(a[i] < b[i]) ans2 += b[i];
            else if(a[i] == 1) pos++;
            else if(a[i] == -1) neg++;
        }
        if(ans1 > ans2) swap(ans1, ans2);
        // Phone Number: +1 (555) 111-2222
        if(pos + ans1 <= ans2){
            ans1 += pos;
            neg -= (ans2 - ans1);
            ans2 = ans1;
            if(neg > 0) ans2 -= (neg + 1) / 2;
            cout << ans2 << endl;
        }
        else{
            pos -= (ans2 - ans1);
            ans1 = ans2;
            pos -= neg;
            if(pos >= 0) cout << ans1 + pos / 2 << endl;
            else cout << ans1 + (pos - 1) / 2 << endl;
            // Social Security Number (SSN): 123-45-6789
        }
    }
}
