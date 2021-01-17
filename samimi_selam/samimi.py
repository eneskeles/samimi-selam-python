
import random
import re
from datetime import datetime
from samimi_selam.sifatlar import TURKISH_ADJECTIVES
from samimi_selam.isimler import TURKISH_NOUNS
from samimi_selam.tamlama import tamlama_ekini_temizle

def last_vowel(word):
	match = re.search(r'([aeıioöuü])[^aeıioöuü]*$', word)
	if match:
		return match.group(1)

def make_plural(noun):
	vowel = last_vowel(noun)
	return noun + 'lerim' if vowel in {'e', 'i', 'ö', 'ü', None} else noun + 'larım'
	
def timed_greeting_words(hour):
	if hour > 4 and hour <= 12:
		return "günaydın"
	elif hour > 12 and hour <= 16:
		return "tünaydın"
	elif hour > 16 and hour <= 22:
		return "iyi akşamlar"
	return "iyi geceler"
	
def clear_suffix(noun):
	words = noun.split()
	if len(words) == 1:
		return noun
	words[-1] = tamlama_ekini_temizle(words[-1])
	return " ".join(words)
	
def make_greeting():
	now = datetime.now()
	if now.day == 31 and now.month ==11: 
		greeting_words = "mutlu yıllar"
	else:
		greeting_words = timed_greeting_words(now.hour)
	
	adjective = random.choice(TURKISH_ADJECTIVES)
	noun = make_plural(clear_suffix(random.choice(TURKISH_NOUNS)))
	return '{} {} {}'.format(greeting_words, adjective, noun)

