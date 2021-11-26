from django.shortcuts import HttpResponse
from django.shortcuts import render
import datetime
import time
from beneficiaires.models import Beneficaires, Nombrepart ,Presencedistribution, Categories, Produit 



# Create your views here.
def index(request):
    return render(request, "base.html", {})

def home(request):
  # result = Produit.objects.all().select_related()
   result = Categories.objects.raw("SELECT * FROM Categories c join Produit p ON c.idcategorie = p.idcategorie")
   cate = Categories.objects.all()
   bene = Beneficaires.objects.all()
   prod = Produit.objects.all()
   return render(request,'home.html',{'test':result,'cate':cate,'bene':bene,'prod':prod})

def addcate(request):
  envoi = "add"
  return render(request,'AjouterCategorie.html',{'envoi':envoi})

def addprod(request):
  envoi = "add"
  result = Categories.objects.raw("SELECT * FROM Categories")
  return render(request,'AjouterProduit.html',{'result':result,'envoi':envoi})

def addbenef(request):
  envoi = "add"
  return render(request,'AjouterBeneficiaire.html',{'envoi':envoi})  

def upcate(request):
  envoi = "update"
  req = request.POST.get("listCate")
  querry = Categories.objects.get(idcategorie=req)
  return render(request,'AjouterCategorie.html',{'envoi':envoi,'req':req,'querry':querry})

def upprod(request):
  envoi = "update"
  req = request.POST.get("listProd")
  querry = Produit.objects.get(idproduit=req)
  result = Categories.objects.raw("SELECT * FROM Categories")
  return render(request,'AjouterProduit.html',{'envoi':envoi,'req':req,'querry':querry,'result':result})

def upbenef(request):
  envoi = "update"
  req = request.POST.get("listBene")
  querry = Beneficaires.objects.get(idbeneficiaire=req)
  return render(request,'AjouterBeneficiaire.html',{'envoi':envoi,'req':req,'querry':querry}) 

def success(request):
  nomBenef = request.POST.get("nom1")
  prenom = request.POST.get("prenom1")
  mail = request.POST.get("mail1")
  tel = request.POST.get("tel1")
  adresse = request.POST.get("adresse1")
  mot = request.POST.get("mot1")
  carte = request.POST.get("carte1")
  remarque = request.POST.get("remarque1")
  idBenef = request.POST.get("id")
  idCate = request.POST.get("idcategorie1")
  NomCate = request.POST.get("nomCategorie1")
  image = request.POST.get("image1")
  unite = request.POST.get("unite1")
  q0_3 = request.POST.get("q0_3")
  q4_14 = request.POST.get("q4_14")
  q15_25 = request.POST.get("q15_25")
  q26_64 = request.POST.get("q26_64")
  q65plus = request.POST.get("q65plus")
  idProduit = request.POST.get("id")
  nomProduit = request.POST.get("nomProduit")
  seuil = request.POST.get("seuil")
  quantite = request.POST.get("quantite")
  presence = request.POST.get("presence1")
  type = request.POST.get("type1")
  focus = request.POST.get("focus1")
  idC = request.POST.get("id")

  if(type == "add"):
    if(focus == "benef"):
      ref = Beneficaires(nom=nomBenef,prenom=prenom,mail=mail,telephone=tel,adressepostale=adresse,motmairie=mot,cartedonnee=carte,remarque=remarque)
      ref.save()
      ref2=Nombrepart(idbeneficiaire=ref,number0_3=q0_3,number_4_14=q4_14,number_15_25=q15_25,number_26_64=q26_64,number_65plus=q65plus)
      ref2.save()
      ref3=Presencedistribution(idbeneficiaire=ref,datedistribution=datetime.datetime.now().date(),presence=presence)
      ref3.save()
    if(focus == "categorie"):
      ref= Categories(nomCategorie=NomCate,image=image,unite=unite)
      ref.save()
    if(focus == "produit"):
      req = Categories.objects.get(idcategorie=idCate)
      ref= Produit(idcategorie=req,nom=nomProduit,quantite=quantite,seuilalerte=seuil)
      ref.save()


  if(type == "update"):
    if(focus == "benef"):
      Beneficaires.objects.filter(idbeneficiaire=idBenef).update(nom=nomBenef,prenom=prenom,mail=mail,telephone=tel,adressepostale=adresse,motmairie=mot,cartedonnee=carte,remarque=remarque)
      Presencedistribution.objects.filter(idbeneficiaire=idBenef).update(presence=presence)
      Nombrepart.objects.filter(idbeneficiaire=idBenef).update(number0_3=q0_3,number_4_14=q4_14,number_15_25=q15_25,number_26_64=q26_64,number_65plus=q65plus)
    if(focus == "categorie"):
      Categories.objects.filter(idcategorie=idC).update(nomCategorie=NomCate,image=image,unite=unite)
    if(focus == "produit"):
      Produit.objects.filter(idproduit=idProduit).update(idcategorie=idCate,nom=nomProduit,quantite=quantite,seuilalerte=seuil)        
  return render(request,"home.html",{'message':'succes'})


def add(request):
  nom = request.POST.get("nom1")
  prenom = request.POST.get("prenom1")
  mail = request.POST.get("mail1")
  tel = request.POST.get("tel1")
  adresse = request.POST.get("adresse1")
  mot = request.POST.get("mot1")
  carte = request.POST.get("carte1")

  ref = Beneficaires(nom=nom,prenom=prenom,mail=mail,telephone=tel,adressepostale=adresse,motmairie=mot,cartedonnee=carte)
  ref.save()
  return render(request, "home.html",{"message":"registered!"})

def test(request):
  id = request.POST.get("id1")
  test = Beneficaires.objects.get(idbeneficiaire= id)
  return render(request,'home.html',{'add':test})

def update(request):
  nom = request.POST.get("nom1")
  prenom = request.POST.get("prenom1")
  mail = request.POST.get("mail1")
  tel = request.POST.get("tel1")
  adresse = request.POST.get("adresse1")
  mot = request.POST.get("mot1")
  carte = request.POST.get("carte1")

  Beneficaires.objects.filter(idbeneficiaire= obj).update(nom=nom,prenom=prenom,mail=mail,telephone=tel,adressepostale=adresse,motmairie=mot,cartedonnee=carte)
  return render(request, "home.html",{"message":"registered!"})