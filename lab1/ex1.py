class ComplexNum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    

    def __add__(self, adder):
        return self.real + adder.real, self.imag + adder.imag

if __name__ == "__main__":
    complex1 = ComplexNum(1,3)
    complex2 = ComplexNum(1,2)

    print(complex1 + complex2)