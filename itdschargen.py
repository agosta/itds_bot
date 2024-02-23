#!/usr/bin/env python3.10

__author__ = 'Giampaolo Agosta'
__version__= '1.0'
__doc__ = """Generazione guidata o casuale di personaggi de Il Tempo della Spada e compilazione delle schede PDF"""

from typing import List
from dataclasses_json import dataclass_json
from dataclasses import dataclass, field
from enum import Enum
from random import choice, randint
from strenum import StrEnum
from string import capwords

global random_gen

def d6(n):
  return [ randint(1,6) for i in range(n) ]

def v_antica(self) : 
  self.caratteristiche['audacia'].modificatore+=1

def v_cortese(self) : 
  self.abilità[sinput('abilità', ['arti liberali', 'autorità', 'empatia' ])].dado_extra+=1

def v_erudita(self):
  self.altro+='1 successo bonus per meditazione, studio e lavoro\n'

def v_guerresca(self):
  self.ferite[1]+=1
  self.ferite[2]+=1
  self.fatica[0]+=1
  self.fatica[1]+=1

def v_intraprendente(self): 
  self.retaggio+=1

def v_laboriosa(self):
  self.denaro*=2
  
def v_meticcio(self):
  self.lingue.append(cinput('lingua', Lingue))
  self.abilità[sinput('abilità', ['storia e leggende', 'usi e costumi' ])].dado_extra+=1

def v_militare(self):
  self.altro+="armi e armature di qualità\n"  #TODO fix after equipment is added

def v_rurale(self):
  self.abilità['sopravvivenza'].dado_extra+=1
  self.abilità['usi e costumi' ].dado_extra+=1

def v_spirituale(self):
  self.spirito+=4

def v_tenace(self):
  self.abilità['forza' ].dado_extra+=1

def v_urbana(self):
  self.altro+="1 successo bonus per creare Contatti\n"
  self.altro+="Le abilità dei ceti superiori sono considerate di 1 livello inferiori"

def e_marziale(self):
  self.abilità[sinput('abilità', ['archi', 'balestre', 'armi corte', 'armi comuni', 'armi da guerra', 'lotta' ])].dado_extra+=1

def e_animale(self):
  self.altro+="1 successo bonus per interazioni con animali\n"

def e_antico(self):
  abils = ['alchimia', 'arti arcane', 'guarigione', 'storia e leggende', 'teologia' ]
  a1 = sinput('abilità', abils)
  self.abilità[a1].dado_extra+=1
  abils.remove(a1)
  self.abilità[sinput('abilità', abils)].dado_extra+=1

def e_apprendistato(self):
  scelte = list(self.artigiano.keys())+list(self.professione.keys())
  if not len(scelte): raise ITDSException("Apprendistato richiede di conoscere almeno una abilità artigiano o professione")
  if len(scelte)==1:
    if scelte[0] in self.artigiano : self.artigiano[scelte[0]].dado_extra+=2
    else : self.professione[scelte[0]].dado_extra+=2
  else :
    for i in range(2):
      scelta = sinput("professione o artigiano", scelte)
      if scelta in self.artigiano : self.artigiano[scelta].dado_extra+=1
      else : self.professione[scelta].dado_extra+=1

def e_cimelio(self):
  self.altro+="1 oggetto di ottima qualità\n"

def e_conoscenze(self):
  self.altro+="1 successo bonus per creare Contatti\n"

def e_dedizione(self):
  abils = ['arte della guerra', 'atletica', 'cavalcare', 'empatia', 'furtività', 'manualità', 'mercatura', 'sopravvivenza', 'usi e costumi' ]
  a1 = sinput('abilità', abils)
  self.abilità[a1].dado_extra+=1
  abils.remove(a1)
  self.abilità[sinput('abilità', abils)].dado_extra+=1

def e_esperienza(self):
  self.altro+="Incrementa una abilità a 3 e due a 2 oltre il normale addrestramento\n"

def e_fascino(self):
  abils = ['arti liberali', 'autorità', 'intrattenere', 'raggirare' ]
  a1 = sinput('abilità', abils)
  self.abilità[a1].dado_extra+=1
  abils.remove(a1)
  self.abilità[sinput('abilità', abils)].dado_extra+=1

def e_indomito(self):
  self.ferite[2]+=1
  self.ferite[3]+=1
  self.ferite[4]+=1
  self.fatica[1]+=1
  self.fatica[2]+=1

def e_istinto(self):
  self.riflessi+=1

def e_legame(self):
  self.altro+="Quando collabora con uno specifico PG, ottengono anche i dadi extra\n"

def e_nomea(self):
  self.fama+=1
  self.denaro*=2

def e_percorso(self):
  self.spirito+=3
  v=None
  while not v:
    v=sinput('valore', ['honor', 'ego', 'fides', 'impietas', 'superstitio', 'ratio'])
    if self.valori[v]>0 : v=None
  self.valori[v]=1

def e_talento(self):
  self.abilità[sinput('abilità base', ['volontà', 'carisma', 'forza', 'agilità', 'ragionamento', 'percezione' ])].dado_extra+=1


