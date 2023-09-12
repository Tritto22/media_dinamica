import re

class Studente:
    def __init__(self, nome, cognome, eta):
        self.nome=nome
        self.cognome=cognome
        self.eta=eta
        self.voti=[]

    def nuovo_voto(self, voto):
        r=re.compile(r'^(10|[0-9])$')
        validazioneVoto=r.match(str(voto))
        if validazioneVoto:
            self.voti.append(voto)
            voti_format = ' // '.join(map(str, self.voti))
            print(f'I voti dello studente {self.cognome} {self.nome} sono: \n \t {voti_format}')
        else:
            print('Il voto inserito deve essere un numero intero compreso tra 0 e 10')

    def media_voti(self):
        if self.voti==[]:
            self.media=-1
            #print(media)
        else:
            self.media=round(sum(self.voti)/len(self.voti),1)
            #print(f'La media di {self.cognome} è {self.media}')

    def valuta_promozione(self):
        if not hasattr(self, 'media'):      #controllo che esista self.media come attributo
            self.media_voti()
        if self.media>=6:        
            print(f'La media di {self.cognome} è {self.media}. Sei stato promosso')
        elif self.media==-1:
            print(f'La media di {self.cognome} non si può calcolare poichè non ha voti.\nImpossibile stabilire una esito')
        else:
            print(f'La media di {self.cognome} è {self.media}. Sei stato bocciato')

    #se vuoi usare property fai
    def media_voti(self):
        if self.voti==[]:
            return -1
        return round(sum(self.voti)/len(self.voti),1)
    
    def valuta_promozione(self):
        if not hasattr(self, 'media'):      #controllo che esista self.media come attributo
            self.media_voti()
        return self.media>=6                #restituisce True o False
    
    # dichiaro i 2 metodi come property per poterli usare come attributi
    promosso=property(valuta_promozione)
    media=property(media_voti)