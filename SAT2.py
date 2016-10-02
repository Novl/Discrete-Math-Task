# -*- coding: UTF-8 -*-
# '! - means negative, e.g. !0 = 1
import sys
import copy

def anti(s):
    if s[0] == "!":
        return s[1:]
    else:
        return "!"+s

def add_Clause(edges, s1, s2):
    edges[anti(s1)].append(s2)
    edges[anti(s2)].append(s1)

def dfs(v, used, edges, reach):
    used[v] = 1
    reach.append(v)
    for i in edges[v]:
        if used[i] == 0:
            dfs(i, used, edges, reach)


def main(input_file = "simple.txt"):
    try:
        input = open(input_file, "r")
    except BaseException as Error:
        return (Error)

    terms = []
    edges = {}

    for str in input:
        if (str[-1] == "\n"):
            str = str[:-1]
        str = str.strip()
        if (str[0] == "#"):
            pass
        else:
            separator = str.find(" ")
            if separator == -1:
                str1 = str
                str2 = "0"
            else:
                str1 = str[:separator]
                str2 = str[separator + 1:]

            if not(str1 in terms):
                terms.append(str1)
                terms.append(anti(str1))
                edges[str1] = []
                edges[anti(str1)] = []
            if not(str2 in terms):
                terms.append(str2)
                terms.append(anti(str2))
                edges[str2] = []
                edges[anti(str2)] = []
            add_Clause(edges, str1, str2)
# end reading
    input.close()
    reachable = {}
    for q in terms:
        reachable[q] = []

    used1 = {}
    for q in terms:
        used1[q] = 0
    for i in terms:
        used = copy.deepcopy(used1)
        dfs(i, used, edges, reach = reachable[i])

    for q in terms:
        if (anti(q) in reachable[q] and q in reachable[anti(q)]):
            return 0
    return 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        rez = main(input_file = sys.argv[1])
    else:
        rez = main()
    if (rez == 1):
        print ("SATISFIED")
    elif (rez == 0):
        print ("NOT SATISFIED")
    else:
        print (rez)

