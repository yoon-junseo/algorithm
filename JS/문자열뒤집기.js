function solution(s) {
  let oneToZeroCount = 0;
  let zeroToOneCount = 0;
  const arr = s.split("").map((a) => Number(a));

  if (arr[0] === 0) {
    zeroToOneCount++;
  } else {
    oneToZeroCount++;
  }

  for (let i = 1; i < arr.length; i++) {
    if (arr[i - 1] !== arr[i]) {
      if (arr[i] === 1) {
        zeroToOneCount++;
      } else {
        oneToZeroCount++;
      }
    }
  }

  console.log(Math.min(oneToZeroCount, zeroToOneCount));
}

solution("0001100");
