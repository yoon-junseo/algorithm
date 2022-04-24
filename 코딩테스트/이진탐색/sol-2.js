const N = 4;
const M = 6;
const arr = [19, 15, 10, 17];

function solution(N, M, arr) {
  const sortedArr = arr.sort();
  let result = 0;
  let start = 0;
  let end = sortedArr[sortedArr.length - 1];

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    let total = 0;
    for (const ddeok of arr) {
      if (ddeok > mid) {
        total += ddeok - mid;
      }
    }
    if (total >= M) {
      result = mid;
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  console.log(result);
}

solution(N, M, arr);
