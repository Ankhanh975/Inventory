import win32api, win32con, ctypes
import time

def turn_capslock(state: bool = False):
        dll = ctypes.WinDLL('User32.dll')
        VK_CAPITAL = 0X14
        if dll.GetKeyState(VK_CAPITAL):
            dll.keybd_event(VK_CAPITAL, 0X3a, 0X1, 0)
            dll.keybd_event(VK_CAPITAL, 0X3a, 0X3, 0)

        return dll.GetKeyState(VK_CAPITAL)

def Sleepp(duration): #High accurate sleep
    now = time.perf_counter()
    end = now + duration
    while now < end:
        if end-now >= 1/61:
            time.sleep(1/1000)
        now = time.perf_counter()
        
import lib._List
import time
def press(args, duration: float=1/500):
    win32api.keybd_event(lib._List.VK_CODE[args], 0,0,0)
    Sleepp(duration)
    win32api.keybd_event(lib._List.VK_CODE[args],0 ,win32con.KEYEVENTF_KEYUP ,0)

def pressAndHold(*args):
    '''
    press and hold. Do NOT release.
    accepts as many arguments as you want.
    e.g. pressAndHold('left_arrow', 'a','b').
    '''
    for i in args:
        win32api.keybd_event(lib._List.VK_CODE[i], 0,0,0)
        Sleepp(1/500)

def release(*args):
    for i in args:
        win32api.keybd_event(lib._List.VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)

def pressHoldRelease(*args):
    for i in args:
        win32api.keybd_event(lib._List.VK_CODE[i], 0,0,0)
        Sleepp(1/500)

    Sleepp(1/100)
    for i in args:
        win32api.keybd_event(lib._List.VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)
        Sleepp(1/500)



def typer(string=None,*args):
##    time.sleep(4)
    turn_capslock()
    for i in string:
        if i == ' ':
            win32api.keybd_event(lib._List.VK_CODE['spacebar'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['spacebar'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '!':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['1'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['1'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '@':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['2'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['2'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '{':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['['], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['['],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '?':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['/'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['/'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == ':':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE[';'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE[';'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '"':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['\''], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['\''],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '}':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE[']'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE[']'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '#':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['3'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['3'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '$':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['4'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['4'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '%':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['5'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['5'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '^':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['6'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['6'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '&':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['7'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['7'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '*':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['8'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['8'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '(':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['9'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['9'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == ')':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['0'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['0'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '_':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['-'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['-'],0 ,win32con.KEYEVENTF_KEYUP ,0)


        elif i == '=':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['+'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['+'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '~':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['`'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['`'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '<':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE[','], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE[','],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == '>':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['.'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['.'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'A':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['a'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['a'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'B':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['b'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['b'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'C':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['c'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['c'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'D':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['d'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['d'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'E':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['e'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['e'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'F':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['f'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['f'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'G':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['g'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['g'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'H':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['h'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['h'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'I':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['i'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['i'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'J':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['j'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['j'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'K':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['k'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['k'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'L':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['l'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['l'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'M':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['m'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['m'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'N':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['n'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['n'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'O':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['o'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['o'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'P':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['p'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['p'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'Q':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['q'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['q'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'R':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['r'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['r'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'S':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['s'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['s'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'T':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['t'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['t'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'U':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['u'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['u'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'V':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['v'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['v'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'W':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['w'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['w'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'X':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['x'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['x'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'Y':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['y'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['y'],0 ,win32con.KEYEVENTF_KEYUP ,0)

        elif i == 'Z':
            win32api.keybd_event(lib._List.VK_CODE['left_shift'], 0,0,0)
            win32api.keybd_event(lib._List.VK_CODE['z'], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE['left_shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)
            win32api.keybd_event(lib._List.VK_CODE['z'],0 ,win32con.KEYEVENTF_KEYUP ,0)

    
        else:    
            win32api.keybd_event(lib._List.VK_CODE[i], 0,0,0)
            Sleepp(1/500)
            win32api.keybd_event(lib._List.VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)


if __name__ == '__main__':
  time.sleep(4)
  press("/")
  Sleepp(1/20)
  press("backspace")
  typer("Hello World")
  press("enter")

