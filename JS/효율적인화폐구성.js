const input = require("fs").readFileSync("./ex.txt").toString().trim();

function solution(n, m, arr) {
  let d = new Array(10001).fill(10001);
  d[0] = 0;

  for (let i = 0; i < n; i++) {
    for (let j = arr[i]; j < m + 1; j++) {
      d[j] = Math.min(d[j], d[j - arr[i]] + 1);
    }
  }

  if (d[m] === 10001) {
    console.log(-1);
  } else {
    console.log(d[m]);
  }
}

solution(3, 4, [3, 5, 7]);
