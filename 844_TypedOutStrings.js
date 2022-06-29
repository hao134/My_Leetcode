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

// better method:
const string1 = "ab#z";
const string2 = "az#z";

var backspaceCompare2 = function (S, T) {
  let p1 = S.length - 1,
    p2 = T.length - 1;

  while (p1 >= 0 || p2 >= 0) {
    if (S[p1] === "#" || T[p2] === "#") {
      if (S[p1] === "#") {
        let backCount = 2;

        while (backCount > 0) {
          p1--;
          backCount--;

          if (S[p1] === "#") {
            backCount += 2;
          }
        }
      }

      if (T[p2] === "#") {
        let backCount = 2;

        while (backCount > 0) {
          p2--;
          backCount--;

          if (T[p2] === "#") {
            backCount += 2;
          }
        }
      }
    } else {
      if (S[p1] !== T[p2]) {
        return false;
      } else {
        p1--;
        p2--;
      }
    }
  }

  return true;
};

console.log(backspaceCompare(string1, string2));
