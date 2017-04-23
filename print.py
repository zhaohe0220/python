import win32ui
import win32print
import win32con

def send_to_printer(title,txt):
    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(win32print.GetDefaultPrinter())
    hDC.StartDoc(title)
    hDC.StartPage()
    hDC.SetMapMode(win32con.MM_TWIPS)

    ulc_x = 1000
    ulc_y = -1000
    lrc_x = 11500
    lrc_y = -11500

    hDC.DrawText(txt,(ulc_x,ulc_y,lrc_x,lrc_y),win32con.DT_LEFT)

    hDC.EndPage()
    hDC.EndDoc()

send_to_printer("123","123")