data = {

'lingue' : [ 'Arabo', 'Castigliano', 'Catalano', 'Cimrico', 'Ebraico', 'Francese', 'Frisone', 'Gaelico', 'Gallego', 'Greco', 'Inglese', 'Ladino', 'Latino', 'Portoghese', 'Provenzale', 'Scandinavo', 'Slavo', 'Tedesco', 'Turco', 'Italiano', 'Greco antico', 'Aramaico', 'Ungherese', 'Basco' ],

'valori' : {
 'fede' : [ 'fides', 'impietas'],
 'onore': [ 'honor', 'ego' ],
 'superstizione': [ 'superstitio', 'ratio'],
},

'caratteristiche' : {
  'audacia': {
   'base': 'volontà',
   'abilità': ['arte della guerra', 'autorità', 'cavalcare', 'teologia', 'volontà'],
  },
  'celeritas':{
   'base': 'agilità',
   'abilità': ['agilità', 'archi', 'armi corte', 'furtività', 'manualità'],
  },
  'fortitudo':{
   'base': 'forza',
   'abilità': ['armi comuni', 'armi da guerra', 'atletica', 'forza', 'lotta'],
  },
  'gratia':{
   'base': 'carisma',
   'abilità': ['carisma', 'intrattenere', 'mercatura', 'raggirare', 'usi e costumi'],
  },
  'mens': {
   'base': 'ragionamento',
   'abilità': ['alchimia', 'arti arcane', 'arti liberali', 'ragionamento', 'storia e leggende'],
  },
  'prudentia': {
   'base': 'percezione',
   'abilità': ['balestre', 'empatia', 'guarigione', 'percezione', 'sopravvivenza', ],
  },
},

'abilità speciali' : {
  'artigiano' : {
    'fortitudo' : ['conciatore', 'fabbro', 'falegname'],
    'mens': ['copista', 'meccanico'],
    'prudentia' : ['arcaio', 'gioielliere', 'pittore', 'sarto'],   
  },
  'professione' : {
    'fortitudo' : ['muratore', 'boscaiolo', 'minatore', 'contadino', 'marinaio', 'pastore'],
    'mens': ['medico', 'avvocato', 'notaio', 'amministratore', 'precettore', 'funzionario', 'banditore', 'carovaniere', 'piloto'],
    'gratia' : ['oste', 'locandiere', 'messaggero', 'cortigiano'],
  }
},

'focus' : {
 'alchimia' : [ 'regno animale', 'regno vegetale', 'regno minerale', 'identificare sostanze', 'acidi', 'antidoti', 'balsami', 'fuoco greco', 'inchiostro simpatico', 'infusi', 'tonici', 'veleni' ], 
 'archi' : ['arco corto', 'arco lungo', 'colpo mirato', 'tiro a parabola' ],
 'armi comuni' : [ 'martello', 'randello', 'bordone', 'falce da guerra', 'lancia da fante', 'roncone', 'scure', 'spiedo' ],
 'armi corte' : [ 'coltello', 'accetta', 'bastoncello', 'coltellaccio' ],
 'armi da guerra' : ['lancia da cavaliere', 'ascia normanna', 'spada da guerra', "spada d'arme", 'brocchiere', 'scudo', 'scudo grande', 'picca', 'pugnale', 'mazza ferrata', 'mannaia inastata' ],
 'arte della guerra' : [ 'assedi', 'sortite', 'guerriglia', 'campagna', 'bosco', 'collina' ],
 'arti arcane' : [ 'affabulare', 'magia ermetica', 'magia popolare', 'magia salomonica', 'demonologia' ],
 'arti liberali' : ['trivio', 'quadrivio', 'letteratura di un regno' ],
 'atletica' : ['correre', 'saltare', 'lanciare', 'scalare', 'nuotare' ],
 'autorità' : ['interrogare', 'intimidazione', 'soldati', 'criminali', 'contadini', 'contesto specifico' ],
 'balestre' : ['balestra leggera', 'balestra a staffa', 'balestra a verricello', 'colpo mirato'],
 'cavalcare' : [ 'cavallo da sella', 'mulo', 'cavallo da guerra', 'dromedario', 'attutire cadute', 'salto di ostacoli', 'giostra', 'combattere a cavallo'],
 'empatia' : ['una cultura', 'una professione', 'umili', 'nobili', 'popolani', 'borghesi', 'interrogare', 'smascherare menzogne', 'calmare animali', 'addestrare animali', 'uni tipo di animale' ],
 'furtività' : ['ambiente urbano', 'boschi', 'caverne', 'muoversi silenziosamente', 'nascondersi', 'pedinare' ],
 'guarigione' : ['curare ferite', 'stabilizzare', 'erboristeria' ],
 'intrattenere' : ["gioco d'azzardo", 'corti nobiliari', 'villaggi', 'mimo', 'buffoneria', 'satira', 'commedia', 'tragedia'],
 'lotta' : ['percussioni', 'prese', 'leve', 'sbilanciamenti'],
 'manualità': ['prestigiatore', 'borseggiatore', 'scassinatore', 'disporre trappole', 'disarmare trappole'],
 'mercatura' : ['armi', 'armature', 'vini', 'gioielli', 'tessuti', 'contabilità', 'rotte commerciali', 'valutare', 'mercanteggiare', 'un tipo di mercanzia'],
 'raggirare' : ['una cultura', 'una professione', 'camuffarsi', 'confondere', 'truffare', 'interrogare', 'sedurre', 'barare' ],
 'ragionamento' : ['indagare', 'memoria', 'calcolo', 'matematica'],
 'sopravvivenza' : ['boschi', 'paludi', 'montagne', 'pianure', 'colline', 'mare', 'deserto', 'orientamento', 'caccia', 'trovare acqua', 'trovare cibo', 'trovare erbe officinali', 'prevedere il tempo atmosferico', 'seguire tracce', 'nascondere tracce' ],
 'storia e leggende' : ['antica Roma', 'un periodo storico', 'un regno', 'creature fantastiche', 'leggende e misteri'],
 'teologia' : ['tradizioni religiose', 'simbologia', 'gerarchia ecclesiastica', 'vite dei santi', 'riti', 'festività religiose', 'eresie', 'abate', 'canonico', 'inquisitore'],
 'usi e costumi': ['un regno', 'umili', 'popolani', 'borghesi', 'nobili', 'un ordine', 'vie commerciali', 'rotte marittime'],
 'arcaio' : [ 'arco corto', 'arco lungo', 'balestra leggera', 'balestra a staffa', 'balestra a verricello', 'frecce', 'quadrelli'],
 'conciatore' : ['conciare pelli', 'conciare pellicce', 'armature di cuoio'],
 'copista' : ['falsificare', 'miniatore', 'scrivano', 'copiare documenti'],
 'fabbro': ['cotta di maglia', 'armature di piastre', 'chiodi', 'asce', 'spade', 'coltelli', 'punte di lancia' ],
 'falegname' : ['manici', 'mobili', 'carri', 'ponteggi', 'oggetti decorativi', 'strumenti musicali', 'bastoni'],
 'gioielliere' : ['oro', 'argento', 'pietre preziose', 'anelli', 'collane'],
 'meccanico' : ['cardini', 'chiavi', 'serrature', 'argani', "macchine d'assedio"],
 'pittore' : ['pittura su legno', 'disegno su carta', 'arazzi', 'affreschi'],
 'sarto' : ['tessere', 'ricamare', 'cucire abiti'],
 'muratore'  : ['un tipo di costruzione'],
 'boscaiolo' : ['un tipo di albero'],
 'minatore'  : ['un minerale'],
 'marinaio'  : ['un tipo di nave'],
 'pastore'   : ['pecoraio', 'bovaro', 'porcaro', 'capraio'],
 'medico'    : ['diagnosi', 'cura delle malattie'],
 'notaio'    : ['un regno o comune'],
 'avvocato'  : ['un regno o comune'],
 'amministratore' : ['un tipo di bene amministrato'],
 'precettore' : ['grammatica', 'retorica', 'dialettica', 'matematica', 'astronomia', 'lingue antiche', 'lingue moderne', 'letteratura'],
 'funzionario': ['un ruolo a corte'],
 'banditore'  : ['un tipo di notizia o avviso'],
 'carovaniere': ['guidare carri', 'caricare soma', 'rotte carovaniere'],
 'piloto'     : ['tracciare rotte', 'pilotare un tipo di nave'],
 'oste'       : ['cucina', 'mescita'],
 'locandiere' : ['locande popolari', 'locande borghesi', 'locande di lusso'],
 'messaggero' : ['un tipo di corte o destinatario'],
 'cortigiano' : ['un tipo di corte', 'un regno o comune'],
},

'culture' : {
  'antica' : {
    'dado extra' : ['carisma', 'volontà'],
    'valori': ['fides', 'superstitio'],
    'vantaggio': v_antica,
  },
  'cortese' : {
    'dado extra' : ['carisma', 'ragionamento'],
    'valori': ['fides', 'honor'],
    'vantaggio': v_cortese,
  },
  'erudita' : {
    'dado extra' : ['percezione', 'ragionamento'],
    'valori': ['ego', 'ratio'],
    'vantaggio': v_erudita,
  },
  'guerresca' : {
    'dado extra' : ['agilità', 'forza'],
    'valori': ['impietas', 'honor'],
    'vantaggio': v_guerresca,
  },
  'intraprendente' : {
    'dado extra' : ['percezione', 'volontà'],
    'valori': ['ego', 'ratio'],
    'vantaggio': v_intraprendente,
  },
  'laboriosa' : {
    'dado extra' : ['percezione', 'ragionamento'],
    'valori': ['honor', 'ratio'],
    'vantaggio': v_laboriosa,
  },
  'meticcio' : {
    'dado extra' : ['agilità', 'forza', 'carisma', 'percezione', 'ragionamento', 'volontà'],
    'valori': ['honor', 'ratio', 'fides', 'impietas', 'superstitio', 'ego'],
    'vantaggio': v_meticcio,
  },
  'militare' : {
    'dado extra' : ['agilità', 'volontà'],
    'valori': ['impietas', 'honor'],
    'vantaggio': v_militare,
  },
  'rurale' : {
    'dado extra' : ['percezione', 'forza'],
    'valori': ['fides', 'superstitio'],
    'vantaggio': v_rurale,
  },
  'spirituale' : {
    'dado extra' : ['carisma', 'volontà'],
    'valori': ['fides', 'superstitio'],
    'vantaggio': v_spirituale,
  },
  'tenace' : {
    'dado extra' : ['percezione', 'volontà'],
    'valori': ['honor', 'superstitio'],
    'vantaggio': v_tenace,
  },
  'urbana' : {
    'dado extra' : ['carisma', 'ragionamento'],
    'valori': ['ego', 'ratio'],
    'vantaggio': v_urbana,
  },
},
'ceto' : {
  'umili' : {
    'retaggio': 0,
    'denaro iniziale' : ['4d6', 'soldi'],
    'rendita': ['0', 'soldi'],
    'costo della vita': ['1', 'soldi'],
    'mestiere' : ['armi corte', 'empatia', 'furtività', 'guarigione', 'professione/fortitudo', 'raggirare', 'sopravvivenza'],
  },
  'popolani' : {
    'retaggio': 1,
    'denaro iniziale' : ['2d6*20', 'soldi'],
    'rendita': ['0', 'soldi'],
    'costo della vita': ['1d6', 'soldi'],
    'mestiere' : ['archi', 'armi comuni', 'artigiano', 'atletica', 'lotta', 'manualità', 'usi e costumi'],
  },
  'borghesi' : {
    'retaggio': 2,
    'denaro iniziale' : ['2d6*100', 'soldi'],
    'rendita': ['4d6', 'soldi'],
    'costo della vita': ['2d6+12', 'soldi'],
    'mestiere' : ['alchimia', 'arti liberali', 'balestre', 'intrattenere', 'mercatura', 'professione/gratia', 'storia e leggende'],
  },
  'nobili' : {
    'retaggio': 3,
    'denaro iniziale' : ['4d6*200', 'soldi'],
    'rendita': ['2d6*20', 'soldi'],
    'costo della vita': ['(1d6+6)*20', 'soldi'],
    'mestiere' : ['armi da guerra', 'arte della guerra', 'arti arcane', 'autorità', 'cavalcare', 'professione/mens', 'teologia'],
  },
},

'ferite' : { 
  'graffi': 0,
  'leggere': 0,
  'gravi': -1,
  'critiche': -2,
  'mortali': -3 
  },
'fatica' : { 'fresco': 0, 'stanco':-1, 'sfinito':-2 },

'tentazioni' : ['nessuna', 'accidia', 'avidità', 'gola', 'invidia', 'ira', 'lussuria', 'superbia' ],

'eventi' : {
 'addrestramento marziale': e_marziale,
 'affinità animale': e_animale,
 'antico sapere': e_antico,
 'apprendistato': e_apprendistato,
 'cimelio': e_cimelio,
 'conoscenze': e_conoscenze,
 'dedizione': e_dedizione,
 'esperienza': e_esperienza,
 'fascino' : e_fascino,
 'indomito' : e_indomito,
 'istinto' : e_istinto,
 'legame' : e_legame,
 'nomea' : e_nomea,
 'percorso spirituale': e_percorso,
 'talento naturale' : e_talento,
},

}

