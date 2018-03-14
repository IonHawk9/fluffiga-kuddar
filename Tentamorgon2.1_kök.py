loop = "intro"
inventory = []
game = True
förrahandling = ""
förrförrahandling = ""
handling = ""
vakenhet = 0

while game:
    while loop == "intro":
        vakenhet = 0
        print("--------------------------------------------------------------------------------------------------")
        print('Välkommen till Tentamorgon! Funktionerna du kan använda är "TITTA PÅ", "TITTA UNDER",')
        print('"ANVÄND" följt av ett objekt som finns i rummet. Ex: "Titta på TVn"')
        print('Du kan också gå till de olika rummen, "SOVRUM", "VARDAGSRUM", "HALL", "BADRUM", "KÖK",')
        print('genom att skriva: "gå till" följt av rummets namn. Ex: "gå till sovrummet"')
        print("--------------------------------------------------------------------------------------------------")
        loop = "vakna"
    while loop == "vakna":
        sängstatus = input("Klockan ringer. Vad vill du göra? Sova, snooza eller vakna?\n")
        sängstatus = sängstatus.lower()
        if sängstatus == "sova":
            print("Du försov dig")
            loop = 10
        if sängstatus == "snooza":
            print("Du förlorade tid")
            loop = 10
        if "vak" in sängstatus:
            loop = 3
        while loop == 3:
            ansträngning = input("Klicka på enter 20 gånger för att vakna\n")
            if ansträngning == "":
                vakenhet += 1
                print(vakenhet)
                if vakenhet > 19:
                    print("Du vaknar och går upp ur sängen.")
                    loop = "sovrum"

        while loop == 10:
            print("Looooser!")
            loop = "intro"


    while loop == "sovrum":
        print("--------------------------------------------------------------------------------------------------")
        print("Du är i sovrummet. Det är stökigt med kläder överallt.")
        print("Du ser en BYRÅ och en SÄNG.")
        print("--------------------------------------------------------------------------------------------------")
        handling = input()
        handling = handling.lower()
        if "gå till vardagsrum" in handling:
            loop = "vardagsrum"
        elif "gå till kök" in handling:
            loop = "kök"
        elif "gå till badrum" in handling:
            loop = "badrum"
        elif "gå till hall" in handling:
            loop = "hall"
        elif handling == "titta på byrå":
            print("Full med damm. Du tror att den var mörblå förut men nu är den mer ljusblå. Du tänker att det är modernt och går vidare.")
        elif handling == "titta under byrå":
            print("En trasig strumpa. Du borde verkligen slänga den")
        elif handling == "använd byrå":
            if "tröja" in inventory:
                print("Den är tom")
            else:
                print("Du öppnar en byrålåda och hittar en t-shirt. Grattis! Du tar på dig den. Luktar lite unket men ingen kommer märka det.")
                inventory.append("tröja")
        elif "kläder" in handling:
            print("Dessa kläder är inte tvättade på veckor. Helt oanvändbara. Måste hitta några som inte lockar råttor.")
        else:
            print('Kommandon: "TITTA PÅ ...", "TITTA UNDER ...", "ANVÄND ...", "GÅ TILL ..."')

    while loop == "vardagsrum":
        print("--------------------------------------------------------------------------------------------------")
        print("Du är i vardagsrummet. Även här inne är det ganska stökigt, du äcklas lite av dig själv när du ser den två veckor gamla skit du lämnat därinne. ")
        print("Du ser en TV och en SOFFA.")
        print("--------------------------------------------------------------------------------------------------")
        handling = input()
        handling = handling.lower()
        if "gå till sovrum" in handling:
            loop = "sovrum"
        elif "gå till kök" in handling:
            loop = "kök"
        elif "gå till hall" in handling:
            loop = "hall"
        elif "gå till badrum" in handling:
            loop = "badrum"
        elif "gå till vardagsrum" in handling:
            print("Du är redan i vardagsrummet din nöt!") #detta funkar inte
        elif handling == "titta på tv":
            print("Det är en gammal tjocktv som du ärvt av din morfar.")
        elif handling == "titta under tv":
            if "räkning" in inventory:
                print("Hur mycket mer kan det finnas under din tv egentligen?")
            else:
                print("Vad ska du hitta under din tv?? Ooh här var den räkningen du letat efter!")
                inventory.append("räkning")
        elif handling == "använd tv":
            if "tv" in inventory:
                print("Bara några minuter till...")
            else:
                print("Du sätter dig och ska bara titta en liten stund på tv, bara lite, lite... och där hade det gått ett helt avsnitt, du förlorar tid.")
                inventory.append("tv")
        elif handling == "titta på soffa":
            print("En relativt fräsh soffa om man bortser från den svaga öldoften ifrån en av sovkuddarna.")
        elif handling == "titta under soffa":
            if "byxor" in inventory:
                print("Det finns inget där utom damms, massor av damm.")
            else:
                print("Du har hittat dina byxor! Du drar snabbt på dig dem och känner dig stolt över denna bedrift.")
                inventory.append("byxor")
        elif handling == "använd soffa":
            if "öldoft" in inventory:
                print("Du funderar över möjliga tvättalternativ för den skitiga soffan.")
            else:
                print("Du sätter dig i soffan och börjar känna dig sömnig igen. Du lägger ned huvudet en stund. Dock äcklas du av öldoften och ställer dig upp igen.")
                inventory.append("öldoft")
        elif "skit" in handling:
            print("Du börjar må illa och måste spy.")
            loop = "badrum"
        else:
            print('Kommandon: "TITTA PÅ ...", "TITTA UNDER ...", "ANVÄND ...", "GÅ TILL ..."')


