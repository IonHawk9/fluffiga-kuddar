loop = "intro"
inventory = []
game = True

while loop == "intro":
    print('Välkommen till Tentamorgon! Funktionerna du kan använda är')
    print('"titta på", "titta under," "använd"')
    print('följt av ett objekt som finns i rummet. Ex: "Titta på TVn"')
    print('Du kan också gå till de olika rummen, "sovrum", "vardagsrum", "')
    print('genom att skriva: "gå till" följt av rummets namn. Ex: "gå till sovrummet"')
    loop = "vakna"
while loop == "vakna":
    sängstatus = input("Klockan ringer. Vad vill du göra? Sova, snooza eller vakna?")
    sängstatus = sängstatus.lower()
    print(sängstatus)
    if sängstatus == "sova":
        print("Du försov dig")
        loop = 10
    if sängstatus == "snooza":
        print("Du förlorade tid")
        loop = 10
    if sängstatus == "vakna":
        print("Du går upp")
        loop = 3
    while loop == 3:
        print ("Med bara underkläder går du upp ur sängen.")
        loop = "sovrum"
    while loop == 10:
        print("Looooser!")
        break

while game: 
    while loop == "sovrum":
        print("Du är i sovrummet. Det är stökigt med kläder överallt. Du ser en byrå och en säng")
        handling = input()
        handling = handling.lower()
        if handling == "gå till vardagsrum":
            loop = "vardagsrum"
        if handling == "gå till kök":
            loop = "kök"
        if handling == "titta på byrå":
            print("Full med damm. Du tror att den var mörblå förut men nu är den mer ljusblå. Du tänker att det är modernt och går vidare.")
        if handling == "titta under byrå":
            print("En trasig strumpa. Du borde verkligen slänga den")
        if handling == "använd byrå":
            if "tröja" in inventory:
                print("Den är tom")
            else:
                print("Du öppnar en byrålåda och hittar en t-shirt. Grattis! Du tar på dig den. Luktar lite unket men ingen kommer märka det.")
                inventory.append("tröja")


    while loop == "vardagsrum":
        print("Du är i vardagsrummet. Även här inne är det ganska stökigt, du äcklas lite av dig själv när du ser den två veckor gamla disken du lämnat därinne. Du ser en tv och en soffa.")
        handling = input()
        handling = handling.lower()
        if handling == "gå till sovrum":
            loop = "sovrum"
        if handling == "gå till kök":
            loop = "kök"
        if handling == "gå till hall":
            loop = "hall"
        if handling == "gå till badrum":
            loop = "badrum"
        if handling == "gå till vardagsrum":
            print("Du är redan i vardagsrummet din nöt!")
        if handling == "titta på tv":
            print("Det är en gammal tjocktv som du ärvt av din morfar.")
        if handling == "titta under tv":
            print("Vad ska du hitta under din tv?? Ooh här var den räkningen du letat efter!")
        if handling == "använd tv":
            print("Du sätter dig och ska bara titta en liten stund på tv, bara lite, lite... och där hade det gått ett helt avsnitt, du förlorar tid.")
        if handling == "titta på soffa":
            print("En relativt fräsh soffa om man bortser från den svaga öldoften ifrån en av sovkuddarna.")
        if handling == "titta under soffa":
            if "byxor" in inventory:
                print("Det finns inget där utom damms, massor av damm.")
            else:
                print("Du har hittat dina byxor! Du drar snabbt på dig dem och känner dig stolt över denna bedrift.")
                inventory.append("byxor")
        if handling == "använd soffa":
            print("Du sätter dig i soffan och börjar känna dig sömnig igen. Du lägger ned huvudet en stund. Dock äcklas du av öldoften och ställer dig upp igen.")

    # ________________________________________________

    while loop == 'kök':
        handling = input('\nDu är i köket, som en stressad zombie står du där och glor på din kaffekokare och ditt kylskåp. \n')
        handling = handling.lower()

        #om tiden är slut looser

        if handling == 'gå till vardagsrum':
            loop = 'vardagsrum'
        elif handling == 'gå till hall':
            loop = 'hall'
        elif handling == 'gå till sovrum':
            loop = 'sovrum'
        elif handling == 'gå till badrum':
            loop = 'badrum'


        elif handling == 'titta på kaffekokare':
            print('Många kaffefläckar här.')

        elif handling == 'titta under kaffekokare':
            print('Vad håller du på med?')

        elif handling == 'använd kaffekokare':
            if 'kaffe' in inventory:
                print('Mer kaffe!! Du börjar känna dig lagom speedad!')
                inventory.append('kaffe')
                #print(inventory)

            else:
                print('Du sätter på en kanna och sörplar i dig lite kaffe.')
                inventory.append('kaffe')
                #print (inventory)


        elif handling == 'titta på kylskåp':
            print('Det är vitt med en hel del fettfläckar på, du börjar planera in en städdag.')
            inventory.append('distraherad')  #skulle kanske kunna göra att saker går långsammare??
            #print(inventory)

        elif handling == 'titta under kylskåp':
            print('Du ångrar omedelbart vad du gjort, fett, slem och damm pryder detta lilla utrymme.')
            inventory.append ('äcklad')  #illamående på tentan? t.ex. om 'äcklad' 2-3 ggr i inventory something bad
            #print(inventory)

        elif handling == 'använd kylskåp':
            if 'ostmacka' in inventory:
                print('Här finns då inget ätbart, om du inte räknar mat som snart kommer börja kräla iväg som ätbart...')
                inventory.append('äcklad')
                #print(inventory)
            else:
                print('Du slänger ihop en ostmacka.')
                inventory.append('ostmacka')
                #print(inventory)

