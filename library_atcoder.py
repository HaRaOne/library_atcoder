# 繰り返し二乗
def repeat_two_square( n ):
    if n == 1:
        return 2
    x = repeat_two_square( n//2 )
    x *= x
    if n % 2 == 1:
        x *= 2
    return x

print(repeat_two_square( 5 ))