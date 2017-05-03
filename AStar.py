

# 'o' represents for open, 'x' for wall, 'm' for mouse and 'c' for cheese
x,o,m,c = 'x', 'o','m','c'
R0 = [o,o,o,o]
R1 = [m,x,o,o]
R2 = [x,x,o,o]
R3 = [c,o,o,o]
M = [R0,R1,R2,R3]



# If M is a Maze and i and j are integers isGoal(M,i,j) iff (i,j) is the position of cheese in M
def G(N):
    (i,j) = N
    if (i >= 4 or j >=4):
        return False
    return M[i][j] == 'c'


    
# if M is a maze and p is a path in M, then children(p,M)
# is the list of all paths in M that extend p by one
# open cell adjacent to the last member of p. 

def children(p,M):
  c = p[len(p)-1]
  (x,y) = c
  c1,c2,c3,c4 = (x+1,y), (x-1,y),(x,y+1),(x,y-1)
  Res = []
  for e in [c1,c2,c3,c4]:
      if open(e,M):
          Res=Res+[p+[e]]
  return Res



# If M is a maze and e is a pair of integers, then open(e,M)
# iff e is a cell in M that doesn't contain 'x'
def open(e,M):
  (i,j) = e
  maxi = len(M)-1
  maxj = len(M[0])-1
  return(0 < i <= maxi and 0 < j <= maxj and M[i][j] in {'o','m','c'})


def AStar(N):
    open = [N]
    closed = []
    #invariant: AStar(N) is the shortest distance (in terms of open nodes) from the mouse to the cheese
    while (not open == []):
        X = open.pop()
        if (G(X)):
            return open
        else:
            closed.append(X)
            #insert the children of X not in closed into open
            if(not children(X,M) in open):
                open.append(children(X,M))
        return None
        
