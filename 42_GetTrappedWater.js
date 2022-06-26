const getTrappedRainwater = function (height) {
  let totalWater = 0;
  for (let p = 0; p < height.length; p++) {
    let leftP = p,
      rightP = p,
      maxLeft = 0,
      maxRight = 0;
    while (leftP >= 0) {
      maxLeft = Math.max(maxLeft, height[leftP]);
      leftP--;
    }
    while (rightP < height.length) {
      maxRight = Math.max(maxRight, height[rightP]);
      rightP++;
    }
    const currentWater = Math.min(maxLeft, maxRight) - height[p];
    if (currentWater >= 0) {
      totalWater += currentWater;
    }
  }
  return totalWater;
};

console.log(getTrappedRainwater([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]));

// better way two pointers

const getTrappedRainwater2 = function (height) {
  let left = 0,
    right = height.length - 1,
    maxLeft = 0,
    maxRight = 0,
    total = 0;

  while (left < right) {
    if (height[left] <= height[right]) {
      if (height[left] >= maxLeft) {
        maxLeft = height[left];
      } else {
        total += maxLeft - height[left];
      }
      left++;
    } else {
      if (height[right] >= maxRight) {
        maxRight = height[right];
      } else {
        total += maxRight - height[right];
      }
      right--;
    }
  }
  return total;
};

console.log(getTrappedRainwater2([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]));
