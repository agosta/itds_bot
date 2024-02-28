#!/usr/env/ python3

# Volontà
def  v_bassifondi(self):
  if self.abilità['volontà'].grado>=3 and self.abilità['furtività'].grado>=3 and self.abilità['raggirare'].grado>=3 and self.abilità['usi e costumi'].grado>=3 :
    self.tfocus.append('interazioni sociali con umili')
    return True
  return False

def  v_diligente(self):
  if self.abilità['volontà'].grado>=3 and self.abilità['mercatura'].grado>=3 and (self.abilità['arti liberali'].grado>=3 or self.abilità['teologia'].grado>=3) and (self.artigiano_a_livello(3) or self.professione_a_livello(3)) :
    return True
  return False

def  v_lottatore(self):
  if self.abilità['volontà'].grado>=3 and self.abilità['lotta'].grado>=3 and (self.abilità['armi comuni'].grado>=3 or self.abilità['armi da guerra'].grado>=3) :
    return True
  return False

def  v_stratega(self):
  if self.abilità['volontà'].grado>=3 and self.abilità['arte della guerra'].grado>=3 and self.abilità['autorità'].grado>=3 and (self.abilità['armi comuni'].grado>=3 or self.abilità['armi da guerra'].grado>=3) :
    return True
  return False

def  v_alfiere(self):
  if self.abilità['volontà'].grado>=4 and self.abilità['autorità'].grado>=4 and (self.abilità['arti liberali'].grado>=4 or self.abilità['teologia'].grado>=4) :
    return True
  return False

def  v_fiore(self):
  if self.abilità['volontà'].grado>=4 and self.abilità['arte della guerra'].grado>=4 and self.abilità['cavalcare'].grado>=4 :
    return True
  return False

def  v_lotta_in_arme(self):
  if self.abilità['volontà'].grado>=4 and self.abilità['lotta'].grado>=4 and (self.abilità['armi comuni'].grado>=4 or self.abilità['armi da guerra'].grado>=4) :
    return True
  return False

def  v_vitalità(self):
  if self.abilità['volontà'].grado>=4 and self.abilità['atletica'].grado>=4 and (self.abilità['lotta'].grado>=4 or self.abilità['sopravvivenza'].grado>=4) :
    return True
  return False

def  v_araldo(self):
  if self.abilità['volontà'].grado>=5 and self.abilità['autorità'].grado>=5 :
    self.caratteristiche['audacia'].caratteristica+=1
    return True
  return False

def  v_condottiero(self):
  if self.abilità['volontà'].grado>=5 and self.abilità['arte della guerra'].grado>=5 :
    return True
  return False

def  v_illuminazione(self):
  if self.abilità['volontà'].grado>=5 and (self.abilità['arti arcane'].grado>=5 or self.abilità['teologia'].grado>=5) :
    p.spirito += p.caratteristiche['mens'].caratteristica
    return True
  return False

def  v_volitivo(self):
  if self.abilità['volontà'].grado>=5 and (self.abilità['intrattenere'].grado>=5 or self.abilità['raggirare'].grado>=5) :
    self.caratteristiche['gratia'].caratteristica+=1
    # si può anche rimuovere una tentazione e cambiare i valori...
    return True
  return False

# Agilità
def  v_combattimento_due_armi(self):
  if self.abilità['agilità'].grado>=3 and self.abilità['atletica'].grado>=3 and self.abilità['armi corte'].grado>=3 and (self.abilità['armi comuni'].grado>=3 or self.abilità['lotta'].grado>=3 or self.abilità['armi da guerra'].grado>=3) :
    return True
  return False

def  v_equitazione(self):
  if self.abilità['agilità'].grado>=3 and self.abilità['atletica'].grado>=3 and self.abilità['cavalcare'].grado>=3 and self.abilità['empatia'].grado>=3 :
    return True
  return False

def  v_grazia_felina(self):
  if self.abilità['agilità'].grado>=3 and self.abilità['atletica'].grado>=3 and self.abilità['furtività'].grado>=3 and (self.abilità['armi corte'].grado>=3 or self.abilità['manualità'].grado>=3) :
    p.riflessi+=1
    p.abilità['agilità'].dado_extra+=1
    return True
  return False

def  v_lingua_sciolta(self):
  if self.abilità['agilità'].grado>=3 and self.abilità['intrattenere'].grado>=3 and self.abilità['raggirare'].grado>=3 and (self.abilità['autorità'].grado>=3 or self.abilità['empatia'].grado>=3) :
    return True
  return False

