# -*- coding: utf-8 -*-
import operator


def is_all_capital(s):
    if len(s):
        return all(x.isupper() or (not x.isalpha()) for x in s)
    else:
        return True


def id_to_list(text):
    l = []
    s = ""
    isac = is_all_capital(text)

    for c in text:
        if not c.isalnum() or (not isac and c.isupper()):
            if len(s):
                l.append(s)
                s = ""
        if not c.isalnum():
            continue
        s += c
    if len(s):
        l.append(s)
    return l


def upper_camel_case(text):
    s = ""
    for x in id_to_list(text):
        s += x[0].upper()
        s += x[1:].lower()
    return s


def lower_camel_case(text):
    if len(text):
        s = upper_camel_case(text)
        return s[0].lower() + s[1:]
    else:
        return ""


def all_caps(text, separator="_"):
    return separator.join(map(lambda x: x.upper(), id_to_list(text)))


def small_caps(text, separator="_"):
    return separator.join(map(lambda x: x.lower(), id_to_list(text)))


def unescape(text):
    text = text.replace("\\n", "\n")
    text = text.replace("\\r", "\r")
    text = text.replace("\\b", "\b")
    text = text.replace("\\t", "\t")
    text = text.replace("\\v", "\v")
    text = text.replace("\\\\", "\\")
    text = text.replace('\\"', '"')
    return text


def indent(s, prefix="  "):
    if type(prefix) == int:
        prefix = "  " * prefix
    return "\n".join((len(x) and prefix + x) or x for x in s.split("\n"))


def dedent(s, spaces=None, tab=4):
    s = s.replace("\t", " " * tab)

    def cws(s):
        l = 0
        for c in s:
            if c == " ":
                l += 1
            else:
                break
        return l

    v = [x.rstrip() for x in s.split("\n")]
    try:
        p = min(cws(x) for x in v if len(x))
    except ValueError:
        return s
    if spaces is None:
        spaces = p
    else:
        spaces = min(spaces, p)
    return "\n".join(x[p:] for x in v)


def escape(txt):
    txt = txt.replace("\\", "\\\\")
    txt = txt.replace("\n", "\\n")
    txt = txt.replace("\r", "\\r")
    txt = txt.replace("\t", "\\t")
    txt = txt.replace("'", "\\'")
    txt = txt.replace('"', '\\"')
    return txt
