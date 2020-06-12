/*
	time:
		best: O(N)
		average: O(N**2)
		worse: O(N**2)
*/


function insertion_sort(nums){
	for(let i = 1; i < nums.length; i++){
		let temp = nums[i];
		let j = i-1;
		while(temp < nums[j] && j >= 0){
			nums[j+1] = nums[j];
			j--;
		}
		nums[j+1] = temp;
	}
}


let array = [12,3,45,6,10,1,2,3,100];

insertion_sort(array);

console.log(array);