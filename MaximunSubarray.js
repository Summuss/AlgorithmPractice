//求跨越中点的最大子数组，leftIndex、rightIndex分别代表数组的左右边界索引
function maxSubarrayCrossing(array, leftIndex, rightIndex) {

    var middleIndex = Math.floor((leftIndex + rightIndex) / 2);
    var maxSum = {
        sum: array[middleIndex],
        left: middleIndex,
        right: middleIndex
    };
    for (var index = middleIndex - 1, currentSum = maxSum.sum; index >= leftIndex; index--) {
        currentSum += array[index];
        if (currentSum > maxSum.sum) {
            maxSum.sum = currentSum;
            maxSum.left = index;
        }
    }

    for (var index = middleIndex + 1, currentSum = maxSum.sum; index <= rightIndex; index++) {
        currentSum += array[index];
        if (currentSum > maxSum.sum) {
            maxSum.sum = currentSum;
            maxSum.right = index;
        }
    }

    return maxSum;
}

function maxSubarray(array, leftIndex, rightIndex) {
    if (leftIndex == rightIndex) {
        return {
            sum: array[leftIndex],
            left: leftIndex,
            right: leftIndex
        };
    } else {
        var middle = Math.floor((leftIndex + rightIndex) / 2);
        var leftMax = maxSubarray.arguments.callee(array, leftIndex, middle);
        var rightMax = maxSubarray.arguments.callee(array, middle + 1, rightIndex);
        var crossingMax = maxSubarrayCrossing(array, leftIndex, rightIndex);
        switch (true) {
            case leftMax.sum >= rightMax.sum && leftMax.sum >= crossingMax.sum:
                return leftMax;
            case rightMax.sum >= leftMax.sum && rightMax.sum >= crossingMax.sum:
                return rightMax;
            case crossingMax.sum >= leftMax.sum && crossingMax.sum >= rightMax.sum:
                return crossingMax;
        }
    }

}

var a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7];
var max = maxSubarray(a, 0, a.length - 1);
console.log(max);

//结果：{sum: 43, left: 7, right: 10}

