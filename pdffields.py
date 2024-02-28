#!/usr/bin/env python3.10
from pypdf import PdfReader, PdfWriter

campi = [
'Anno', 'Araldica_af_image', 'Armatura 1', 'Armatura 2', 'Armatura 3', 'Armi 1', 'Armi 2', 'Armi 3', 'Armi 4', 'Armi 5', 'Artigiano 1', 'Artigiano 5', 'Artigiano2', 'Artigiano3', 'Artigiano4', 'Audacia', 'Carartigiano2', 'Carartigiano3', 'Carartigiano4', 'Carartigiano5', 'Caratteristica Artigiano 1', 'Celeritas', 'Ceto', 'Critiche Residue', 'Critichetotali', 'Cultura', 'DAgilità', 'DAlchimia', 'DArchi', 'DArmiComuni', 'DArmiCorte', 'DArmiGuerra', 'DArteGuerra', 'DArtiArcane', 'DArtiLiberali', 'DAtletica', 'DAutorità', 'DBalestre', 'DCarisma', 'DCavalcare', 'DEmpatia', 'DForza', 'DFurtività', 'DGuarigione', 'DIntrattenere', 'DLotta', 'DManualità', 'DMercatura', 'DPercezione', 'DRaggirare', 'DRagionamento', 'DSopravvivenza', 'DStoriaLeggende', 'DTeologia', 'DUsiCostumi', 'DVolontà', 'Dannoarma1', 'Dannoarma2', 'Dannoarma3', 'Dannoarma4', 'Dannoarma5', 'Dartigianato1', 'Dartigianato2', 'Dartigianato3', 'Dartigianato4', 'Dartigianato5', 'Denari', 'Ego', 'Equipaggiamento 10D', 'Equipaggiamento 10S', 'Equipaggiamento 11D', 'Equipaggiamento 11S', 'Equipaggiamento 12D', 'Equipaggiamento 12S', 'Equipaggiamento 13D', 'Equipaggiamento 13S', 'Equipaggiamento 14S', 'Equipaggiamento 15S', 'Equipaggiamento 1D', 'Equipaggiamento 1S', 'Equipaggiamento 2D', 'Equipaggiamento 2S', 'Equipaggiamento 3D', 'Equipaggiamento 3S', 'Equipaggiamento 4D', 'Equipaggiamento 4S', 'Equipaggiamento 5D', 'Equipaggiamento 5S', 'Equipaggiamento 6D', 'Equipaggiamento 6S', 'Equipaggiamento 7D', 'Equipaggiamento 7S', 'Equipaggiamento 8D', 'Equipaggiamento 8S', 'Equipaggiamento 9D', 'Equipaggiamento 9S', 'Eventi 1', 'Eventi 2', 'Eventi 3', 'Eventi 4', 'Eventi 5', 'Eventi 6', 'Eventi 7', 'Fama', 'Fides', 'Focus 1', 'Focus 2', 'Focus 3', 'Focus 4', 'Focus 5', 'Focus 6', 'Fortitudo', 'Fresco residuo', 'Frescototale', 'Gartigianato1', 'Gartigianato2', 'Gartigianato3', 'Gartigianato4', 'Gartigianato5', 'Genere', 'Grado Agilità', 'Grado Alchimia', 'Grado Archi', 'Grado Armi Comuni', 'Grado Armi Corte', 'Grado Armi da Guerra', 'Grado Arte guerra', 'Grado Arti Arcane', 'Grado Arti Liberali', 'Grado Atletica', 'Grado Autorità', 'Grado Balestre', 'Grado Carisma', 'Grado Cavalcare', 'Grado Empatia', 'Grado Forza', 'Grado Furtività', 'Grado Guarigione', 'Grado Intrattenere', 'Grado Lotta', 'Grado Manualità', 'Grado Mercatura', 'Grado Percezione', 'Grado Raggirare', 'Grado Ragionamento', 'Grado Sopravvivenza', 'Grado Storia e Leggende', 'Grado Teologia', 'Grado Usi e Costumi', 'Grado Volontà', 'Graffi Residue', 'Graffitotali', 'Gratia', 'Gravi Residue', 'Gravitotali', 'Honor', 'Impietas', 'Ingombro Leggero', 'Ingombro Massimo', 'Ingombro Moderato', 'Ingombro Pesante', 'Leggere Residue', 'Leggeretotali', 'Lingue', "Lire d'oro", 'Mens', 'Mestiere', 'Misuraarma1', 'Misuraarma2', 'Misuraarma3', 'Misuraarma4', 'Misuraarma5', 'Mod Audacia', 'Mod Celeritas', 'Mod Fortitudo', 'Mod Gratia', 'Mod Mens', 'Mod Prudentia', 'Mortali Residue', 'Mortalitotali', 'Nessun Ingombro', 'Nome', 'Note Armatura 2', 'Note Armatura 3', 'Note armatura 1', 'Ordine', 'PE Liberi', 'PE spesi', 'Parata1', 'Parata2', 'Parata3', 'Parata4', 'Parata5', 'PequipD1', 'PequipD10', 'PequipD11', 'PequipD12', 'PequipD13', 'PequipD2', 'PequipD3', 'PequipD4', 'PequipD5', 'PequipD6', 'PequipD7', 'PequipD8', 'PequipD9', 'PequipS1', 'PequipS10', 'PequipS11', 'PequipS12', 'PequipS13', 'PequipS14', 'PequipS15', 'PequipS2', 'PequipS3', 'PequipS4', 'PequipS5', 'PequipS6', 'PequipS7', 'PequipS8', 'PequipS9', 'Peso totale trasportato', 'Pregiarmi1', 'Pregiarmi2', 'Pregiarmi3', 'Pregiarmi4', 'Pregiarmi5', 'Protezione Armatura', 'Prudentia', 'Ratio', 'Regioni Fama 1', 'Regioni Fama 2', 'Regioni Fama 3', 'Regioni Fama 4', 'Riflessi attuali', 'Riflessi massimi', 'Ritratto_af_image', 'Robustezza Armatura', 'Sfinito residuo', 'Sfinitototale', 'Soldi', 'Spiritoresiduo', 'Spiritototale', 'Stanco residuo', 'Stancototale', 'Superstitio', 'Talenti 1', 'Talenti10', 'Talenti11', 'Talenti12', 'Talenti13', 'Talenti14', 'Talenti2', 'Talenti3', 'Talenti4', 'Talenti5', 'Talenti6', 'Talenti7', 'Talenti8', 'Talenti9', 'Tentazione', 'Tratti 1', 'Tratti 2', 'Tratti 3', 'Tratti 4'
]

