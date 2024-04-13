#!/usr/bin/env python3.10
import fitz

__doc__ = '''Script di utilità per sostituire il campo Ritratto_af_image con una illustrazione del personaggio'''


def find_widget(page,fieldname):
  found=False
  w=page.first_widget
  if not w.field_name==fieldname :
    while True:
      w=w.next
      if not w or w.field_name==fieldname : 
        found=True
        break
  else : found=True
  if not w or not found:
    raise Exception(f"{fieldname} widget not found")
  return w

def replace_widget(page,w,img):
  rect=w.rect
  page.delete_widget(w)
  pix=fitz.Pixmap(img)
  page.insert_image(
    rect,                  # where to place the image (rect-like)
    filename=None,         # image in a file
    stream=None,           # image in memory (bytes)
    pixmap=pix,            # image from pixmap
    mask=None,             # specify alpha channel separately
    rotate=0,              # rotate (int, multiple of 90)
    xref=0,                # re-use existing image
    oc=0,                  # control visibility via OCG / OCMD
    keep_proportion=True,  # keep aspect ratio
    overlay=True,          # put in foreground
  )


if __name__=='__main__':
  from sys import argv
  from os.path import exists
  random=False
  pdf=None
  portrait=None
  arms=None
  for a in argv:
    if exists(a) : 
      if a.endswith('.pdf'): pdf=a
      elif a.endswith('.jpg') or a.endswith('.png'):
        if not portrait: portrait=a
        elif not arms : arms=a
  if not pdf or not portrait:
    raise Exception(f"missing filenames: '{pdf}' '{portrait}'")
  doc = fitz.open(pdf,filetype='pdf')
  page=doc[1]
  w=find_widget(page,'Ritratto_af_image')
  replace_widget(page,w,portrait)
  if arms:
    w=find_widget(page,'Araldica_af_image')
    replace_widget(page,w,arms)
  doc.save('./out/'+pdf)
  
