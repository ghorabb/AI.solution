from pyamaze import maze,agent,COLOR
def DFS(m):
    start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dSearch=[start]
    dfsPath={}
    while len(frontier)>0:
        currCell=frontier.pop()
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dSearch.append(childCell)
                dfsPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return [dSearch,fwdPath]
    


if __name__=='__main__':
    m=maze(15,15)
    m.CreateMaze()
    dSearch,fwdPath=DFS(m)
    a=agent(m,shape="arrow",footprints=True,color=COLOR.blue,filled=True)
    b=agent(m,shape="arrow",footprints=True,color=COLOR.green,filled=True)
    m.tracePath({a:dSearch} , delay=20,kill=True)
    m.tracePath({b:fwdPath} , delay=50)
    
    m.run()