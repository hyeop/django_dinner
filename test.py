import googletrans
from googletrans import Translator

text1 = "학생여러분 안녕하세요. 오늘 하루도 고생하셨습니다."

translator = Translator()
trans1 = translator.translate(text1, src='ko', dest='en')
print("English to Japanese: ", trans1.text)

#  'zh-cn': 'chinese (simplified)',
#  'en': 'english',
#     'ko': 'korean',
#  'vi': 'vietnamese',
#    'ja': 'japanese',