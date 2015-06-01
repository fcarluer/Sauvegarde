'''
Created on 28 mai 2015

@author: fcarluer
'''
from Personne import Personne

if __name__ == '__main__':
    pass
Jose=Personne("José", "Sperer") 
print("{} {} agé de {} et habitant à {}.".format(Jose.nom,Jose.prenom,Jose.age, Jose.lieu_residence))

Jose.lieu_residence="Marseille"
i=chr(121)
s=chr(247)
p=chr(95)
m=chr(167)
Largeur=(20)

print("{} {} agé de {} et habitant à {}.".format(Jose.nom,Jose.prenom,Jose.age, Jose.lieu_residence))
print(Jose)
print(m*Largeur)
print("#    "+i+"#")
print("#####"+p+"#")
print("#     #")
print("# #####")
print("#     "+s)
print("#######")
#for j in range(1,255):
#    print(j,"=",chr(j))
    
