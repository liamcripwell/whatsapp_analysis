# whatsapp_analysis
This repo can be used to analyze a WhatsApp chat log. Instructions for obtaining your own chat log file from WhatsApp can be found here:
  * [iPhone](https://faq.whatsapp.com/en/iphone/20888066)
  * [Android](https://faq.whatsapp.com/en/android/23756533/?category=5245251)

## WhatsappAnalyzer
The ```WhatsappAnalyzer``` class can be used as follows:
```python
from whatsapp import WhatsappAnalyzer   # import

wa = WhatsappAnalyzer('data/_chat.txt') # construct instance with path to chat log 

wa.parse()                              # run parsing process
```
