import  perceptron



zeka=perceptron.Perceptron()

zeka.ekle([5,4,6],[3,4,3])
print(zeka.baslat())
zeka.egitim(0,1,0)
print(zeka.baslat())