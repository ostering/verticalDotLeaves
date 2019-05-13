# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class VerticalDotLeaves:

    PTR_ID = 'portroot'  # POINTER ID

    def row(self, singleNode):
        return '<TR><TD>{}</TD></TR>\n'.format(singleNode.name)

    def dot_table(self, rows):
        return '<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="{}" >' \
               '\n{}</TABLE>'.format(self.PTR_ID, rows)

    def create_lable_table(self, nodes, lblName):
        rows = ''.join(map(self.row, nodes))

        return '"{0}"[label=<\n{1}\n>];\n\n' \
               .format(lblName, self.dot_table(rows))

    def lst_to_str(self, lst):
        ''' converts lst (list) to string '''
        return '' if not lst else '\n'.join(lst) + '\n\n'

    def create_edge(self, fromName, toName):
        return '"{0}":{2} -> "{1}":{2};'.format(fromName, toName, self.PTR_ID)

    def DotGraph(self, tree):
        subTrees = []
        edges = []
        leafNodes = []

        # subtrees
        for c in tree.children:
            if not c.is_leaf:
                # create label for subtree graph
                subTrees.append(self.DotGraph(c))

                # create edge from tree to subTree
                edges.append(self.create_edge(tree.name, c.name))
            else:
                leafNodes.append(c)

        # leaves
        lbLeaves = ''
        if leafNodes:
            # create edge from tree to leaves
            tleavesName = '{0}leaves'.format(tree.name)
            edges.append(self.create_edge(tree.name, tleavesName))
            lbLeaves = self.create_lable_table(leafNodes, tleavesName)

        lbThis = self.create_lable_table([tree], tree.name)

        dotResult = '{}{}{}{}'.format(lbThis, lbLeaves,
                                      self.lst_to_str(subTrees),
                                      self.lst_to_str(edges))

        return dotResult


def DotGraph(node):
    v = VerticalDotLeaves()

    # always add the option node[shape=none]
    options = 'node [shape=none];\n\n'
    r = v.DotGraph(node)
    return '\ndigraph tree {{\n\n{0}{1}}}\n'.format(options, r)