def  v_senso_pericolo(self):
  if self.abilità['agilità'].grado>=4 and self.abilità['furtività'].grado>=4 and self.abilità['sopravvivenza'].grado>=4 :
    self.caratteristiche['celeritas'].caratteristica+=1
    return True
  return False

def  v_sicario(self):
  if self.abilità['agilità'].grado>=4 and self.abilità['furtività'].grado>=4 and self.abilità['armi corte'].grado>=4 :
    return True
  return False

def  v_stile_due_armi(self):
  if self.abilità['agilità'].grado>=4 and self.abilità['armi corte'].grado>=4 and (self.abilità['armi da guerra'].grado>=4 or self.abilità['lotta'].grado>=4):
    return True
  return False

def  v_tempismo(self):
  if self.abilità['agilità'].grado>=4 and self.abilità['armi da guerra'].grado>=4 and self.abilità['armi comuni'].grado>=4 :
    return True
  return False

def  v_maestro_di_lotta(self):
  if self.abilità['agilità'].grado>=5 and self.abilità['lotta'].grado>=5 :
    return True
  return False

def  v_maestro_di_scudo(self):
  if self.abilità['agilità'].grado>=5 and self.abilità['armi da guerra'].grado>=5 :
    return True
  return False

def  v_ombra(self):
  if self.abilità['agilità'].grado>=5 and self.abilità['furtività'].grado>=5 :
    return True
  return False

def  v_fulmine(self):
  if self.abilità['agilità'].grado>=6 :
    a = set(self.abilità_a_livello(6)).intersection(['armi comuni', 'armi corte', 'armi da guerra', 'lotta'])
    if len(a)>=2 :
      self.caratteristiche['prudentia'].caratteristica+=1
      return True
  return False

# Forza
def  v_giostrare(self):
  if self.abilità['forza'].grado>=3 and self.abilità['armi comuni'].grado>=3 and self.abilità['armi da guerra'].grado>=3 and self.abilità['cavalcare'].grado>=3 :
    return True
  return False

def  v_incoccare(self):
  if self.abilità['forza'].grado>=3 and self.abilità['atletica'].grado>=3 and (self.abilità['archi'].grado>=3 or self.abilità['balestre'].grado>=3) :
    return True
  return False

def  v_minaccioso(self):
  if self.abilità['forza'].grado>=3 and self.abilità['atletica'].grado>=3 and self.abilità['autorità'].grado>=3 and self.abilità['lotta'].grado>=3 :
    p.abilità['autorità'].dado_extra+=1
    return True
  return False

def  v_sbracciata(self):
  if self.abilità['forza'].grado>=3 and self.abilità['atletica'].grado>=3 and (self.abilità['armi comuni'].grado>=3 or self.abilità['armi da guerra'].grado>=3) :
    return True
  return False

def  v_carovaniere(self):
  if self.abilità['forza'].grado>=4 and self.abilità['mercatura'].grado>=4 and self.abilità['sopravvivenza'].grado>=4 :
    return True
  return False

def  v_fanteria(self):
  if self.abilità['forza'].grado>=4 and self.abilità['armi comuni'].grado>=4 and self.abilità['armi da guerra'].grado>=4 :
    return True
  return False

def  v_mente_guerriero(self):
  if self.abilità['forza'].grado>=4 and self.abilità['arti liberali'].grado>=4 and self.abilità['lotta'].grado>=4 :
    self.caratteristiche['prudentia'].caratteristica+=1
    return True
  return False

def  v_mitridatismo(self):
  if self.abilità['forza'].grado>=4 and self.abilità['guarigione'].grado>=4 :
    return True
  return False

def  v_bestia_soma(self):
  if self.abilità['forza'].grado>=5 and self.abilità['atletica'].grado>=5 :
    self.caratteristiche['fortitudo'].caratteristica+=1
    self.fatica = [ i+1 for i in self.fatica ]
    return True
  return False

def  v_duellante(self):
  if self.abilità['forza'].grado>=5 and self.abilità['armi corte'].grado>=5 :
    return True
  return False

def  v_maestro_arma(self):
  if self.abilità['forza'].grado>=5 and self.abilità['armi da guerra'].grado>=5 and self.abilità['armi comuni'].grado>=5 :
    return True
  return False

