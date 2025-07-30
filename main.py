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
	X2=S.get_chat_messages(chatId=O,size=1).messageId
	for X3 in X2:
		X4=S.get_message_info(chatId=O,messageId=X3)
		X5=X4.author.userId
		X6=X4.content
		if X5 in U:
			print("نوبة فاضية")
		if X6!=None:
			if X6.startswith("."):
				print("نوبة فاضية")
		if X5 not in U:
			X8=S.get_chat_users(chatId=O,start=0,size=100).userId
			if X5 in X8:
				XX=" واحد دخل الشات الحقه"
				url = f"https://api.telegram.org/bot{TT}/sendMessage"
				params = {"chat_id": TC,"text": XX,"parse_mode": "HTML"}
				response = requests.post(url, params=params)
				print(0)
				pass
			else:
				print("نوبة فاضية")
	time.sleep(60)
