function solution(N, stock, M, order) {
  const sortedStock = stock.sort();
  const sortedOrder = order.sort();

  for (const item of sortedOrder) {
    const result = binarySearch(sortedStock, Number(item), 0, N - 1);
    if (result) {
      console.log("yes");
    } else {
      console.log("no");
    }
  }
}

function binarySearch(array, target, start, end) {
  while (start <= end) {
    const mid = Math.floor((start + end) / 2);
    if (Number(array[mid]) === target) {
      return mid;
    }
    if (Number(array[mid]) > target) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return false;
}

const N = 5;
const stock = [8, 3, 7, 9, 2];
const M = 3;
const order = [5, 7, 9];

solution(N, stock, M, order);
