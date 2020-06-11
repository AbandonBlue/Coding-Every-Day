// merge part, the most important part in this algorithm
function merge(left, right){
    let result = [];
    // console.log(left, right);
    while(left.length > 0 && right.length > 0){
        if(left[0] < right[0]){
            result.push(left.shift());
        }else{
            result.push(right.shift());
        }
    }
    return result.concat(left, right);   // because there must be left one element either in left or right 
}

function merge_sort(nums){
    // special case
    if(nums.length <= 1) return nums;
    
    // divide
    let middle = Math.floor(nums.length / 2);
    let left = nums.slice(0, middle);   // 0 to middle-1 
    let right = nums.slice(middle);     // middle to end
    return merge(merge_sort(left), merge_sort(right));

}







// original array
let array = [100, 100, 1, 3, 22, 312, 123123, 123, 1000];
console.log(array);

// sorted array
array = merge_sort(array);
console.log(array);