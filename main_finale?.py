from pytube import *
from pytube import extract
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import re
from youtube_transcript_api import YouTubeTranscriptApi



SAVE_PATH = os.getcwd()  # to_do

lista_video = []
lista_video_re =[]
dizionario = {}
dizionario_esito = {}


#################DA COMPLETARE###################
word = 'rita de crescenzo' #qua cerchi la parola chiave
possibili_alternative_str = ['quello', 'quella'] #aggiungete qua le parole come nell'esempio]
#################non toccare più###################

s = Search(word)
for numero in range(1):
    s.results
    s.get_next_results()

for v in s.results:
  lista_video.append(v.watch_url)

for l in lista_video:
    video_id = extract.video_id(l)
    try:
     subtitle = YouTubeTranscriptApi.get_transcript(video_id, languages=['it'])
     #print(subtitle)
     dizionario[l] = subtitle
    except:
     continue


print("ok")
print("ja")


for pa in possibili_alternative_str:
 for key, value in dizionario.items():
    video = value #creo una lista di dizionari
    valore_lista = []
    for frase in video: #itero per ogni dizionario
        for chiave, valore in frase.items(): #itero in ogni dizionario (frase)
         lista = list(frase.items())
         testo = str(valore)
         ricerca = re.findall(pa, testo) #lasciare search
         if ricerca:
             #[x.group() for x in re.finditer(pa, testo)]
             tuplo = lista[1]
             valore = tuplo[1]
             valore_lista.append(valore)
             #valore = str(datetime.timedelta(seconds=valore))
             dizionario_esito[key] = valore_lista





for link, tempistica in dizionario_esito.items():
    video = YouTube(link)
    file_video = video.streams.filter(only_audio=True).first().download()
    iterazioni = len(tempistica)
    for minuto in tempistica:
     volta = str(tempistica.index(minuto))
     nome = video.title
     print(file_video)
     minuto_fine_ms = minuto + 7
     estratto= volta+"Ext_"+nome+'.mp4'
     try:
      ffmpeg_extract_subclip(file_video, minuto, minuto_fine_ms, targetname=estratto)
     except:
         continue
















