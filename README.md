# com.hujunbo.sample.test01
learn python for kids

## Python命名規則一覧
|対象|ルール|例|
|:---|:---|:---|
|パッケージ|全小文字 なるべく短くアンダースコア非推奨|tqdm, requests ...|
|モジュール|全小文字 なるべく短くアンダースコア可|sys, os,...|
|クラス|最初大文字 + 大文字区切り|MyFavoriteClass|
|例外|最初大文字 + 大文字区切り|MyFuckingError|
|型変数|最初大文字 + 大文字区切り|MyFavoriteType|
|メソッド|全小文字 + アンダースコア区切り|my_favorite_method|
|関数|全小文字 + アンダースコア区切り|my_favorite_function|
|変数|全小文字 + アンダースコア区切り|my_favorite_instance|
|定数|全大文字 + アンダースコア区切り|MY_FAVORITE_CONST|

- C/C++ のモジュールはアンダースコアで開始
- 自クラス内でのみ使用する内部変数と内部メソッドはアンダースコアで開始


## Python 言語独特文
### 空の関数を定義（pass文）
pass 文は何もしません。 pass は、文を書くことが構文上要求されているが、プログラム上何の動作もする必要がない時に使われます:
```
>>>
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...
```
これは最小のクラスを作るときによく使われる方法です:
```
>>>
>>> class MyEmptyClass:
...     pass
...
```
pass のもう 1 つの使い道は、新しいコードを書いているときの関数や条件文の仮置きの本体としてです。こうすることで、より抽象的なレベルで考え続けられます。 pass は何事も無く無視されます
```
>>>
>>> def initlog(*args):
...     pass   # Remember to implement this!
...
```

## 参考サイト：  
[Python 3 標準ライブラリ](https://docs.python.org/ja/3/library/index.html)  
[Python命名規則一覧](https://qiita.com/naomi7325/items/4eb1d2a40277361e898b)  

