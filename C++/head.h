#ifndef HEAD_H
#define HEAD_H
#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string>
#define VNAME(value) (#value)
using namespace std;

void link_list_main();

void in(int &var, string hint="");
void in(double &var, string hint="");
void in(string &var, string hint="");
void in(char var[], string hint="");

/**
 * @description: 带回车的输出
 * @param {要输出的变量} 
 * @return: 
 */
template <typename T>
void out(T var){
    cout<<var<<endl;
}

#endif