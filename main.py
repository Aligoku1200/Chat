import os
os.system("pip install amino.li")
os.system("pip install requests")
import aminoli,time,requests 
os.system("clear")
Ç=aminoli.Client()
Ç.login("xzv@usbc.be","GOKU12")
TT="8227089815:AAEAWDTBkzNtTfuf0PfFZvh-wEFAKSihU2w"
TC="8100160592"
U=[]
L=Ç.get_from_code("http://aminoapps.com/p/prd2qm")
C=L.comId
O=L.objectId
S=aminoli.SubClient(comId=C,profile=Ç.profile)
X1=S.get_chat_users(chatId=O,start=0,size=100).userId
U.append(X1)
while 1:
	X2=S.get_chat_users(chatId=O,start=0,size=100).userId
	if X2==U:
		print("نوبة فاضية")
		pass
	elif X2!=U:
		XX=" واحد دخل الشات الحقه"
		url = f"https://api.telegram.org/bot{TT}/sendMessage"
		params = {"chat_id": TC,"text": XX,"parse_mode": "HTML"}
		response = requests.post(url, params=params)
		print(0)
		pass
	time.sleep(60)
