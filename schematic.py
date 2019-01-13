import sys
import numpy as np
from nbtlib import nbt
from nbtlib import tag

class schematic:
    def __init__(self, filename=None):
        
        self.filename = filename

        if filename != None:
            self.load_data(filename)

        self.sortmode = 0

    def load_data(self, filename=None):
        if filename == None:
            if self.filename == None:
                print('Error!')
            filename = self.filename
        self.rawdata = nbt.load(filename)
        self.maindata = self.rawdata['Schematic']

        self.analyze_data()

    def analyze_data(self):
        self.block = list(np.copy(self.maindata['Blocks']))
        self.data = list(np.copy(self.maindata['Data']))
        self.length = int(np.copy(self.maindata['Length']))
        self.height = int(np.copy(self.maindata['Height'])) #y
        self.width = int(np.copy(self.maindata['Width']))
        
        for i in range(len(self.block)):
            if self.block[i] < 0:
                self.block[i] += 256
        
        self.tag()
        self.count_block()
        self.sort()

    def tag(self):
        self.combined = []
        for i in range(len(self.block)):
            t = str(self.block[i]) + ':' + str(self.data[i])
            self.combined.append(t)

    def count_block(self):
        count = {}
        for n in self.combined:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        self.count = []        
        for key, val in count.items():
            self.count.append({'Name': key, 'Num': val})

    def sort(self):
        if self.sortmode == 0:
            self.count.sort(key=lambda x: -x['Num'])
        elif self.sortmode == 1:
            self.count.sort(key=lambda x: x['Num'])

    def rebuild(self):
        self.block_re = []
        self.data_re = []
        for i in range(len(self.count)):
            name, data = self.count[i]['Name'].split(':')
            name = int(name)
            data = int(data)
            self.block_re.append([])
            self.data_re.append([])
            for j in range(len(self.block)):
                if (self.block[j], self.data[j]) == (name, data):
                    self.block_re[i].append(int(name))
                    self.data_re[i].append(int(data))
                else:
                    self.block_re[i].append(int(0))
                    self.data_re[i].append(int(0))
        self.block_re.insert(0, self.block)
        self.data_re.insert(0, self.data)

        shape = (1, (len(self.count) + 1) * len(self.block))
        self.block_re = np.reshape(self.block_re, shape).tolist()[0]
        self.data_re = np.reshape(self.data_re, shape).tolist()[0]

        self.rawdata.root['Blocks'] = tag.ByteArray(self.block_re)
        self.rawdata.root['Data'] = tag.ByteArray(self.data_re)
        self.rawdata.root['Height'] = tag.Short(len(self.count) + 1)

def main():
    name = sys.argv[1]
    filename = name + '.schematic'
    d = schematic(filename)
    d.rebuild()
    d.rawdata.save(name + '_rebuild.schematic')

if __name__ == '__main__':
    main()
