const input = require("fs").readFileSync("./ex.txt").toString().trim();

function solution(number) {
  const numberStr = String(number);
  let left = 0;
  let right = 0;

  for (let i = 0; i < numberStr.length; i++) {
    if (i >= numberStr.length / 2) {
      right += +numberStr[i];
    } else {
      left += +numberStr[i];
    }
  }
  return left === right ? "LUCKY" : "READY";
}

console.log(solution(input));
