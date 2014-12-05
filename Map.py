import os

""" Represents one individual tile on the map """
class Tile:
    def __init__(self, ID, Name, Obstacle):
        self.ID = ID               # ID number for the tile
        self.Name = Name           # Name of the material/texture (also the file name)
        self.Obstacle = Obstacle   # Does it obstruct movement?

""" Represents one vertical column of the map """
class MapColumn:
    def __init__(self, Pattern):
        self.Data = []
        self.Size = 0

        tokens = Pattern.split(' ')
        self.Size = len(tokens)

        for i in range(0, self.Size):
            self.Data.append(int(tokens[i]))

""" The map object: only one is needed for the game object """
class Map:

    def __init__(self):
        self.VersionString = 'Version 1'

        self.CurrentMap = None
        self.MapLoaded = False

        self.StartPosX = 0
        self.StartPosY = 0

        self.Tiles = []   # Contains a list of tile objects
        self.NumTiles = 0

        self.MapData = []
        self.NumColumns = 0

    """ Clear object data """
    def Clear(self):
        self.CurrentMap = None
        self.MapLoaded = False

        self.StartPosX = 0
        self.StartPosY = 0

        self.Tiles = []
        self.NumTiles = 0

        self.MapData = []
        self.NumColumns = 0

    """ Return X and Y start co-ordinates in a map """
    def getStartX(self):
        return self.StartPosX

    def getStartY(self):
        return self.StartPosY

    def Info(self):
        print('This map has ' + str(self.NumColumns) + ' columns')

    """ Check if block at x,y co-ordinates are solid or not
        These are map values, not pixel """
    def isSolid(self, x, y):
        Result = False
        TileID = self.MapData[int(x/32)].Data[int(y/32)]

        for i in range(0, self.NumTiles):
            if int(TileID) == int(self.Tiles[i].ID):
                if self.Tiles[i].Obstacle == True:
                    Result = True
                    break
        return Result

    """ Return the tile ID at map x,y """
    def getTileID(self, x, y):
        return self.MapData[x].Data[y]


    """ Load a map by name """
    def Load(self, MapName):

        self.Clear()
        infile = open('map/' + MapName + '.map', 'r')
        state = 0

        while True:
            # Read in a line and remove the newline character
            line = str.rstrip(infile.readline())

            # Stop at EOF
            if line == '':
                break

            # Verify version information
            if (state == 0) and (line == self.VersionString):
                state = 1
                continue
            elif (state == 0) and (line != self.VersionString):
                print('Invalid map file or incorrect version.')
                break

            if state > 0:
                if state == 1:
                    tokens = line.split(' ')
                    if tokens[0] == 'Start':
                        self.StartPosX = (int(tokens[1]) * 32)
                        self.StartPosY = (int(tokens[2]) * 32)
                        continue
                    if tokens[0] == 'Tiles':
                        state = 2
                        continue

                if state == 2:
                    if line == 'Pattern':
                        state = 3
                        continue
                    else:
                        # Read in tile data
                        self.NumTiles += 1
                        tokens = line.split(' ')
                        self.Tiles.append(Tile(tokens[0], tokens[1], True if int(tokens[2]) == 1 else False))

                if state == 3:
                    if line == 'End':
                        self.MapLoaded = True
                        break
                    else:
                        # Read in map pattern data, one column at a time
                        self.NumColumns += 1
                        self.MapData.append(MapColumn(line))

        infile.close()
