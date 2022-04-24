const getPermutations = (arr, selectNumber) => {
  const results = [];

  if (selectNumber === 1) {
    return arr.map((el) => [el]);
  }

  arr.forEach((fixed, index) => {
    const rest = [...arr.slice(0, index), ...arr.slice(index + 1)];
    const permutations = getPermutations(rest, selectNumber - 1);
    const attached = permutations.map((el) => [fixed, ...el]);

    results.push(...attached);
  });

  return results;
};

const arr = [1, 2, 3, 4];

console.log(getPermutations(arr, 2));
