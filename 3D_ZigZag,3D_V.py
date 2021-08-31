import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices_zigzag = (
    (-1, 1, -1),
    (-1, 1, 1),
    (0, -1, -1),
    (0, -1, 1),
    (1, 1, -1),
    (1, 1, 1),
    (2, -1, 1),
    (2, -1, -1),
    (3, 1, -1),
    (3, 1, 1),
    (4, -1, 1),
    (4, -1, -1),
    (5, 1, -1),
    (5, 1, 1),
    (6, -1, -1),
    (6, -1, 1),
    # (-1.6, -1, -1),
    # (-1.6, -1, 1),
    # (-1.6,-1.5,-1),
    # (-1.6,-1.5,1),
    # (7.6,-1,-1),
    # (7.6,-1,1),
    # (7.6,-1.5,-1),
    # (7.6,-1.5,1)
)
edges_zigzag = (
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 5),
    (4, 7),
    (5, 6),
    (6, 7),
    (6, 9),
    (7, 8),
    (8, 9),
    (8, 11),
    (9, 10),
    (10, 13),
    (10, 11),
    (11, 12),
    (12, 13),
    (12, 14),
    (13, 15),
    (14, 15),
    # (16,17),
    # (16,18),
    # (16,20),
    # (17,19),
    # (17,21),
    # (18,19),
    # (18,22),
    # (19,23),
    # (20,21),
    # (20,22),
    # (21,23),
    # (22,23)
)
Surfaces_zigzag = (
    (0, 1, 2, 3),
    (2, 3, 4, 5),
    (4, 5, 6, 7),
    (6, 7, 8, 9),
    (8, 9, 10, 11),
    (10, 11, 12, 13),
    (12, 13, 14, 15),
    # (16,17,18,19),
    # (16,18,20,22),
    # (16,17,20,21),
    # (17,19,21,23),
    # (18,19,22,23),
    # (20,21,22,23)
)
vertices_v = (
    (0, -1, 1),
    (0, -1, -1),
    (0.4, 0, 1),
    (0.4, 0, -1),
    (-0.5, 1.2, 1),
    (-0.5, 1.2, -1),
    (0, 0, 1),
    (0, 0, -1),
    (-1, -1, -1),
    (-1, -1, 1),
    ####
    (-0.6, 0, -1),
    (-0.6, 0, 1),
    (-1.5, 1.2, 1),
    (-1.5, 1.2, -1),
    (-1, 0, 1),
    (-1, 0, -1),
    (-2, -1, -1),
    (-2, -1, 1),
)
edges_v = (
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 5),
    (4, 6),
    (5, 7),
    (6, 7),
    (6, 9),
    (7, 8),
    (8, 9),
    (8, 10),
    (9, 11),
    (10, 11),
    (10, 13),
    (11, 12),
    (12, 13),
    (12, 14),
    (13, 15),
    (14, 15),
    (14, 17),
    (15, 16),
    (16, 17),
)
Surfaces_v = (
    (0, 1, 2, 3),
    (2, 3, 4, 5),
    (4, 5, 6, 7),
    (6, 7, 8, 9),
    (8, 9, 10, 11),
    (10, 11, 12, 13),
    (12, 13, 14, 15),
    (14, 15, 16, 17),
)
Colors = (
 (1, 0, 0),
 (0, 1, 0),
 (0, 0, 1),
 (0, 0, 0),
 (1, 1, 1),
 (0, 1, 1),
 (1, 0, 0),
 (0, 1, 0),
 (0, 0, 1),
 (0, 0, 0),
 (1, 1, 1),
 (0, 1, 1),
)
def ZigZag():
    glBegin(GL_QUADS)
    for surface in Surfaces_zigzag:
        x = 0
        for vertex in surface:
            x +=1
            glColor3fv(Colors[x])
            glVertex3fv(vertices_zigzag[vertex])
    glEnd()
    glLineWidth(10)
    glBegin(GL_LINES)
    for edge in edges_zigzag:
        for vertex in edge:
            glVertex3fv(vertices_zigzag[vertex])
    glEnd()
def V():
    glBegin(GL_QUADS)
    for surface in Surfaces_v:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(Colors[x])
            glVertex3fv(vertices_v[vertex])
    glEnd()
    glLineWidth(1)
    glBegin(GL_LINES)
    glColor(0,1,1)
    for edge in edges_v:
        for vertex in edge:
            glVertex3fv(vertices_v[vertex])
    glEnd()
def main():
    pygame.init()
    display = (1000,1500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Aryan8221")
    gluPerspective(45,(display[0]/display[1]), 0.1 ,50)
    glTranslatef(0.5,6,-30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         glTranslatef(-1,0,0)
            #     if event.key == pygame.K_RIGHT:
            #         glTranslatef(1,0,0)
            #     if event.key == pygame.K_UP:
            #         glTranslatef(0,1,0)
            #     if event.key == pygame.K_DOWN:
            #         glTranslatef(0,-1,0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 :
                    glTranslatef(0,0,1)
                if event.button == 5:
                    glTranslatef(0, 0, -1)
        glRotatef(1,3,1,1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # ZigZag()
        V()
        pygame.display.flip()
        pygame.time.wait(10)
main()
