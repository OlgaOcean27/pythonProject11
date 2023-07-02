import telebot


TOKEN = "6288638036:AAHO89P731KrK4wtS_jreeI-p_JcQSEA25U"


bot = telebot.TeleBot(TOKEN)

keys = {
    'евро': 'EUR',
    'доллар': 'USD',
    'биткоин': 'BTC',
    'эфириум': 'ETH',
}