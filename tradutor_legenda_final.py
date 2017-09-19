import io
from mtranslate import translate

l1=io.open('legenda_ingles2.srt','r',encoding='utf-8')
l3=io.open('legenda_traduzida.srt','w',encoding='utf-8')
#traduz do google

while 1:
	line=l1.readline()
	if not line:
		l3.write(translate(line,'pt','en'))
		break
	l3.write(translate(line,'pt','en'))
	l3.write('\n')
l1.close()
l3.close()



#corrige erro google translate
l1=io.open('legenda_traduzida.srt','r',encoding='utf-8')
l2=io.open('legenda_traduzida.srt','r',encoding='utf-8')
l3=io.open('legenda_final.srt','w',encoding='utf-8')


prox=l2.read(1)
anterior='c'

atual=l1.read(1)
while(atual!=""):
	prox=l2.read(1)
	if(atual=='-' and prox=='>'):
		l3.write('-')
	if(atual!='\n'):	
		if(prox!=""):
			if((ord(prox)<58) and (ord(prox)>47)):
				if((ord(anterior)!=62)):
					atual=l1.read(1)
					prox=l2.read(1)
	anterior=atual;
	l3.write(atual)
	#print(atual)
	atual=l1.read(1)


l1.close()
l2.close()
l3.close()