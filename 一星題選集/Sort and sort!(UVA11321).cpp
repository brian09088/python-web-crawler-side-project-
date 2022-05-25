/*Sample Input
15 3
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
0 0
Sample Output
15 3
15
9
3
6
12
13
7
1
4
10
11
5
2
8
14
0 0
*/

#include <iostream>
#include <algorithm>
using namespace std;
int a[10000],n,m;

bool cmp(int a, int b){
 int  aodd=abs(a%2);
 int  bodd=abs(b%2);
 if(a%m != b%m){return a%m < b%m;} //�N����ͬ��С��ǰ��������
 if(aodd!=bodd){return aodd;} //�N����ͬ����ż��ͬ���攵ǰ��ż����
 if(aodd){return a>b;} //�N����ͬ��ȫ���攵������ǰ��С����
 return a<b; //�N����ͬ��ȫ��ż����С��ǰ��������
}

int main(){
 while(cin>>n>>m){
 if(n==0){break;}
 for(int i=0; i<n ; i++){cin>>a[i];}
 sort(a,a+n,cmp);
 cout<<n<<" "<<m<<endl;
 for(int i=0; i<n ; i++){cout<<a[i]<<endl;}
 }
 return 0;
}
