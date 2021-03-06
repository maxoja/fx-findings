from enum import Enum, auto, IntEnum

class Timeframe(str, Enum):
    D1 = 'D1'
    H4 = 'H4'
    H1 = 'H1'
    M5 = 'M5'
    M15 = 'M15'
    M20 = 'M20'

class Quote(str, Enum):
    AUDCAD = 'AUDCAD'
    EURCHF = 'EURCHF'
    EURUSD = 'EURUSD'
    USDJPY = 'USDJPY'

class Col(str, Enum):
    DATETIME = '<DATETIME>'
    OPEN = '<OPEN>'
    CLOSE = '<CLOSE>'
    HIGH = '<HIGH>'
    LOW = '<LOW>'
    VOL = '<VOL>'
    SPREAD = '<SPREAD>'
    RISE = 'RISE'
    FALL = 'FALL'
    BODY = 'BODY'
    WICK_T = 'WICK_T'
    WICK_B = 'WICK_B'
    HEIGHT = 'HEIGHT'

class Broker(str, Enum):
    PEPPER = 'pepper'
    XM = 'xm'
    XM_LOW = 'xm-low'

class PosType(IntEnum):
    SHORT = -1
    LONG = 1

class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()

class Clr(str, Enum):
    LIGHT_RED = '#ffe7e6'
    LIGHT_BLUE = '#e6e7ff'
    DEFAULT_BLUE = '#1f77b4'
    RED = 'red'
    ROSE = 'pink'
    LAVENDER = 'purple'