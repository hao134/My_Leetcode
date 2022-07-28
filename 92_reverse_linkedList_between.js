// consider example:
// 1 -> 2 -> 3 -> 4 -> 5 -> null
// left = 2 , right = 4

const reverseBetween = function (head, left, right) {
  let currentPos = 1,
    currentNode = head,
    start = head;

  while (currentPos < left) {
    start = currentNode;
    currentNode = currentNode.next;
    currentPos++;
  }
  // at this instance, start at 1, currentNode, currentPos at 2

  let newList = null,
    tail = currentNode;

  while (currentPos >= left && currentPos <= right) {
    const next = currentNode.next;
    currentNode.next = newList;
    newList = currentNode;
    currentNode = next;
    currentPos++;
  }

  start.next = newList;
  tail.next = currentNode;

  if (left > 1) {
    return head;
  } else {
    return newList;
  }
};
