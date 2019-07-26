from ToolsUtil.ConsoleTools import ConsoleTools


def main():
    print("Start Main")


if __name__ == "__main__":
    main()

# 改行
print()
ConsoleTools.print_main("# ============== 算数（さんすう） ")
num01 = 99999
num02 = 888
ConsoleTools.print_sub("# -------------- 足し算(たしざん) ")
print("{} + {} = ".format(num01, num02), end="")
i = num01 + num02
print(i)

num03 = 45
num04 = 35
ConsoleTools.print_sub("# -------------- 引き算(ひきざん) ")
print("{} - {} = ".format(num03, num04), end="")
i = num03 - num04
print(i)

num05 = 3
num06 = 2
ConsoleTools.print_sub("# -------------- 掛け算(かけざん) ")
print("{} * {} = ".format(num05, num06), end="")
i = num05 * num06
print(i)

num07 = 40
num08 = 8
# (Python2とPython3で挙動が違うので注意)
ConsoleTools.print_sub("# -------------- 割り算(わりざん) ")
print("{} / {} = ".format(num07, num08), end="")
i = num07 / num08
print(i)

num09 = 43
num10 = 8
ConsoleTools.print_sub("# -------------- 割り算(わりざん)(少数切り捨て) ")
print("{} / {} = ".format(num09, num10), end="")
i = num09 // num10
print(i)

num11 = 49
num12 = 9
ConsoleTools.print_sub("# -------------- 剰余(じょうよ) ")
print("{} * {} = ".format(num11, num12), end="")
i = num11 % num12
print(i)

num13 = 12
num14 = 2
ConsoleTools.print_sub("# -------------- 冪乗(べきじょう)平方 ")
print("{} ** {} = ".format(num13, num14), end="")
i = num13 ** num14
print(i)

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

# 改行
print()
ConsoleTools.print_main("# ============== ループ数字(すうじ)")
ConsoleTools.print_sub("# -------------- for range(int)")
for i in range(5):
    print(i)
ConsoleTools.print_sub("# -------------- for range(int,int)")
for i in range(1, 5):
    print(i)
ConsoleTools.print_sub("# -------------- for with if")
for i in range(11):
    if i % 3 == 0:
        print(i)

# 改行
print()
ConsoleTools.print_main("# ============== ループ文字列(もじれつ)")
ConsoleTools.print_sub("# -------------- for char in [string]")
for char in 'hello':
    print(char)

# 改行
print()
ConsoleTools.print_main("# ============== ループ配列(はいれつ)")
ConsoleTools.print_sub("# -------------- for string in string[] with if, break")
strings = ['ruby', 'python', 'perl', 'java', 'c']
for string in strings:
    if string == 'python':
        print('OK -> ' + string)
        break  # 一致したので、breakで抜ける
    print(string)

ConsoleTools.print_sub("# -------------- for string in string[] with if, break, continue")
strings = ['ruby', 'python', 'perl', 'java', 'c']
for string in strings:
    if string != 'python':
        print(string)
        continue  # 一致していないので、次のループへ
    print('OK')
    break

ConsoleTools.print_sub("# -------------- for-else with if, break")
scores = [100, 71, 80, 99, 75]  # 70点以下はないので、合格
for score in scores:
    if score <= 70:
        break
else:
    print('合格')

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

# 改行
print()
print("# 参考サイト： ")
print('【Python入門】for文を使った繰り返し文の書き方')
print("https://qiita.com/Morio/items/e8aed85346c0055beea7")
