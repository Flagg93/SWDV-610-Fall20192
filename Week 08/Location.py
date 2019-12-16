from Asset import *
class Location:
    def __init__(self, name):
        self.Name = name
        self.Assets = list()
    
    def GetAllAssets(self):
        assets = list()
        for x in self.Assets:
            assets.append(x.AssetTag)
        return assets

    def GetAsset(self, tag):
        index = self.GetAllAssets().index(tag)
        if index != None:
            return self.Assets[index]


