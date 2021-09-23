import telebot
import datetime
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

CHAVE = os.getenv("API_KEY")

bot = telebot.TeleBot(CHAVE)


@bot.message_handler(commands=["DiasParaGloria"])
def DiasParaGloria(mensagem):
    ano = 2021
    mes = 12
    dia = 21

    maindata = datetime.date(ano, mes, dia)

    todayDate = datetime.date.today()

    if maindata > todayDate:
        delta = maindata - todayDate
    elif maindata <= todayDate:
        delta = todayDate - maindata

    textoFinal = "Faltam %d dias para o fim do período. Fé!" % (
        int(delta.days))
    bot.reply_to(
        mensagem, textoFinal)


@bot.message_handler(commands=["DefinicaoStudentBot"])
def DefinicaoStudentBot(mensagem):
    bot.send_message(
        mensagem.chat.id, "O Student Bot é um bot para Telegram criado com o objetivo principal de dizer quantos dias faltam para o fim do período 2021.1 da UFPE.")


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
        Para continuar, escolha uma opção clicando em um dos itens abaixo (responder qualquer outra coisa não vai funcionar, clique em um dos itens):
          01- /DiasParaGloria : Saber quantos dias faltam para o final do período.
          02- /DefinicaoStudentBot : Saber o que é o Student Bot e para que ele foi criado.
            """
    bot.reply_to(mensagem, texto)


bot.polling()
