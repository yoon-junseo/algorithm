const input = require("fs").readFileSync("./ex.txt").toString().trim();

function solution(n, arr) {
  let d = new Array(n + 1).fill(-1);
  d[0] = arr[0];
  d[1] = Math.max(arr[0], arr[1]);

  for (let i = 2; i < n; i++) {
    d[i] = Math.max(d[i - 1], d[i - 2] + arr[i]);
  }
  console.log(d[n - 1]);
}

solution(4, [1, 3, 1, 5]);
