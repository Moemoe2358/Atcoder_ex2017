# 3 本の柱が等間隔に並んでいます。柱の高さは左から順に a メートル, b メートル, c メートル です。 柱の先端が同一直線上に並んでいる時、つまり b−a=c−b を満たしているとき、 この柱の並び方を美しいと呼びます。
# 柱の並び方が美しいかどうかを判定してください。

a, b, c = map(int, raw_input().split())

if c - b == b - a:
	print "YES"
else:
	print "NO"