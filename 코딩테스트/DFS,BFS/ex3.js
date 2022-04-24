const dfs = (graph, N, M, x, y) => {
  if (x < 0 || x >= N || y < 0 || y >= M) return false;

  if (graph[x][y] === 0) {
    graph[x][y] = 1;

    dfs(graph, N, M, x - 1, y);
    dfs(graph, N, M, x + 1, y);
    dfs(graph, N, M, x, y - 1);
    dfs(graph, N, M, x, y + 1);
    return true;
  }
  return false;
};

const solution = (N, M, ices) => {
  const graph = [];
  let result = 0;
  ices.split("\n").forEach((ice) => {
    ice = ice.split("").map((i) => Number(i));
    graph.push(ice);
  });

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (dfs(graph, N, M, i, j)) {
        result += 1;
      }
    }
  }
  console.log(result);
};

const ices = "00110\n00011\n11111\n00000";

solution(4, 5, ices);