# ____Kök____________________________________________

    while loop == 'kök':

        disgusted = inventory.count('äcklad')
        if disgusted == 3:
            loop = 'replay'
            print('Du blir så äcklad av allt smuts, slem och mögel att du blir tvungen att spendera')
            print('resten av dagen hulkandes över toaletten. Du missar både tentan OCH eftertenta ölen.')
        else:
            print("--------------------------------------------------------------------------------------------------")
            handling = input('Du är i köket, som en stressad zombie står du där och glor på din KAFFEKOKARE, ditt KYLSKÅP och KÖKSBORDET.\n')
            print("--------------------------------------------------------------------------------------------------")

            handling = handling.lower()

            if 'gå till vardagsrum' in handling:
                loop = 'vardagsrum'
            elif 'gå till hall' in handling:
                loop = 'hall'
            elif 'gå till sovrum' in handling:
                loop = 'sovrum'
            elif 'gå till badrum' in handling:
                loop = 'badrum'

            elif 'titta på kaffekokare' in handling:
                print('Många kaffefläckar här.')
                inventory.append('äcklad')

            elif 'titta under kaffekokare' in handling:
                print('Woah! Vad var det som sprang iväg?!')
                inventory.append('äcklad')

            elif 'använd kaffekokare' in handling:
                coffee = inventory.count('kaffe')
                if coffee == 2:
                    print('COFFEE! Du får en regäl överdos av kaffe och får omedelbums läggas in akut på sjukhuset.')
                    print('Du missar tentan och den ack så viktiga eftertenta ölen.')
                    loop = 'replay'

                elif 'kaffe' in inventory:
                    print('Mer kaffe!! Du börjar känna dig lagom speedad!')
                    inventory.append('kaffe')
                else:
                    print('Du sätter på en kanna och sörplar i dig lite kaffe.')
                    inventory.append('kaffe')


            elif 'titta på kylskåp' in handling:
                print('Det är vitt med en hel del fettfläckar på.')
                inventory.append('äcklad')

            elif 'titta under kylskåp' in handling:
                print('Du ångrar omedelbart vad du gjort, fett, slem och damm pryder detta lilla utrymme.')
                inventory.append('äcklad')

            elif 'använd kylskåp' in handling:
                if 'ostmacka' in inventory:
                    print('Här finns då inget ätbart, om du inte räknar mat som snart kommer börja kräla iväg som ätbart...')
                    inventory.append('äcklad')

                else:
                    print('Du fascineras av allt rosa och gult mögel du har lyckats samla på dig, det ser ut som sockervadd...')
                    print('Du vet dock bättre än att äta sockervadd på morgonen..eller hur var det nu??\nHungrig som du är så slänger du ändå ihop en ostmacka.')
                    inventory.append('ostmacka')
                    inventory.append('äcklad')

            elif 'titta på köksbord' in handling:
                if 'id' in inventory:
                    print('Inte så mycket här, om man bortser från disken från de senaste två veckorna.')
                    inventory.append('äcklad')
                else:
                    print('"Oooh sheeet! Tur att jag kollade här" säger du och tar upp ditt ID kort.')
                    inventory.append('id')

            elif 'titta under köksbord' in handling:
                print('Här dansar dammråttorna vilt omkring, vilt omkring!')
                inventory.append('äcklad')

            elif 'använd köksbord' in handling:
                print('Du slår dig ner och försöööker att hålla öögonen öppna...\n.....\n.....\n.....')
                print('Du vaknar sömndrucket mitt på dagen och inser att du missat tentan,')
                print('oh well du kan iallafall gå på eftertenta ölen med dina klasskamrater.')
                loop = 'replay'

            else:
                print('Kommandon: "TITTA PÅ ...", "TITTA UNDER ...", "ANVÄND ...", "GÅ TILL ..."')



