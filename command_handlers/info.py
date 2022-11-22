from telegram import Update
from telegram.ext import ContextTypes

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message when '/info' is issued."""
    await update.message.reply_text("""
        Ulak bota hoşgeldiniz. Bu botu kullanarak hisse senetlerinin fiyatları ve değerleme endekslerine erişim sağlayabilirsiniz.

        /stock komutu ardına güncel fiyatını öğrenmek istediğiniz hisse senetlerinin sembollerini (BIST hisseleri için sonuna '.IS' koyarak yazmalısınız.) yazarak öğrenebilirsiniz.
        /analys komutu size mevcut değerlendirme endekslerini gösterir. Analiz komutlarının ardına hisse senedi sembollerini yazarak analiz sonuçlarına ulaşabilirsiniz.

        Yatırım Tavsiyesi Değildir. -RedKit
        
    """)