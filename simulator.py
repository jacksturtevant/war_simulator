from graphics import *
from agents import *
poly_arr = [[Point(2, 3), Point(4, 6), Point(2, 6)], [Point(9, 1), Point(5, 6), Point(3, 8), Point(2, 7)], [Point(6, 2), Point(3.5, 0.2), Point(8.43, 6.73)]]
fight_arr = [[Point(2, 2), Point(3,3)], [Point(8, 8), Point(7,7)]]
move_list = [[Point(1.5, 4), Point(1.5, 5), Point(6, 8.5), Point(5, 8.5)], 
            [Point(1.5, 6.25), Point(2, 6.75), Point(4, 8.5), Point(3, 8.5)], 
            [Point(2.5, 6.25), Point(1, 7.5), Point(2, 8.5), Point(1.5, 7.5)],
            [Point(2.5, 6.25), Point(1, 7.5), Point(1.5, 7.5), Point(1.5, 6.5)],
            [Point(2.5, 6.25), Point(1.5, 7.5), Point(1.5, 7.5), Point(2.5, 6.25)]]

def setWindow():
    win = GraphWin(width=900, height=900)
    win.setCoords(0,0,10,10)
    win.setBackground("green")
    rect = Rectangle(Point(0.1, 0.1), Point(9.9,9.9))
    rect.draw(win)
    rect.setFill("#654321")
    return win

def setObstacles(win, polygons):
    for polygon in polygons:
        p = Polygon(polygon)
        p.draw(win)
        p.setFill("green")
        p.setOutline("green")

def setFighters(win, fs):
    f1 = Fighter(0, fs[0], win)
    f1.draw()
    f2 = Fighter(1, fs[1], win)
    f2.draw()
    return f1, f2

def end_game(win, winner, f1, f2):
    victor = ""
    if winner:
        f2.die()
        win.getMouse()
        f2.undraw()
        f1.toggle_fire()
        victor = "1"
    else:
        f1.die()
        win.getMouse()
        f1.undraw()
        f2.toggle_fire()
        victor = "2"
    t = Text(Point(5,5), "Fighter "+ victor +" Wins")
    t.setSize(30)
    t.draw(win)
    win.getMouse()

def simulate():
    win = setWindow()
    setObstacles(win, poly_arr)


    f1, f2 = setFighters(win, fight_arr)
   
    win.getMouse()
    while len(move_list) > 0:
        moves = move_list.pop(0)
        f1.update(moves[0:2])
        f2.update(moves[2:])
        if len(move_list) == 0:
            f1.toggle_fire()
            f1.toggle_view()
        win.getMouse()
    end_game(win, True, f1, f2)
    win.close()

#MacOS fix 2
#tk.Toplevel(_root).destroy()

# MacOS fix 1
update()

if __name__ == "__main__":
    simulate()