from lark import Lark

littleDuckParser = Lark(open("littleDuckRules.txt", 'r').read())
parser = littleDuckParser.parse

test_files = ['test1.in', 'test2.in', 'test3.in',
              'test4.in', 'test5.in', 'test6.in', 'test7.in']

for test in test_files:
    try:
        s = open('tests/' + test, 'r').read()
        parser(s).pretty()
        print("Bien :)")
    except Exception:
        print("Error de sintaxis :(")
