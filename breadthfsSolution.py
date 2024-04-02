from pyamaze import maze,agent,COLOR
def BFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    frontier=[start]
    explored=[start]
    bSearch=[start]
    bfsPath={}
    while len(frontier)>0:
        currCell=frontier.pop(0)
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bSearch.append(childCell)
                bfsPath[childCell]=currCell

    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    
    return [bSearch,fwdPath]

if __name__=='__main__':
    m=maze(15,15)
    m.CreateMaze(loopPercent=10)
    bSearch,fwdPath=BFS(m)
    a=agent(m,shape="square",footprints=True,color=COLOR.blue,filled=True)
    b=agent(m,shape="square",footprints=True,color=COLOR.red,filled=True)
    m.tracePath({a:bSearch} , kill=True,delay=20 )
    m.tracePath({b:fwdPath} , delay=50 )
    m.run()