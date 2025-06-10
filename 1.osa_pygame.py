
import pygame
from math import *
def paike(algus):
    # x=200
    # y=0
    # for i in range(30):       
    #     x-=7
    #     y+=7
    #     if i in range(10, 20):
    #         pygame.draw.line(ekraani_pind, kollane, (0, 0), (x+i, y+i), 5)
    #     else:
    #         pygame.draw.line(ekraani_pind, kollane, (0, 0), (x, y), 5)
    for nurk in range(0, 90, 3):
        nurk_rad = radians(nurk)
        
        # Alguspunkt päikese serval
        x1 = cos(nurk_rad) * algus
        y1 = sin(nurk_rad) * algus
        
        # Lõpp-punkt väljaspool ringi (pikem kiir)
        x2 = cos(nurk_rad) * (algus + 200)
        y2 = sin(nurk_rad) * (algus + 200)
        
        pygame.draw.line(ekraani_pind, kollane, (x1, y1), (x2, y2), 2)
pygame.init()
kollane=[255, 255, 0]
punane=[255, 0, 0]
sinine=[0,0,255]
hall=[128, 128, 128]
pruun=[139, 69, 19]

ekraani_pind=pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame aken")
ekraani_pind.fill(hall)
#päike
pygame.draw.rect(ekraani_pind, kollane, (0, 0, 100, 100))
paike(0)

pygame.draw.circle(ekraani_pind, punane, (400, 300), 50)
pygame.draw.polygon(ekraani_pind, sinine, [(600, 100), (700, 100), (650, 50)])
pygame.draw.line(ekraani_pind, pruun, (100, 500), (700, 500), 10)

pilt1=pygame.image.load("ope.png")
pilt1=pygame.transform.scale(pilt1, (100, 100))
ekraani_pind.blit(pilt1, (300, 400))
ekraani_pind.blit(pilt1, (500, 400))
# tekst 
font=pygame.font.SysFont('Arial', 50)
sõnum="Tere tulemast!"
teksti_lisamine=font.render(sõnum, True, punane)
ekraani_pind.blit(teksti_lisamine, (500, 500))
#-----------------------
pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: break
pygame.quit()




