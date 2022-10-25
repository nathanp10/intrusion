intru=open("intrusion.txt","r")
i=intru.read()
if i=="Il y a eu une intrusion":
    print(i)
    intru=open("intrusion.txt","w")
    intru.write("")

intrusion=True
essaies=5
username='nathan'
mdp='1234'


while essaies>0:
    ton_username=input('saisissez votre username ')
    ton_mdp=input('saisissez votre mot de passe ')
    if ton_username ==username and ton_mdp==mdp:
        print('bienvenue sur ton compte ')
        essaies=-1
        
    else:
        essaies=essaies-1
        print('Attention il te reste',essaies,'essaies ')
        
    
    if essaies==0:
        intru=open("intrusion.txt","w")
        intru.write("Il y a eu une intrusion")
        print("Vous êtes un inposteur sortez de ce programme !!! ")
        intrusion=False


chiffrage={"a":"1","b":"10","c":"11","d":"100","e":"101","f":"110","g":"111","h":"1000","i":"1001","j":"1010","k":"1011","l":"1100","m":"1101","n":"1111","o":"10000","p":"10001","q":"10010","r":"10011","s":"10100","t":"10101","u":"10111","v":"11000","w":"11001","x":"11011","y":"11100","z":"11101","A":"11111","B":"100000","C":"100001","D":"100010","E":"100011","F":"100100","G":"100101","H":"100110","I":"100111","J":"101000","K":"101001","L":"101010","M":"101011","N":"101100","O":"101101","P":"101110","Q":"101111","R":"110000","S":"110001","T":"110010","U":"110011","V":"110100","W":"110101","X":"110110","Y":"110111","Z":"111000",",":"111001",".":"111010","'":"111011","(":"111100",")":"111101","!":"111110","?":"111111",'"':"1000000"," ":"1000001"}

while 1==1 and intrusion==True:

    fichier_a_crypter=str(input('Quel est votre fichier a crypter '))
    fichier_crypter= "fichier_crypter.txt"

    phraseCryptée=""
    
    fichier=open(fichier_a_crypter,"r")
    read=fichier.readlines()
    for p in range(len(read)):
        ligneMot=read[p].split()
        for l in range(len(ligneMot)):
            mot=ligneMot[l]
            
            for lettre in mot:
                if lettre in chiffrage:
                    phraseCryptée += chiffrage[lettre] + " "
                else:
                    phraseCryptée += lettre
            phraseCryptée+=chiffrage[" "] + " "
    fichier.close()
    fichier=open(fichier_crypter, "w")
    fichier.write(phraseCryptée)
    fichier.close()
    print("Voila ta réussi a crypté, j'espère tu aime les 1 et 0 :)")