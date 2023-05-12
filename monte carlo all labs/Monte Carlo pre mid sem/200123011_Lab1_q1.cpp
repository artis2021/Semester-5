#include<iostream>
#include<bits/stdc++.h>
using namespace std;

void fun(int a,int b,int m,int x,vector<vector<int>> &v)
{
   vector<int> temp;
   temp.push_back(x);
   for(int i=0; ;i++)
   {
    int y=(a*temp[temp.size()-1]+b)%m;
    if(y!=temp[0])
    {
        temp.push_back(y);

    }
    else
    {
     temp.push_back(y);
     v.push_back(temp);
     return;
    }
    }
   

}

int main()
{vector<vector<int>>v;
     int a=6,b=0,m=11,x=10;
     for(int i=0;i<=x;i++)
     {
        fun(a,b,m,i,v);
     }


    cout<<"below sequences are of a=6,b=0,m=11,0<=x<=10"<<endl<<endl;
     for(int i=0;i<v.size();i++)
     {cout<<"sequence of x="<<v[i][0]<<endl;
        for(int j=0;j<v[i].size();j++)
        {
            cout<<v[i][j]<<" ";
            
        }
        cout<<endl;
     }


cout<<endl<<endl;
vector<vector<int>> p;
a=3;
for(int i=0;i<=10;i++)
fun(a,b,m,i,p);

 cout<<"below sequences are of a=3,b=0,m=11,0<=x<=10"<<endl<<endl;
     for(int i=0;i<p.size();i++)
     {cout<<"sequence of x="<<v[i][0]<<endl;
        for(int j=0;j<p[i].size();j++)
        {
            cout<<p[i][j]<<" ";
            
        }
        cout<<endl;
     }


}