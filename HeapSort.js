function maxHeapify(heap, index) {
    var left = 2 * index + 1;
    var right = 2 * index + 2;
    var largest = index;
    if (left <= heap.size-1 && heap.array[left] > heap.array[largest]) {
        largest = left;
    }
    if (right <= heap.size-1 && heap.array[right] > heap.array[largest]) {
        largest = right;
    }
    if (largest != index) {
        var t = heap.array[index];
        heap.array[index] = heap.array[largest];
        heap.array[largest] = t;
        arguments.callee(heap, largest);
    }
}

function buildMaxHeap(heap) {
    // leafMinIndex为叶子最小索引，小于此值的索引为结点索引
    var leafMinIndex=Math.ceil((heap.size-1)/2) ;
    for (var i=leafMinIndex-1;i>=0;i--){
        maxHeapify(heap,i);
    }
}

function heapSort(heap){
    while (heap.size>=2){
        var t=heap.array[0];
        heap.array[0]=heap.array[heap.size-1];
        heap.array[heap.size-1]=t;
        heap.size--;
        maxHeapify(heap,0);
    }

}

heap={
    array:[2,5,1,4,3],
    size:5
};
buildMaxHeap(heap);
heapSort(heap);
console.log(heap);

