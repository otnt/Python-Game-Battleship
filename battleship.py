# -*- coding: cp936 -*-
import pygame,sys
from graphics_menu import *
from random import *
from math import *
def drawMap():
	global table1
	global table2
	global win
	for i in range(10):
		for j in range(15):
			if table2[i][j]:
				table1[i][j].undraw()
				targetX = 20 * (j + 1) + 10 + 5.0 * (j / 10.0)
				targetY = 20 * (i + 1) + 12 + 3.0 * (i / 15.0)
				table1[i][j].move(targetX - table1[i][j].anchor.x, targetY - table1[i][j].anchor.y)
				table1[i][j].draw(win)

def drawMapcom():
	global table1com
	global table2com
	global win
	for i in range(10):
		for j in range(15):
			if table2com[i][j]:
				table1com[i][j].undraw()
				targetX = 20 * (j + 1) + 10 + 5.0 * (j / 10.0)
				targetY = 20 * (i + 1) + 12 + 3.0 * (i / 15.0)
				table1com[i][j].move(targetX - table1com[i][j].anchor.x, targetY - table1com[i][j].anchor.y)
				table1com[i][j].draw(win)

def drawMapPut():
	global table1put
	global table2put
	global win
	for i in range(10):
		for j in range(15):
			if table2put[i][j]:
				table1put[i][j].undraw()
				targetX = 20 * (j + 1) + 10 + 5.0 * (j / 10.0)
				targetY = 20 * (i + 1) + 12 + 3.0 * (i / 15.0)
				table1put[i][j].move(targetX - table1put[i][j].anchor.x, targetY - table1put[i][j].anchor.y)
				table1put[i][j].draw(win)

def createMatrix(num):
	m0 = []
	for i in range(10):
		m0.append([])
		for j in range(15):
			m0[i].append(num)
	return m0

def checkh(px, py, l):
	global table0
	if py + l > 15:
		return False
	for i in range(l):
		if table0[px][py + i]:
			return False
	return True

def checkv(px, py, l):
	global table0
	if px + l > 10:
		return False
	for i in range(l):
		if table0[px + i][py]:
			return False
	return True

def placeh(px, py, ii):
	global table0
	global shipSize
	for i in range(shipSize[ii]):
		table0[px][py + i] = ii

def placev(px, py, ii):
	global table0
	global shipSize
	for i in range(shipSize[ii]):
		table0[px + i][py] = ii

def placehcom(px, py, ii):
	global table0com
	global shipSizecom
	for i in range(shipSizecom[ii]):
		table0com[px][py + i] = ii

def placevcom(px, py, ii):
	global table0com
	global shipSizecom
	for i in range(shipSizecom[ii]):
		table0com[px + i][py] = ii

def placehuser(px, py, ii):
	global table0user
	global shipSize
	for i in range(shipSize[ii]):
		table0user[px][py + i] = ii

def placevuser(px, py, ii):
	global table0user
	global shipSize
	for i in range(shipSize[ii]):
		table0user[px + i][py] = ii

def makeup(st):
	if(len(st) == 3):
		return st
	elif len(st) == 2:
		return " " + st
	elif len(st) == 1:
		return "  " + st
	else:
		return st
def checkPut(shipnum):
        global table2put
        default = [False,False,False,False,False]
        #检查长度，必须在2-6之间,并记录下最后一艘船的位置信息
        size = 0
        row = 0
        column = 0
        for tx in range(10):
                for ty in range(15):
                        if(table2put[tx][ty] == shipnum):
                                size += 1
                                row = tx
                                column=ty
                                
        if(not (2<=size<=6) ):
                return default

        #检查是否在同一行， 或者同一列
        isOneRow = True
        isOneColumn = True
        for tx in range(10):
                for ty in range(15):
                        if(table2put[tx][ty] == shipnum):
                                if(not (row == tx)):
                                        isOneRow = False;
        for tx in range(10):
                for ty in range(15):
                        if(table2put[tx][ty] == shipnum):
                                if(not (column == ty)):
                                        isOneColumn = False;

        if(not (isOneRow or isOneColumn) ):
                return default

        #检查在这行，或这列中，是否相邻
        array = []
        for tx in range(10):
                for ty in range(15):
                        if(table2put[tx][ty] == shipnum):
                                if(isOneRow):
                                        array.append(ty)
                                if(isOneColumn):
                                        array.append(tx)
        array.sort()
        length =  len(array)
        first = array[0]
        last = array[length-1]
        if( (first+length) == (last+1)):
                if(isOneRow):
                        vOrh = 0
                        px = row
                        py = first
                elif(isOneColumn):
                        vOrh = 1
                        px = first
                        py = column
                info = [True,length,vOrh,px,py]
                return info;
        else:
                return default;




