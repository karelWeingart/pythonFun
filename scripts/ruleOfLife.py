from graphics import *
import time

#this is representation of one cell
class GameRectangle:
    
    def __init__(self,win,ltPoint, height, width, color, shown=False, changed=False ):
        self.ltPoint=ltPoint
        self.rbPoint=Point(ltPoint.getX()+width,ltPoint.getY()+height)
        self.shown=shown
        self.changed=changed
        self.win=win
        self.rect=Rectangle(self.ltPoint,self.rbPoint)
        self.rect.setFill(color)
        self.rect.undraw()

    def changeDrawState(self):
        self.changed=True

    def repaint(self):
        if self.changed==True:
            if self.shown==False:                
                self.rect.draw(self.win)
            else:                
                self.rect.undraw()
            self.changed=False
            self.shown=not self.shown
        print(str(self.changed)+"::"+str(self.shown))

#represents the matrix with all the cells in array
class LifeMatrix:
    
    def __init__(self):
        self.cells=[]

    def getNeigbourhods(self,x,y):
        nCells=[]
        if y>0:
            if x>0:
                nCells.append(self.cells[x-1][y-1])
            nCells.append(self.cells[x][y-1])
            if x<29:
                nCells.append(self.cells[x+1][y-1])
        if x>0:
            nCells.append(self.cells[x-1][y])
        if x<29:
            nCells.append(self.cells[x+1][y])
        if y<29:
            if x>0:
                nCells.append(self.cells[x-1][y+1])
            nCells.append(self.cells[x][y+1])
            if x<29:
                nCells.append(self.cells[x+1][y+1])
        
        return nCells

    def applyLifeRulesToCell(self,x,y):
        neighboroughs=self.getNeigbourhods(x,y)
        liveCells = 0
        for neigh in neighboroughs:
            if neigh.shown == True:
                liveCells+=1
        
        if self.cells[x][y].shown==False:
            if liveCells==3:
                print(str(x)+"::"+str(y)+" will be shown")
                self.cells[x][y].changeDrawState()
              

        if self.cells[x][y].shown==True:
            if liveCells>3 or liveCells<2:
                print(str(x)+"::"+str(y)+" will be hidden")
                self.cells[x][y].changeDrawState()

    def processLifeMatrix(self):

        i=0
        for row in self.cells:
            a=0
            for cell in row:
                self.applyLifeRulesToCell(a,i)
                a+=1
            i+=1

    def repaint(self):
        for row in self.cells:
            for cell in row:
                cell.repaint() 

        

              





lifeMatrix = LifeMatrix()
def main():
    win = GraphWin("Rules of Life", 300, 300)
    win.setBackground("black")
    plotMatrix(win)
    plotMatrix(win, "vertical")
    initRects(win)
    lifeMatrix.cells[10][12].changeDrawState()
    lifeMatrix.cells[10][13].changeDrawState()
    #lifeMatrix.cells[10][14].changeDrawState()
    lifeMatrix.cells[11][14].changeDrawState()
    lifeMatrix.cells[11][13].changeDrawState()
    lifeMatrix.cells[11][12].changeDrawState()
    lifeMatrix.cells[12][12].changeDrawState()
    lifeMatrix.cells[12][13].changeDrawState()
    lifeMatrix.cells[12][14].changeDrawState()
    lifeMatrix.cells[14][14].changeDrawState()
    lifeMatrix.cells[9][12].changeDrawState()
    lifeMatrix.cells[9][13].changeDrawState()
    lifeMatrix.cells[9][15].changeDrawState()
    lifeMatrix.cells[9][16].changeDrawState()
    lifeMatrix.cells[9][17].changeDrawState()
    lifeMatrix.cells[10][18].changeDrawState()
    lifeMatrix.cells[11][18].changeDrawState()
    lifeMatrix.cells[12][18].changeDrawState()

    #lifeMatrix.showNeigbourhods(10,12)
    lifeMatrix.repaint()
    time.sleep(0.5)
    while True:
        lifeMatrix.processLifeMatrix()
        lifeMatrix.repaint()
        #time.sleep(0.5)
        win.getMouse() # pause for click in window
    win.close()

def initRects(win, stepX=10, stepY=10, color="white", rows=31, cols=31):
    for i in range(rows-1):
        row=[]
        for a in range(cols-1):
            gRectangle=GameRectangle(win,Point(i*stepY,a*stepX),stepX,stepY,color, False,False)
            row.append(gRectangle)
        lifeMatrix.cells.append(row)


def plotMatrix(win, direction = "horizontal", step = 10, max = 300):
    linePos = 0
    xPoint = 0
    yPoint = 0
    while linePos < 300:        
        if direction == "horizontal":
            yPoint=linePos
            endPoint = Point(max, yPoint)
        else:
            xPoint=linePos
            endPoint = Point(xPoint, max)
        line = Line(Point(xPoint, yPoint), endPoint)
        line.setOutline("yellow")
        line.draw(win)
        linePos += step
main()
