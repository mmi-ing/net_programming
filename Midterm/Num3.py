class MyComplex:
    def __init__(self, real_1, imaginary_1, real_2, imaginary_2):
        self.real_1 = real_1
        self.imaginary_1 = imaginary_1
        self.real_2 = real_2
        self.imaginary_2 = imaginary_2
    def multiplication(self):
        a = self.real_1
        b = self.imaginary_1
        c = self.real_2
        d = self.imaginary_2
        result_real_plus = a + c
        result_imaginary_plus = b + d
        print(f"{result_real_plus}{result_imaginary_plus:+}i")
        result_real = a - c
        result_imaginary = b - d
        print(f"{result_real}{result_imaginary:+}i")


result = MyComplex(2, -3, -5, 4)
result.multiplication()
