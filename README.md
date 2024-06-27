# ナンプレのテストプログラム
※最終的には（https://www.lifewithpython.com/2020/02/python-sudoku-solver.html）のプログラムを参考に、mp24_5.pyとして導入しました。  
## main.py
周囲を完全にトリミングされたナンプレの画像から一マスずつ数字を認識し、空白部は0として配列に格納します  
## imgmodel.py
サンプルとして用意したナンプレの数字画像（正方形）から数字のみを切り取り、学習します
## trim.py
main.pyにもある、数字部分を切り取るプログラムです。使用した画像はフォントの大きさの関係で、ほぼ同じサイズに切り取ることができました
## allcheck.py
3✕3ナンプレの解を全探索するプログラム、
