# 筋力をつけたい高橋君は、AtCoder 社のトレーニング設備で、トレーニングをすることにしました。
# AtCoder 社のトレーニング設備には N 個のボタンがついており、ちょうど 1 個のボタンが光っています。 ボタンには、1 から N までの番号がついています。 ボタン i が光っているときにそのボタンを押すと、ボタン i の明かりが消え、その後ボタン ai が光ります。i=ai であることもあります。 光っていないボタンを押しても、何も起こりません。
# 最初、ボタン 1 が光っています。高橋君は、ボタン 2 が光っている状態で、トレーニングをやめたいと思っています。
# そのようなことは可能かどうか判定し、もし可能なら最低で何回ボタンを押す必要があるかを求めてください。

n = input()
l = []

for i in range(n):
	a = input()
	l.append(a)

count = 0
b = 1
while b != 2 and count <= n:
	count += 1
	b = l[b - 1]

if count > n:
	print -1
else:
	print count