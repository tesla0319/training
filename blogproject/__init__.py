print('私の名前は鈴木彩音です')
print('Python難しいです')

i = 365
if i < 500:
  print('500より小さい')
else:
  print('500より大きい')

class Profile:
 def __init__(self,name,age,sex):
   self.name = name
   self.age = age
   self.sex = sex

 def show(self):
   print(f'名前：{self.name} 年齢：{self.age} 性別：{self.sex}')

if __name__ == '__main__':
 p1 = Profile('町田聖子','45歳','女')
 p2 = Profile('中崎啓人','65歳','男')
 p1.show()
 p2.show()

 print(p1.show(),p2.show())

