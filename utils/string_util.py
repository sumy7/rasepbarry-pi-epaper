# coding=utf-8

def chunk(in_str, n):
    # type:(str, int)->list[str]
    """
    将字符串按照指定长度切分
    """
    return [in_str[i:i + n] for i in range(0, len(in_str), n)]
