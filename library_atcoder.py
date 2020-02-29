'''
# 繰り返し二乗
# aのn乗を高速に計算する
'''
def repeat_any_square( a,n ):
    if n == 1:
        return a
    x = repeat_any_square( a,n//2 )
    x *= x
    if n % 2 == 1:
        x *= a
    return x

'''
# ユークリッドの互除法 最大公約数
# a >= b
'''
def gcd(a,b):
    if a % b == 0:
        return b
    surplus = a % b
    ans = gcd(b,surplus)
    return ans

print(repeat_any_square( 7,7 ))
print(gcd(3355,2379))