def userPutBattleships():
        global win
        global totalShips
        global restCount
        global table1put
        global table2put
        global shipSize
        global restShips
        global restCells
        #table2put = createMatrix(0)
        
        shipChoose = Text(Point(410,50),"How many battleships?")
        shipChoose.draw(win)
        shipNumber = Text(Point(410,100),"3              4              5")
        shipNumber.draw(win) 

        while(1):
                point = win.getMouse()
                px = int(floor(point.y / 20.4)) - 1
                py = int(floor(point.x / 20.4)) - 1
                if(3<=px<=4 and 15<=py<=16):
                        a=3
                        break
                elif(3<=px <=4 and 18<= py <=19):
                        a=4
                        break
                elif(3<=px <=4 and 21<=py <=22):
                        a=5
                        break
                else:
                        continue
        shipChoose.setText("Your ship quantity is")
        shipNumber.setText(str(a))
        totalShips = a
        restCount = totalShips
        
        shipPut = Text(Point(410,150),"")
        shipPut.draw(win)
        makesure = Text(Point(410,200),"OK")
        makesure.draw(win)
        table2put = createMatrix(0)
        for shipnum in range (1,totalShips+1):
                shipPut.setText("Set ship"+str(shipnum))
                shipColor[shipnum] = randrange(0, 5)

                while(1):
                        point = win.getMouse()
                        px = int(floor(point.y / 20.4)) - 1
                        py = int(floor(point.x / 20.4)) - 1
                        #print px,py
                        if(7<=px<=9 and 18<=py<=20):#click OK
                                info = checkPut(shipnum)
                                if(info[0]):
                                        shipSize[shipnum] = info[1]

                                        if (info[2]):
                                                placevuser(info[3], info[4], shipnum)
                                                placev(info[3], info[4], shipnum)
                                        else:
                                                #print "info here: ",info[3], info[4]
                                                placehuser(info[3], info[4], shipnum)
                                                placeh(info[3], info[4], shipnum)
                                        restShips[shipSize[shipnum]] += 1
                                        restCells[shipnum] = shipSize[shipnum]
                                        
                                        break;
                                else:
                                        for t2x in range (10):
                                                for t2y in range (15):
                                                        if(table2put[t2x][t2y] == shipnum):
                                                                table1put[t2x][t2y].undraw()
                                                                table1put[t2x][t2y] = 0
                                                                table2put[t2x][t2y] = 0
                                        #table2put = createMatrix(0);                                        
                                        continue;                                        
                        elif(px < 0 or py < 0 or px > 9 or py > 14):#out of range
                                continue
                        elif(table2put[px][py] > 0):#already set
                                print "yes"
                                continue
                        else:           #set battleship
                                table2put[px][py] = shipnum
                                table1put[px][py] = Image(Point(-30, -30), color0[shipColor[shipnum]])
                                table1put[px][py].draw(win)
                                drawMapPut();
                                
                
        
        shipPut.setText("Remember Your Ships")
        makesure.setText("Continue")
        point = win.getMouse()
        px = int(floor(point.y / 20.4)) - 1
        py = int(floor(point.x / 20.4)) - 1
        if(7<=px<=9 and 16<=py<=21):
                shipChoose.undraw()
                shipNumber.undraw()
                shipPut.undraw()
                makesure.undraw()
                for t2x in range (10):
                        for t2y in range (15):
                                if(table2put[t2x][t2y] > 0):
                                        table1put[t2x][t2y].undraw()
                                        table1put[t2x][t2y] = 0

