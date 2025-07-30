import os
os.system("pip install amino.li")
os.system("pip install requests")
import aminoli,time,sleep
os.system("clear")
Ç=aminoli.Client(devicId="19EC08F654EDA29F919257B18C9B7F4985D59C48BE179EE53DA63532F7588BB92505525E82A3E707C0")
Ç.login("xzv@usbc.be","GOKU12")
TT="8227089815:AAEAWDTBkzNtTfuf0PfFZvh-wEFAKSihU2w"
TC="8100160592"
L=Ç.get_from_code("http://aminoapps.com/p/prd2qm")
C=L.comId
O=L.objectId
S=aminoli.SubClient(comId=C,profile=Ç.profile)
X1=S.get_chat_messages(chatId=O,size=1).messageId
while True:
	for X2 in X1:
		X3=S.get_message_info(chatId=O,messageId=X2)
		X4=X3.messageType
		if X4==101:
			XX=" واحد دخل الشات الحقه"
			url = f"https://api.telegram.org/bot{TT}/sendMessage"
			params = {"chat_id": TC,"text": XX,"parse_mode": "HTML"}
			response = requests.post(url, params=params)
			print(response.json())
			pass
	time.sleep(60)
			
	