from equip import equip, Arma, Armatura, Oggetto
data['armi'] = equip.armi
data['armature'] = equip.armature
data['oggetti'] = equip.oggetti

lingue_to_ita = {
'Italian' : 'Italiano',
'French'  : 'Francese',
'Occitan' : 'Provenzale',
'Catalan' : 'Catalano',
'Welsh'   : 'Cimrico',
'English' : 'Inglese',
'German'  : 'Tedesco',
'Gaelic'  : 'Gaelico',
'Arabic'  : 'Arabo',
'Slavonic': 'Slavo',
'Greek'   : 'Greco',
'Spanish' : 'Castigliano',
'Portuguese':'Portoghese',
'Norse'   : 'Scandinavo',
'Hungarian':'Ungherese',
'Basque'  : 'Basco',
} 


# Carica i dati esterni dai file YAML corrispondenti
import yaml
with open("data/professioni.yaml","r") as fin:
  professioni = yaml.load(fin.read(), yaml.Loader)
with open("data/tratti.yaml","r") as fin:
  tratti = yaml.load(fin.read(), yaml.Loader)
  tratti_per_regione = { i : tratti[i]['tratti'] for i in tratti }
  lingue_per_regione = { i : tratti[i]['lingua'] for i in tratti }


import re

def calcolo_denaro(s):
  def matched(obj):
    n=int(obj.group(0)[:-2])
    return str(sum(d6(n)))
  return eval(re.sub(r'(\d+d6)',matched,s))*12 #in denari!

