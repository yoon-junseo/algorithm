function solution(str) {
  const arr = str.split("").map((a) => Number(a));
  let result = arr[0];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= 1 || result <= 1) {
      result += arr[i];
    } else {
      result *= arr[i];
    }
  }
  console.log(result);
}

solution("567");
