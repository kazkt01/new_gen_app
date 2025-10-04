# pythonの復習
# 変数の復習
hoge = "こんにちは"
print(hoge)
a = 1
b = 2
sum = a + b
print(sum)

# 関数
def sum():
    return a + b
print(sum())
# テンプレートリテラル "f"
msg = "禁止区域です"
def alert(msg):
    return f"ここは、{msg}"
print(alert(msg))

age = 12

if  age >= 20:
    msg = "禁止区域です"
    def alert(msg):
        return f"ここは、{msg}"
    hoge = alert(msg)
    print(hoge)
else:
    msg = "安全区域です"
    def alert(msg):
        return f"ここは、{msg}"
    hoge = alert(msg)
    print(hoge)