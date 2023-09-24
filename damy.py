import pprint
from PIL import Image

def da_sa(sachovnica, row, col):
    for i in range(row):
        if sachovnica[i]==col or sachovnica[i]-i==col-row or sachovnica[i]+i==col+row:
            return False
    return True

def solve_queens(row, sachovnica, kombinacie):
    if row==8:
        pprint.pprint(sachovnica)
        print("***")
        kombinacie[0]+=1
        display_komb(sachovnica, kombinacie[0])
        return

    for col in range(8):
        if da_sa(sachovnica, row, col):
            sachovnica[row]=col
            solve_queens(row+1, sachovnica, kombinacie)

#vytlaci nie ze:
# [0, 0, 0, 1, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 1, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 1]
# [0, 0, 0, 0, 0, 0, 1, 0]
# [1, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 1, 0, 0, 0, 0, 0]
# [0, 1, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 1, 0, 0, 0]

#ale vytlaci:
#[7, 3, 0, 2, 5, 1, 6, 4] ==== pocet cisel=pocet rows, cisla:column kde dama je
# 8 rows, dama je v stlpci: cisla

def chessboard_image(cell_size):
    img=Image.new(mode="RGBA", size=(cell_size*8, cell_size*8), color=(121, 46, 219, 255)) #fialova #792edb
    pix=img.load()
    for y in range(img.size[1]-1):
        for x in range(img.size[0]-1):
            if x//100%2==y//100%2:
                pix[x,y]=(255, 255, 255)
    return img

def display_komb(board, count):
    global img, queen, cell_size
    for row in range(8):
        col=sachovnica[row]
        img.paste(queen, (col*cell_size, row*cell_size), queen)
    image_name="damy "+ str(count) + ".png"
    img.save(image_name)
    img=chessboard_image(cell_size)

sachovnica=[-1]*8
solutions_count=[0]
cell_size=100
img=chessboard_image(cell_size)

queen=Image.open("queenie.png")
queen=queen.resize((cell_size, cell_size))

solve_queens(0, sachovnica, solutions_count)
print("pocet kombinacii:", solutions_count[0])