#---------- init starts
wWidth = 505
wHeight = 290
win = GraphWin("4399 TOP 1", 505, 290)
while 1:
        backImage = Image(Point(wWidth / 2, wHeight / 2), "start.gif")
        backImage.draw(win)
        p = win.getMouse()
        if p.x>390 and p.x<470:
                if p.y>215 and p.y<265:
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load("start.wav")
                        pygame.mixer.music.play()
                        break
print("game begin now")                
backImage = Image(Point(wWidth / 2, wHeight / 2), "background.gif")
backImage.draw(win)
# cyan red blue green magenta
color0 = ["cyan0.gif", "red0.gif", "blue0.gif", "green0.gif", "magenta0.gif"]
color1 = ["cyan1.gif", "red1.gif", "blue1.gif", "green1.gif", "magenta1.gif"]

isReview = False
#总得大循环
while(1): 
        # table0 - mark
        # 0      blank
        # 1-8    undiscovered ship cells
        # 11-18  discovered ship cells
        # -1     missed missiles
        table0 = createMatrix(0)#真正存储战舰摆放信息

        table0user = createMatrix(0)#存储用户的战舰摆放信息
        table2 = createMatrix(1)#记录投掷炸弹情况
        table1 = createMatrix(0)#画图
        table1put = createMatrix(0)#画图

        table0com = createMatrix(0)#存储电脑的战舰摆放信息
        table2com = createMatrix(1)#记录投掷炸弹情况
        table1com = createMatrix(0)#画图


        for tmp in range(10):
                for tmp0 in range(15):
                        table1[tmp][tmp0] = Image(Point(-20, -20), "test.gif")
                        table1[tmp][tmp0].draw(win)

        for tmp in range(10):
                for tmp0 in range(15):
                        table1com[tmp][tmp0] = Image(Point(-20, -20), "test.gif")
                        table1com[tmp][tmp0].draw(win)		
        drawMap()
        drawMapcom()

        table2 = createMatrix(0)
        table2com = createMatrix(0)
        table2put = createMatrix(0)

        restShips = [0, 0, 0, 0, 0, 0, 0,0,0,0]
        restCells = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        shipSize = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        shipColor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        totalShips = 0
        restCount = totalShips

        restShipscom = [0, 0, 0, 0, 0, 0, 0,0,0,0]
        restCellscom = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        shipSizecom = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        shipColorcom = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        totalShipscom = 0#保证电脑和用户战舰数量相同
        restCountcom = totalShipscom

        shipName = ["", "ROWBOAT", "SUBMARINE", "SPEEDBOAT", "BATTLESHIP", "LONGBOAT"]

        #用户摆放战舰
        userPutBattleships()
        totalShipscom = restCountcom = restCount = totalShips


        restShips,restShipscom = restShipscom,restShips
        restCells,restCellscom = restCellscom,restCells
        shipSize,shipSizecom = shipSizecom,shipSize
        shipColor,shipColorcom = shipColorcom,shipColor
        table2,table2com = table2com,table2
        table0user,table0com = table0com,table0user
        table1,table1com = table1com,table1

        

        #初始化生成用户和电脑的战舰
        for i in range(1, totalShips + 1):
                shipSize[i] = shipSizecom[i]#大小都一样
                shipColor[i] = randrange(0, 5)
                horv = randrange(0, 2)
                posx = randrange(0, 10)
                posy = randrange(0, 15)
                while not ((horv == 0 and checkh(posx, posy, shipSize[i])) or (horv == 1 and checkv(posx, posy, shipSize[i]))):
                        horv = randrange(0, 2)
                        posx = randrange(0, 10)
                        posy = randrange(0, 15)
                if horv:
                        placevuser(posx, posy, i)
                        placev(posx, posy, i)
                else:
                        placehuser(posx, posy, i)
                        placeh(posx, posy, i)
                restShips[shipSize[i]] += 1
                restCells[i] = shipSize[i]

        
        #backup for review
        table0review = createMatrix(0)
        table0userreview = createMatrix(0)
        table0comreview = createMatrix(0)
        table2review = createMatrix(0)
        table2comreview = createMatrix(0)
        
        for tmp in range(10):
                for tmp0 in range(15):
                        table0review[tmp][tmp0] = table0[tmp][tmp0]
                        table0userreview[tmp][tmp0] = table0user[tmp][tmp0]
                        table0comreview[tmp][tmp0] = table0com[tmp][tmp0]
                        table2review[tmp][tmp0] = table2[tmp][tmp0]
                        table2comreview[tmp][tmp0] = table2com[tmp][tmp0]
        
        
