## Bot di Supporto per "Il Tempo della Spada"

Gli script contenuti in questa cartella implementano quattro funzionalità utili per il GdR "Il Tempo della Spada":
 - Lancio dei dadi, con risoluzione dei successi (da bot Discord)
 - Generazione di nomi medioevali (da bot Discord o direttamente da `namegen.py`)
 - Generazione di personaggi casuali (da bot Discord o usando i due script `itdschargen.py` e `pdffields.py`)
 - Generazione guidata di personaggi (da bot Discord o usando i due script `itdschargen.py` e `pdffields.py`)

### Installazione
L'installazione non è, purtroppo, del tutto elementare.
In un ambiente Linux con Python 3.10, dovrebbe essere sufficiente eseguire lo script `install.sh`.
Con un po' di fortuna, le stesse cose potrebbero funzionare anche su altri sistemi operativi compatibili con lo standard POSIX.

### Esecuzione

#### Bot Discord
 - Il bot Discord è (al momento) pensato per essere eseguito localmente (i.e., sul proprio PC), dato che non gestisce la creazione di PG/PNG da parte di più persone contemporaneamente.
 - Per il bot Discord, bisogna quindi procurarsi un token dal Discord Developer Portal e inserirlo in `config.py`
 - Dopodiché, è sufficiente eseguire il comando `./rundiscord.py`
 - Il bot dispone di un suo help, ottenibile con `!h`

#### Script singoli
 - Una volta completata l'installazione, è anche possibile eseguire i singoli script.
 - Attivare preliminarmente l'ambiente virtuale con `. ./venv/bin/activate`
 - `namegen.py` dispone di un help abbastanza completo, ottenibile con `./namegen.py --help`
 - La generazione di personaggi casuali si ottiene con `./itdschargen.py r`. Lo script produce un file testuale nella cartella `json` con nome uguale al nome del personaggio, più l'estensione `.json`. Questo può essere convertito in PDF con `./pdffields.py json/{nome del personaggio}.json`
 - Per la creazione guidata, la procedura è identica, ma va omesso il parametro `r` nell'invocazione di `./itdschargen`
 
### Note
 - La generazione di PDF si basa su pypdf, che ha qualche problema -- ho prodotto una patch che viene installata automaticamente nell'ambiente virtuale
 
### TODO
Idee per estensioni, divise per argomento.

#### Funzionalità
 - Mantenere per ciascun giocatore un personaggio con i punteggi del quale fare tiri senza dover specificare i punteggi
 - Gestire l'equipaggiamento con la qualità dello stesso
 - Gestire l'avanzamento (e talenti e ordini)

#### Supporto bot/hosting/etc.
 - Supportare la creazione contemporanea da più giocatori/magistri
 - Supportare un modo di selezionare le opzioni più adatto ad un bot (virtual keyboard?)
 - Generare la scheda in un formato diverso se `pypdf` non funziona 
 - Sanitizzare l'input dal bot (in ottica di hostare il bot da qualche parte)

