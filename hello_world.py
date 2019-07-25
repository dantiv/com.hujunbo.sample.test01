def main():
    print("Start Main")


if __name__ == "__main__":
    main()

print()
print("# ============== 算数（さんすう） ")
num01 = 105
num02 = 335
print("# -------------- 足し算(たしざん) ")
print("# {} + {} = ".format(num01, num02), end="")
i = num01 + num02
print(i)

num03 = 45
num04 = 35
print("# -------------- 引き算(ひきざん) ")
print("# {} - {} = ".format(num03, num04), end="")
i = num03 - num04
print(i)

num05 = 35
num06 = 8
print("# -------------- 掛け算(かけざん) ")
print("# {} * {} = ".format(num05, num06), end="")
i = num05 * num06
print(i)

num07 = 40
num08 = 8
# (Python2とPython3で挙動が違うので注意)
print("# -------------- 割り算(わりざん) ")
print("# {} / {} = ".format(num07, num08), end="")
i = num07 / num08
print(i)

num09 = 43
num10 = 8
print("# -------------- 割り算(わりざん)(少数切り捨て) ")
print("# {} / {} = ".format(num09, num10), end="")
i = num09 // num10
print(i)

num11 = 49
num12 = 9
print("# -------------- 剰余(じょうよ) ")
print("# {} * {} = ".format(num11, num12), end="")
i = num11 % num12
print(i)

num13 = 12
num14 = 2
print("# -------------- 冪乗(べきじょう)平方 ")
print("# {} ** {} = ".format(num13, num14), end="")
i = num13 ** num14
print(i)

print()
text = "Hello World  "
print("# ============== 文字列（もじれつ） ")
print("# >> {} <<".format(text))
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