def  v_macchina_guerra(self):
  if self.abilità['forza'].grado>=6 and self.abilità['lotta'].grado>=6 :
    self.caratteristiche['celeritas'].caratteristica+=1
    return True
  return False

# Gratia
def  v_affarista(self):
  if self.abilità['carisma'].grado>=3 and self.abilità['mercatura'].grado>=3 and self.abilità['raggirare'].grado>=3 and self.abilità['usi e costumi'].grado>=3 :
    self.tfocus.append('interazioni sociali con borghesi')
    return True
  return False

def  v_cortesia(self):
  if self.abilità['carisma'].grado>=3 and self.abilità['arti liberali'].grado>=3 and self.abilità['autorità'].grado>=3 and (self.abilità['intrattenere'].grado>=3 or self.abilità['raggirare'].grado>=3) :
    return True
  return False

def  v_fattucchiera(self):
  if self.abilità['carisma'].grado>=3 and self.abilità['alchimia'].grado>=3 and self.abilità['raggirare'].grado>=3 and self.abilità['arti arcane'].grado>=3 :
    return True
  return False

def  v_trovatore(self):
  if self.abilità['carisma'].grado>=3 and self.abilità['intrattenere'].grado>=3 and self.abilità['storia e leggende'].grado>=3 and self.abilità['usi e costumi'].grado>=3 :
    return True
  return False

def  v_compagni_fedeli(self):
  if self.abilità['carisma'].grado>=4 and self.abilità['empatia'].grado>=4 and (self.abilità['cavalcare'].grado>=4 or self.abilità['sopravvivenza'].grado>=4) :
    return True
  return False

def  v_retore(self):
  if self.abilità['carisma'].grado>=4 and self.abilità['arti liberali'].grado>=4 and self.abilità['intrattenere'].grado>=4 :
    return True
  return False

def  v_seduttore(self):
  if self.abilità['carisma'].grado>=4 and self.abilità['raggirare'].grado>=4 and self.abilità['intrattenere'].grado>=4 :
    self.caratteristiche['gratia'].caratteristica+=1
    return True
  return False

def  v_senza_volto(self):
  if self.abilità['carisma'].grado>=4 and self.abilità['raggirare'].grado>=4 and self.abilità['furtività'].grado>=4 :
    return True
  return False

def  v_intuito(self):
  if self.abilità['carisma'].grado>=5 and self.abilità['arti liberali'].grado>=5 :
    self.caratteristiche['mens'].caratteristica+=1
    return True
  return False

def  v_ispirare(self):
  if self.abilità['carisma'].grado>=5 and self.abilità['empatia'].grado>=5 and (self.abilità['intrattenere'].grado>=5 or self.abilità['autorità'].grado>=5) :
    return True
  return False

def  v_rete_contatti(self):
  if self.abilità['carisma'].grado>=5 and self.abilità['usi e costumi'].grado>=5 :
    return True
  return False

def  v_maestà(self):
  if self.abilità['carisma'].grado>=6 and self.abilità['autorità'].grado>=6 :
    self.caratteristiche['audacia'].caratteristica+=1
    return True
  return False

# Ragionamento
def  v_determinazione(self):
  if self.abilità['ragionamento'].grado>=3 and self.abilità['autorità'].grado>=3 and (self.abilità['intrattenere'].grado>=3 or self.abilità['raggirare'].grado>=3 or self.abilità['arti liberali'].grado>=3) :
    return True
  return False

def  v_ingegno(self):
  if self.abilità['ragionamento'].grado>=3 and self.abilità['arti liberali'].grado>=3 and self.abilità['storia e leggende'].grado>=3 and (self.artigiano_a_livello(3) or self.professione_a_livello(3)) :
    return True
  return False

def  v_medico_campo(self):
  if self.abilità['ragionamento'].grado>=3 and self.abilità['empatia'].grado>=3 and self.abilità['guarigione'].grado>=3 and self.abilità['sopravvivenza'].grado>=3 :
    return True
  return False

def  v_meditazione(self):
  if self.abilità['ragionamento'].grado>=3 and self.abilità['arti liberali'].grado>=3 and self.abilità['teologia'].grado>=3 and (self.abilità['arti arcane'].grado>=3 and self.abilità['empatia'].grado>=3) :
    self.spirito+=self.caratteristiche['mens'].modificatore
    self.spirito+=self.caratteristiche['prudentia'].modificatore
    return True
  return False