def mod_base(car):
  if car<7: return -1
  return (car-6)//2

def penalita_ingombro(ingombro, ingombro_base):
  if ingombro<ingombro_base*2 : return 0
  if ingombro<ingombro_base*4 : return -1
  if ingombro<ingombro_base*6 : return -2
  if ingombro<ingombro_base*8 : return -3
  return -4

# OGGETTI
#TODO creazione di oggetti di qualità superiore

qualità_livelli = ['normale', 'buona', 'eccellente', 'ottima', 'straordinaria', 'scadente' ] # scadente = -1

from copy import deepcopy

def qualità_oggetto(o, q):
  if q=='normale': return o
  if q=='buona' : 
    o=deepcopy(o)
    o['qualità']='buona'
    o['costo']=o['costo']*3
    return o

Culture  = StrEnum('Culture', list(data['culture'].keys()))
Ceti     = StrEnum('Ceti', list(data['ceto'].keys()))
Lingue   = StrEnum('Lingue', data['lingue'])
Caratteristiche = StrEnum('Caratteristiche', list(data['caratteristiche'].keys()))
EAbilità = StrEnum('Abilità', sum([ data['caratteristiche'][d]['abilità'] for d in data['caratteristiche']],[]))
Tentazioni = StrEnum('Tentazioni',data['tentazioni'])
Genere   = StrEnum('Genere', ['maschio', 'femmina'])
Mestiere = StrEnum('Mestiere', sum([ data['ceto'][d]['mestiere'] for d in data['ceto']],[]))
AbLibere = StrEnum('AbLibere', list(set(sum([ data['caratteristiche'][d]['abilità'] for d in data['caratteristiche']],[])).union(set(sum([ data['ceto'][d]['mestiere'] for d in data['ceto']],[])))))

