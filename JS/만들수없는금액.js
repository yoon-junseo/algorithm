function solution(n, arr) {
  arr.sort();
  let target = 1;

  for (let i = 0; i < arr.length; i++) {
    if (target < arr[i]) {
      break;
    }
    target += arr[i];
  }

  console.log(target);
}

solution(5, [3, 2, 1, 1, 9]);
