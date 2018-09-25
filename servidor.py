import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
from firebase_admin import db

credencial = credentials.Certificate({
  "type": "service_account",
  "project_id": "notificacoes-felipe",
  "private_key_id": "9144b9f3662b5e838bafdb8c464ad483bdc6b261",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDtOay2LJBEXRon\nNOqhQ4Df7YJEy6bvxZm+oH2DaTqIbH7HGjfN1gCpx57jbr1nDBDT24Koh7bHFU3Z\nGnxjv26hl8S4qti1ZF5E93NM8F7ciidwBn35M7JvLoBr8eVU6GLD5E6BxEnshCfU\nXTbYHAUyZqElQC/4/wMG9SgaJ2cxy7bYP4iwJb6O61GQHOYMfV9xnolThRR9UDRQ\n0nZsZn2pn2o6faFS1aY11pZ9m0xhjN3F/UkT6SaofjNICebVbdwVxqsRC9m90J44\n5/LAIQDDix6tqBD9AWOWfCW/g6l11zYE8Ev/gIi804WEEIFRcssa+z+OogLcnMee\nivKwUTBlAgMBAAECggEAE+BzgX8p5mSDqrnTGAiLLZgdxGxo9CmzKGcTpTVlt2UZ\n2U5v0xIlk5Q7krRmb9IxvcKkh8D5VmSJVZHTztrNJwKLs+pyxn4erPor4cw5MpLr\n24Xbu8vyXUEA9yp5S/w9vEqurk5XYFcxbCiUThbI87BoO7INYvhhFU3o2oonKiON\nhiFaJOoCaR7X7MixjxTiqDcxSchG23F8YL6O+dR+xL97ltBOzJJK0MCQtVdQ0GS9\nZ02clp5GWaxgYq486rJQiUoW5wVLkVa/RVl86WcOed92yKFNS/VnX6wsrb8BCeSm\nhbSL1meUMqrszU7y5oyM/O3T8ATs+U9vWLsOdVnEMQKBgQD2yHxW874pJEIA1tkI\nlqmJjzerWhpYNyHj6GDYsgcNizkH9NRPjUmmouuVgqv5msVKuRzCQdB6nexLnWMK\nmxXc8Rnd+YXpDtFQTJhqiWt+c0l1sk49B5PO3OLJ3rxxjRQLDJzs/Vawha0KYRZ8\nbvihyyuP6tHT0UdNI0te/Sc09QKBgQD2Fc40/6J19DlbLxE+VayYDOcSJI90G722\ndZH4th6/pvLhNBouJfO1fkVjs54L5KwCJJIeFDiVqpHPGGxw+4ZQZXtpDX2jQ/Si\nkXLYjlr6uT8loG1OhW09N2ZdLOlCwMn0d304zlOKgyhqyRsKEjrHv97AHYsd+23g\nYlulEetnsQKBgQDRTAuYOzSF9Ag+afi7vfuffOV73/kD5A5MGmM4pRQyOmduBgii\nR3O1betba+2qzcaRrxli7yp/M7yaDKtY7VrHfXuwtNULadO/xJZnlJCkN+aPeV+9\nhtWm1dNJ3iv4KexbyqC0pc+F+nldmiXV9s/LeGJDtqWqfY15MHvV3eIImQKBgQDV\n67C9O7hzx2GQ1cKsqHeIGjdI+0VFTtRFZ8EELvVd73hVsyBLG6zXCjSx7jOm7Rtm\nJXpr8XIbERL9r6KdONnSy9VTRmoAYpOoOr5WaLHIIP8261X6G10SCTXQK7l+0O7+\nuFy/5ASVdVzOL5J019IHUNEHuubzol0q4PX/8irskQKBgQCgYbuOe2jVd/o7T8rw\nN9vAT9E/uBKVD4eb8x/63EpMAWJFZID6UWe2aLF3PTeYSn5uzRvp049PnnQoNVQY\nkHIe/L1t3zOP9eb2V8xy5UH0ni6/tS/oXQw/CXXfXL7fgFRTvxvIDWTY2LFs6OQv\nOCMPej2GEsy0Jc1E+Isu+zISEw==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-59u1h@notificacoes-felipe.iam.gserviceaccount.com",
  "client_id": "101274586052327269153",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-59u1h%40notificacoes-felipe.iam.gserviceaccount.com"
})

URL_DB = "https://notificacoes-felipe.firebaseio.com/"

app = firebase_admin.initialize_app(credencial, {'databaseURL': URL_DB })

'''
ref = db.reference('tokens')

tokens = ref.get()

for i,t in tokens.items():

    token = t['token']

    mensagem = messaging.Message(
        data={
            'title': 'Viva !!!',
            'body':'Finalmente funcionou :) '
        },
        token=token,
    )

    resposta = messaging.send(mensagem)
    print('Mensagem enviada com sucesso:', resposta)
'''

token = "dgq6eSU9m6M:APA91bGheaft5apH_I3mebqiHbAdSSqWBIkWWPPx4_9IWo54az4Hsfsl55mCawsHhsJ8d0MuWIdMeQGsDbcVIMSHIoNOAzwVuL9ThjumyMVp6Wa1OKQtA9dR6srTlTG6AfNJS8oh0Oaz"

mensagem = messaging.Message(
    data={
            'title': 'Nova Mensagem !!!',
            'body':'Conteudo'
    },
    token=token,
)

resposta = messaging.send(mensagem)
print('Mensagem enviada com sucesso:', resposta)
    
