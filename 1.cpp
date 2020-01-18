#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>   
using namespace std;
using namespace __gnu_pbds;
#define int long long
#define ll long long
#define endl "\n"
#define lu unsigned long long
#define mod 1000000007
#define ld long double
#define f(i, n) for(ll i = 0; i < n; i++)
#define ff(i,n) for(int i=1;i<=n;i++)
#define pb push_back
#define mp make_pair
#define v vector<ll>
#define vv vector<vector<ll> >
#define vs vector<string>
#define vpr vector<pair<ll,ll>>
#define fi first
#define se second
#define all(x)  x.begin(),x.end()
#define bg(x)  x.begin()
#define sz(x)  x.size()
#define in(x,n) f(i,n) cin>>x[i]
#define out(x,n) f(i,n) cout<<x[i]<<" "
#define lcm(x, y) ((x) * (y) / __gcd(x, y))
#define mxt(a) *(max_element(a.begin(),a.end()))
#define mnt(a)  *(min_element(a.begin(),a.end()))
#define mem(x,val) memset(x,val,sizeof(x))
#define tc    ll t;cin>>t;while(t--)
#define pi pair<int,int>
#define prfloat(val,precise) cout<<fixed<<setprecision(precise)<<val<<endl;
const ld PI = 2 * acos(0.0);
void yes(){ cout<<"YES\n";}
void no(){cout<<"NO\n";}
ll m(ll a){ return (a+mod)%mod;}
ll cel(ll x1,ll y1){ ;if((x1%y1)==0)return x1/y1;return x1/y1+1;}
ll power(ll a,ll b){ if(b==0)return 1;ll d=power(a,b/2);d=m(d*d);
if(b&1)d=m(d*a);return d;}
// set_name.find_by_order(k) It returns to an iterator to the kth element (counting from zero) in the set in O(logn) time
// set_name.order_of_key(k) It returns to the number of items that are strictly smaller than our item k in O(logn) time.
/*string operations :
str.substr (x,y) : returns a substring str[x],str[x+1],...str[x+y-1]
str.substr (x) : returns a substring str[x],... end of string
str.find(qtr) : returns the first occurenece of qtr in str */

int32_t main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;cin>>n;
	vs grid(n+1);
	for(int i=0;i<n;i++)
		fgets(grid[i])

	cout<<"[";
	for(int i=0;i<n;i++)
	{
		cout<<"[";
		int l=sz(grid[i]);
		for(int j=0;j<l-1;j++)
			cout<<"'"<<grid[i][j]<<"'"<<",";
		cout<<"'"<<grid[i][l-1]<<"'"<<"]";
		if(i!=(n-1))
			cout<<",";
	}

	cout<<"]";
	return 0;
}