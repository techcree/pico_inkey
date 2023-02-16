#import led
import inputtext
from settext_file import settext
from settextb_file import settextb
from settextc_file import settextc
from picographics import PicoGraphics, DISPLAY_INKY_PACK


#TEXT_SIZE
LINE_HEIGHT = 20

display = PicoGraphics(display=DISPLAY_INKY_PACK)

# Clear to white
display.set_pen(15)
display.clear()

#next
display.set_pen(0)

TEXT_SIZE = 0.96
y = 25 + int(LINE_HEIGHT / 3)

display.set_font("serif")

display.text(settext, 10,30,240,1)
display.text(settextb, 10,70,240,2)
display.text(settextc, 10,110,240,0.8)

display.update()

