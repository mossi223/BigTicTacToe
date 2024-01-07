import turtle
import time
def next_click(x, y):#설명에서 다음으로 넘어갈때 텍스트&그림 변경
  global n, desc
  if n <= 6:
    text.clear()
    n += 1
    text.write(desc[n - 1], font=("210 콤퓨타세탁 L", 12, "normal"), align="center")
    bg.shape("./images/desc-" + str(n) + '.gif')
  else:
    skip_click(x,y)

def prev_click(x, y):#설명에서 뒤로갈떄 텍스트&그림
  global n, desc
  if n >= 2:
    text.clear()
    n -= 1
    text.write(desc[n - 1], font=("210 콤퓨타세탁 L", 12, "normal"), align="center")
    bg.shape("./images/desc-" + str(n) + '.gif')

def skip_click(x, y):#스킵 눌렀을떄 설명 다 없에기
  bg.hideturtle()
  next.hideturtle()
  prev.hideturtle()
  skip.hideturtle()
  text.clear()
  create_board()

def create_board(x=0,y=0):#스킵을 눌렀거나 끝까지 다음 버튼 눌렀을떄 보드 생성&시작 선언
  global b, game_start, check, player, placed, gcl, grid, bggrid, game_won
  player = 0
  restart.hideturtle()
  placed = []
  gcl = []
  grid = [[[2 for _ in range(3)] for _ in range(3)] for _ in range(9)]
  bggrid = [[2 for _ in range(3)] for _ in range(3)]
  game_won = []
  b.clear()
  bga.clear()
  piece_shape.clear()
  b.color("black")
  #b.hideturtle()
  b.pensize(4)
  turtle.tracer(False)
  b.penup()
  b.goto(25,25)
  b.pendown()
  for i in range(9):
    b.penup()
    x = 25+ (i%3) * 300
    y = 25+ (i//3)*300
    b.goto(x, y)
    b.pendown()
    for _ in range(4):
      b.forward(300)
      b.left(90)
    b.penup()
    b.goto(x+15, y+15)
    b.pendown()
    for k in range(9):
      b.penup()
      x1 = x+15 + (k % 3) * 90
      y1 = y+15 + (k // 3) * 90
      b.goto(x1, y1)
      b.pendown()
      for _ in range(4):
        b.forward(90)
        b.left(90)
  turn()
  check = 1
  turtle.tracer(True)

def piece_position(x,y):#화면클릭->보드 위치(스킵을 눌렀을떄도 실행됨)
  global game_start, check
  if game_start == False and check == 1:
    game_start = True
    return
  if game_start == False:
    return
  piece(x,y)

def turn():#누구 차례인지 계산-> 배경 색칠
  global player, turn_color, anim_delay
  anim_delay = False
  turn_color.speed(0)
  if player == 0:
    turn_color.color('green')
    player = 1
  else:
    turn_color.color('red')
    player = 0
  turn_color.pensize(44)
  for i in range(4):
    turn_color.forward(950)
    turn_color.left(90)
  anim_delay = True

def piece(x,y):#말 그리기
  global player, piece_shape, placed, gcl, grid, game_won, anim_delay
  if anim_delay == False:
    return
  stx = ((x - 25) // 300) * 300 + 25
  sty = ((y - 25) // 300) * 300 + 25
  sstartx = (x - (stx + 15)) // 90
  sstarty = (y - (sty + 15)) // 90
  ans_x = (stx + 15) + 90 * sstartx
  ans_y = (sty + 15) + 90 * sstarty
  gc = [(x - 25) // 300 + (((y - 25) // 300) * 3), sstartx + sstarty * 3]
  if [stx, sty, ans_x, ans_y] in placed or win_check(int(gc[0])):
    return
  if len(gcl) > 0:
    if gcl[-1][1] != gc[0]:
      return
  chek = [(x - 25) // 300, (((y - 25) // 300) ), sstartx , sstarty]
  for i in chek:
    if i <= -1 or i >= 3:
      return

  placed.append([stx, sty, ans_x, ans_y])
  piece_shape.pensize(7)
  piece_shape.hideturtle()
  piece_shape.speed(0)
  piece_shape.penup()

  if player == 1:
    piece_shape.goto(ans_x+45, ans_y+20)
    piece_shape.pendown()
    piece_shape.color('green')
    piece_shape.circle(25)
  else:
    piece_shape.goto(ans_x+45, ans_y)
    piece_shape.color('red')
    piece_shape.write("x", font=("",70 ,"bold"),align="center")
  gcl.append(gc)
  grid[int(gc[0])][int(sstarty)][int(sstartx)] = player
  if win_check(int(gc[0])):
    gcl =[]
    game_won.append(gc[0])
    bggrid[int(gc[0]//3)][int(gc[0]-((gc[0]//3)*3))] = player

    win_draw(stx+15, sty+15,gc)

  else:
    if gc[1] in game_won:
      gcl=[]
    bg_aval(((gc[1]%3)*300)+32.5,((gc[1]//3)*300)+32.5)

def bg_aval(x,y):
  global bga, gcl
  bga.clear()
  if gcl == []:
    turn()
    return
  bga.speed(0)
  bga.pensize(12)
  bga.penup()
  bga.goto(x,y)
  bga.pendown()
  bga.color([245/255, 216/255, 51/255])
  for _ in range(4):
    bga.forward(285)
    bga.left(90)
  turn()

def win_check(posi):
  global gcl, grid, player
  for i in range(3):
    if grid[posi][i][0] == grid[posi][i][1] and grid[posi][i][0] == grid[posi][i][2] and grid[posi][i][0] != 2:
      return True
    if grid[posi][0][i] == grid[posi][1][i] and grid[posi][0][i] == grid[posi][2][i] and grid[posi][0][i] != 2:
      return True
  if grid[posi][0][0] == grid[posi][1][1] and grid[posi][0][0] == grid[posi][2][2] and grid[posi][0][0] != 2:
    return True
  if grid[posi][0][2] == grid[posi][1][1] and grid[posi][0][2] == grid[posi][2][0] and grid[posi][0][2] != 2:
    return True

  return False

def win_draw(x,y,gc):
  global player, b,bggrid
  b.pensize(15)
  color = [[250/255, 122/255, 122/255], [122/255, 250/255, 125/255]]
  b.color(color[player])
  b.penup()
  b.goto(x, y)
  b.speed(0)
  for i in range(9):
    b.penup()
    x1 = x + (i % 3) * 90
    y1 = y + (i // 3) * 90
    b.goto(x1,y1)
    b.pendown()
    for j in range(4):
      b.forward(90)
      b.left(90)
  if win(bggrid):
    ending(player)
    return
  bg_aval(((gc[1] % 3) * 300) + 32.5, ((gc[1] // 3) * 300) + 32.5)

def win(g):
  for i in range(3):
    if g[i][0] == g[i][1] and g[i][0] == g[i][2] and g[i][0] != 2:
      return True
    elif g[0][i] == g[1][i] and g[0][i] == g[2][i] and g[0][i] != 2:
      return True
  if g[0][0] == g[1][1] and g[0][0] == g[2][2] and g[0][0] != 2:
    return True
  elif g[0][2] == g[1][1] and g[0][2] == g[2][0] and g[0][2] != 2:
    return True

def ending(p):
  global b, restart, game_start
  game_start = False
  b.color('black')
  s = [500,300]
  b.penup()
  b.goto(225, 325)
  b.begin_fill()
  for i in range(4):
    b.forward(s[i%2])
    b.left(90)
  b.end_fill()
  b.color('white')
  b.goto(475, 500)
  tx = ['X', 'O']
  b.write(f'{tx[p]}가 승리하였습니다', font=('210 콤퓨타세탁 L', 25, 'bold'), align = 'center')
  restart = turtle.Turtle()
  restart.penup()
  restart.speed(0)
  restart.goto(475, 430)
  restart.showturtle()
  restart.shape("./images/restart.gif")
  restart.onclick(create_board)

desc = ["게임이 시작되면 첫번째 플레이어는 어느 곳이든 자신의 말을 놓을 수 있다",
        "다음 플레이어는 이전 플레이어가 선택한 보드 안에 위치와 같은 \n큰 보드 위치의 원하는 곳에 말을 놓는다",
        "이러한 과정을 반복한다",
        "이러한 과정을 반복한다",
        "작은 보드에서 3개 연속되게 말을 놓으면 그 보드를 가지게 된다",
        "만약에 다음 위치가 누군가의(자신 포함) 소유가 됐다면 원하는 위치에 말을 놓을 수 있다",
        "플레이어 중 소유한 보드 3개가 연속된 경우 그 플레이어의 승리로 게임 종료"]

n = 1
game_start = False
turtle.setup(950, 950)
turtle.tracer(False)
check = 0
anim_delay = True
turtle.setworldcoordinates(0, 0, 950, 950)
b = turtle.Turtle()
restart = turtle.Turtle()
restart.hideturtle()
bga = turtle.Turtle()
b.hideturtle()


for i in range(1, 8):
  turtle.addshape("./images/desc-" + str(i) + '.gif')
turtle.addshape("./images/next.gif")
turtle.addshape("./images/Prev.gif")
turtle.addshape("./images/Skip.gif")
turtle.addshape("./images/greenbox.gif")
turtle.addshape("./images/restart.gif")

bga.hideturtle()

bg = turtle.Turtle()
bg.shape("./images/desc-1.gif")
bg.penup()
bg.goto(475, 550)

next = turtle.Turtle()
next.shape("./images/next.gif")
next.penup()
next.goto(850, 70)
next.onclick(next_click)

prev = turtle.Turtle()
prev.shape("./images/Prev.gif")
prev.penup()
prev.goto(100, 70)
prev.onclick(prev_click)

skip = turtle.Turtle()
skip.shape("./images/Skip.gif")
skip.penup()
skip.goto(810, 140)
skip.onclick(skip_click)

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(475, 60)
text.write(desc[0], font=("210 콤퓨타세탁 L", 12, "normal"), align="center")

turn_color = turtle.Turtle()
turn_color.hideturtle()
piece_shape = turtle.Turtle()
piece_shape.hideturtle()
turtle.onscreenclick(piece_position)

turtle.tracer(True)
turtle.mainloop()
