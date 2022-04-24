// const dfs = (graph, startNode) => {
//   let needVisitStack = [];
//   let visitedQueue = [];

//   needVisitStack.push(startNode);

//   while (needVisitStack.length !== 0) {
//     const node = needVisitStack.pop();
//     if (!visitedQueue.includes(node)) {
//       visitedQueue.push(node);
//       needVisitStack = [...needVisitStack, ...graph[node]];
//     }
//   }
//   return visitedQueue;
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

// console.log(dfs(graph, "A"));

const dfs = (graph, v, visited) => {
  visited[v] = true;
  console.log(v);

  for (const i of graph[v]) {
    if (!visited[i]) {
      dfs(graph, i, visited);
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

dfs(graph, 1, visited);