def  v_ippocrate(self):
  if self.abilità['ragionamento'].grado>=4 and self.abilità['alchimia'].grado>=4 and self.abilità['guarigione'].grado>=4 :
    self.abilità['guarigione'].dado_extra+=1
    self.abilità['alchimia'].dado_extra+=1
    return True
  return False

def  v_mondano(self):
  if self.abilità['ragionamento'].grado>=4 and self.abilità['arti liberali'].grado>=4 and self.abilità['usi e costumi'].grado>=4 :
    self.abilità['carisma'].dado_extra+=1
    return True
  return False

def  v_vagabondo(self):
  if self.abilità['ragionamento'].grado>=4 and self.abilità['storia e leggende'].grado>=4 and self.abilità['usi e costumi'].grado>=4 :
    self.caratteristiche['audacia'].caratteristica+=1
    return True
  return False

def  v_vita_strada(self):
  if self.abilità['ragionamento'].grado>=4 and self.abilità['furtività'].grado>=4 and self.abilità['usi e costumi'].grado>=4 :
    self.abilità['percezione'].dado_extra+=1
    return True
  return False

def  v_chiave_mappa(self):
  if self.abilità['ragionamento'].grado>=5 and self.artigiano_a_livello(5):
    return True
  return False

def  v_colpo_occhio(self):
  if self.abilità['ragionamento'].grado>=5 and (self.abilità['manualità'].grado>=5 or self.abilità['sopravvivenza'].grado>=5) :
    self.caratteristiche['prudentia'].caratteristica+=1
    return True
  return False

def  v_eponimo(self):
  if self.abilità['ragionamento'].grado>=5 and self.abilità['arti liberali'].grado>=5 :
    return True
  return False

def  v_custode_sapere(self):
  if self.abilità['ragionamento'].grado>=6 and (self.abilità['arti arcane'].grado>=6 or self.abilità['teologia'].grado>=6) :
    self.caratteristiche['mens'].caratteristica+=1
    return True
  return False

# Percezione
def  v_arrocco(self):
  if self.abilità['percezione'].grado>=3 and self.abilità['arte della guerra'].grado>=3 and self.abilità['sopravvivenza'].grado>=3 :
    if len(set(self.abilità_a_livello(3,greater=True)).intersection(['armi corte', 'armi comuni', 'armi da guerra', 'archi', 'balestre'])) :
      return True
  return False

def  v_avanguardia(self):
  if self.abilità['percezione'].grado>=3 and self.abilità['autorità'].grado>=3 and self.abilità['furtività'].grado>=3 and self.abilità['sopravvivenza'].grado>=3 :
    return True
  return False

def  v_battipista(self):
  if self.abilità['percezione'].grado>=3 and self.abilità['atletica'].grado>=3 and self.abilità['usi e costumi'].grado>=3 and self.abilità['sopravvivenza'].grado>=3 :
    return True
  return False

def  v_scienza_antica(self):
  if self.abilità['percezione'].grado>=3 and self.abilità['alchimia'].grado>=3 and self.abilità['arti arcane'].grado>=3 and self.artigiano_a_livello(3) :
    for a in self.artigiano :
      self.artigiano[a].dado_extra+=1
    return True
  return False

def  v_aggiustare_tiro(self):
  if self.abilità['percezione'].grado>=4 and self.abilità['atletica'].grado>=4 and self.abilità['archi'].grado>=4 :
    return True
  return False

def  v_bruciapelo(self):
  if self.abilità['percezione'].grado>=4 and self.abilità['balestre'].grado>=4 :
    return True
  return False

def  v_cercatore(self):
  if self.abilità['percezione'].grado>=4 and self.abilità['furtività'].grado>=4 and self.abilità['sopravvivenza'].grado>=4 :
    self.caratteristiche['prudentia'].caratteristica+=1
    return True
  return False

def  v_tattiche_guerriglia(self):
  if self.abilità['percezione'].grado>=4 and self.abilità['arte della guerra'].grado>=4 and self.abilità['sopravvivenza'].grado>=4 :
    return True
  return False

def  v_armonioso(self):
  if self.abilità['percezione'].grado>=5 and self.abilità['atletica'].grado>=5 :
    self.caratteristiche['celeritas'].caratteristica+=1
    return True
  return False

def  v_cecchino(self):
  if self.abilità['percezione'].grado>=5 and self.abilità['balestre'].grado>=5 :
    return True
  return False

