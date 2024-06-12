class Chamber:
    def __init__(self, superlayerlist, width, datastore):

        self.Field = []
        self.Width = width
        self.Superlayerlist = superlayerlist
        self.Hight = sum(self.Superlayerlist)
        datastore.put("chamber", self)

        t = True
        for i in range(len(self.Superlayerlist)):
            for j in range(int(self.Superlayerlist[i])):
                if t:
                    self.Field.append(str("o") * self.Width)
                else:
                    self.Field.append(str("O") * self.Width)
            t = not t

    def getFeld(self):
        return self.Field

    def getWidth(self):
        return self.Width

    def getHight(self):
        return self.Hight

    def execute(self, datastore):  # Output in correct format
        pass

    def __del__(self):
        print('"Chamber" module destroyed')
