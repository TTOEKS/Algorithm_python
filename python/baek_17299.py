if __name__=="__main__":
  N = int(input())
  arr = list(map(int, input().split()))

  count = [0] * 1000001
  stack = []
  res = [-1] * N

  for i in range(N):
    count[arr[i]] += 1

  for i in range(N):
    while stack and count[arr[stack[-1]]] < count[arr[i]]:
      res[stack.pop()] = arr[i]
    stack.append(i)

  print(" ".join(map(str, res)))

  
  
