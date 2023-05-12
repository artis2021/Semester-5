#include<iostream>
#include<bits/stdc++.h>
using namespace std;

void fun(long long int  x,long long int  a,long long int  m,vector<int> &v)
{
    v.push_back(x);
    for(int i=0; ;i++)
    {
        long long int y=(a*v[v.size()-1])%m;
        if(y!=v[0])
        v.push_back(y);
        else
        {
            v.push_back(y);
            return;
        }
    }
}

int main()
{
    long long int  x=1,a=1597,m=244944;
    vector<int > v;
    fun(x,a,m,v);
    vector<double> u;
    for(int i=0;i<v.size();i++)
    u.push_back((double)v[i]/m);

    for(int i=0;i<v.size();i++)
    cout<<v[i]<<"                   "<<u[i]<<endl;

}
