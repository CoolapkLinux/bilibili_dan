import jieba
import random

def jb(text):
    wordlist = jieba.cut(text)
    wl = " ".join(wordlist)
    return wl

def r_color(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = random.randint(120, 250)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random.randint(60, 120)) / 255.0)
    return "hsl({}, {}%, {}%)".format(h, s, l)
