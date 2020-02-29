'''
# 繰り返し二乗
# 2のn乗を高速に計算する
'''
def repeat_two_square( n ):
    if n == 1:
        return 2
    x = repeat_two_square( n//2 )
    x *= x
    if n % 2 == 1:
        x *= 2
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

print(repeat_two_square( 5 ))
print(gcd(3355,2379))