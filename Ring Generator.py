from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

arr1 = []
flag1 = False
init_radius = 50
mouse_y = 500


def MidPointCircle(cx, cy, radius):
    d = 1 - radius
    x = 0
    y = radius
    CirclePoints(x, y, cx, cy)
    while x < y:
        if d < 0:
            d = d + 2 * x + 3
            x += 1
        else:
            d = d + 2 * x - 2 * y + 5
            x += 1
            y = y - 1
        CirclePoints(x, y, cx, cy)


def CirclePoints(x, y, cx, cy):
    glVertex2f(x + cx, y + cy)
    glVertex2f(y + cx, x + cy)
    glVertex2f(y + cx, -x + cy)
    glVertex2f(x + cx, -y + cy)
    glVertex2f(-x + cx, -y + cy)
    glVertex2f(-y + cx, -x + cy)
    glVertex2f(-y + cx, x + cy)
    glVertex2f(-x + cx, y + cy)


def specialKeyboardListener(key,x,y):
    global flag1
    if key == b' ':
        if flag1 == False:
            flag1 = True
        else:
            flag1 = False


def mouseListener(button, state, x, y):
    global arr1
    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            if flag1 == False:
                arr1.append([x, mouse_y - y, init_radius])


def animate():
    glutPostRedisplay()
    global flag1, arr1
    if not flag1:
        for i in arr1:
            i[2] += 0.5
        remove()


def remove():
    global arr1
    rem_arr1 = []  
    for i in arr1: 
        if i[2] <= 500:  
            
            rem_arr1.append(i)
    arr1 = rem_arr1  


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0.447, 1.0, 0.973)
    glPointSize(2)
    glBegin(GL_POINTS)

    for j in arr1:
        MidPointCircle(j[0], j[1], j[2]) 

    glEnd()
    glutSwapBuffers()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


glutInit()

glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)


wind = glutCreateWindow(b"Lab03: Water Ripple (20301317)")
iterate()


glutMouseFunc(mouseListener)
glutIdleFunc(animate)
glutDisplayFunc(display)

glutKeyboardFunc(specialKeyboardListener)

glutMainLoop()
