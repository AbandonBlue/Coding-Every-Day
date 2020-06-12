function bubble_sort(nums){
    for(let i = 0; i < nums.length-1; i++){
    	for(let j = 0; j < nums.length-i; j++){
    		if(nums[j] > nums[j+1]){
    		    let temp = nums[j];
    		    nums[j] = nums[j+1];
    		    nums[j+1] = temp;
    		}
		}
		
	}
}


let array = [2, 1, 100,10, 9, 2, 9, 8, 100, 3, 1, 100];
bubble_sort(array);

console.log(array);