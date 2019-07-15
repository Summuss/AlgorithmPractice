#include "head.h"
#define SPACE_SIZE 100
typedef int elemType;
struct StaticNode
{
    elemType data;
    int cur;
};

//��ʼ���ռ�,�������
void init_space(StaticNode space[])
{
    for (int i = 0; i < SPACE_SIZE - 2; i++)
    {
        space[i].cur = i + 1;
    }
    space[SPACE_SIZE - 1].cur = 0;
}

//0�ŵ�Ԫ��curָ����һ�����ÿռ�
int malloc_sn(StaticNode space[])
{
    int i = space[0].cur;
    space[0].cur = space[i].cur;
    return i;
}

//��k�ŵ�Ԫ����,�����뵽0�ŵ�Ԫ����
void free_sn(StaticNode space[], int k)
{
    space[k].cur = space[0].cur;
    space[0].cur = k;
}

//������̬����,β�巨
void create_static_linklist(StaticNode space[], int head, int len)
{
    int tail = head;
    for (int i = 0; i < len; i++)
    {
        int k = malloc_sn(space);
        space[tail].cur = k;
        space[k].cur = 0;
        in(space[k].data, "������������");
        tail = k;
    }
}

void out_static_linklist(StaticNode space[], int head)
{
    for (int i = space[head].cur; i; i = space[i].cur)
    {
        out(space[i].data);
    }
}

void main_static_linklist()
{
    StaticNode space[SPACE_SIZE];
    init_space(space);
    int head = malloc_sn(space);
    space[head].cur = 0;
    create_static_linklist(space, head, 5);
    out_static_linklist(space, head);
}