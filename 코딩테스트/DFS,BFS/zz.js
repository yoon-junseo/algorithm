// 상 하 좌 우
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

const bfs = (graph, N, M, x, y) => {
  const queue = [];
  queue.push([x, y]);

  while (queue.length !== 0) {
    const [x, y] = queue.shift();
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
        continue;
      }

      if (graph[nx][ny] === 1) {
        graph[nx][ny] += graph[x][y];
        queue.push([nx, ny]);
      }
    }
  }
};

function solution(N, M, maze) {
  const graph = [];
  maze.split("\n").forEach((ice) => {
    ice = ice.split("").map((i) => Number(i));
    graph.push(ice);
  });

  bfs(graph, N, M, 0, 0);
  console.log(graph[N - 1][M - 1]);
}

const maze = "101010\n111111\n000001\n111111\n111111\n";

solution(5, 6, maze);