dado_extra_ab = [ 'DAgilità', 'DAlchimia', 'DArchi', 'DArmiComuni', 'DArmiCorte', 'DArmiGuerra', 'DArteGuerra', 'DArtiArcane', 'DArtiLiberali', 'DAtletica', 'DAutorità', 'DBalestre', 'DCarisma', 'DCavalcare', 'DEmpatia', 'DForza', 'DFurtività', 'DGuarigione', 'DIntrattenere', 'DLotta', 'DManualità', 'DMercatura', 'DPercezione', 'DRaggirare', 'DRagionamento', 'DSopravvivenza', 'DStoriaLeggende', 'DTeologia', 'DUsiCostumi', 'DVolontà' ]
grado_ab = [ 'Grado Agilità', 'Grado Alchimia', 'Grado Archi', 'Grado Armi Comuni', 'Grado Armi Corte', 'Grado Armi da Guerra', 'Grado Arte guerra', 'Grado Arti Arcane', 'Grado Arti Liberali', 'Grado Atletica', 'Grado Autorità', 'Grado Balestre', 'Grado Carisma', 'Grado Cavalcare', 'Grado Empatia', 'Grado Forza', 'Grado Furtività', 'Grado Guarigione', 'Grado Intrattenere', 'Grado Lotta', 'Grado Manualità', 'Grado Mercatura', 'Grado Percezione', 'Grado Raggirare', 'Grado Ragionamento', 'Grado Sopravvivenza', 'Grado Storia e Leggende', 'Grado Teologia', 'Grado Usi e Costumi', 'Grado Volontà' ]

