from ToolsUtil.ConsoleTools import ConsoleTools


# 入口
def main():
    print("Start Main")


if __name__ == "__main__":
    main()

#
# Python 初心者ノット
# コメント付きで出力してよりわかりやすくPython言語を理解する
# 1.基本な値と演算式
#
# 改行
print()
ConsoleTools.print_main("# ============== 算数（さんすう） ")
num01 = 99999
num02 = 888
ConsoleTools.print_sub("# -------------- 足し算(たしざん) ")
print("{} + {} = ".format(num01, num02), end="")
i = num01 + num02
print(i)

num01 = 45
num02 = 35
ConsoleTools.print_sub("# -------------- 引き算(ひきざん) ")
print("{} - {} = ".format(num01, num02), end="")
i = num01 - num02
print(i)

num01 = 45
num02 = 35
ConsoleTools.print_sub("# -------------- 掛け算(かけざん) ")
print("{} * {} = ".format(num01, num02), end="")
i = num01 * num02
print(i)

num01 = 45
num02 = 35
# (Python2とPython3で挙動が違うので注意)
ConsoleTools.print_sub("# -------------- 割り算(わりざん) ")
print("{} / {} = ".format(num01, num02), end="")
i = num01 / num02
print(i)

num01 = 45
num02 = 35
ConsoleTools.print_sub("# -------------- 割り算(わりざん)(少数切り捨て) ")
print("{} / {} = ".format(num01, num02), end="")
i = num01 // num02
print(i)

num01 = 45
num02 = 35
ConsoleTools.print_sub("# -------------- 剰余(じょうよ) ")
print("{} * {} = ".format(num01, num02), end="")
i = num01 % num02
print(i)

num01 = 45
num02 = 35
ConsoleTools.print_sub("# -------------- 冪乗(べきじょう)平方 ")
print("{} ** {} = ".format(num01, num02), end="")
i = num01 ** num02
print(i)

#
# 2.基本な文字列操作
#
# 改行
print()
text = "Hello World  "
ConsoleTools.print_main("# ============== 文字列（もじれつ） ")
print(">> {} <<".format(text))
ConsoleTools.print_sub("# -------------- 前後の空白文字/改行文字を消し去る")
print(text.strip())

ConsoleTools.print_sub("# -------------- 分割")
print(text.split())

ConsoleTools.print_sub("# -------------- 左H文字を消し去る")
print(text.lstrip("H"))

ConsoleTools.print_sub("# -------------- 結合")
print("Hello" + "World")

ConsoleTools.print_sub("# -------------- 文字列フォーマット")
print("{} {}".format("Hello", "World"))

ConsoleTools.print_sub("# -------------- 文字列フォーマットその2")
print("{1} {0}".format("Hello", "World"))

ConsoleTools.print_sub("# -------------- 文字列フォーマットその3")
print("{word2} {word1}".format(word1="Hello", word2="World"))

#
# 3.条件分岐、繰り返し、例外処理
#
# 改行
print()
ConsoleTools.print_main("# ============== FOR ループ数字(すうじ)")
ConsoleTools.print_sub("# -------------- for range(int)")
for i in range(5):
    print("i = " + str(i))
ConsoleTools.print_sub("# -------------- for range(int,int)")
for i in range(1, 5):
    print("i = " + str(i))
ConsoleTools.print_sub("# -------------- for with if")
for i in range(11):
    if i % 3 == 0:
        print("i = " + str(i))

# 改行
print()
ConsoleTools.print_main("# ============== FOR ループ文字列(もじれつ)")
ConsoleTools.print_sub("# -------------- for char in [string]")
for char in 'hello':
    print("char = " + char)

# 改行
print()
ConsoleTools.print_main("# ============== FOR ループ配列(はいれつ)")
ConsoleTools.print_sub("# -------------- for string in string[] with if, break")
strings = ['ruby', 'python', 'perl', 'java', 'c']
for string in strings:
    if string == 'python':
        print('OK -> ' + string)
        break  # 一致したので、breakで抜ける
    print("item = " + string)

ConsoleTools.print_sub("# -------------- for string in string[] with if, break, continue")
strings = ['ruby', 'python', 'perl', 'java', 'c']
for string in strings:
    if string != 'python':
        print("item = " + string)
        continue  # 一致していないので、次のループへ
    print('OK')
    break

ConsoleTools.print_sub("# -------------- for-else with if, break")
scores = [100, 71, 80, 99, 75]  # 70点以下はないので、合格
for score in scores:
    print("score = " + str(score))
    if score <= 70:
        break
else:
    print('合格')

# 改行
print()
ConsoleTools.print_main("# ============== WHILE ループ数字(すうじ)")
ConsoleTools.print_sub("# -------------- while")
num = 1
while num < 4:
    print("num = " + str(num))
    num += 1
ConsoleTools.print_sub("# -------------- while with else")
ConsoleTools.print_sub("# while文の最後に実行される処理を記述する")
total = 0
num = 1
while num < 4:
    print("num = " + str(num))
    total += num
    num += 1
else:
    print("Total = " + str(total))

#
# console 出力関連
#
# 改行
print()
ConsoleTools.print_main("# ============== コンソール出力（しゅつりょく）")
ConsoleTools.print_sub("# -------------- console color コンソールカラー")
print(ConsoleTools.RED + "{}".format("RED") + ConsoleTools.END)
print(ConsoleTools.BLUE + "{}".format("BLUE") + ConsoleTools.END)
print(ConsoleTools.YELLOW + "{}".format("YELLOW") + ConsoleTools.END)
print(ConsoleTools.CYAN + "{}".format("CYAN") + ConsoleTools.END)
print(ConsoleTools.BOLD + "{}".format("BOLD") + ConsoleTools.END)
print(ConsoleTools.GREEN + "{}".format("GREEN") + ConsoleTools.END)
print(ConsoleTools.BLACK + "{}".format("BLACK") + ConsoleTools.END)

#
# 参考、引用コード、学習におすすめ参考サイト
#
# 改行
print()
print("# 参考サイト： ")
print('【Python入門】for文を使った繰り返し文の書き方')
print("https://qiita.com/Morio/items/e8aed85346c0055beea7")
