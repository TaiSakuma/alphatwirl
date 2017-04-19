# Tai Sakuma <tai.sakuma@cern.ch>

import ROOT

from ..roottree.Events import Events

##__________________________________________________________________||
class TTreeWrapper(object):
    """wrap ExRootTreeReader so that Events can treat it as TTree
    """
    def __init__(self, treeReader):
        self.treeReader = treeReader

    def GetDirectory(self):
        return None

    def GetEntries(self):
        return self.treeReader.GetEntries()

    def GetEntry(self, entry):
        return self.treeReader.ReadEntry(entry)

##__________________________________________________________________||
class DelphesEvents(Events):
    def __init__(self, tree, maxEvents = -1, start = 0):
        self.treeReader = ROOT.ExRootTreeReader(tree)
        super(DelphesEvents, self).__init__(
            tree = TTreeWrapper(self.treeReader),
            maxEvents = maxEvents, start = start
        )
        self.file = tree.GetDirectory() # so a file won't close

        self.branches = { }

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            super(DelphesEvents, self)._repr_contents()
        )

    def __getattr__(self, name):

        if name in self.branches:
            return self.branches[name]

        branch = self.treeReader.UseBranch(name)
        self.branches[name] = branch

        if self.iEvent >= 0:
            self.tree.GetEntry(self.start + self.iEvent)

        return self.branches[name]

##__________________________________________________________________||
