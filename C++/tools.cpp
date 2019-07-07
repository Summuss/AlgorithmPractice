#include "head.h"

/**
 * @description: 自定义的输入函数
 * @param {要输入的变量,输入提示} 
 * @return: 
 */
void in(int &var, string hint)
{
    if (hint == "")
    {
        cout << "input:  ";
    }
    else
    {
        cout << "input " << hint << ":  ";
    }
    cin >> var;
}

/**
 * @description: 自定义的输入函数
 * @param {要输入的变量,输入提示} 
 * @return: 
 */
void in(double &var, string hint)
{
    if (hint == "")
    {
        cout << "input:  ";
    }
    else
    {
        cout << "input " << hint << ":  ";
    }
    cin >> var;
}

/**
 * @description: 自定义的输入函数
 * @param {要输入的变量,输入提示} 
 * @return: 
 */
void in(string &var, string hint)
{
    if (hint == "")
    {
        cout << "input:  ";
    }
    else
    {
        cout << "input " << hint << ":  ";
    }
    cin >> var;
}

/**
 * @description: 自定义的输入函数
 * @param {要输入的变量,输入提示} 
 * @return: 
 */
void in(char var[], string hint)
{
    if (hint == "")
    {
        cout << "input:  ";
    }
    else
    {
        cout << "input " << hint << ":  ";
    }
    cin >> var;
}
