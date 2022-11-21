import telegram.ext
import pandas_datareader.data as web
f = open("token.txt", "r")
tkn = f.read()
f.close()

borsalar={"XU100.IS":"BIST100", "^GSPC":"S&P 500", "^DJI":"Dow 30", "^IXIC":"Nasdaq", "^N225":"Nikkei 225", "^GDAXI":"DAX PERFORMANCE-INDEX", "IMOEX.ME":"MOEX Russia Index", "^BVSP":"IBOVESPA"}
fx={"TRY=X":"USD/TRY", "EURTRY=X":"EUR/TRY", "GBPTRY=X":"GBP/TRY", "TRYJPY=X":"TRY/JPY","EURUSD=X":"EUR/USD", "GBPUSD=X":"GBP/USD", "JPY=X":"USD/JPY"}
def start(update, context):
    update.message.reply_text("""
    Hoşgeldiniz, takip eden komutlar ile devam edebilirsiniz;
    
    /start -> Bu mesajı tekrar çağırır.
    /info -> Botunun kullanımını anlatan dökümasyondur. İlk defa kullananacaksanız okumanız önemle tavsiye edilir.
    /indx -> Piyasa endeksleri.
    /stock -> Seçeceğiniz hisse senedinin fiyatını iletir.
    /fs -> Seçtiğiniz hisse senetlerinin açıklanan son iki finansal tablolarını getirir.
    /news -> Güncel haberleri iletir.
    /fx -> Döviz kurlarını getirir.
    /analys -> Hisse analizlerini hesaplar.
    
    """)
def info(update, context):
    update.message.reply_text("""
    Ulak bota hoşgeldiniz. Bu botu kullanarak hisse senetlerinin fiyatları ve değerleme endekslerine erişim sağlayabilirsiniz.
    
    /stock komutu ardına güncel fiyatını öğrenmek istediğiniz hisse senetlerinin sembollerini (BIST hisseleri için sonuna '.IS' koyarak yazmalısınız.) yazarak öğrenebilirsiniz.
    /analys komutu size mevcut değerlendirme endekslerini gösterir. Analiz komutlarının ardına hisse senedi sembollerini yazarak analiz sonuçlarına ulaşabilirsiniz.
    
    Yatırım Tavsiyesi Değildir. -RedKit
     
    """)

def analys(update, context):
    update.message.reply_text("""
    /capm -> Sermaye Varlıkları Fiyatlama Modeli (Hisse senedinin yüksek ya da az değer biçildiğini ölçmek amacıyla oluşturulan benchmark modelidir.)
    /pddd -> Piyasa Değeri/Defter Değeri Rasyosu
    /fk -> Fiyat/Kar Rasyosu
    
    
    """)
def fs(update, context):
    update.message.reply_text("""
    Menü yapım aşamasındadır.
    """)
def fx(update, context):
    ticker = list(fx.keys())
    data = {}
    message = ""
    for t in ticker:
        prices = web.DataReader(t, "yahoo")
        data[t] = prices
        message += f"{fx[t]}: {prices.iloc[-1]['Close']:.4f}\n"
    update.message.reply_text(message)
def indx(update, context):
    ticker = ["XU100.IS", "^GSPC", "^DJI", "^IXIC", "^N225", "^GDAXI", "IMOEX.ME", "^BVSP"]
    data={}
    message=""
    for t in ticker:
        prices = web.DataReader(t, "yahoo")
        data[t] = prices
        message += f"{borsalar[t]}: {prices.iloc[-1]['Close']:.2f}\n"
    #price = data.iloc[-1]['Close']
    update.message.reply_text(message)
def news(update, context):
    update.message.reply_text("""
    Menü yapım aşamasındadır.
    """)
def stock(update, context):
    ticker = context.args[0]
    data = web.DataReader(ticker, "yahoo")
    price = data.iloc[-1]['Close']
    update.message.reply_text(f"{ticker} için son fiyat; {price:.2f}")


updater = telegram.ext.Updater(tkn, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("news", news))
disp.add_handler(telegram.ext.CommandHandler("fx", fx))
disp.add_handler(telegram.ext.CommandHandler("info", info))
disp.add_handler(telegram.ext.CommandHandler("stock", stock))
disp.add_handler(telegram.ext.CommandHandler("fs", fs))
disp.add_handler(telegram.ext.CommandHandler("analys", analys))
disp.add_handler(telegram.ext.CommandHandler("indx", indx))
updater.start_polling()
updater.idle()
