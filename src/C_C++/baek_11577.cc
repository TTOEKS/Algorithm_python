#include<bits/stdc++.h>

using namespace std;

const int MAX = 100000;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int n, k, ans=0;
	bool bulb[MAX+1];

	cin >> n >> k;
	//bulb 배열 초기화
	bulb[0] = 0;
	for(int i=1; i<=n; ++i)
		cin >> bulb[i];
	//xBulb 배열 초기화
j
	bool xBulb[MAX+1];
	xBulb[0] = 0;

	for(int i=1; i<=n; ++i)
		xBulb[i] = bulb[i-1] ^ bulb[i];
	//시뮬레이션

	for(int i=1; i<=n-k+2; ++i){ //toggle [i ~ i+k)
		if(xBulb[i]){//i번째 전구가 켜져있으면
			xBulb[i]^=1, xBulb[i+k]^=1; //i와 i+k를 토글
			++ans;
		}
	}

	//고려되지 않은 [n-k+2~n]전구의 상태 확인
	for(int i=n-k+2; i<=n; ++i)
		if(xBulb[i]){
			cout << "Insomnia";
			return 0;
		}
	cout << ans;
}
