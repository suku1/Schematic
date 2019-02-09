# Schematic
Minecraftにおけるポスター制作補助用プログラム.  
Schematicファイルを自動でブロックID毎に分割, 数が多い順に並べ替えて積層する. 

## Requires  
必須モジュール  
 - [Numpy](https://github.com/numpy/numpy)
```bash
$ pip install numpy
```
 - [NBTlib](https://github.com/vberlier/nbtlib)  
```bash
$ pip install nbtlib
```

## Usage
1. schematic.pyおよびSchematic.batと目的のSchematicファイル*.schematicを同じフォルダに置く.  
2. SchematicファイルをSchematic.batにドラッグ&ドロップ. 
3. 同じフォルダに変換後のファイル*_rebuild.schematicが生成される. 
  
※高さ1以外のファイルは使用不可. 

## Licence

MIT

## Author

[suku1](https://github.com/suku1)
