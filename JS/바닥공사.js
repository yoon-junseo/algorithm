const input = require("fs").readFileSync("./ex.txt").toString().trim();

function solution(n) {
  let d = new Array(1001).fill(0);
  d[1] = 1;
  d[2] = 3;

  for (let i = 3; i < n + 1; i++) {
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796;
  }

  console.log(d[n]);
}

solution(input);
