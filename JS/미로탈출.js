<<<<<<< Updated upstream
function solution(N, M, maze) {
  const graph = maze
    .split("\n")
    .map((row) => row.split("").map((item) => Number(item)));

  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  const queue = [];

=======
const solution = (N, M, maze) => {
  const graph = maze.split("\n").map((v) => {
    v = v.split("").map((m) => Number(m));
    return v;
  });
  const queue = [];

  // 상, 하, 좌, 우
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

>>>>>>> Stashed changes
  queue.push([0, 0]);

  while (queue.length !== 0) {
    const [x, y] = queue.shift();

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

<<<<<<< Updated upstream
      if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
        continue;
      }
=======
      if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;

      if (graph[nx][ny] === 0) continue;
>>>>>>> Stashed changes

      if (graph[nx][ny] === 1) {
        graph[nx][ny] = graph[x][y] + 1;
        queue.push([nx, ny]);
      }
    }
  }
<<<<<<< Updated upstream

  console.log(graph[N - 1][M - 1]);
}

const maze = "101010\n111111\n000001\n111111\n111111";
const N = 5;
const M = 6;

solution(N, M, maze);
=======
  console.log(graph[N - 1][M - 1]);
};

const maze = "101010\n111111\n000001\n111111\n111111";

solution(5, 6, maze);
>>>>>>> Stashed changes
