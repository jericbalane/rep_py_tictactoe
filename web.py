# #############################################
# TIC-TAC-TOE program in python with html/css
# writted by: JERIC BALANE
# dated: 28.05.2015
# for Alvin Gonzales of webcotrans
# #############################################

import utils

app = utils.App()


xoro = "x"
player = 1
total = 0
mainTotal = 0
takenCells = []
isIntakenCell = False
selectedCells = []
isWin = False

a1 = "-"
a2 = "-"
a3 = "-"
b1 = "-"
b2 = "-"
b3 = "-"
c1 = "-"
c2 = "-"
c3 = "-"

@app.route('/')
def index():
    global a1,a2,a3,b1,b2,b3,c1,c2,c3,player,isWin
    
    print """<html>
        <head>
            <link rel="stylesheet" href="/index.css">
        </head>
        <body>
            
            <div id="header">
                <h1>Tic Tac Toe</h1>
            </div>
            
            <div id="mainGame">
                <table>
                    <tr>
                        <td>
                            <div class="content" id="a1"><a class="hiddencell" href="/set-tile?row=0&col=0">""" + a1 + """</a></div>
                        </td>
                        <td>
                            <div class="content" id="a2"><a class="hiddencell" href="/set-tile?row=0&col=1">""" + a2 + """</a></div>
                        </td>
                        <td>
                            <div class="content" id="a3"><a class="hiddencell" href="/set-tile?row=0&col=2">""" + a3 + """</a></div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div class="content" id="b1"><a class="hiddencell" href="/set-tile?row=1&col=2">""" + b1 + """</a></div>
                        </td>
                        <td>
                            <div class="content" id="b2"><a class="hiddencell" href="/set-tile?row=1&col=3">""" + b2 + """</a></div>
                        </td>
                        <td>
                            <div class="content" id="b3"><a class="hiddencell" href="/set-tile?row=1&col=4">""" + b3 + """</a></div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div class="content" id="c1"><a class="hiddencell" href="/set-tile?row=2&col=4">""" + c1 + """</a></div>
                        </td>
                        <td>
                            <div class="content" id="c2"><a class="hiddencell" href="/set-tile?row=2&col=5">""" + c2 + """</a></div>
                        </td>
                        <td>
                            <div class="content" id="c3"><a class="hiddencell" href="/set-tile?row=2&col=6">""" + c3 + """</a></div>
                        </td>
                    </tr>
                <table>
                
            </div>    
            
            <div id="buttons">
                    <p><a href="/start-over" id="highlightClearMoves"> CLEAR ALL MOVES </a></p>
                    
                    <a href="/shutdown">SHUTDOWN APP</a>
            </div>
            
        </body>
    </html>"""
    
    if isWin == False:
        print """ <p>Turn: Player: """+ str(player) +"""</p> """

@app.route('/start-over')
def startOver():
    clear_var()
    index()

def clear_var():
    global xoro,player,total,mainTotal,takenCells,isIntakenCell,isWin,a1,a2,a3,b1,b2,b3,c1,c2,c3

    xoro = "x"
    player = 1
    total = 0
    mainTotal = 0
    takenCells =[]
    isIntakenCell = False
    selectedCells = []
    isWin = False
    
    a1 = "-"
    a2 = "-"
    a3 = "-"
    b1 = "-"
    b2 = "-"
    b3 = "-"
    c1 = "-"
    c2 = "-"
    c3 = "-"
    
@app.route('/set-tile')
def set_tile(row, col):
    global player,total,mainTotal
    
    total = get_total(row,col)
    move(total)
    
    index()
    
    
    print "<p>Recently selected cell: " + str(total) + "</p>"
    print "<p>Main Total: " + str(mainTotal) + "</p>"
    
    takenCells.sort()
    
    print "<p>Taken Cell"
    print takenCells
    print "</p>"
    
    print "Number of selected cells: " + str(len(takenCells))
    
    
def change_player():
    global player,xoro
    
    if  player != 1: 
        player = 1
        xoro = "o"
    else:
        player = 2
        xoro = "x"
    
def move(local_move_total):
    global a1,a2,a3,b1,b2,b3,c1,c2,c3,total,xoro,mainTotal,selectedCells
    
    add_selected_to_taken_cell(total)
    
    if isIntakenCell != True and isWin != True:
        
        change_player()
        mainTotal +=total
        
        if total==0:
            a1 = xoro
            selectedCells.append("a1"+xoro)
        elif total == 1:
            a2 = xoro
            selectedCells.append("a2"+xoro)
        elif total == 2:
            a3 = xoro
            selectedCells.append("a3"+xoro)
        elif total == 3:
            b1 = xoro
            selectedCells.append("b1"+xoro)
        elif total == 4:
            b2 = xoro
            selectedCells.append("b2"+xoro)
        elif total == 5:
            b3 = xoro
            selectedCells.append("b3"+xoro)
        elif total == 6:
            c1 = xoro
            selectedCells.append("c1"+xoro)
        elif total == 7:
            c2 = xoro
            selectedCells.append("c2"+xoro)
        elif total == 8:
            c3 = xoro
            selectedCells.append("c3"+xoro)
    
    checkWin()
    
def get_total(row, col):
    global total
    total = int(row) + int(col)
    return total

