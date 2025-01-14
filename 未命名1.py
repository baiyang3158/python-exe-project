{\rtf1\ansi\ansicpg936\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;\f1\fnil\fcharset134 PingFangSC-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0\c85098;\cssrgb\c0\c0\c0\c3922;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs30 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import ctypes\
from ctypes import wintypes\
\
# 
\f1 \'b6\'a8\'d2\'e5\'b3\'a3\'c1\'bf
\f0 \
WS_EX_LAYERED = 0x80000\
WS_EX_TRANSPARENT = 0x20\
WS_EX_TOPMOST = 0x8\
WS_POPUP = 0x80000000\
LWA_COLORKEY = 0x1\
LWA_ALPHA = 0x2\
\
user32 = ctypes.windll.user32\
gdi32 = ctypes.windll.gdi32\
kernel32 = ctypes.windll.kernel32\
\
class RECT(ctypes.Structure):\
    _fields_ = 
\f1 [
\f0 \
        ("left", ctypes.c_long),\
        ("top", ctypes.c_long),\
        ("right", ctypes.c_long),\
        ("bottom", ctypes.c_long),\
    
\f1 ]
\f0 \
\
def main():\
    h_instance = kernel32.GetModuleHandleW(None)\
\
    # 
\f1 \'d7\'a2\'b2\'e1\'b4\'b0\'bf\'da\'c0\'e0
\f0 \
    WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_void_p, ctypes.c_uint, ctypes.c_wparam, ctypes.c_lparam)\
    wndclass = wintypes.WNDCLASSEX()\
    wndclass.cbSize = ctypes.sizeof(wndclass)\
    wndclass.style = 0\
    wndclass.lpfnWndProc = WNDPROC(wnd_proc)\
    wndclass.cbClsExtra = 0\
    wndclass.cbWndExtra = 0\
    wndclass.hInstance = h_instance\
    wndclass.hIcon = None\
    wndclass.hCursor = user32.LoadCursorW(0, 32512)  # 
\f1 \'c4\'ac\'c8\'cf\'b9\'e2\'b1\'ea
\f0 \
    wndclass.hbrBackground = gdi32.CreateSolidBrush(0x00FF00)  # 
\f1 \'c2\'cc\'c9\'ab\'b1\'b3\'be\'b0
\f0 \
    wndclass.lpszMenuName = None\
    wndclass.lpszClassName = "GreenOverlay"\
    wndclass.hIconSm = None\
\
    if not user32.RegisterClassExW(ctypes.byref(wndclass)):\
        raise ctypes.WinError(ctypes.get_last_error())\
\
    # 
\f1 \'bb\'f1\'c8\'a1\'c6\'c1\'c4\'bb\'b7\'d6\'b1\'e6\'c2\'ca
\f0 \
    screen_width = user32.GetSystemMetrics(0)\
    screen_height = user32.GetSystemMetrics(1)\
\
    # 
\f1 \'b4\'b4\'bd\'a8\'b4\'b0\'bf\'da
\f0 \
    hwnd = user32.CreateWindowExW(\
        WS_EX_LAYERED | WS_EX_TOPMOST | WS_EX_TRANSPARENT,  # 
\f1 \'c0\'a9\'d5\'b9\'b4\'b0\'bf\'da\'d1\'f9\'ca\'bd
\f0 \
        wndclass.lpszClassName,\
        "Green Screen Tool",\
        WS_POPUP,  # 
\f1 \'ce\'de\'b1\'df\'bf\'f2\'b4\'b0\'bf\'da
\f0 \
        0, 0, screen_width, screen_height,  # 
\f1 \'c8\'ab\'c6\'c1\'c4\'bb\'b8\'b2\'b8\'c7
\f0 \
        None, None, h_instance, None\
    )\
\
    if not hwnd:\
        raise ctypes.WinError(ctypes.get_last_error())\
\
    # 
\f1 \'c9\'e8\'d6\'c3\'cd\'b8\'c3\'f7\'b6\'c8\'ba\'cd\'d1\'d5\'c9\'ab\'bc\'fc
\f0 \
    user32.SetLayeredWindowAttributes(hwnd, 0x00FF00, int(255 * 0.8), LWA_ALPHA | LWA_COLORKEY)\
\
    # 
\f1 \'cf\'d4\'ca\'be\'b4\'b0\'bf\'da
\f0 \
    user32.ShowWindow(hwnd, 1)  # SW_SHOWNORMAL\
    user32.UpdateWindow(hwnd)\
\
    # 
\f1 \'cf\'fb\'cf\'a2\'d1\'ad\'bb\'b7
\f0 \
    msg = wintypes.MSG()\
    while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:\
        user32.TranslateMessage(ctypes.byref(msg))\
        user32.DispatchMessageW(ctypes.byref(msg))\
\
def wnd_proc(hwnd, msg, wparam, lparam):\
    if msg == 0x0010:  # WM_CLOSE\
        user32.DestroyWindow(hwnd)\
    elif msg == 0x0002:  # WM_DESTROY\
        user32.PostQuitMessage(0)\
    else:\
        return user32.DefWindowProcW(hwnd, msg, wparam, lparam)\
    return 0\
\
if __name__ == "__main__":\
    main()}