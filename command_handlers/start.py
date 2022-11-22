from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes) -> None:
    """Sends a message when '/start' is issued."""
    await update.message.reply_text("""
        Hoşgeldiniz, takip eden komutlar ile devam edebilirsiniz;
        
        /start   -> Bu mesajı tekrar çağırır.
        /info    -> Botunun kullanımını anlatan dökümasyondur. İlk defa kullananacaksanız okumanız önemle tavsiye edilir.
        /fx      -> Döviz kurlarını getirir.
        /markets -> Piyasa endeksleri.
        /stock   -> Seçeceğiniz hisse senedinin fiyatını iletir.
        /fs      -> Seçtiğiniz hisse senetlerinin açıklanan son iki finansal tablolarını getirir.
        /analyze -> Hisse analizlerini hesaplar.
        /crypto  -> Kripto para marketinin hacimi en yüksek 10 kripto para birimine ait güncel fiyatları getirir.
        /news    -> Güncel haberleri iletir.
        
    """)