def  v_occhio_falco(self):
  if self.abilità['percezione'].grado>=5 and self.abilità['archi'].grado>=5 and self.abilità['atletica'].grado>=5 :
    return True
  return False

def  v_giudice(self):
  if self.abilità['percezione'].grado>=6 and self.abilità['autorità'].grado>=6 and (self.abilità['arti liberali'].grado>=6 or self.abilità['raggirare'].grado>=6) :
    self.caratteristiche['gratia'].caratteristica+=1
    return True
  return False

talenti = {
 'bassifondi' : v_bassifondi,
 'diligente'  : v_diligente,
 'lottatore'  : v_lottatore,
 'stratega'   : v_stratega,
 'alfiere'    : v_alfiere,
 'fiore della cavalleria' : v_fiore,
 'lotta in arme' : v_lotta_in_arme,
 'vitalità'   : v_vitalità,
 'araldo'     : v_araldo,
 'condottiere': v_condottiero,
 'illuminazione' : v_illuminazione,
 'volitivo'   : v_volitivo,
 'combattimento con due armi' : v_combattimento_due_armi,
 'equitazione': v_equitazione,
 'grazia felina' : v_grazia_felina,
 'lingua sciolta': v_lingua_sciolta,
 'senso del pericolo' : v_senso_pericolo,
 'sicario'    : v_sicario,
 'stile a due armi' : v_stile_due_armi,
 'tempismo'   : v_tempismo,
 'maestro di lotta' : v_maestro_di_lotta,
 'maestro di scudo' : v_maestro_di_scudo, 
 'ombra'      : v_ombra,
 'fulmine di guerra': v_fulmine,
 'giostrare'  : v_giostrare,
 'incoccare'  : v_incoccare,
 'minaccioso' : v_minaccioso,
 'sbracciata' : v_sbracciata,
 'carovaniere': v_carovaniere,
 'fanteria'   : v_fanteria,
 'mente del guerriero' : v_mente_guerriero,
 'mitridatismo' : v_mitridatismo,
 'bestia da soma' : v_bestia_soma,
 'duellante'  : v_duellante,
 'maestro d\'arma' : v_maestro_arma,
 'macchina da guerra' : v_macchina_guerra,
 'affarista'  : v_affarista,
 'cortesia'   : v_cortesia,
 'fattucchiere' : v_fattucchiera,
 'trovatore'  : v_trovatore,
 'compagni fedeli' : v_compagni_fedeli,
 'retore'     : v_retore,
 'seduttore'  : v_seduttore,
 'senza volto': v_senza_volto,
 'intuito'    : v_intuito,
 'ispirare'   : v_ispirare,
 'rete di contatti' : v_rete_contatti,
 'maestà'     : v_maestà,
 'determinazione' : v_determinazione,
 'ingegno'    : v_ingegno,
 'medico da campo' : v_medico_campo,
 'meditazione' : v_meditazione,
 'giuramento di ippocrate' : v_ippocrate,
 'mondano'    : v_mondano,
 'vagabondo'  : v_vagabondo,
 'vita di strada' : v_vita_strada,
 'chiave della mappa' : v_chiave_mappa,
 "colpo d'occhio" : v_colpo_occhio,
 'eponimo'    : v_eponimo,
 'custode del sapere' : v_custode_sapere,
 'arrocco'    : v_arrocco,
 'avanguardia': v_avanguardia,
 'battipista' : v_battipista,
 'scienza antica' : v_scienza_antica,
 'aggiustare il tiro' : v_aggiustare_tiro,
 'bruciapelo' : v_bruciapelo,
 'cercatore'  : v_cercatore,
 'tattiche di guerriglia' : v_tattiche_guerriglia,
 'armonioso'  : v_armonioso,
 'cecchino'   : v_cecchino,
 'occhio di falco' : v_occhio_falco,
 'giudice'    : v_giudice,
}


def v_milites(self):
    pass

def v_clerici(self):
    pass

def v_vagantes(self):
    pass

ordini = {
 'milites' : v_milites,
 'clerici' : v_clerici,
 'vagantes': v_vagantes,
}

def verifica_talenti(p):
   for t in talenti :
       if t in p.talenti : continue
       r = talenti[t](p)
       if r : 
           p.talenti.append(t)
       # verificare se ha senso fare qui i controlli su modificatori

