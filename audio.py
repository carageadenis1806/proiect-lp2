import urllib.request
from pydub import AudioSegment
from pydub.playback import play
#introducem fisierul in pydub
beat1 = AudioSegment.from_wav("beat1.wav")
 #se repeta beat-ul de 2 ori
loop = beat1 * 2
# lungimea in milisecunde
length = len(beat1)
# fade time
fade_time = int(length * 0.5)
# fade in/fade out
faded = beat1.fade_in(fade_time).fade_out(fade_time)
#se introduce al doilea beat in pydub
beat2 = AudioSegment.from_wav("beat2.wav")
#se mixeaza cu primul beat
mixed = beat2[:length].overlay(beat1)
filtered = beat2.low_pass_filter(3000)
beat1 = loop.reverse().pan(-0.5).overlay(loop.pan(0.5))
final = filtered.overlay(loop - 3, loop=True)
final.export("final.wav",format="wav")

