#include "head.h"
struct Node
{
    int data;
    Node *next;
};

void init_linklist(Node &head)
{
    head.next = nullptr;
}

/**
 * @description: 头插法创建链表
 * @param {头结点}
 * @return: 
 */
void create_linklist_head(Node &head)
{
    int num;
    in(num, "num");
    for (int i = 0; i < num; i++)
    {
        Node *node = new Node;
        in(node->data, "节点数据");
        node->next = head.next;
        head.next = node;
    }
}

/**
 * @description: 尾插法创建链表
 * @param {头结点} 
 * @return: 
 */
void create_linklist_tail(Node &head)
{
    Node *tail = &head;
    int num;
    in(num, "num");
    for (int i = 0; i < num; i++)
    {
        Node *node = new Node;
        in(node->data, "节点数据");
        tail->next = node;
        tail = node;
    }
    tail->next = nullptr;
}

/**
 * @description: 以数组为元素创建链表
 * @param {头结点,数组,长度} 
 * @return: 
 */
void create_linklist_array(Node &head,int arr[],int len){
    Node* tail=&head;
    for(int i=0;i<len;i++ ){
        Node *node=new Node;
        node->data=arr[i];
        node->next=tail->next;
        tail->next=node;
        tail=node;
    }
}

/**
 * @description:获取链表中第i个元素 
 * @param {头结点,i} 
 * @return: 第i个元素
 */
int get_linklist_elem(Node head, int i)
{
    Node *node = head.next;
    int j;
    for (j = 0; j < i && node; j++, node = node->next)
        ;
    if (i == j && node)
    {
        return node->data;
    }
    else
    {
        out("超出链表范围");
        exit(1);
    }
}

Node merge_linklist(Node l1, Node l2)
{
    Node l3;
    l3.data=1;
    l3.next=nullptr;
    Node *p1 = l1.next, *p2 = l2.next, *p3 = &l3;
    while (p1 && p2)
    {
        if (p1->data > p2->data)
        {
            out("p3->next=p2");
            p3->next = p2;
        }
        else
        {
            
            out("p3->next=p1");
            p3->next = p1;
        }
        p3 = p3->next;
        p1 = p1->next;
        p2 = p2->next;
    }
    p3->next = p1 ? p2 : p1;
    return l3;
}

/**
 * @description: 输出链表元素
 * @param {头结点} 
 * @return: 
 */
void out_linklist(Node head)
{
    for (Node *node = head.next; node; node = node->next)
    {
        out(node->data);
    }
}

void link_list_main()
{
    Node l1,l2;
    init_linklist(l1);
    init_linklist(l2);
    int a1[5]={1,3,5,8,9};
    int a2[3]={2,5,7};
    out_linklist(l1);
    out_linklist(l2);
    Node l3=merge_linklist(l1,l2);
    if(l3.next==nullptr)
    {
        out("l3.next=null");
    }
}
