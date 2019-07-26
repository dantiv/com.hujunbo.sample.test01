from ToolsUtil.ConsoleColors import ConsoleColors


def main():
    print("Start Main")


if __name__ == "__main__":
    main()

# 改行
print()
print(ConsoleColors.BOLD + "# ============== 算数（さんすう） " + ConsoleColors.END)
num01 = 99999
num02 = 888
print("# -------------- 足し算(たしざん) ")
print("{} + {} = ".format(num01, num02), end="")
i = num01 + num02
print(i)

num03 = 45
num04 = 35
print("# -------------- 引き算(ひきざん) ")
print("{} - {} = ".format(num03, num04), end="")
i = num03 - num04
print(i)

num05 = 3
num06 = 2
print("# -------------- 掛け算(かけざん) ")
print("{} * {} = ".format(num05, num06), end="")
i = num05 * num06
print(i)

num07 = 40
num08 = 8
# (Python2とPython3で挙動が違うので注意)
print("# -------------- 割り算(わりざん) ")
print("{} / {} = ".format(num07, num08), end="")
i = num07 / num08
print(i)

num09 = 43
num10 = 8
print("# -------------- 割り算(わりざん)(少数切り捨て) ")
print("{} / {} = ".format(num09, num10), end="")
i = num09 // num10
print(i)

num11 = 49
num12 = 9
print("# -------------- 剰余(じょうよ) ")
print("{} * {} = ".format(num11, num12), end="")
i = num11 % num12
print(i)

num13 = 12
num14 = 2
print("# -------------- 冪乗(べきじょう)平方 ")
print("{} ** {} = ".format(num13, num14), end="")
i = num13 ** num14
print(i)

# 改行
print()
text = "Hello World  "
print(ConsoleColors.BOLD + "# ============== 文字列（もじれつ） " + ConsoleColors.END)
print(">> {} <<".format(text))
print("# -------------- 前後の空白文字/改行文字を消し去る")
print(text.strip())

print("# -------------- 分割")
print(text.split())

print("# -------------- 左H文字を消し去る")
print(text.lstrip("H"))

print("# -------------- 結合")
print("Hello" + "World")

print("# -------------- 文字列フォーマット")
print("{} {}".format("Hello", "World"))

print("# -------------- 文字列フォーマットその2")
print("{1} {0}".format("Hello", "World"))

print("# -------------- 文字列フォーマットその3")
print("{word2} {word1}".format(word1="Hello", word2="World"))

# 改行
print()
print(ConsoleColors.BOLD + "# ============== ループ数字(すうじ)" + ConsoleColors.END)
print("# -------------- for range(int)")
for i in range(5):
    print(i)
print("# -------------- for range(int,int)")
for i in range(1, 5):
    print(i)
print("# -------------- for with if")
for i in range(11):
    if i % 3 == 0:
        print(i)

# 改行
print()
print(ConsoleColors.BOLD + "# ============== ループ文字列(もじれつ)" + ConsoleColors.END)
print("# -------------- for char in [string]")
for char in 'hello':
    print(char)

# 改行
print()
print(ConsoleColors.BOLD + "# ============== ループ配列(はいれつ)" + ConsoleColors.END)
print("# -------------- for string in string[] with if, break")
strings = ['ruby', 'python', 'perl', 'java', 'c']
for string in strings:
    if string == 'python':
        print('OK -> ' + string)
        break  # 一致したので、breakで抜ける
    print(string)

print("# -------------- for string in string[] with if, break, continue")
strings = ['ruby', 'python', 'perl', 'java', 'c']
for string in strings:
    if string != 'python':
        print(string)
        continue  # 一致していないので、次のループへ
    print('OK')
    break

print("# -------------- for-else with if, break")
scores = [100, 71, 80, 99, 75]  # 70点以下はないので、合格
for score in scores:
    if score <= 70:
        break
else:
    print('合格')

# 改行
print()
print(ConsoleColors.BOLD + "# ============== コンソール出力（しゅつりょく）" + ConsoleColors.END)
print("# -------------- console color コンソールカラー")
print(ConsoleColors.RED + "{}".format("RED") + ConsoleColors.END)
print(ConsoleColors.BLUE + "{}".format("BLUE") + ConsoleColors.END)
print(ConsoleColors.YELLOW + "{}".format("YELLOW") + ConsoleColors.END)
print(ConsoleColors.CYAN + "{}".format("CYAN") + ConsoleColors.END)
print(ConsoleColors.BOLD + "{}".format("BOLD") + ConsoleColors.END)
print(ConsoleColors.GREEN + "{}".format("GREEN") + ConsoleColors.END)
print(ConsoleColors.BLACK + "{}".format("BLACK") + ConsoleColors.END)

# 改行
print()
print("# 参考サイト： ")
print('【Python入門】for文を使った繰り返し文の書き方')
print("https://qiita.com/Morio/items/e8aed85346c0055beea7")