@dataclass_json
@dataclass
class Abilità:
  nome       : str = ''
  grado      : int = 0
  mestiere   : bool = False
  dado_extra : int = 0
  successo_bonus : int = 0
  focus      : list[str] = field(default_factory=list)

@dataclass_json
@dataclass
class Caratteristica:
  nome         : str = ''
  caratteristica : int = 5
  modificatore : int = -1
  abilità      : list[str] = field(default_factory=list)

@dataclass_json
@dataclass
class AbilitàSpeciale:
  nome       : str = ''
  caratteristica : Caratteristiche = list(Caratteristiche)[0]
  grado      : int = 0
  mestiere   : bool = False
  dado_extra : int = 0
  successo_bonus : int = 0
  focus      : list[str] = field(default_factory=list)


@dataclass_json
@dataclass
class Personaggio:
  nome       : str = ''
  luogo_nascita : str = ''
  anno_nascita  : int = 18
  genere     : Genere = list(Genere)[0] 
  caratteristiche : dict[str,Caratteristica] = field(default_factory=dict)
  cultura    : tuple(Culture) = (list(Culture)[0],list(Culture)[1])
  ceto       : Ceti = list(Ceti)[0]
  mestiere   : str = ''
  valori     : dict[str,int] = field(default_factory=lambda : { 'honor':0, 'ego':0, 'fides':0, 'impietas':0, 'superstitio':0, 'ratio':0 })
  abilità    : dict[str,Abilità] = field(default_factory=dict)
  professione: dict[str,AbilitàSpeciale] = field(default_factory=dict)
  artigiano  : dict[str,AbilitàSpeciale] = field(default_factory=dict)
  riflessi   : int = 0
  ferite     : list[int] = field(default_factory=lambda : [0,0,0,0,0]) # 5 elementi
  ingombro_base : int = 0
  spirito    : int = 0
  fatica     : list[int] = field(default_factory=lambda : [0,0,0]) # 3 elementi
  tentazione : str = ''
  ordine     : str = ''
  lingue     : list[Lingue] = field(default_factory=list)
  pe_spesi   : int = 0
  pe_liberi  : int = 0
  retaggio   : int = 3
  altro      : str = ''
  fama       : int = 0
  denaro     : int = 0 #in denari
  eventi     : list[str] = field(default_factory=list)
  armi       : List[Arma] = field(default_factory=list)
  armatura   : Armatura = field(default_factory=lambda: Armatura(data['armature']['abiti normali']))
  equipaggiamento : List[Oggetto] = field(default_factory=list)

  def mod(self,c):
    return self.caratteristiche[c].modificatore

  def __post_init__(self):
    for c in Caratteristiche :
      if c.name not in self.caratteristiche : 
        self.caratteristiche[c.name]=Caratteristica(c.name,7,0,data['caratteristiche'][c.name]['abilità'])
    for a in EAbilità :
      if a.name not in self.abilità : 
        self.abilità[a.name]=Abilità(a.name)
    
  def riflessi_init(self):
    self.riflessi += self.caratteristiche['prudentia'].caratteristica + self.mod('celeritas')

  def ferite_init(self):
    ferite = self.caratteristiche['fortitudo'].caratteristica + self.mod('fortitudo') + self.abilità['forza'].grado
    for i in range(5):
      self.ferite[i] += ferite//5
    ferite %= 5
    for i in range(ferite):
      self.ferite[i]+=1
  
  def ingombro_base_init(self):
    self.ingombro_base = self.caratteristiche['fortitudo'].caratteristica + self.abilità['forza'].grado
  
  def fatica_init(self):
    fatica = self.caratteristiche['fortitudo'].caratteristica + self.caratteristiche['audacia'].caratteristica
    for i in range(3):
      self.fatica[i] += fatica//3
    fatica %= 3
    for i in range(fatica):
      self.fatica[i]+=1
  
  def spirito_init(self):
    self.spirito += self.caratteristiche['fortitudo'].caratteristica + self.mod('celeritas') + self.abilità['volontà'].grado

  def retaggio_init(self):
    self.retaggio+=self.mod('gratia')

  def abilità_a_livello(self,livello=1):
    r = [ a for a in self.abilità if self.abilità[a].grado==livello ]
    r+= [ a for a in self.artigiano if self.artigiano[a].grado==livello ]
    r+= [ a for a in self.professione if self.professione[a].grado==livello ]
    return r
    
  def incrementa_abilità(self,abilità,livello):
    if abilità in self.abilità : self.abilità[abilità].grado=livello
    elif abilità in self.artigiano : self.artigiano[abilità].grado=livello
    elif abilità in self.professione : self.professione[abilità].grado=livello

