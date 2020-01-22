
import signal
from os import system, name 
from dragon import Dragon,DRAGON_BULLET
from board import Board
from nonblockinginput import KBHit
from mando import Mando
from getch import _getChUnix as getChar
import sys
import time 
def cursor_hide():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
def cursor_show():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()
    
i=0
j=0
flg=0
timeout=0.01
magnetss=[]
is_bullet=False
st=0
st0=st
bullets=[]
previous_time=0
dragon_came=False
KB = KBHit()
time_for_fire=time.time()
ccc=1
ttt=1
fir=1
mando=Mando(i,j,150)
board=Board(55,200,magnetss) # adjusting using the current screen size 
mando.add_to_board(board,st,st0,dragon_came)
board.printboard(st,dragon_came)
dragon=Dragon(41,155)
dragon_finished=False
dragon_bullets=[]
cursor_hide()



while True:
    for cor in magnetss:
        for i in range(0,3):
            for j in range(0,3):
                board.set_grid(cor[0]+i,cor[1]+j,'#')
    if dragon_came:
        dragon.remove_from_board(board,st)
        dragon.chase(mando)
        if time.time() -time_for_fire >=2 or ccc == 1: 
            time_for_fire=time.time()          
            dragon_bullet=dragon.fire()
            dragon_bullets.append(dragon_bullet)
            ccc=0
        dragon.add_to_board(board,st) 
    to_be_removed=[]
    to_remove=[]
    if mando.timeout() == 0:
        mando.game_over(True)
    


    if dragon_came:
        for it in dragon_bullets:
            if it.detect_colision(mando,board,st0,st)==1:
                if mando.decrease_lives()==0:
                    cursor_show()
                    mando.game_over()

                to_remove.append(it)
                it.remove_from_board(board,st,0)
            else:
                it.remove_from_board(board,st,0)
                ch=it.move_left(st,st0,mando)
                if ch == 0:
                    it.remove_from_board(board,st,0)
                    to_remove.append(it)
                else:
                    it.add_to_board(board,st,0)
    for it in to_remove:
        dragon_bullets.remove(it)
    for it in bullets:
        it.remove_from_board(board,0,st0)
        ch=it.move_right(2,st,st0)
        if ch==0:
            to_be_removed.append(it)
        else:
            if it.detect_colision(board,st0) == 1:
                if dragon_came:
                    ch1=dragon.decrease_lives()
                    if ch1==1:
                        dragon.remove_from_board(board,st)
                        dragon.kill()
                        for it in dragon_bullets:
                            it.remove_from_board(board,st,0)
                        dragon_bullets=[]
                        dragon_came=False
                        dragon_finished=True
                    print("decrease_lives")
                to_be_removed.append(it)
            else:
                it.add_to_board(board,0,st0)
    for it in to_be_removed:
        if it in bullets:
            bullets.remove(it)


    mando.detect_shield()
    mando.remove_from_board(board,st0)
    if dragon_came==False:
        mando.move_right(1,st,board,dragon_finished)
    if mando.detect_colision(board,st0) == 1:
            flg=1
    if mando.detect_dragon_mode(board) ==1:
    	print("HEY DRAGON!!")
    	quit()
    check=mando.detect_magnet(board,st,st0)
    flg1=0
    if check["move_up"]:
        mando.move_up(board)
        flg1=1
    if check["move_down"]:
        mando.move_down(board,ttt)
        flg1=1
    if check["move_right"]:
        mando.move_right(4,st,board,dragon_finished)
        flg1=1
    if check["move_left"]:
        mando.move_left(st,board)
        flg1=1
    if flg1==1:
        ttt=1.2
    dragon_lives=dragon.get_lives();
    mando.add_to_board(board,st,st0,dragon_came,dragon_lives)
    if st >=1961  and fir ==1:
        fir=0
        if dragon_came == False:
            dragon_came=True
            time_for_fire=time.time()-2
    elif fir ==1:
        st=st+1
    board.printboard(st,dragon_came)
    if flg == 1:
        if mando.decrease_lives()==0:
            cursor_show()
            mando.game_over()
        else:
            flg=0
    if mando.detect_dragon_mode(board)  == 1:
        mando.remove_from_board(board,st0)
        mando.move_right(3,st,board,dragon_finished)
        st=st+3
        timeout=0.00001
    else:
        timeout=0.01
    if mando.on_ground() == 0:
        mando.remove_from_board(board,st0)
        mando.move_down(board,ttt)
        ttt=ttt+0.05
        if mando.detect_colision(board,st0) == 1:
            flg=1
    else:
        ttt=1
    system('sleep 0.01')
    if KB.kbhit():
        KEY = KB.getch()
    else:
        KEY = ""

    char = KEY
    if char == 'd':
        mando.remove_from_board(board,st0)
        mando.move_right(5,st,board,dragon_finished)
        if mando.detect_dragon_mode(board)  == 1:   	
        	print("he;o")
        else:
        	timeout=0.01
        if mando.detect_colision(board,st0) == 1:
            flg=1
    if char == 'a':
        mando.remove_from_board(board,st0)
        mando.move_left(st,board,st0)
        if mando.detect_dragon_mode(board)  == 1:
            timeout=0.00001
        else:
            timeout=0.01
        if mando.detect_colision(board,st0) == 1:
            flg=1
    if char == 'w':
        mando.remove_from_board(board,st0)
        mando.move_up(board)
        ttt=1.2
        if mando.detect_dragon_mode(board)  == 1:
            timeout=0.00001
        else:
            timeout=0.01             
        if mando.detect_colision(board,st0) == 1:
            flg=1
    if char == ' ':
        mando.shield(board,True)
    if char == 'f':
        if is_bullet==False or (time.time()-previous_time)>=0.2:
            bullet=mando.fire()
            previous_time=time.time() 
            bullets.append(bullet)
            bullet.add_to_board(board,0,st0)
            is_bullet=True
    if char == 'e' and dragon_came==	False:
    	mando.remove_from_board(board,st0)
    	mando.move_right(3,st,board,dragon_finished)
    	st=st+3
    if char == 'q':
        cursor_show()
        quit()
