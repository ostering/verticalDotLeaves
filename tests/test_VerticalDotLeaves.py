# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from anytree import Node, RenderTree

import context
from verticalDotLeaves import verticalDotLeaves
import unittest


class test_VerticalDotLeaves(unittest.TestCase):

    def print_tree(self, node, indent=8):

        spaces = indent * ' '

        print ("\n{}# tree:".format(spaces))
        for pre, _, node in RenderTree(node):
            print("{}# {}{}".format(spaces, pre, node.name))

    def test_lst_to_str_None_returns_empty_string(self):
        v = verticalDotLeaves.VerticalDotLeaves()
        actual = v.lst_to_str(None)
        self.assertEqual(actual, '')

    def test_lst_to_str_empty_list_returns_empty_string(self):
        v = verticalDotLeaves.VerticalDotLeaves()
        actual = v.lst_to_str([])
        self.assertEqual(actual, '')

    def test_lst_to_str_one_elem_ends_with_two_new_lines(self):
        v = verticalDotLeaves.VerticalDotLeaves()
        actual = v.lst_to_str(['a'])
        self.assertEqual(actual, 'a\n\n')

    def test_lst_to_str_two_elems_ends_with_two_new_lines(self):
        v = verticalDotLeaves.VerticalDotLeaves()
        actual = v.lst_to_str(['a', 'b'])
        self.assertEqual(actual, 'a\nb\n\n')

    def test_utf8_chars_handled_correctly(self):
        n = Node("ö")
        # self.print_tree(n)  # DEBUG
        actual = verticalDotLeaves.DotGraph(n)
        # print actual  # DEBUG
        expected = """
digraph tree {

node [shape=none];

"ö"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>ö</TD></TR>
</TABLE>
>];

}
"""
        self.assertMultiLineEqual(actual, expected)

    def test_one_node(self):
        a = Node("a")
        # self.print_tree(a) # DEBUG
        # tree:
        # a
        actual = verticalDotLeaves.DotGraph(a)
        # print actual # DEBUG

        expected = """
digraph tree {

node [shape=none];

"a"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>a</TD></TR>
</TABLE>
>];

}
"""
        self.assertMultiLineEqual(actual, expected)

    def test_two_nodes(self):
        a = Node("a")
        Node("b", a)  # b

        # self.print_tree(a) # DEBUG
        # tree:
        # a
        # └── b

        # result http://bit.ly/2PBKxp7

        actual = verticalDotLeaves.DotGraph(a)
        # print actual # DEBUG
        expected = """
digraph tree {

node [shape=none];

"a"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>a</TD></TR>
</TABLE>
>];

"aleaves"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>b</TD></TR>
</TABLE>
>];

"a":portroot -> "aleaves":portroot;

}
"""
        self.assertMultiLineEqual(actual, expected)

    def test_three_nodes(self):
        a = Node("a")
        Node("b", a)  # b
        Node("c", a)  # c

        # self.print_tree(a) # DEBUG
        # tree:
        # a
        # ├── b
        # └── c

        # result http://bit.ly/2Px2tl1

        actual = verticalDotLeaves.DotGraph(a)
        # print actual # DEBUG
        expected = """
digraph tree {

node [shape=none];

"a"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>a</TD></TR>
</TABLE>
>];

"aleaves"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>b</TD></TR>
<TR><TD>c</TD></TR>
</TABLE>
>];

"a":portroot -> "aleaves":portroot;

}
"""
        self.assertMultiLineEqual(actual, expected)

    def test_three_nodes_deep(self):
        a = Node("a")
        b = Node("b", a)  # b
        Node("c", b)  # c

        # self.print_tree(a) # DEBUG
        # tree:
        # a
        # └── b
        #     └── c

        # result http://bit.ly/2PATijs

        actual = verticalDotLeaves.DotGraph(a)
        # print actual # DEBUG
        expected = """
digraph tree {

node [shape=none];

"a"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>a</TD></TR>
</TABLE>
>];

"b"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>b</TD></TR>
</TABLE>
>];

"bleaves"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>c</TD></TR>
</TABLE>
>];

"b":portroot -> "bleaves":portroot;



"a":portroot -> "b":portroot;

}
"""
        self.assertMultiLineEqual(actual, expected)

    def test_five_nodes(self):
        a = Node("a")
        b = Node("b", a)
        Node("c", a)  # c
        Node("d", b)  # d
        Node("e", b)  # e

        # self.print_tree(a) # DEBUG
        # tree:
        # a
        # ├── b
        # │   ├── d
        # │   └── e
        # └── c

        # result http://bit.ly/2Pz0YTn

        actual = verticalDotLeaves.DotGraph(a)
        # print actual # DEBUG
        expected = """
digraph tree {

node [shape=none];

"a"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>a</TD></TR>
</TABLE>
>];

"aleaves"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>c</TD></TR>
</TABLE>
>];

"b"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>b</TD></TR>
</TABLE>
>];

"bleaves"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>d</TD></TR>
<TR><TD>e</TD></TR>
</TABLE>
>];

"b":portroot -> "bleaves":portroot;



"a":portroot -> "b":portroot;
"a":portroot -> "aleaves":portroot;

}
"""
        self.assertMultiLineEqual(actual, expected)

    def test_nine_nodes(self):
        a = Node("a")
        b = Node("b", a)
        Node("c", a)  # c
        Node("d", b)  # d
        Node("e", b)  # e
        f = Node("f", a)  # f
        Node("g", f)  # g
        Node("h", f)  # h
        Node("i", f)  # i

        # self.print_tree(a) # DEBUG
        # tree:
        # a
        # ├── b
        # │   ├── d
        # │   └── e
        # ├── c
        # └── f
        #     ├── g
        #     ├── h
        #     └── i

        # result http://bit.ly/2Pzb0DN

        actual = verticalDotLeaves.DotGraph(a)
        # print actual # DEBUG
        expected = """
digraph tree {

node [shape=none];

"a"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>a</TD></TR>
</TABLE>
>];

"aleaves"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>c</TD></TR>
</TABLE>
>];

"b"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>b</TD></TR>
</TABLE>
>];

"bleaves"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>d</TD></TR>
<TR><TD>e</TD></TR>
</TABLE>
>];

"b":portroot -> "bleaves":portroot;


"f"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>f</TD></TR>
</TABLE>
>];

"fleaves"[label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="portroot" >
<TR><TD>g</TD></TR>
<TR><TD>h</TD></TR>
<TR><TD>i</TD></TR>
</TABLE>
>];

"f":portroot -> "fleaves":portroot;



"a":portroot -> "b":portroot;
"a":portroot -> "f":portroot;
"a":portroot -> "aleaves":portroot;

}
"""
        self.assertMultiLineEqual(actual, expected)


def runOneTest(testName):
    # run one test
    suite = unittest.TestSuite()
    suite.addTest(test_VerticalDotLeaves(testName))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    # run one test, used for debugging (uncomment)
    # runOneTest('test_two_nodes')

    unittest.main(verbosity=3)
