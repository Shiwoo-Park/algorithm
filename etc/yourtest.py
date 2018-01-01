import xml.etree.ElementTree as ET
import re
import urllib2

def string_contains(s, text):
    text = str(text)
    s_arr = text.split()
    for piece in s_arr:
        if s == piece:
            return True
    return False

def re_match(regex, text):
    return re.match(regex, text)


def re_match2(regex, text):
    print regex
    text = str(text)
    expressions = {
        "\d": ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    }
    regex_point = 0
    text_point = 0

    while text_point < len(text):
        c = text[text_point]
        piece = regex[regex_point]

        exp = None
        if (piece == '\\') and ((len(regex) - regex_point) > 2):
            piece = regex[text_point:regex_point + 2]
            if ((len(regex) - regex_point) > 3) and (regex[regex_point + 2] == "+"):
                piece = regex[regex_point:regex_point + 3]
        print "CHAR", c
        print "EXP", piece
        break

        # if piece in expressions:
        #     if expressions[piece]:

        # else:

    return False


def get_sum(arr):
    total = 0
    for n in arr:
        total += int(n)
    return total


def average(arr):
    count = len(arr)
    total = get_sum(arr)
    return total / count


def wc(text):
    ret = {}
    arr = text.split()
    for word in arr:
        if word in ret:
            ret[word] += 1
        else:
            ret[word] = 1
    return ret


def isInt(s):
    try:
        t = int(s)
        return True
    except:
        return False


def convert_from_json(json_text):
    ret = {}
    json_text = str(json_text).strip()
    if not json_text.startswith("{") or not json_text.endswith("}"):
        raise Exception('Invalid')
    kv_arr = json_text[1:-1].split(",")

    for kv in kv_arr:
        kv = kv.split(":")
        key = kv[0].strip()
        val = kv[1].strip()
        print key, "/", val
        if not key.startswith("\"") or not key.endswith("\""):
            raise Exception('Invalid')
        key = key[1:-1]
        if val.startswith("\"") or val.endswith("\""):
            val = val[1:-1]
        else:
            if isInt(val):
                val = int(val)
            elif val.startswith("{"):
                val = convert_from_json(val)
            else:
                raise Exception('Invalid')
        ret[key] = val
    return ret


def sorter(arr):
    arr.sort()
    return arr


def sortbyage(arr):
    arr.sort(key=lambda elem: elem["birthyear"])
    ret = []
    for elem in arr:
        ret.append(elem["name"])
    return ret

def handler():  # ????????
    # urllib2.urlopen("http://naver.com").read()
    return

def get_user_city(xml):
    try:
        root = ET.fromstring(xml)
        node = root.find("korean").find("user").find("netInfo").find("addr")
        return node.text
    except:
        raise Exception('Parse Error')


class VideoGameCharacter:
    def __init__(self):
        self.name = None
        self.company = None

    def get_name(self):
        return self.name

    def get_company(self):
        return self.company


class Mario(VideoGameCharacter):
    def __init__(self):
        VideoGameCharacter.__init__(self)
        self.name = "Mario"
        self.company = "Nintendo"


class Megaman(VideoGameCharacter):
    def __init__(self):
        VideoGameCharacter.__init__(self)
        self.name = "Megaman"
        self.company = "Capcom"

