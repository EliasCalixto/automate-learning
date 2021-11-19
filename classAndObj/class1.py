class Fraccion:

    def __init__(self,n,d):
        self.num = n
        self.den = d

    def imprime(self):
        print(self.num,"/",self.den)

def main():
    A = Fraccion(5,6)
    A.imprime()
    B = Fraccion(1,2)
    B.imprime()

if __name__ == "__main__":
    main()
