import ctypes
from ctypes import wintypes

# 定义常量
WS_EX_LAYERED = 0x80000
WS_EX_TRANSPARENT = 0x20
WS_EX_TOPMOST = 0x8
WS_POPUP = 0x80000000
LWA_COLORKEY = 0x1
LWA_ALPHA = 0x2

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
kernel32 = ctypes.windll.kernel32

class RECT(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_long),
        ("top", ctypes.c_long),
        ("right", ctypes.c_long),
        ("bottom", ctypes.c_long),
    ]

def main():
    h_instance = kernel32.GetModuleHandleW(None)

    # 注册窗口类
    WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_void_p, ctypes.c_uint, ctypes.c_wparam, ctypes.c_lparam)
    wndclass = wintypes.WNDCLASSEX()
    wndclass.cbSize = ctypes.sizeof(wndclass)
    wndclass.style = 0
    wndclass.lpfnWndProc = WNDPROC(wnd_proc)
    wndclass.cbClsExtra = 0
    wndclass.cbWndExtra = 0
    wndclass.hInstance = h_instance
    wndclass.hIcon = None
    wndclass.hCursor = user32.LoadCursorW(0, 32512)  # 默认光标
    wndclass.hbrBackground = gdi32.CreateSolidBrush(0x00FF00)  # 绿色背景
    wndclass.lpszMenuName = None
    wndclass.lpszClassName = "GreenOverlay"
    wndclass.hIconSm = None

    if not user32.RegisterClassExW(ctypes.byref(wndclass)):
        raise ctypes.WinError(ctypes.get_last_error())

    # 获取屏幕分辨率
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    # 创建窗口
    hwnd = user32.CreateWindowExW(
        WS_EX_LAYERED | WS_EX_TOPMOST | WS_EX_TRANSPARENT,  # 扩展窗口样式
        wndclass.lpszClassName,
        "Green Screen Tool",
        WS_POPUP,  # 无边框窗口
        0, 0, screen_width, screen_height,  # 全屏幕覆盖
        None, None, h_instance, None
    )

    if not hwnd:
        raise ctypes.WinError(ctypes.get_last_error())

    # 设置透明度和颜色键
    user32.SetLayeredWindowAttributes(hwnd, 0x00FF00, int(255 * 0.8), LWA_ALPHA | LWA_COLORKEY)

    # 显示窗口
    user32.ShowWindow(hwnd, 1)  # SW_SHOWNORMAL
    user32.UpdateWindow(hwnd)

    # 消息循环
    msg = wintypes.MSG()
    while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
        user32.TranslateMessage(ctypes.byref(msg))
        user32.DispatchMessageW(ctypes.byref(msg))

def wnd_proc(hwnd, msg, wparam, lparam):
    if msg == 0x0010:  # WM_CLOSE
        user32.DestroyWindow(hwnd)
    elif msg == 0x0002:  # WM_DESTROY
        user32.PostQuitMessage(0)
    else:
        return user32.DefWindowProcW(hwnd, msg, wparam, lparam)
    return 0

if __name__ == "__main__":
    main()
