const findTwoSum = function (nums, target) {
  for (let p1 = 0; p1 < nums.length; p1++) {
    const numberToFind = target - nums[p1];
    for (p2 = p1 + 1; p2 < nums.length; p2++) {
      if (numberToFind === nums[p2]) {
        return [p1, p2];
      }
    }
  }
  return null; // no solution
};
