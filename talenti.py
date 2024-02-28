#!/usr/env/ python3

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

def  v_combattimento_due_armi(self):
  pass

def  v_equitazione(self):
  pass

def  v_grazia_felina(self):
  pass

def  v_lingua_sciolta(self):
  pass

def  v_senso_pericolo(self):
  pass

def  v_sicario(self):
  pass

def  v_stile_due_armi(self):
  pass

def  v_tempismo(self):
  pass

def  v_maestro_di_lotta(self):
  pass

def  v_maestro_di_scudo(self):
  pass

def  v_ombra(self):
  pass

def  v_fulmine(self):
  pass

def  v_giostrare(self):
  pass

def  v_incoccare(self):
  pass

def  v_minaccioso(self):
  pass

def  v_sbracciata(self):
  pass

def  v_carovaniere(self):
  pass

def  v_fanteria(self):
  pass

def  v_mente_guerriero(self):
  pass

def  v_mitridatismo(self):
  pass

def  v_bestia_soma(self):
  pass

def  v_duellante(self):
  pass

def  v_maestro_arma(self):
  pass

def  v_macchina_guerra(self):
  pass

def  v_affarista(self):
  pass

def  v_cortesia(self):
  pass

def  v_fattucchiera(self):
  pass

def  v_trovatore(self):
  pass

def  v_compagni_fedeli(self):
  pass

def  v_retore(self):
  pass

def  v_seduttore(self):
  pass

def  v_senza_volto(self):
  pass

def  v_intuito(self):
  pass

def  v_ispirare(self):
  pass

def  v_rete_contatti(self):
  pass

def  v_maestà(self):
  pass

def  v_determinazione(self):
  pass

def  v_ingegno(self):
  pass

def  v_medico_campo(self):
  pass

def  v_meditazione(self):
  pass

def  v_ippocrate(self):
  pass

def  v_mondano(self):
  pass

def  v_vagabondo(self):
  pass

def  v_vita_strada(self):
  pass

def  v_chiave_mappa(self):
  pass

def  v_colpo_occhio(self):
  pass

def  v_eponimo(self):
  pass

def  v_custode_sapere(self):
  pass

def  v_arrocco(self):
  pass

def  v_avanguardia(self):
  pass

def  v_battipista(self):
  pass

def  v_scienza_antica(self):
  pass

def  v_aggiustare_tiro(self):
  pass

def  v_bruciapelo(self):
  pass

def  v_cercatore(self):
  pass

def  v_tattiche_guerriglia(self):
  pass

def  v_armonioso(self):
  pass

def  v_cecchino(self):
  pass

def  v_occhio_falco(self):
  pass

def  v_giudice(self):
  pass

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

