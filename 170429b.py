# あなたは、正の整数をいくつか選び、それらの総和を求めます。
# 選ぶ数の上限や、選ぶ整数の個数に制限はありません。 どんなに大きな整数を選んでもよいですし、整数を 5000 兆個選んでもよいです。 ただし、選ぶ数はすべて A の倍数でなくてはいけません。 また、少なくとも 1 つは整数を選ばなくてはいけません。
# そして総和を B で割ったあまりが C となるようにしたいです。 こうなるように整数を選ぶことが出来るか判定してください。
# 出来るならば YES、そうでないならば NO を出力してください。

a, b, c = map(int, raw_input().split(' '))

i = 0

while (i < 1000):
	i += 1
	if (a * i) % b == c:
		print "YES"
		break

if i == 1000:
	print "NO"