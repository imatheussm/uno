import data_structures as ds

use_pgzero=None
while use_pgzero!="y" and use_pgzero!="n":
    use_pgzero=input("Use pygamezero? [Y]/n: ").lower()
    if use_pgzero=="": use_pgzero="y"
    if use_pgzero!="y" and use_pgzero!="n": print("Unknown option. Try again.")

if use_pgzero=="" or use_pgzero=="y": use_pgzero=True
elif use_pgzero=="n": use_pgzero=False

if use_pgzero==True:
    try: import pgzero
    except:
        use_pgzero=False
        raise ImportWarning("pgzero not found. Generating a random game in text mode...")

# colors (with an additional set omitting "black", for its cards are all special only
ALL_COLORS          = ["black","blue","green","red","yellow"] 
NORMAL_COLORS       = ALL_COLORS[1:]
# 1 zero + 2*(1, ..., 9)
NUMBERS             = list(range(10))
# special cards
SPECIAL_CARD_TYPES  = ["skip","reverse","+2"]
BLACK_CARD_TYPES    = ["wildcard","+4"]
# cards seen under each color (other than black)
COLOR_CARD_TYPES    = NUMBERS+SPECIAL_CARD_TYPES
# all possible cards
CARD_TYPES          = set(NUMBERS+SPECIAL_CARD_TYPES+BLACK_CARD_TYPES)

class UnoCard:
    """
    Represents a single Uno Card, given a valid color and card type.

    color: string
    card_type: string/int

    >>> card = UnoCard("red", 5)
    """
    def __init__(self, color, card_type):
        self._validate(color, card_type)
        self.color = color
        self.card_type = card_type
        self.temp_color = None
        try: self.sprite = Actor("{}_{}".format(color, card_type))
        except: pass

    def __repr__(self):
        return "<UnoCard object>\n{:>7}{}\n{:>7}{}".format("Color: ",self.color,
                                                           "Type: ",self.card_type)

    def __str__(self):
        return "{}{}".format(self.color_short, self.card_type_short)

    def __format__(self, f):
        if f == "full":
            return "{} {}".format(self.color, self.card_type)
        else:
            return str(self)

    def __eq__(self, other):
        return self.color == other.color and self.card_type == other.card_type

    def validate(self, color, card_type):
        """
        Check the card is valid, raise exception if not.
        """
        if color not in ALL_COLORS:
            raise ValueError("Invalid color")
        if color == "black" and card_type not in BLACK_CARD_TYPES:
            raise ValueError("Invalid card type")
        if color != "black" and card_type not in COLOR_CARD_TYPES:
            raise ValueError("Invalid card type")

    @property
    def color_short(self):
        return self.color[0].upper()

    @property
    def card_type_short(self):
        if self.card_type in ("skip", "reverse", "wildcard"):
            return self.card_type[0].upper()
        else:
            return self.card_type

    @property
    def color(self):
        return self.temp_color if self.temp_color else self.color

    @property
    def temp_color(self):
        return self._temp_color

    @temp_color.setter
    def temp_color(self, color):
        if color is not None and color not in COLORS: raise ValueError("Invalid color")
        self._temp_color = color

    def playable(self, other):
        """
        Return True if the other card is playable on top of this card,
        otherwise return False
        """
        return self._color==other.color or self.card_type==other.card_type or other.color=="black"