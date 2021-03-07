# CHAVE TATIL
from pyfirmata import Arduino, INPUT, OUTPUT, util
import lcd
import time

board=Arduino ('COM5')
verm = 7
botao1 = 2

it = util.Iterator(board)
it.start()

board.digital[botao1].mode = INPUT
board.digital[verm].mode = OUTPUT

while True:
    estado = board.digital[botao1].read()
    board.digital[verm].write(estado)