from treeit import Tree, TreeCmd, execute_from_command_line

demo = """
.
├── a
│   ├── a
│   │   ├── a
│   │   │   ├── a
│   │   │   └── b
│   │   └── b
│   │       ├── a
│   │       └── b
│   └── b
├── b
└── c
"""


def test_1():
    a = dict()
    a['a'] = dict(a=dict(a=dict(a=1, b=1), b=dict(a=1, b=1)), b=1)
    a['b'] = 1
    a['c'] = 1

    t = Tree(a, color=False)
    res = t.result()
    return res
    # print(res)
    # diff = difflib.ndiff(res, demo)
    # print(''.join(diff))


def test_2():
    a = dict()
    a['a'] = dict(a=dict(a=dict(a=1, b=1), b=dict(a=1, b=1)), b=1)
    a['b'] = 1
    a['c'] = 1

    t = TreeCmd(a)
    res = t.result()


def test_3():
    execute_from_command_line()


if __name__ == '__main__':
    print(test_1())
    test_2()
    test_3()
