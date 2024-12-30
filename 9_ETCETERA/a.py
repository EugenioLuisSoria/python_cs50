aaa = 0

def main():
    global aaa
    aaa += 1
    print(aaa)
    
def main2():
    global aaa
    aaa += 1    
    print(aaa)

main()
main2()