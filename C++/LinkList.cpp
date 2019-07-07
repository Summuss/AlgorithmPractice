#include "head.h"
struct Node
{
    int data;
    Node *next;
};

void init_linklist()
{
    Node node = {3, nullptr};
    cout << node.data << endl;
}

void link_list_main()
{
    init_linklist();
}
