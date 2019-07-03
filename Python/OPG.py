def getLASTVT(generations, vn, vt):
    """求LASTVT"""
    # 定义一个二维数组，第一维为vn，第二维为vt
    F = []
    for i in range(0, len(vn)):
        arr = []
        for j in range(0, len(vt)):
            arr.append(0)
        F.append(arr)

    # 对T->....a或T->....aR形式的产生式，令F[T][a]=1
    for generation in generations:
        length = len(generation)

        # T->....a形式
        if (generation[length - 1] in vt):
            rowindex = vn.index(generation[0])
            columnindex = vt.index(generation[length - 1])
            F[rowindex][columnindex] = 1
        # T->...Ra形式
        elif (generation[length - 2] in vt and generation[length - 1] in vn):
            rowindex = vn.index(generation[0])
            columnindex = vt.index(generation[length - 2])
            F[rowindex][columnindex] = 1

    # 将F表中每一个为1的位置（i，j）入栈
    stack = []
    for i in range(0, len(vn)):
        for j in range(0, len(vt)):
            if F[i][j] == 1:
                stack.append([i, j])

    # 对每一个T->...R的产生式，若F[T,a]为0，则使其值为1
    # 并将其入栈
    while stack:

        temp = stack.pop()
        rowindex = temp[0]
        columnindex = temp[1]
        for generation in generations:
            # 产生式的左部元素
            head = generation[0]
            # 产生式的最后一个最后一个元素
            tail = generation[len(generation) - 1]

            if tail == vn[rowindex]:
                if (F[vn.index(head)][columnindex] == 0):
                    # 置1
                    F[vn.index(head)][columnindex] = 1
                    # 入栈
                    stack.append([vn.index(head), columnindex])

    # 根据F表求LASTVT
    # 若F[T][a]=1，则a属于LASTVT(T)
    LASTVT = {}
    for i in range(0, len(vn)):
        arr = []
        LASTVT[vn[i]] = arr
        for j in range(0, len(vt)):
            if F[i][j] == 1:
                arr.append(vt[j])
    return LASTVT


def getFIRSTVT(generations, vn, vt):
    """求FIRSTVT"""
    # 定义一个二维数组，第一维为vn，第二维为vt
    L = []
    for i in range(0, len(vn)):
        arr = []
        for j in range(0, len(vt)):
            arr.append(0)
        L.append(arr)

    # 对T->a....或T->Ra....形式的产生式，令L[T][a]=1
    for generation in generations:
        length = len(generation)

        # T->a....形式
        if (generation[3] in vt):
            rowindex = vn.index(generation[0])
            columnindex = vt.index(generation[3])
            L[rowindex][columnindex] = 1

        # T->Ra...形式
        elif (len(generation) > 4 and generation[4] in vt and generation[3] in vn):
            rowindex = vn.index(generation[0])
            columnindex = vt.index(generation[4])
            L[rowindex][columnindex] = 1

    stack = []
    # 将L表中每一个为1的位置（i，j）入栈
    for i in range(0, len(vn)):
        for j in range(0, len(vt)):
            if L[i][j] == 1:
                stack.append([i, j])

    # 对每一个T->R...的产生式，若L[T,a]为0，则使其值为1
    # 并将其入栈
    while stack:
        temp = stack.pop()
        rowindex = temp[0]
        columnindex = temp[1]
        for generation in generations:

            # 产生式的左部元素
            head = generation[0]

            # 产生式的右部第一个元素
            tail = generation[3]
            if tail == vn[rowindex]:
                if (L[vn.index(head)][columnindex] == 0):
                    # 置1
                    L[vn.index(head)][columnindex] = 1
                    # 入栈
                    stack.append([vn.index(head), columnindex])
    FIRST = {}
    # 根据L表求FIRSTVT
    # 若L[T][a]=1，则a属于FIRST(T)
    for i in range(0, len(vn)):
        arr = []
        FIRST[vn[i]] = arr
        for j in range(0, len(vt)):
            if L[i][j] == 1:
                arr.append(vt[j])
    return FIRST