#_____Badrum______________

    while loop == "badrum":
        if "badrum besökt" in inventory:
            print("--------------------------------------------------------------------------------------------------")
            print("Du ser ett ostädat SKÅP, en oborstad TOALETT och ett HANDFAT med tandkrämsavlagringar från 2009 på sig.")
            print("--------------------------------------------------------------------------------------------------")
        else:
            print("--------------------------------------------------------------------------------------------------")
            print("Du är nu i badrummet. Du ser dig förtvivlat omkring. Du borde verkligen ha städat toaletten igår. ")
            print("Odören har spridit sig och intagit hela badrummet. Du sträcker dig efter luftrenaren och sprutar")
            print("slut på hela burken. Skönt. Du kan nu andas igen. Nu när du kan andas ser du dig omkring och ser")
            print("ett ostädat skåp, en oborstad toalett och ett handfat med tandkrämsavlagringar från 2009 på sig.")
            print("--------------------------------------------------------------------------------------------------")
            inventory.append("badrum besökt")

        förrförrahandling = förrahandling
        förrahandling = handling
        handling = input()
        handling = handling.lower()

                #Förflyttningssätt
        if handling == "gå till sovrum":
            loop = "sovrum"
        if handling == "gå till kök":
            loop = "kök"
        if handling == "gå till hall":
            loop = "hall"
        if handling == "gå till badrum":
            loop = "Tyvärr så befinner du dig redan i ditt väldigt illaluktande badrum."
        if handling == "gå till vardagsrum":
            loop = "vardagsrum"

                    #Handlingar i badrummet
                        #Toalett sekvens
        if handling == "titta på toalett":
            if "städad toalett" in inventory:
                print("Du ser med lyckliga ögon på din nu, väldigt vackra och välstädade toalett.")
            elif "städad toalett" not in inventory:
                print("Ångesten sköljer över dig när du beskådar din orengjorda toalett. Du står inte ut, du tar på dig ett par handskar och beväpnar dig med din knappt använda toaborste. Efter fem minuter och en gedigen mängd miljöfarliga ämnen är din toalett äntligen ren. Detta tog dock mer tid än vad du tänkt. Ajdå.")
                inventory.append("städad toalett")


        if handling == "titta under toalett":
            if "städad toalett" in inventory:
                print("Du var nogrann när du städade toaletten så här fanns det inget äckelpäckel!")
            elif "städad toalett" not in inventory:
                print("BLUUÄÄÄRGHH här bodde det inte bara smuts, utan även en och annan rodent och insekt...")
                inventory.append("äckelpäckel")
            if "äckelpäckel" in inventory:
                print("Där vill du INTE titta igen föräns toaletten är rengjord!")


        if handling == "använd toalett":
            if "städad toalett" in inventory:
                print("Du sätter dig på din fina, rengjorda toalett, tar fram din telefon och \n spelar lite angry birds. När du sitter och spelar får du ett meddelande från\n personen du gillar, den har svarat ja på din förfrågan om att gå ut\n på en dejt! Är detta dagen då ditt liv vänder runt?")
                inventory.append("dejt")
            elif "städad toalett" not in inventory:
                print("Toaletten ser obrukbar ut. Vill du använda den ändå? Ja/Nej")
        if förrahandling == "använd toalett" and handling == "ja":
            print("trots din initiala oro över att du inte städat toaletten så sätter du dig på toaletten. Du inser snabbt ditt misstag. DET ÄR NÅGOT SOM KRYPER PÅ DIG! DU STÄLLER DIG UPP, SKRIKER I PANIK OCH SPRINGER UT UR BADRUMMET. Tyvärr hade du placerat en blöt handduk väldigt välplacerat på golvet. Så du halkar, trillar och bryter nacken.")
            print("Din själ färdas till toalettriket. Spelet är över")
            loop = "intro"
        if förrahandling == "använd toalett" and handling == "nej":
            print("Bra val!")


                    #Handfat

        if handling == "titta på handfat":
            if "tittat på handfat" in inventory:
                print("Vill du verkligen titta på ditt ostädade handfat en gång till? Nej. Antog det.")
            elif "tittat på handfat" not in inventory:
                print("Du ser ett ganska ostädat handfat med tandkrämsavlagringar från långt innan du huserade i denna lägenheten")
                inventory.append("tittat på handfat")

        if handling == "använd handfat":
            if "borstat tänderna" in inventory:
                print ("jag har ju redan både borstat tänderna och tvättat mina händer! Vad mer begär du av mig!?")
            elif "borstat tänderna" not in inventory:
                print ("På handfatet står en tandborste. Du plockar upp denna och börjar borsta dina tänder. När du är färdig tävttar du dina händer")
                inventory.append("borstat tänderna")

        if handling == "titta under handfat":
            if "tittat under handfat" in inventory:
                print("Du har ju redan frågat dig själv denna frågan!")
            elif "tittat under handfat" not in inventory:
                print("Är du säker ja/nej")
        if förrahandling == "titta under handfat" and handling == "ja":
            print("Du tittar under handfatet och ser att det nu bor en kackerlacksfamilj där. Du Svimmar och slår huvudet i ditt handfat. Du missar tentan.")
            print("spelet är över")
            print ("Vill du spela en gång till? Ja/nej")
        if förrförrahandling == "titta under handfat" and förrahandling == "ja" and handling == "ja":
            loop = "intro"
        if förrförrahandling == "ja" and förrahandling == "ja" and handling =="nej":
            print("det var väl kanske lika bra.")
            inventory.append("tittat under handfat")

                    #Skåp

        if handling == "titta på skåp":
            if "tittat på skåp" in inventory:
                print("Det finns inget mer att se här, du ha ju inte skaffat dig en älskare under de senaste... fem sekundrarna!")
            elif "tittat på skåp" not in inventory:
                print("här fanns det lite damm och mycket plats för en älskares hudvårdsprodukter.....")
                inventory.append("tittat på skåp")

        if handling == "titta under skåp":
            if "tittat under skåp" in inventory:
                print("Det har nog inte hänt något nytt där...")
            elif "tittat under skåp" not in inventory:
                print("Du hittar en kupong för billigare hamburgare på MD donalds, det blir middag idag ändå! Hurra.... !")
                inventory.append("tittat under skåp")
                inventory.append("kupong")

        if handling == "använd skåp":
            if "använt skåp" in inventory:
                print("Du har redan ont i pannan....")
            elif "använt skåp" not in inventory:
                print("Du bankar huvudet långsamt i skåpet i ett försök att förtrycka din tentaångest. Det hälper inte...")
                inventory.append("använt skåp")
        else:
            print('Kommandon: "TITTA PÅ ...", "TITTA UNDER ...", "ANVÄND ...", "GÅ TILL ..."')

    while loop == "hall":
        print("--------------------------------------------------------------------------------------------------")
        print("Du är i hallen men är för stressad för att se något annat än den lockande DÖRREN till utgången.")
        print("--------------------------------------------------------------------------------------------------")
        handling = input()
        handling = handling.lower()
        if "använd dörr" in handling:
            loop = "exit"
        elif "gå till sovrum" in handling:
            loop = "sovrum"
        elif "gå till kök" in handling:
            loop = "kök"
        elif "gå till vardagsrum" in handling:
            loop = "vardagsrum"
        elif "gå till badrum" in handling:
            loop = "badrum"
        else:
            print('Kommandon: "TITTA PÅ ...", "TITTA UNDER ...", "ANVÄND ...", "GÅ TILL ..."')

    while loop == "exit":
        if "byxor" not in inventory:
            print("Du kommer utanför lägenheten men grannen larmar om människa utan byxor till polisen och du åker in i fängelse.")
            print("Du missar tentan, dina vänner överger dig och din familj säger upp kontakten. The end")
            loop = "replay"
        else:
            if "tröja" not in inventory:
                print("Din bara överkropp är för otränad och du blir utskrattad på väg till tentasalen. Du förlorar allt hopp och")
                print("skippar tentan och anställer en PT. Tyvärr så går resten av dina pengar åt att betala räntan på studieskulderna.")
                print("Du har inte råd med gains och svälter ihjäl och dör")
                loop = "replay"

            else:
                if 'id' not in inventory:
                    print('Du glömde ditt leg! Du får inte skriva tentan,\n men du kan iallafall ta dig till eftertenta ölen senare och dränka dina sorger.')
                    loop = 'replay'

                else:
                    if "kaffe" not in inventory:
                        print("Du hann till tentan! Men ditt TV-serie tittande dagen innan har renderat dig utmattad så du somnar på bänken,")
                        print("snarkar högljutt och råkar prutta. Du vaknar och upptäcker en misslyckad tenta och en skrattande kursdeltagare.")
                        loop = "replay"
                    else:
                        if "borstat tänderna" not in inventory:
                            print("Du hinner till tentan och det känns bra. Du kommer förhoppningsvis klara ett G. Men när det är dags")
                            print("för tentaölen flyr dina kurskamrater din andedräkt och säger upp vänskapen med dig. Du bestämmer dig")
                            print("för att skippa skolan och leva resten av ditt liv som en eremit på kebnekaise. På vägen dit blir du")
                            print("dock uppäten av en björn och dör. The end.")
                            loop = "replay"
                        else:
                            if "dejt" in inventory:
                                print("Du hinner till tentan och det känns bra. Du kommer förhoppningsvis klara ett G. Dags att fira!")
                                print("Du har en fantastisk kväll med dina kurskamrater. Dessutom kommer personen som du med på mobilen")
                                print("dit. Det visar sig vara 'the love of your life'. Ni bestämmer er för att gifta er på plats.")
                                print("Detta är den bästa tentaölen i ditt liv. Du känner att allt är som det ska.")
                                print("...")
                                print("Fram till nästa tenta då förstås.")
                                loop = "replay"
                            else:
                                print("Du hinner till tentan och det känns bra. Du kommer förhoppningsvis klara ett G. Dags att fira!")
                                print("Du har en fantastisk kväll med dina kurskamrater och livet går bra nu. Du känner att allt är")
                                print("som det ska. Fram till nästa tenta då förstås.")
                                loop = "replay"


            print("")
    while loop == "replay":
        print("--------------------------------------------------------------------------------------------------")
        handling = input("Vill du spela igen? Ja/Nej\n")
        handling = handling.lower()
        if "ja" in handling:
            inventory = []
            loop = "intro"
        elif "nej" in handling:
            exit()

# ['tröja', 'badrum besökt', 'städad toalett', 'dejt', 'borstat tänderna', 'kaffe', 'ostmacka', 'byxor']

