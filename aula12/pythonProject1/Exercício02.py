
def primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

print(primo(45))
print(primo(7))
print(primo(11))
print(primo(10))