def add_selected_to_taken_cell(total):
    global takenCells,isIntakenCell,isWin
    
    isIntakenCell = False
    
    for index in range(len(takenCells)):
        if takenCells[index] == total:
            isIntakenCell = True
    
    if isWin == False:
        if isIntakenCell == True: 
            print """<p style="color:red">"SORRY, THIS IS TAKEN. PLEASE SELECT ANOTHER ONE."</p>"""
        else:
            takenCells.append(total)
        
        if len(takenCells) == 9 and isWin !=False:
            print """<p><a href="/start-over" style="color:red;"> It's a tie! Please CLICK ME to start anew. </a></p>"""
        
def checkWin():
    global isWin
    
    if (a1 == "x" and a2 == "x" and a3 == "x" or \
        b1 == "x" and b2 == "x" and b3 == "x" or \
        c1 == "x" and c2 == "x" and c3 == "x" or \
        a1 == "x" and b1 == "x" and c1 == "x" or \
        a2 == "x" and b2 == "x" and c2 == "x" or \
        a3 == "x" and b3 == "x" and c3 == "x" or \
        a1 == "x" and b2 == "x" and c3 == "x" or \
        c1 == "x" and b2 == "x" and a3 == "x" or \
        a1 == "o" and a2 == "o" and a3 == "o" or \
        b1 == "o" and b2 == "o" and b3 == "o" or \
        c1 == "o" and c2 == "o" and c3 == "o" or \
        a1 == "o" and b1 == "o" and c1 == "o" or \
        a2 == "o" and b2 == "o" and c2 == "o" or \
        a3 == "o" and b3 == "o" and c3 == "o" or \
        a1 == "o" and b2 == "o" and c3 == "o" or \
        c1 == "o" and b2 == "o" and a3 == "o"  ):
        
        isWin = True
        
        if player == 1:
            print """<p><a href="/start-over" style="color:red;"> PLAYER 2 using """ +str(xoro)+ """ WINS!</a></p>"""
        else:
            print """<p><a href="/start-over" style="color:red;"> PLAYER 1 using """ +str(xoro)+ """ WINS!</a></p>"""
        
@app.route('/index.css')
def css():
    global isWin
    print """
    body {
        font-family: verdana, sans serif;
        line-height: 1.3;
        font-size: 83%;
    }

    h1, h2, h3, h4, h5 {
        font-size: 1.5em;
    }
	
	table {
		font-size: 100px;
		text-align: center;
		width:35%;
		color: #fff;
	}
	td {
		width:30%;
		position:relative;
	}
	td:after {
		content:'';
		display:block;
		margin-top:100%;
	}
	td .content {
		position:absolute;
		top:0;
		bottom:0;
		left:0;
		right:0;
		background:yellow;
        overflow:hidden;
	}
    a.hiddencell {
        text-decoration:none;
        color:orange;
    }
    
    #header {
        background-color:black;
        color:white;
        text-align:center;
        padding:1px;
        width:35%
    }
    
    """
    
    if isWin == True:
        print """
            #highlightClearMoves {
            color:red;
            }
        
            a.hiddencell {
            pointer-events: none;
            cursor: default;
            }"""
        highlight_winningBox()

def highlight_winningBox():
    global a1,a2,a3,b1,b2,b3,c1,c2,c3
    
    if (a1 == "x" and a2 == "x" and a3 == "x"): print """ #a1,#a2,#a3{background-color:red;}"""
    if (b1 == "x" and b2 == "x" and b3 == "x"): print """ #b1,#b2,#b3{background-color:red;}"""
    if (c1 == "x" and c2 == "x" and c3 == "x"): print """ #c1,#c2,#c3{background-color:red;}"""
    if (a1 == "x" and b1 == "x" and c1 == "x"): print """ #a1,#b1,#c1{background-color:red;}"""
    if (a2 == "x" and b2 == "x" and c2 == "x"): print """ #a2,#b2,#c2{background-color:red;}"""
    if (a3 == "x" and b3 == "x" and c3 == "x"): print """ #a3,#b3,#c3{background-color:red;}"""
    if (a1 == "x" and b2 == "x" and c3 == "x"): print """ #a1,#b2,#c3{background-color:red;}"""
    if (c1 == "x" and b2 == "x" and a3 == "x"): print """ #c1,#b2,#a3{background-color:red;}"""
    if (a1 == "o" and a2 == "o" and a3 == "o"): print """ #a1,#a2,#a3{background-color:red;}"""
    if (b1 == "o" and b2 == "o" and b3 == "o"): print """ #b1,#b2,#b3{background-color:red;}"""
    if (c1 == "o" and c2 == "o" and c3 == "o"): print """ #c1,#c2,#c3{background-color:red;}"""
    if (a1 == "o" and b1 == "o" and c1 == "o"): print """ #a1,#b1,#c1{background-color:red;}"""
    if (a2 == "o" and b2 == "o" and c2 == "o"): print """ #a2,#b2,#c2{background-color:red;}"""
    if (a3 == "o" and b3 == "o" and c3 == "o"): print """ #a3,#b3,#c3{background-color:red;}"""
    if (a1 == "o" and b2 == "o" and c3 == "o"): print """ #a1,#b2,#c3{background-color:red;}"""
    if (c1 == "o" and b2 == "o" and a3 == "o"): print """ #c1,#b2,#a3{background-color:red;}"""
    
@app.route('/redirect-test')
def redirect_test():
    utils.redirect("/set-tile?row=1&col=1")
	
if __name__ == "__main__":
    print "Run the file run.py instead."
    raw_input()

    # app.run()

	