# GESTIONE INPUT O GENERAZIONE CASUALE
def sinput(nome, lis):
  global random_gen
  if not len(lis): raise ITDSException(f"{nome} non può essere scelto, perché non ci sono opzioni disponibili")
  if random_gen : return choice(lis)
  r = None
  s = [ f'({lis.index(l)+1}) {l}' for l in lis ]
  while not r:
    r = input(f"Scegliere un(a) {nome} tra: {', '.join(s)}\n>>>\t")
    try : 
      pos = int(r)-1
      if pos>=0 and pos<len(lis) : r=lis[pos]
    except Exception: pass
    if r not in lis : r = None
  return r.lower()

def cinput(nome, ecls):    
  return sinput(nome, [m.name for m in ecls])

def ainput(nome, ecls, pers=None, remaining=1):
  global random_gen
  if random_gen and remaining>1:
     ab = list(professioni[pers.ceto][pers.mestiere]['abilità'])
     sab= list([ p['abilità'] for p in professioni[pers.ceto][pers.mestiere]['abilità_speciali']])
     try :
       l1=[ a for a in ab if (a not in pers.abilità or pers.abilità[a].grado==0) ]
       l2=[ a for a in sab ]
       l=l1 + (l2 if not len(pers.professione) and not len(pers.artigiano) else [])
       if len(l):
         return choice(l)
     except Exception as e:
       print("Tentativo di scegliere una abilità professionale fallito", e)
       pass
  return sinput(nome, [m.name for m in ecls])

def iinput(nome, min_=None, max_=None):
  global random_gen
  if random_gen :
    if not min_ : min_=1
    if not max_ : max_=6
    return randint(min_,max_)
  r = None
  while not r:
    r = input(f"{nome} ({min_ if min_ else 'N/A'}-{max_ if max_ else 'N/A'}):\n>>>\t")
    try : 
      r = int(r)
      if min_ and r<min_ : r=None
      if max_ and r>max_ : r=None
    except Exception : r=None
  return r

def distanza_ceti(ceto1, ceto2):
  c1 = data['ceto'][ceto1]['retaggio']
  c2 = data['ceto'][ceto2]['retaggio']
  return c1-c2

def distanza_abilità(ceto, abilità):
  ceto_ab = None
  for c in data['ceto']:
    if abilità in data['ceto'][c]['mestiere']: 
      return distanza_ceti(c,ceto)
  return 0

def input_abilità_speciale(tipo, pers, mestiere=False):
  global random_gen
  if random_gen : 
    l = [ e for e in professioni[pers.ceto][pers.mestiere]['abilità_speciali'] if e['abilità']==tipo ]
    try : 
      c = choice(l)
      sottotipo=None
      if c['abilità'] == 'artigiano' :
        for d in data['abilità speciali']['artigiano'] :
          if c['specialità'] in data['abilità speciali']['artigiano'][d]: sottotipo=d
      else :
        sottotipo=c['abilità'].split('/')[-1]
      return AbilitàSpeciale(nome=c['specialità'],caratteristica=sottotipo, grado=1, mestiere=mestiere)
    except Exception : pass    
  #print(tipo, mestiere)
  if tipo == 'artigiano':
    sottotipo = sinput('caratteristica di riferimento',['fortitudo','mens','prudentia'])
    nome = sinput('artigiano',data['abilità speciali']['artigiano'][sottotipo])
    return AbilitàSpeciale(nome=nome,caratteristica=sottotipo,grado=1,mestiere=mestiere)
  else :
    sottotipo=tipo.split('/')[-1]
    nome = sinput('professione',data['abilità speciali']['professione'][sottotipo])
    return AbilitàSpeciale(nome=nome,caratteristica=sottotipo,grado=1,mestiere=mestiere)

def input_info_base(genere):
  global random_gen
  if random_gen : 
    from namegen import get_name
    luogo = choice(list(lingue_per_regione.keys()))
    nome = get_name(gender='male' if genere=='maschio' else 'female', language=lingue_per_regione[luogo])
  else :
    nome  = input("Nome del personaggio:\n>>>\t")
    luogo = input("Luogo di nascita:\n>>>\t")
  return nome, luogo

def input_mestiere(pers):
  global random_gen
  if random_gen :
    return choice(list(professioni[pers.ceto].keys()))
  else :
    return input("Mestiere:\n>>>\t")

def input_cultura(pers):
  global random_gen
  if random_gen :
    return tratti_per_regione[pers.luogo_nascita]
  else :
    cultura1 = cinput('tratto culturale', Culture)
    while True: # assicura due tratti diversi
      cultura2 = cinput('tratto culturale', Culture)
      if cultura2!=cultura1 : break
    return cultura1, cultura2

