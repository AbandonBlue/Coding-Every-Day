function binary_search(nums, target, l, r){
    // console.log(nums);
    if(l <= r){
        let mid_idx = Math.floor((l+r)/2);
		if(nums[mid_idx] == target){
		     return true;
		}else if(nums[mid_idx] > target){
		     return binary_search(nums, target, l, mid_idx-1);
		}else{
            return binary_search(nums, target, mid_idx+1, r);
	}
    }else{
        return false;
    }
}


let array = [1,1,2,2,3,4,5,6,6,7,8,9,100];

for(let i = 0; i < 10; i++){
    console.log(i);
    console.log(binary_search(array, i, 0, array.length));
}

console.log(binary_search(array, 100, 0, array.length));