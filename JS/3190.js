const input = require("fs").readFileSync("./ex.txt").toString().split("\n");

function findApple(applePositionList, nx, ny) {
  return applePositionList.findIndex(([x, y]) => nx === x && ny === y);
}

function findSnake(snakePosition, nx, ny) {
  return snakePosition.findIndex(([x, y]) => nx === x && ny === y);
}

function solution(N, K, applePositionList, L, directionInfoList) {
  const snakePosition = [[1, 1]];
  const DIRECTION = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  let [curX, curY] = [1, 1];
  let directionIndex = 0;
  let time = 0;

  while (true) {
    // 방향 설정
    if (directionInfoList[0] && Number(directionInfoList[0][0]) === time) {
      const [_, command] = directionInfoList.shift();

      if (command.trim() === "D") {
        directionIndex = (directionIndex + 1) % 4;
      } else {
        directionIndex--;
        if (directionIndex < 0) {
          directionIndex += 4;
        }
      }
    }
    time++;

    const [dx, dy] = DIRECTION[directionIndex];
    const [nx, ny] = [curX + dx, curY + dy];

    // 벽꿍
    if (nx > N || nx < 1 || ny > N || ny < 1) {
      console.log(time);
      return;
    }

    const snakeIndex = findSnake(snakePosition, nx, ny);

    // 자기 몸에 꿍
    if (snakeIndex > -1) {
      console.log(time);
      return;
    }

    snakePosition.push([nx, ny]);

    const appleIndex = findApple(applePositionList, nx, ny);

    if (appleIndex > -1) {
      applePositionList.splice(appleIndex, 1);
    } else {
      snakePosition.shift();
    }

    curX = nx;
    curY = ny;
  }
}

const N = Number(input[0]);
const K = Number(input[1]);
const applePositionList = input
  .slice(2, 2 + K)
  .map((v) => v.split(" ").map((v) => Number(v)));
const L = Number(input[2 + K]);
const directionInfoList = input.slice(3 + K).map((v) => v.split(" "));

solution(N, K, applePositionList, L, directionInfoList);