class ITDSException(Exception):
  pass

# CREAZIONE DEL PERSONAGGIO
def creazione(random=False):
  # Definisce se la generazione è casuale oppure no. Serve una variabile globale per tenere traccia di tutti i metodi di input
  global random_gen 
  random_gen =random
  
  genere = cinput('genere',Genere)
  nome, luogo = input_info_base(genere)
  
  anno  = iinput("Anno di nascita:",1000,1400)
  p = Personaggio(nome,luogo,anno,genere)  
  punti_car = 54
  count=5 # contatore delle caratteristiche a cui assegnare punti, esclusa quella presente
  for c in Caratteristiche:
    while True:
      car = iinput(f'{c.name} (punti residui={punti_car}) ',5,13)
      if count*5+car>punti_car : continue # conta se rimangono abbastanza punti per allocare tutte le caratteristiche residue, in caso contrario ripete la richiesta
      count-=1
      punti_car-=car
      p.caratteristiche[c.name].caratteristica=car
      p.caratteristiche[c.name].modificatore=mod_base(car)
      break
  # assegna grado 1 a tutte le abilità di base
  for a in p.abilità:
    for c in Caratteristiche:
      if data['caratteristiche'][c.name]['base']==a : 
        p.abilità[a].grado=1
  # Tratti culturali
  cultura1,cultura2 = input_cultura(p)
  p.cultura=(cultura1,cultura2)
  data['culture'][cultura1]['vantaggio'](p)
  data['culture'][cultura2]['vantaggio'](p)
  s1=sinput("dado extra",data['culture'][cultura1]['dado extra'])
  p.abilità[s1].dado_extra+=1
  s2=sinput("dado extra",data['culture'][cultura2]['dado extra'])
  p.abilità[s2].dado_extra+=1
  # Assegna i valori se il modificatore di audacia è maggiore di 0
  punti_valore = max(0, p.mod('audacia'))
  timeout=0
  if punti_valore>0:
    v1=sinput("valore",data['culture'][cultura1]['valori'])
    v2=sinput("valore",data['culture'][cultura2]['valori'])
    while punti_valore>0 and timeout<10:
      v=sinput(f"valore a cui aggiungere un punto ({punti_valore} punti residui)",[v1,v2])
      if p.valori[v]<3 : 
        p.valori[v]+=1
        punti_valore-=1
      else : 
        timeout+=1
        print(f"{v} ha già raggiunto il valore massimo")
  # Ceto e professione
  p.retaggio_init()
  while True:
    ceto = cinput('ceto sociale',Ceti)
    if p.retaggio>=data['ceto'][ceto]['retaggio'] : break # verifica che il personaggio abbia abbastanza punti retaggio per il ceto scelto.
  p.ceto=ceto
  p.retaggio-=data['ceto'][ceto]['retaggio']
  p.fama+=data['ceto'][ceto]['retaggio']
  p.denaro = calcolo_denaro(data['ceto'][ceto]['denaro iniziale'][0])
  if p.retaggio<0: raise ITDSException("Personaggi con modificatore di gratia negativo non possono essere nobili!") # questa eccezione non dovrebbe mai verificarsi 
  mestiere = input_mestiere(p) # al momento il mestiere è solo una stringa di testo senza particolare significato
  p.mestiere=mestiere
  #print(p.mestiere)
  # Abilità del mestiere
  p_mestiere=6
  abilità_già_scelte = []
  while p_mestiere>0:
    ab = ainput(f"abilità del mestiere (punti residui {p_mestiere})",Mestiere,p,p_mestiere)
    if ab in abilità_già_scelte and ab != 'artigiano' and 'professione' not in ab: continue
    elif random_gen and 'professione' in ab and len(p.professione)>2 : continue # se generazione casuale limita il numero di professioni e artigianati
    elif random_gen and 'artigiano' == ab and len(p.artigiano)>2 : continue
    else : abilità_già_scelte.append(ab)
    d = distanza_abilità(p.ceto,ab)
    if cultura1=='urbana' or cultura2=='urbana':
      if d>0 : d=d-1 # applica il vantaggio della cultura urbana
    if d<0 : d=-d # tutti i costi sono positivi
    if d!=0: d-=1 # ceti vicini sono gratis
    d+=1 # costo =1 + distanza
    if p_mestiere-d>=0:
      if ab == 'artigiano' :
        abd=None
        while not abd or abd.nome in p.artigiano:
          abd=input_abilità_speciale(ab, p, mestiere=True)
        p.artigiano[abd.nome]=abd
      elif 'professione' in ab : 
        abd=None
        while not abd or abd.nome in p.professione:
          abd=input_abilità_speciale(ab, p, mestiere=True)
          print(abd)
          print(abd.nome)
        p.professione[abd.nome]=abd
      else :
        p.abilità[ab].grado+=1
        p.abilità[ab].mestiere=True
      p_mestiere-=d
    else : 
      print(f"Abilità \"{ab}\" troppo costosa, {d} punti contro un residuo di {p_mestiere} punti")
  p.tentazione=cinput("tentazione (opzionale)", Tentazioni)
  if p.tentazione!='nessuna': p.retaggio+=1
  # Abilità libere
  p_libere=p.caratteristiche['mens'].caratteristica
  while p_libere>0:
    ab = cinput(f"abilità libere (punti residui {p_libere})",AbLibere)
    d = distanza_abilità(p.ceto,ab)
    if cultura1=='urbana' or cultura2=='urbana':
      if d>0 : d=d-1 # applica il vantaggio della cultura urbana
    if d<0 : d=-d # tutti i costi sono positivi
    if d!=0: d-=1 # ceti vicini sono gratis
    d+=1 # costo =1 + distanza
    if p_libere-d>=0:
      if ab == 'artigiano' :
        ab=input_abilità_speciale(ab,p)
        ab=p.artigiano[ab.nome]=ab
      elif 'professione' in ab : 
        ab=input_abilità_speciale(ab,p)
        p.professione[ab.nome]=ab
      else :
        p.abilità[ab].grado+=1
      p_libere-=d
    else : 
      print(f"Abilità troppo costosa, {d} punti contro un residuo di {p_mestiere} punti")

  p.fatica_init()
  p.ferite_init()
  p.spirito_init()
  p.ingombro_base_init()
  p.riflessi_init()

  # Eventi
  while p.retaggio>0:
    ev = sinput("evento", list(data['eventi'].keys()))
    if ev not in p.eventi:
      try : 
        data['eventi'][ev](p)
        p.eventi.append(ev)
        p.retaggio-=1
      except Exception as e: 
        print(e)

  #Addestramento
  ab3 =  3 if 'esperienza' in p.eventi else 2
  ab2 = 10 if 'esperienza' in p.eventi else 8
  while ab3>0:
    scelte = p.abilità_a_livello(1)
    scelta = sinput("abilità da portare al grado 3", scelte)
    p.incrementa_abilità(scelta,3)
    ab3-=1
  while ab2>0:
    scelte = p.abilità_a_livello(1)
    scelta = sinput("abilità da portare al grado 2", scelte)
    p.incrementa_abilità(scelta,2)
    ab2-=1

  # lingue
  n_lingue = 1 + p.mod('mens') + p.abilità['usi e costumi'].grado//2
  if p.abilità['arti liberali'].grado>=2 : p.lingue.append('Latino')
  if p.abilità['arti liberali'].grado>=4 : p.lingue.append('Greco antico')
  if p.abilità['arti liberali'].grado>=6 : p.lingue.append('Aramaico')
  if luogo in lingue_per_regione :
    p.lingue.append(lingue_to_ita[lingue_per_regione[luogo]])
    n_lingue-=1
  for i in range(n_lingue):
    while True :
      l = cinput("lingua",Lingue)
      if l not in p.lingue  and l not in ['Latino', 'Greco antico', 'Aramaico']:
        p.lingue.append(l)
        break

  # focus
  for a in p.abilità :
    if p.abilità[a].mestiere and p.abilità[a].grado>=3:
      for i in range(p.abilità[a].grado//3):
        p.abilità[a].focus.append(sinput(f"focus per {a}", data['focus'][a]))

  #TODO equipaggiamento: oggetti diversi da armi e armature, definizione della qualità degli oggetti e, nel caso di scelta casuale, impatto delle abilità di mestiere
  while True:
    armatura = sinput('armatura', list(data['armature'].keys()))
    if data['armature'][armatura]['costo']<p.denaro :
      p.denaro -= data['armature'][armatura]['costo']
      p.armatura = data['armature'][armatura]
      break
  larmi=[]
  while len(p.armi)<5:
    arma = sinput('arma', list(data['armi'].keys()))
    if data['armi'][arma]['costo']<p.denaro :
      p.denaro -= data['armi'][arma]['costo']
      larmi.append(data['armi'][arma])
    if sinput("acquistare altre armi? ", ["sì", "no"])=='no':
      break
  p.armi=larmi

  logg = []
  
  from equip import TipoOggetto
  for categoria in TipoOggetto:
    oggetti = [ o for o in data['oggetti'] if data['oggetti'][o].categoria==categoria ]
    if categoria not in [ 'armi', 'armature'] and len(oggetti) and sinput(f"acquistare oggetti dalla categoria {categoria}? ", ["sì", "no"])=='sì':
      while True:
        oggetto = sinput('oggetto', oggetti)
        if data['oggetti'][oggetto]['costo']<p.denaro :
          p.denaro -= data['oggetti'][oggetto]['costo']
          logg.append(data['oggetti'][oggetto])
        if sinput(f"acquistare altri oggetti ({categoria})? ", ["sì", "no"])=='no':
          break
  p.equipaggiamento=logg
  
  # Personaggio completo
  return p


# JSON
def tojson(p):
  return p.to_json()

def fromjson(fname):
  with open(fname,"r") as fin:
    return Personaggio.from_json(fin.read())


if __name__=='__main__':
  from sys import argv
  from os.path import exists
  random=False
  c = None
  for a in argv[1:]:
    if a in ['random', 'rand', 'r'] : random = True
    elif exists(a) : 
      c = fromjson(a)
  while not c: 
    try :
      c = creazione(random=random)
      with open('./json/'+c.nome+'.json',"w") as fout:
        fout.write(tojson(c))
    except ITDSException as e:
      print(e)
  print(c)
  print(c.nome)
  
