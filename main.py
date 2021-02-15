import sys
input=sys.stdin.readline

def f(N):
  if N<=1:
    return 1
  else: return (N*f(N-1))


N, K=map(int, input().split())


print(round(f(N)/(f(K)*f(N-K))))
