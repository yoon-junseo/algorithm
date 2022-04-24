const bfs = (graph, start, visited) => {
  const queue = [];

  visited[start] = true;

  queue.push(start);

  while (queue.length !== 0) {
    const v = queue.shift();
    console.log(v);

    for (const i of graph[v]) {
      if (!visited[i]) {
        queue.push(i);
        visited[i] = true;
      }
    }
  }
};

const graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7],
];

const visited = new Array(9).fill(false);

bfs(graph, 1, visited);
