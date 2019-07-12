# coding: utf-8
# Projeto Criado Por: Cleiton Junior
print("""
#######   #         ######   #     #
#         #         #    #    #  # 
#         #         ######      #
#         #         #    #      #
#######   ########  #    #      #  | Tabuada de Multiplicação
""")
tabuada=int(input("Tabuada do numero: "))

for count in range(20): # Caso queira aumentar valor da tabuada so alterar o 20
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )

