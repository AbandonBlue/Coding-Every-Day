function selection_sort(nums){
    for(let i = 0; i < nums.length-1; i++){
		let min = nums[i];
		let idx = i;
    	for(let j = i+1; j < nums.length; j++){
    		if(nums[j] < min){
    		    min = nums[j];
    		    idx = j;
    		}
		}
		if(idx != i){
			// in-place
			let temp = nums[i];
		    nums[i] = min;
		    nums[idx] = temp;
		}
	}
}


let array = [10, 9, 8, 2, 100, 1, 7, 34, 28];

selection_sort(array);
console.log(array);