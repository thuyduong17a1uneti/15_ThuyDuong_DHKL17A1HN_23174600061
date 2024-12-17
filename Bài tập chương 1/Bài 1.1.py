class Hinhchunhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def chu_vi(self):
        return (self.dai + self.rong) * 2
       
    def dien_tich(self):
        return self.dai * self.rong
    
    def in_thong_tin(self):
        print(f"Độ dài cạnh:{self.dai}")
        print(f"Độ rộng cạnh:{self.rong}")
        print(f"Chu vi hình chữ nhật:{self.chu_vi()}")
        print(f"Diện tích hình chữ nhật:{self.dien_tich()}")


dai = float(input("Độ dài cạnh là:"))
rong = float(input("Độ rộng cạnh là:"))

Hcn = Hinhchunhat ( dai, rong)
Hcn.in_thong_tin()