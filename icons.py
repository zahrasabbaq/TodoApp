from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QByteArray
import base64

# یک آیکون ساده برای تم
theme_icon_base64 = """
iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABTklEQVR4nK2Tz0oCURTFf+dEyqSgxNso
VdOkWdlGJmlliKCQjIKiIUEZ2BkY2ZBIKCdClsorLa2S7zcfR69J1s7s9977z/nO+cGQwDPaYAGNYA61
gArYAyfiJwFfADtmSxK1kbJwHdyZrIIAQgT8hpvhI83sG1HXqiSgE2CqNdplEFuQNBqINr7gC9qhURiE
oEZ9qjSE7sFDNShQnmoTwJpCgC8rC5wEXwCZAMNnAjm4gGeI9quZIu44Qy5Z8QLHDLydki4De1yS+rDE
EM8FAq34sTUJT8zoHqZD4GrfZ60AdHzvYx8E64AsZSOAZWLKorz6LMqHDeEWBn2euYXOCQtO3NittHjJ
4TLp9v5wFIMY2IQ2XzjR6S7pX8gLmEC+qjayuldt7Fefq6S2HrLSW6J7XqwTX8ACjs7uDJIAAAAASUVO
RK5CYII=
"""

theme_icon = QIcon()
theme_icon.addPixmap(QIcon(QByteArray(base64.b64decode(theme_icon_base64))).pixmap(32, 32))
