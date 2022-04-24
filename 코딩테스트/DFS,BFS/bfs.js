// const bfs = (graph, startNode) => {
//   let visited = [];
//   let needVisit = [];

//   needVisit.push(startNode);

//   while (needVisit.length !== 0) {
//     const node = needVisit.shift();
//     if (!visited.includes(node)) {
//       visited.push(node);
//       needVisit = [...needVisit, ...graph[node]];
//     }
//   }
//   return visited;
// };

// const graph = {
//   A: ["B", "C"],
//   B: ["A", "D"],
//   C: ["A", "G", "H", "I"],
//   D: ["B", "E", "F"],
//   E: ["D"],
//   F: ["D"],
//   G: ["C"],
//   H: ["C"],
//   I: ["C", "J"],
//   J: ["I"],
// };

// console.log(bfs(graph, "A"));

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
