const input = require("fs").readFileSync("./ex.txt").toString().trim();

function solution(input) {
  const regStr = /[^a-zA-Z]/g;
  const regNum = /[^0-9]/g;

  const str = input.replace(regStr, "");
  const num = input.replace(regNum, "");

  const answer =
    str.split("").sort().join("") +
    num.split("").reduce((acc, cur) => Number(acc) + Number(cur), 0);
  console.log(answer);
}

solution(input);
