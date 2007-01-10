from futil.foaf.foafFilter import FoafFilter

class NameFilter(FoafFilter):
    
    def __init__(self, next=None):
        self.next = next
        if ( next ):
            FoafFilter.__init__(next)

    
    
    def process(self, data, foaf):
        print "Proccessing ", self.__class__
        foaf['name'] = "Unimplemented"
        return foaf