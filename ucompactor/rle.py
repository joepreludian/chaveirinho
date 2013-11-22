from itertools import groupby


def compress_rle (plainText):
    res = []

    for k,i in groupby(plainText):
        run = list(i)
        if len(run) > 4:
            res.append("/{:02}{}".format(len(run), k))
        else:
            res.extend(run)

    return "".join(res)