ferite  = [ 'Graffitotali', 'Leggeretotali', 'Gravitotali', 'Critichetotali', 'Mortalitotali' ]
feriter = [ 'Graffi Residue', 'Leggere Residue', 'Gravi Residue', 'Critiche Residue', 'Mortali Residue' ]
fatica  = [ 'Frescototale', 'Stancototale', 'Sfinitototale' ]
faticar = [ 'Fresco residuo', 'Stanco residuo', 'Sfinito residuo' ]
denaro  = [ "Lire d'oro", "Soldi", "Denari" ]

def denaro_split(d):
  lire   = (d//12)//20 #lire
  soldi  = (d//12)%20 #soldi
  denari = d%12 #denari
  return lire, soldi, denari

def capitalize(s):
  return s.capitalize()

def fill(p):
  fields = {
   "Nome": p.nome,
   "Anno": str(p.anno_nascita),
   "Genere": 'o' if p.genere=='maschio' else 'a',
   "Cultura": f'{p.cultura[0]}/{p.cultura[1]}',
   "Ceto": p.ceto.name,
   "Mestiere": p.mestiere,
   "Ordine": p.ordine,
   "Tentazione": p.tentazione,
   "Fama": str(p.fama),
   "Spiritototale" : str(p.spirito),
   "Spiritoresiduo" : str(p.spirito),
   "Riflessi massimi": str(p.riflessi),
   "Riflessi attuali": str(p.riflessi),
   "Nessun Ingombro": str(p.ingombro_base),
   "Ingombro Leggero": str(p.ingombro_base*2),
   "Ingombro Moderato": str(p.ingombro_base*4),
   "Ingombro Pesante": str(p.ingombro_base*6),
   "Ingombro Massimo": str(p.ingombro_base*8),
   "Lingue": ', '.join(p.lingue),
   "PE Liberi" : str(p.pe_liberi),
   "PE spesi" : str(p.pe_spesi),
   "Denari" : '0',
   "Armatura 1" : f'{p.armatura.nome} {"("+p.armatura.qualità+")" if p.armatura.qualità!="normale" else ""}',
   "Protezione Armatura" : str(p.armatura.protezione),
   "Robustezza Armatura" : str(p.armatura.protezione*10),
   "Note Armatura 1": ', '.join(p.armatura.pregi),
   "Peso totale trasportato" : str(p.armatura.peso + sum([ a.peso for a in p.armi]) + sum([o.peso for o in p.equipaggiamento])),
  }
  fields[denaro[0]], fields[denaro[1]], fields[denaro[2]] = denaro_split(p.denaro)

  tratti = p.altro.split('\n')
  i=1
  for t in tratti:
    fields[f"Tratti {i}"]=t
    i+=1

  i=1
  lato='S'
  for a in p.equipaggiamento:
    fields[f'Equipaggiamento {i}{lato}']=f'{a.nome} {"("+a.qualità+")" if a.qualità!="normale" else ""}'
    fields[f'Pequip{lato}{i}']=a.peso
    i=i+1
    if i>15 : 
      i-=15
      lato='D'

  i=1
  for a in p.armi:
    print(a)
    fields[f'Armi {i}']=f'{a.nome} {"("+a.qualità+")" if a.qualità!="normale" else ""}'
    fields[f'Parata{i}']=f'+{a.parata}'
    fields[f'Dannoarma{i}']=f"+{a.danno}{a.tipo}"
    fields[f'Misuraarma{i}']=f"{a.misura if a.misura!='N/A' else ''} {str(a.gittata)+'m' if a.gittata!=0 else ''}"
    fields[f'Pregiarmi{i}']=f"{', '.join(a.pregi)}"
    i+=1

  i=1
  for a in p.abilità:
    if len(p.abilità[a].focus): 
      fields[f'Focus {i}']=f'{a}: {", ".join(p.abilità[a].focus)}'
      i+=1
  for a in p.artigiano:
    if len(p.artigiano[a].focus): 
      fields[f'Focus {i}']=f'{a}: {", ".join(p.artigiano[a].focus)}'
      i+=1
  for a in p.professione:
    if len(p.professione[a].focus): 
      fields[f'Focus {i}']=f'{a}: {", ".join(p.professione[a].focus)}'
      i+=1

  for f,v,r in zip(ferite,p.ferite,feriter):
    fields[f]=str(v)
    fields[r]=str(v)

  for f,v,r in zip(fatica,p.fatica,faticar):
    fields[f]=str(v)
    fields[r]=str(v)

  for c in p.caratteristiche:
    fields[capitalize(c)]=str(p.caratteristiche[c].caratteristica)
    fields['Mod '+capitalize(c)]=str(p.caratteristiche[c].modificatore)

  ab = sorted(list(p.abilità.keys()))
  for c,g,d in zip(ab,grado_ab,dado_extra_ab) :
    fields[d]=str(p.abilità[c].dado_extra)
    fields[g]=str(p.abilità[c].grado)+('*' if p.abilità[c].mestiere else '')
  for v in p.valori:
    fields[capitalize(v)]=str(p.valori[v])

  ab = sorted(list(p.artigiano.keys()))
  i=1
  for c in ab :
    fields[f'Artigiano {i}']=c
    fields[f'Artigiano{i}']=c
    fields[f'Dartigianato{i}']=str(p.artigiano[c].dado_extra)
    fields[f'Gartigianato{i}']=str(p.artigiano[c].grado)+('*' if p.artigiano[c].mestiere else '')
    if i==1 : fields[f'Caratteristica Artigiano {i}']=str(p.artigiano[c].caratteristica)
    else : fields[f'Carartigiano{i}']=str(p.artigiano[c].caratteristica)
    i+=1
  ab = sorted(list(p.professione.keys()))
  for c in ab :
    fields[f'Artigiano {i}']=c
    fields[f'Artigiano{i}']=c
    fields[f'Dartigianato{i}']=str(p.professione[c].dado_extra)
    fields[f'Gartigianato{i}']=str(p.professione[c].grado)+('*' if p.professione[c].mestiere else '')
    if i==1 : fields[f'Caratteristica Artigiano {i}']=str(p.professione[c].caratteristica)
    else : fields[f'Carartigiano{i}']=str(p.professione[c].caratteristica)
    i+=1

  i=1
  for e in p.eventi:
    fields[f'Eventi {i}']=e
    i+=1

  i=1
  for e in p.talenti:
    fields[f'Talenti {i}']=e
    fields[f'Talenti{i}']=e
    i+=1

  return fields
  #p.luogo_nascita 
  #p.retaggio   


def write_pdf(p):
  reader = PdfReader("scheda_template.pdf")
  writer = PdfWriter()
  writer.clone_reader_document_root(reader)
  #for page in reader.pages: 
  #  writer.add_page(page)
  fields = fill(p)
  print(fields)
  writer.update_page_form_field_values(writer.pages[0], fields)
  writer.update_page_form_field_values(writer.pages[1], fields)
  with open(f"./pdf/{p.nome}.pdf", "wb") as output_stream:
    writer.write(output_stream)

from itdschargen import fromjson, Personaggio
import dataclasses

if __name__=='__main__':
  from sys import argv
  from os.path import exists
  random=False
  for a in argv[1:]:
    if exists(a) : 
      c = fromjson(a) #TODO sembra che fromjson perda le armi (lista di dataclass)
      for field in dataclasses.fields(c):
        field_name = field.name
        field_value = getattr(c, field_name)
        print(f"{field_name}: {field_value}")
      print("-----------------------------------------------------------------")
      write_pdf(c)
      
