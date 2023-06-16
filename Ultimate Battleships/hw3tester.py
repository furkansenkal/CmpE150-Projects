from subprocess import PIPE, Popen
import os.path
from pathlib import Path

testSayisi = 5  # Buraya hocanın gönderdiği test inputlarının sayısını yazıyoruz.
# Hoca yeni bir input serisi gönderene kadar 5 tane olduğu için şimdilik kodda değiştirilecek herhangi bir durum yok.
# Main.py dosyasında FILE_OUTPUT_FLAG = True olmalı ve tüm dosyaların aynı dizinde olması gereklidir!
# Dosyaların adı hocanın gönderdiği şekilde default input1 input2 output1 output2 şeklinde olmalıdır.
# Kodunuzun çıktıları testOutput.txt lerin içine depolanacağı için yanlış kısımlarınızı ordan kontrol edebilirsiniz.
for i in range(1, testSayisi+1):
	INP_FILE_NAME = f'input{i}.txt'
	OUT_FILE_NAME = f'output{i}.txt'
	CODE_FILE_NAME = 'Main.py'  # Default Main.py
	inpFile = open(INP_FILE_NAME, 'r')
	try:
		inpList = inpFile.readlines()
		inpList[-1] = inpList[-1] + "\n"
		inp = ''.join(inpList)
		child = Popen(['python', CODE_FILE_NAME], stdin=PIPE, stdout=PIPE)
		child.communicate(inp.encode('ascii'))
		with open(OUT_FILE_NAME, 'r') as f:
			u = open("UltimateBattleships.txt", "r")
			if f.read() == u.read():
				print(f"input{i} doğru")
			else:
				print(f"input{i} kod düzgün fakat çıktı Hatalı")
			u.close()
	except:
		inpFile.close()
		del child
		print(f"input{i} kod düzgün çalışmıyor")
	else:
		inpFile.close()
		del child
		a = os.path.isfile(f"testOutput{i}.txt")
		if a:
			os.remove(f"testOutput{i}.txt")
		os.rename("UltimateBattleships.txt", f"testOutput{i}.txt")
