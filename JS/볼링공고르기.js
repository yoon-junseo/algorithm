function solution(n, m, arr) {
  let result = 0;
  const ballList = new Array(11).fill(0);
  arr.sort();

  arr.forEach((a) => {
    ballList[a] += 1;
  });

  for (let i = 1; i < m + 1; i++) {
    n -= ballList[i];
    result += ballList[i] * n;
  }

  console.log(result);
}

solution(5, 3, [1, 3, 2, 3, 2]);
