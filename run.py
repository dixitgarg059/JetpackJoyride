
import signal
from os import system, name 
from board import Board
import cursor
from mando import Mando
from getch import _getChUnix as getChar
from alarmexception import AlarmException
# from time import sleep 
import time
# import sleep to show output for some time period 
cursor.hide()
def alarmhandler(signum, frame):
    raise AlarmException
def user_input(timeout=0.05):
    signal.signal(signal.SIGALRM, alarmhandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = getChar()()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

# define our clear function 
# arr=[]

# from enemy import Enemy
# from board import Board
# from check import checkboard
# from bomb import Bomb
# from manage import Manage
# from getch import _getChUnix as getChar

    # print()    
i=51
j=0
flg=0
mando=Mando(i,j,200)
board=Board(55,200) # adjusting using the current screen size
# _ = system('clear') 
st=0
mando.add_to_board(board,st)
board.printboard(0)
# clear()
# position(i,j)
# printboard()
# board.printboard()
# #
# game_over()
timeout=0.1
# quit()/
is_bullet=False
bullets=[]
previous_time=0
# speed_boost=False

# mando.game_over()

while True:
    # system('clear')
    # print(mando.points) 
    to_be_removed=[]
    # if speed_boost:
        # #
        # timeout=0.01
    if mando.timeout() == 0:
        mando.game_over(True)
    for it in bullets:
        it.remove_from_board(board)
        ch=it.move_right(2,st,board)
        if ch==0:
            to_be_removed.append(it)
        else:
            if it.detect_colision(board) == 1:
                to_be_removed.append(it)
            else:
                it.add_to_board(board,st)
    for it in to_be_removed:
        bullets.remove(it)


    # if is_bullet:
    #     bullet.remove_from_board(board)
    #     bullet.move_right(2,st,board)
    #     if bullet.detect_colision(board)==1:
    #         is_bullet=False
    #     else:
    #         bullet.add_to_board(board,st)

    mando.detect_shield()
    mando.remove_from_board(board)
    mando.move_right(1,st,board)
    if mando.detect_speed_boost(board)  == 1:
            timeout=0.0001 
    else:
        timeout=0.1
    if mando.detect_colision(board) == 1:
            flg=1
    check=mando.detect_magnet(board,st)
    if check["move_up"]:
        mando.move_up(board)
    if check["move_down"]:
        mando.move_down(board)
    if check["move_right"]:
        mando.move_right(4,st,board)
    if check["move_left"]:
        mando.move_left(st,board)
    mando.add_to_board(board,st)
    st=st+1
    board.clear()
    board.printboard(st)
    if flg == 1:
        if mando.decrease_lives()==0:
            mando.game_over()
        else:
            flg=0

    if mando.on_ground() == 0:
        mando.remove_from_board(board)
        mando.move_down(board)
        if mando.detect_speed_boost(board)  == 1:
            timeout=0.0001
        else:
            timeout=0.1
        if mando.detect_colision(board) == 1:
            flg=1
        # mando.add_to_board(board,st)
    # mando.detect_colision(board,speed_boost)
    char = user_input(timeout)# Pressing 'i' is a cheat code, that adds extra life.
    if char == 'd':
        mando.remove_from_board(board)
        mando.move_right(3,st,board)
        if mando.detect_speed_boost(board)  == 1:
            timeout=0.0001
        else:
            timeout=0.1
        if mando.detect_colision(board) == 1:
            flg=1

        # mando.add_to_board(board,st)
        # board.printboard(st)
        # st=st+5
        # #
    if char == 'a':
        mando.remove_from_board(board)
        mando.move_left(st,board)
        if mando.detect_speed_boost(board)  == 1:
            timeout=0.0001
        else:
            timeout=0.1
        if mando.detect_colision(board) == 1:
            flg=1

        # mando.add_to_board(board,st)
        # board.printboard(st)
        # st=st+5
    if char == 'w':
        mando.remove_from_board(board)
        mando.move_up(board)
        if mando.detect_speed_boost(board)  == 1:
            timeout=0.0001
        else:
            timeout=0.1             
        if mando.detect_colision(board) == 1:
            flg=1
    if char == ' ':
        mando.shield(board,True)
        # mando.add_to_board(board,st)
        # board.printboard(st)
        # st=st+5s
    # time.sleep(0.05)

    if char == 'f':
        if is_bullet==False or (time.time()-previous_time)>=0.2:
            bullet=mando.fire()
            previous_time=time.time() 
            bullets.append(bullet)
            bullet.add_to_board(board,st)
            is_bullet=True
    # Press 'q' for quit.
    if char == 'q':
        quit()