##        restCells,restCellscom = restCellscom,restCells
##        shipSize,shipSizecom = shipSizecom,shipSize
##        shipColor,shipColorcom = shipColorcom,shipColor
##        table2,table2com = table2com,table2
##        table0user,table0com = table0com,table0user
##        table1,table1com = table1com,table1

        restShipsreview = []
        restShipscomreview = []
        restCellsreview = []
        restCellscomreview = []
        shipSizereview = []
        shipSizecomreview = []
        shipColorreview = []
        shipColorcomreview = []
        for tmp in range(10):
                restShipsreview.append(0)
                restShipsreview[tmp] = restShips[tmp]
                restShipscomreview.append(0)
                restShipscomreview[tmp] = restShipscom[tmp]
                restCellsreview.append(0)
                restCellsreview[tmp] = restCells[tmp]
                restCellscomreview.append(0)
                restCellscomreview[tmp] = restCellscom[tmp]
                shipSizereview.append(0)
                shipSizereview[tmp] = shipSize[tmp]
                shipSizecomreview.append(0)
                shipSizecomreview[tmp] = shipSizecom[tmp]
                shipColorreview.append(0)
                shipColorreview[tmp] = shipColor[tmp]
                shipColorcomreview.append(0)
                shipColorcomreview[tmp] = shipColorcom[tmp]


        #restShipsreview = 


        restCountreview = restCount
        restCountcomreview = restCountcom
        #print "  is table0review"
        #print restCountreview


        ##for i in range(1, totalShipscom + 1):
        ##	shipSizecom[i] = shipSize[i]#大小都一样
        ##	shipColor[i] = randrange(0, 5)#颜色可不同
        ##	horv = randrange(0, 2)
        ##	posx = randrange(0, 10)
        ##	posy = randrange(0, 15)
        ##	while not ((horv == 0 and checkh(posx, posy, shipSize[i])) or (horv == 1 and checkv(posx, posy, shipSize[i]))):
        ##		horv = randrange(0, 2)
        ##		posx = randrange(0, 10)
        ##		posy = randrange(0, 15)
        ##	if horv:
        ##		placevcom(posx, posy, i)
        ##		placev(posx, posy, i)
        ##	else:
        ##		placehcom(posx, posy, i)
        ##		placeh(posx, posy, i)
        ##	restShipscom[shipSizecom[i]] += 1
        ##	restCellscom[i] = shipSizecom[i]
        ##

                
        print """I, the masterful computer, have hidden some battleships on the board
        above. It is your mission to try to sink my battleships with the %d
        missiles I spot you. You will specify which cells on the board that
        you want to fire the missiles upon by clicking the mouse.  After
        each missile is fired, I will tell you if it hit a ship or not.  I
        will also let you know if you have completely sunk the ship, which
        happens when you've hit all of the ship.  The game ends when you run
        out of missiles, or when you sink all of the ships."""
        print "\n\nuser has to hit (computer's battleships)\n"
        for i in range(10):
                for j in range(15):
                        print table0user[i][j],
                print ""
        print "\n\ncomputer has to hit (user's battleships)\n"
        for i in range(10):
                for j in range(15):
                        print table0com[i][j],
                print ""
        print "\n\nboth sides' battleships\n"
        for i in range(10):
                for j in range(15):
                        print table0[i][j],
                print ""
                
        restMissile = 100
        hitMissile = 0
        hitrate = 0

        restMissilecom = restMissile
        hitMissilecom = 0
        hitratecom = 0

        conditionText = Text(Point(410,25),"Player's condition:")
        conditionText.draw(win)
        leftMissileText = Text(Point(410, 50), "Missiles left: 100")
        leftMissileText.draw(win)
        shipsToSinkText = Text(Point(410, 75), "Ships to sink: " + str(restCount))
        shipsToSinkText.draw(win)
        hitRate = Text(Point(410, 100), "Hit rate:  0%")
        hitRate.draw(win)

        conditionTextcom = Text(Point(410,140),"Computer's condition:")
        conditionTextcom.draw(win)
        leftMissileTextcom = Text(Point(410, 165), "Missiles left: 100")
        leftMissileTextcom.draw(win)
        shipsToSinkTextcom = Text(Point(410, 190), "Ships to sink: " + str(restCount))
        shipsToSinkTextcom.draw(win)
        hitRatecom = Text(Point(410, 215), "Hit rate:  0%")
        hitRatecom.draw(win)


        caption = Text(Point(wWidth / 2, 243), "Click on a square to fire.")
        caption.draw(win)        

        #重放功能
        replayPlayer = []
        replayComputer = []

        # Game Starts
        #win.getMouse()
        while restMissile and restCount and restMissilecom and restCountcom:
                point = win.getMouse()
                px = int(floor(point.y / 20.4)) - 1
                py = int(floor(point.x / 20.4)) - 1
                if(px < 0 or py < 0 or px > 9 or py > 14):
                        caption.setText("That's not a valid square, try again.")
                        continue
                table2 = createMatrix(0)
                if(table0[px][py] < 0 or table0[px][py] > 10):
                        caption.setText("Already been hit, try again.")
                        continue
                else:
                        if(table0[px][py] == 0):
                                pygame.mixer.music.load("3.wav")
                                pygame.mixer.music.play()
                                caption.setText("Haha! Missed me.")
                                table2[px][py] = 1
                                restMissile -= 1
                                table1[px][py] = Image(Point(-30, -30), "cross.gif")
                                table1[px][py].draw(win)
                                table0[px][py] = -1
                        elif(0<table0user[px][py] and table0user[px][py]<10):
                                pygame.mixer.music.load("1.wav")
                                pygame.mixer.music.play()
                                tship = table0[px][py]
                                restMissile -= 1
                                table0[px][py] += 10
                                table0user[px][py] += 10
                                restCells[tship] -= 1
                                hitMissile += 1
                                if(restCells[tship] > 0):
                                        table2[px][py] = 1
                                        table1[px][py] = Image(Point(-30, -30), color0[shipColor[tship]])
                                        table1[px][py].draw(win)
                                        caption.setText("Direct hit!")
                                else:
                                        for ti in range(10):
                                                for tj in range(15):
                                                        if(table0user[ti][tj] == table0[px][py]):
                                                                table2[ti][tj] = 1
                                                                table1[ti][tj].undraw()
                                                                table1[ti][tj] = Image(Point(-30, -30), color1[shipColor[tship]])
                                                                table1[ti][tj].draw(win)
                                        restCount -= 1
                                        restShips[shipSize[tship]] -= 1
                                        caption.setText("You sunk one " + shipName[shipSize[tship]] + "! " + str(restShips[shipSize[tship]]) + shipName[shipSize[tship]] + "s left!")
                        else:
                               caption.setText("That's your own ship!")
                               continue;
                replayPlayer.append(px)
                replayPlayer.append(py)
                leftMissileText.setText("Missiles left: " + makeup(str(restMissile)))
                shipsToSinkText.setText("Ships to sink: " + str(restCount))
                hitrate = (hitMissile*100)/(100-restMissile)
                hitRate.setText("Hit rate: " + makeup(str(hitrate)) + "%")
                
        #################################################################################################

                while(1):
                        px = randrange(0,10)
                        py = randrange(0,15)

                        table2com = createMatrix(0)
                        if(table0[px][py] < 0 or table0[px][py] > 10):
                                continue
                        else:
                                if(table0[px][py] == 0):
                                        pygame.mixer.music.load("3.wav")
                                        pygame.mixer.music.play()
                                        caption.setText("I missed one, but next time I won't make mistake!")
                                        table2com[px][py] = 1
                                        restMissilecom -= 1
                                        table1com[px][py] = Image(Point(-30, -30), "circle.gif")
                                        table1com[px][py].draw(win)
                                        table0[px][py] = -1
                                        break
                                elif(0<table0com[px][py] and table0com[px][py]<10):
                                        pygame.mixer.music.load("1.wav")
                                        pygame.mixer.music.play()
                                        tship = table0[px][py]
                                        restMissilecom -= 1
                                        table0[px][py] += 10
                                        table0com[px][py] += 10
                                        restCellscom[tship] -= 1
                                        hitMissilecom += 1
                                        if(restCellscom[tship] > 0):
                                                table2com[px][py] = 1
                                                table1com[px][py] = Image(Point(-30, -30), color0[shipColor[tship]])
                                                table1com[px][py].draw(win)
                                                caption.setText("Computer direct hit!")
                                        else:
                                                for ti in range(10):
                                                        for tj in range(15):
                                                                if(table0com[ti][tj] == table0[px][py]):
                                                                        table2com[ti][tj] = 1
                                                                        table1com[ti][tj].undraw()
                                                                        table1com[ti][tj] = Image(Point(-30, -30), color1[shipColor[tship]])
                                                                        table1com[ti][tj].draw(win)
                                                restCountcom -= 1
                                                restShipscom[shipSizecom[tship]] -= 1
                                                caption.setText("Haha! I sunk one " + shipName[shipSize[tship]] + "! " + str(restShips[shipSize[tship]]) + shipName[shipSize[tship]] + "s left!")
                                        break
                                else:
                                       continue;
                replayComputer.append(px)
                replayComputer.append(py)
                leftMissileTextcom.setText("Missiles left: " + makeup(str(restMissilecom)))
                shipsToSinkTextcom.setText("Ships to sink: " + str(restCountcom))
                hitratecom = (hitMissilecom*100)/(100-restMissilecom)
                hitRatecom.setText("Hit rate: " + makeup(str(hitratecom)) + "%")
                
        ####################################################################################################

                drawMap()
                drawMapcom()
        if (restCount==0 and restCountcom==0):
                caption.setText("Tie!")
        elif restCount:
                caption.setText("I, computer won!")
        else:
                caption.setText("You win!")

        #print "this is table0review again"
        #print restCountreview


        
        exitGame = Text(Point(wWidth / 4, 265), "EXIT")
        exitGame.draw(win)
        reviewGame = Text(Point(wWidth / 2, 265), "REVIEW")
        reviewGame.draw(win)
        restartGame = Text(Point(wWidth / 4 * 3, 265), "RESTART")
        restartGame.draw(win)
        while(1):
               
                point = win.getMouse()
                px = int(floor(point.y / 20.4)) - 1
                py = int(floor(point.x / 20.4)) - 1
                print px,py
                
                if(11<=px<=12 and 4<=py<=6):
                        win.close()
                        exit
                if(11<=px<=12 and 15<=py<=19):
                        conditionText.undraw()
                        leftMissileText.undraw()
                        shipsToSinkText.undraw()
                        hitRate.undraw()

                        conditionTextcom.undraw()
                        leftMissileTextcom.undraw()
                        shipsToSinkTextcom.undraw()
                        hitRatecom.undraw()

                        caption.undraw()
                        exitGame.undraw()
                        reviewGame.undraw()
                        restartGame.undraw()
        
                        table2 = createMatrix(1)#记录投掷炸弹情况
                        table2com = createMatrix(1)#记录投掷炸弹情况

                        for tmp in range(10):
                                for tmp0 in range(15):
                                        table1[tmp][tmp0].undraw()
                                        table1com[tmp][tmp0].undraw()
                        break;
                elif(11<=px<=12 and 10<=py<=12):
                        #initial replay
                        restMissile = 100
                        hitMissile = 0
                        hitrate = 0
                        restMissilecom = restMissile
                        hitMissilecom = 0
                        hitratecom = 0

                        leftMissileText.setText("Missiles left: 100")
                        shipsToSinkText.setText("Ships to sink: " + str(restCount))
                        hitRate.setText("Hit rate:  0%")

                        leftMissileTextcom.setText("Missiles left: 100")
                        shipsToSinkTextcom.setText("Ships to sink: " + str(restCount))
                        hitRatecom.setText("Hit rate:  0%")

                        caption.setText("Reviewing")

                        table2 = createMatrix(1)#记录投掷炸弹情况
                        table2com = createMatrix(1)#记录投掷炸弹情况

                        for tmp in range(10):
                                for tmp0 in range(15):
                                        table1[tmp][tmp0].undraw()
                                        table1com[tmp][tmp0].undraw()	

                        for tmp in range(10):
                                for tmp0 in range(15):
                                        table1[tmp][tmp0] = Image(Point(-20, -20), "test.gif")
                                        table1[tmp][tmp0].draw(win)

                        for tmp in range(10):
                                for tmp0 in range(15):
                                        table1com[tmp][tmp0] = Image(Point(-20, -20), "test.gif")
                                        table1com[tmp][tmp0].draw(win)		
                        drawMap()
                        drawMapcom()

                        table2 = createMatrix(0)
                        table2com = createMatrix(0)
                      
                        for tmp in range(10):
                                for tmp0 in range(15):
                                        table0[tmp][tmp0] = table0review[tmp][tmp0]
                                        table0user[tmp][tmp0] = table0userreview[tmp][tmp0]
                                        table0com[tmp][tmp0] = table0comreview[tmp][tmp0]
                                        table2[tmp][tmp0] = table2review[tmp][tmp0]
                                        table2com[tmp][tmp0] = table2comreview[tmp][tmp0]
                        
                        
                ##        restCells,restCellscom = restCellscom,restCells
                ##        shipSize,shipSizecom = shipSizecom,shipSize
                ##        shipColor,shipColorcom = shipColorcom,shipColor
                ##        table2,table2com = table2com,table2
                ##        table0user,table0com = table0com,table0user
                ##        table1,table1com = table1com,table1

                        for tmp in range(10):
                                restShips[tmp] = restShipsreview[tmp]
                                restShipscom[tmp] = restShipscomreview[tmp]
                                restCells[tmp] = restCellsreview[tmp]
                                restCellscom[tmp] = restCellscomreview[tmp]
                                shipSize[tmp] = shipSizereview[tmp]
                                shipSizecom[tmp] = shipSizecomreview[tmp]
                                shipColor[tmp] = shipColorreview[tmp]
                                shipColorcom[tmp] = shipColorcomreview[tmp]


                        #restShipsreview = 


                        restCount = restCountreview
                        restCountcom = restCountcomreview
                        


                        #begin replay
                        delayms = 500
                        times = -1
                        while restMissile and restCount and restMissilecom and restCountcom:
                                times += 1

                                pygame.time.delay(delayms)
                                px = replayPlayer[times*2+0]
                                py = replayPlayer[times*2+1]
                                if(table0[px][py] < 0 or table0[px][py] > 10):
                                        caption.setText("Already been hit, try again.")
                                        continue
                                else:
                                        if(table0[px][py] == 0):
                                                pygame.mixer.music.load("3.wav")
                                                pygame.mixer.music.play()
                                                caption.setText("Haha! Missed me.")
                                                table2[px][py] = 1
                                                restMissile -= 1
                                                table1[px][py] = Image(Point(-30, -30), "cross.gif")
                                                table1[px][py].draw(win)
                                                table0[px][py] = -1
                                        elif(0<table0user[px][py] and table0user[px][py]<10):
                                                pygame.mixer.music.load("1.wav")
                                                pygame.mixer.music.play()
                                                tship = table0[px][py]
                                                restMissile -= 1
                                                table0[px][py] += 10
                                                table0user[px][py] += 10
                                                restCells[tship] -= 1
                                                hitMissile += 1
                                                if(restCells[tship] > 0):
                                                        table2[px][py] = 1
                                                        table1[px][py] = Image(Point(-30, -30), color0[shipColor[tship]])
                                                        table1[px][py].draw(win)
                                                        caption.setText("Direct hit!")
                                                else:
                                                        for ti in range(10):
                                                                for tj in range(15):
                                                                        if(table0user[ti][tj] == table0[px][py]):
                                                                                table2[ti][tj] = 1
                                                                                table1[ti][tj].undraw()
                                                                                table1[ti][tj] = Image(Point(-30, -30), color1[shipColor[tship]])
                                                                                table1[ti][tj].draw(win)
                                                        restCount -= 1
                                                        restShips[shipSize[tship]] -= 1
                                                        caption.setText("You sunk one " + shipName[shipSize[tship]] + "! " + str(restShips[shipSize[tship]]) + shipName[shipSize[tship]] + "s left!")
                                        else:
                                               caption.setText("That's your own ship!")
                                               continue;
                                leftMissileText.setText("Missiles left: " + makeup(str(restMissile)))
                                shipsToSinkText.setText("Ships to sink: " + str(restCount))
                                hitrate = (hitMissile*100)/(100-restMissile)
                                hitRate.setText("Hit rate: " + makeup(str(hitrate)) + "%")
                                
                        #################################################################################################
                                pygame.time.delay(delayms)
                                while(1):
                                        px = replayComputer[times*2+0]
                                        py = replayComputer[times*2+1]

                                        table2com = createMatrix(0)
                                        if(table0[px][py] < 0 or table0[px][py] > 10):
                                                continue
                                        else:
                                                if(table0[px][py] == 0):
                                                        pygame.mixer.music.load("3.wav")
                                                        pygame.mixer.music.play()
                                                        caption.setText("I missed one, but next time I won't make mistake!")
                                                        table2com[px][py] = 1
                                                        restMissilecom -= 1
                                                        table1com[px][py] = Image(Point(-30, -30), "circle.gif")
                                                        table1com[px][py].draw(win)
                                                        table0[px][py] = -1
                                                        break
                                                elif(0<table0com[px][py] and table0com[px][py]<10):
                                                        pygame.mixer.music.load("1.wav")
                                                        pygame.mixer.music.play()
                                                        tship = table0[px][py]
                                                        restMissilecom -= 1
                                                        table0[px][py] += 10
                                                        table0com[px][py] += 10
                                                        restCellscom[tship] -= 1
                                                        hitMissilecom += 1
                                                        if(restCellscom[tship] > 0):
                                                                table2com[px][py] = 1
                                                                table1com[px][py] = Image(Point(-30, -30), color0[shipColor[tship]])
                                                                table1com[px][py].draw(win)
                                                                caption.setText("Computer direct hit!")
                                                        else:
                                                                for ti in range(10):
                                                                        for tj in range(15):
                                                                                if(table0com[ti][tj] == table0[px][py]):
                                                                                        table2com[ti][tj] = 1
                                                                                        table1com[ti][tj].undraw()
                                                                                        table1com[ti][tj] = Image(Point(-30, -30), color1[shipColor[tship]])
                                                                                        table1com[ti][tj].draw(win)
                                                                restCountcom -= 1
                                                                restShipscom[shipSizecom[tship]] -= 1
                                                                caption.setText("Haha! I sunk one " + shipName[shipSize[tship]] + "! " + str(restShips[shipSize[tship]]) + shipName[shipSize[tship]] + "s left!")
                                                        break
                                                else:
                                                       continue;
                                leftMissileTextcom.setText("Missiles left: " + makeup(str(restMissilecom)))
                                shipsToSinkTextcom.setText("Ships to sink: " + str(restCountcom))
                                hitratecom = (hitMissilecom*100)/(100-restMissilecom)
                                hitRatecom.setText("Hit rate: " + makeup(str(hitratecom)) + "%")
                                
                        ####################################################################################################
                                drawMap()
                                drawMapcom()
                        if (restCount==0 and restCountcom==0):
                                caption.setText("Tie!")
                        elif restCount:
                                caption.setText("I, computer won!")
                        else:
                                caption.setText("You win!")