def getPriorityList(generations, FIRSTVT, LASTVT,vt,vn):
    """根据FIRSTVT和LASTVT求优先级表"""
    # 定义一个二维数组，若a=b,priority[a][b]=2
    # 若a>b，priority[a][b]=1
    # 若a<b,priority[a][b]=-1
    priority = []
    for i in range(0, len(vt) + 1):
        arr = []
        for j in range(0, len(vt) + 1):
            arr.append(0)
        priority.append(arr)

    # 根据每条产生式判断优先级
    for generation in generations:
        for i in range(3, len(generation)):
            # Xi和Xi+1 皆为vt，则Xi=Xi+1
            if len(generation) > i + 1 and generation[i] in vt and generation[i + 1] in vt:
                priority[vt.index(generation[i])][vt.index(generation[i + 1])] = 2

            # Xi和Xi+2为vt，Xi+1为vn，则Xi=Xi+2
            if len(generation) > i + 2 and generation[i] in vt and generation[i + 1] in vn and generation[i + 2] in vt:
                priority[vt.index(generation[i])][vt.index(generation[i + 2])] = 2

            # 若Xi是vt，Xi+1是vn，Xi<FIRSTVT(Xi+1)
            if len(generation) > i + 1 and generation[i] in vt and generation[i + 1] in vn:
                for first in FIRSTVT[generation[i + 1]]:
                    rowindex = vt.index(generation[i])
                    columnindex = vt.index(first)
                    priority[rowindex][columnindex] = -1

            # 若Xi是vn，Xi+1是vt，LASTVT(Xi)>Xi+1
            if len(generation) > i + 1 and generation[i] in vn and generation[i + 1] in vt:
                for last in LASTVT[generation[i]]:
                    rowindex = vt.index(last)
                    columnindex = vt.index(generation[i + 1])
                    priority[rowindex][columnindex] = 1

    # 设置#的优先级
    for i in range(0, len(vt) + 1):
        priority[len(vt)][i] = -1
        priority[i][len(vt)] = 1
    priority[vt.index('(')][len(vt)] = 0
    priority[len(vt)][vt.index(')')] = 0
    priority[len(vt)][len(vt)] = 2

    # 将#添加到vt
    vt.append('#')

    return priority


def isContailVt(generation, vt):
    """判断一个产生式是否包含终结符"""
    for ch in generation:
        if ch in vt:
            return True
    return False


def toString(stack):
    """将一个列表转换为字符串"""
    string = ""
    for ch in stack:
        string = string + ch
    return string


def analysis(generations, priority, inputstring,vt):
    """根据产生式，优先级表来判断输入串是否合法"""
    # 将输入串加上#
    inputstring = inputstring + '#'
    stack = []  # 分析栈
    k = 0  # 输入串的位置
    stack.append('#')  # #入栈

    print('%-10s' % "符号栈" + '%-10s' % "输入串" + '%-10s' % "优先关系" + '%-10s' % "动作")
    while True:
        ch = inputstring[k]  # 输入串的位置元素

        # 如果栈顶是vt
        if stack[-1] in vt:
            j = -1
        else:
            j = -2
            if ch == '#' and stack[j] == ch:
                return "合法"

        # 如果栈顶优先级大于等于输入串首元素，移进栈
        if priority[vt.index(stack[j])][vt.index(ch)] == -1 \
                or priority[vt.index(stack[j])][vt.index(ch)] == 2:
            print('%-12s' % toString(stack) + '%-12s' % toString(inputstring[k:]) +
                  '%-13s' % (stack[j] + "<=" + ch) + '%-10s' % "移进")

            # 入栈
            stack.append(ch)
            k = k + 1

        # 如果栈顶优先级小于等于输入串首元素，归约
        elif priority[vt.index(stack[j])][vt.index(ch)] == 1:
            # 寻找合适的产生式
            for generation in generations:
                # 获得产生式的右部
                right = generation[3:]

                # 如果产生式右部包含vt
                if isContailVt(right, vt):
                    if len(stack) > len(right):
                        # 判断产生式和栈元素是否对应
                        for index in range(-len(right), 0):

                            # 产生式的终结符必须和栈中的相等
                            if right[index] in vt and not stack[index] == right[index]:
                                break

                            # 如果不是终结符则产生式和栈元素对应即可
                            if stack[index] in vt and not stack[index] == right[index]:
                                break
                            index = index + 1

                        # 如果产生式和栈匹配成功，用该产生式归约
                        if index == 0:
                            print('%-12s' % toString(stack) + '%-12s' % toString(inputstring[k:]) +
                                  '%-13s' % (stack[j] + ">" + ch) + '%-10s' % ("用" + generation + "归约"))

                            # 开始归约
                            stack = stack[0:-len(right)]
                            stack.append(generation[0])

                            break;

        # 不存在优先级关系，不合法
        else:
            return "不合法"


def Main():
    n=int(input("请输入产生式条数:"))

    #原始输入的字符串
    raw_generations = []
    for i in range(0,n):
        raw_generations.append(input("请输入第"+str(i+1)+'条产生式').strip())
    # raw_generations.append("E->E+T|T")
    # raw_generations.append("T->T*F|F")
    # raw_generations.append("F->(E)|i")

    vt = []
    vn = []
    generations = []
    # 将原始输入的产生式根据|分割成多个产生式
    for raw_generation in raw_generations:
        head = raw_generation[0:3]
        individuals = raw_generation[3:].split('|')
        for individual in individuals:
            generations.append(head + individual)

    #求vn
    for generation in generations:
        vn.append(generation[0])

    #求vt
    for generation in generations:
        for char in generation[3:]:
            if char not in vn:
                vt.append(char)
    #去重
    vn = list(set(vn))
    vt = list(set(vt))

    firstvt = getFIRSTVT(generations, vn, vt)
    lastvt = getLASTVT(generations, vn, vt)
    prioritytable = getPriorityList(generations, firstvt, lastvt,vt,vn)
    print(vt)
    print(prioritytable)
    sentence=input("请输入要分析的句子")
    print(analysis(generations, prioritytable, sentence,vt))


Main()













