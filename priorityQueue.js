function PriorityQueue(queueArray) {
    this.queueArray = queueArray;
    this.size = queueArray.length;
    {
        var leafMinIndex = Math.ceil((this.size - 1) / 2);
        for (var i = leafMinIndex - 1; i >= 0; i--) {
            maxHeapify(this, i);
        }
    }

    function maxHeapify(priorityQueue, index) {
        var left = 2 * index + 1;
        var right = 2 * index + 2;
        var largest = index;
        if (left <= priorityQueue.size - 1 && priorityQueue.queueArray[left].priority > priorityQueue.queueArray[largest].priority) {
            largest = left;
        }
        if (right <= priorityQueue.size - 1 && priorityQueue.queueArray[right].priority > priorityQueue.queueArray[largest].priority) {
            largest = right;
        }
        if (largest != index) {
            var t = priorityQueue.queueArray[index];
            priorityQueue.queueArray[index] = priorityQueue.queueArray[largest];
            priorityQueue.queueArray[largest] = t;
            arguments.callee(priorityQueue, largest);
        }
    }

    PriorityQueue.prototype.top = function () {
        return this.size == 0 ? null : this.queueArray[0];
    };
    PriorityQueue.prototype.pop = function () {
        if (this.size == 0) {
            return null;
        }
        var first = this.queueArray[0];
        if (this.size == 1) {
            this.size--;
        } else {
            this.queueArray[0] = this.queueArray[this.size - 1];
            this.size--;
            maxHeapify(this, 0);
        }
        return first;
    }
    PriorityQueue.prototype.push = function (elem) {
        this.queueArray[this.size] = elem;
        this.size++;
        //将元素添加到最后，并依次对其父节点heapify
        for (var par = Math.floor((this.size - 1 - 1) / 2); par >= 0; par = Math.floor((par - 1) / 2)) {
            maxHeapify(this, par);
        }
    }


}

function T(n) {
    this.priority = n;
}

queue = new PriorityQueue([new T(2), new T(5), new T(1), new T(4), new T(3)]);
queue.push(new T(7));
queue.push(new T(6));
console.log(queue);