texto = "We are learning/ Python for DevOps"
#Separated by space use split with double comillas ""
new_texto = texto.split("/")
#print("Words:",new_texto)


#print(texto.split("/")[1])

arn = "arn:partition:service:region:account-id:resource-type/resource-id"

new_arn = arn.split('/')
#print("display arn:", new_arn)
#print("display arn:", new_arn[0])

mi_lista = [1,2,3,4,5,6]
mi_lista[1]=8
# print("my list:",mi_lista)
servers=['192.168.1.2','192.168.1.4','192.168.1.5','192.168.1.6']
print("servidores:",servers)
servers.append('192.168.1.8')
print("servidores:",servers)