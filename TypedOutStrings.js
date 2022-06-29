const buildString = function (string) {
  const builtArray = [];
  for (let p = 0; p < string.length; p++) {
    if (string[p] !== "#") {
      builtArray.push(string[p]);
    } else {
      builtArray.pop();
    }
  }
  return builtArray;
};

const backSpaceCompare = function (S, T) {
  const finalS = buildString(S);
  const finalT = buildString(T);
  if (finalS.length !== finalT.length) {
    return false;
  } else {
    for (let p = 0; p < finalS.length; p++) {
      if (finalS[p] !== finalT[p]) {
        return false;
      }
    }
  }
  return true;
};
console.log(
  backSpaceCompare(["a", "b", "c", "#", "d"], ["a", "c", "c", "#", "c"])
);
