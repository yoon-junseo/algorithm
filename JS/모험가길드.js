function solution(n, arr) {
  let result = 0;
  let count = 0;
  arr.sort();

  for (const i of arr) {
    count++;
    if (count >= i) {
      result++;
      console.log(i);
      count = 0;
    }
  }

  console.log(result);
}

solution(5, [2, 3, 1, 2, 2]);
