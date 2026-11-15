taches = []                                                        
choix = ""                                                         
while choix != "0":                                                
    print("\n=== GESTION DES TÂCHES ===")                          
    print("1. Ajouter une tâche")                                  
    print("2. Afficher les tâches")                                
    print("3. Rechercher une tâche")                               
    print("0. Quitter")                                            
    choix = input("Votre choix : ").strip()                        
                                                                               
    if choix == "1":                                               
        titre = input("Titre de la tâche : ").strip()              
        if titre == "":                                            
            print("Erreur : le titre ne peut pas être vide.")      
        else:                                                      
            taches.append(titre)                                   
            print("Tâche ajoutée avec succès.")                    
                                                                                                            
    elif choix == "2":                                             
        if len(taches) == 0:                                       
            print("Aucune tâche pour le moment.")                  
        else:                                                      
            print("\nListe des tâches :")                          
            for i in range(len(taches)):                           
                print(f"{i + 1}. {taches[i]}")                     
                                                                                                                     
    elif choix == "3":                                             
        mot = input("Mot-clé à rechercher : ").strip().lower()     
        trouve = False                                             
        for i in range(len(taches)):                               
            if mot in taches[i].lower():                           
                print(f"{i + 1}. {taches[i]}")                     
                trouve = True                                      
        if not trouve:                                             
            print("Aucune tâche trouvée.")                         
                                                                     
    elif choix == "0":                                             
        print("Au revoir !")                                                     
    else:                                                          
        print("Erreur : option invalide, choisissez 0, 1, 2 ou 3.")
    