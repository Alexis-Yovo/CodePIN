PIN="0339"
PIN_saisie=input("Code PIN ? ")
nb_essai=1
while ((PIN_saisie!=PIN) and (nb_essai<=3)):
     PIN_saisie=input("Code Pin ?")
     nb_essai=nb_essai + 1
if (nb_essai>3):
  print("Carte avalée,contactez votre conseiller")
else :
  print("Code bon")
