function merge_sort(nums){
    function divide(nums){
        if(nums.length == 0){
            return [];
        }else if(nums.length == 1){
            return nums;
        }
        let left = [];
        let right = [];
        let pivot = nums[nums.length-1];
        for(let i = 0; i < nums.length-1; i++){ // remember -1
            if(nums[i] >= pivot){
                right.push(nums[i]);
            }else{
                left.push(nums[i]);
            }
        }
        return divide(left).concat([pivot]).concat(divide(right));
    }
    return divide(nums); // execute 
}

// original array
let array = [100, 100, 1, 3, 22, 312, 123123, 123, 1000];
console.log(array);

// sorted array
array = merge_sort(array);
console.log(array);