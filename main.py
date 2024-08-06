import random
import os
import importlib.util
from highrise import*
from highrise import BaseBot,Position
from highrise.models import SessionMetadata

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("funcionando")
        await self.highrise.walk_to(Position(16.5 , 16.25 , 19.5 , "FrontRight"))
        
    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} entrou na sala")      

        await self.highrise.send_whisper(user.id,f"[📜]Convite] - [{user.username} Venha visitar o nosso [Bar] e se deliciar com nossas [Bebidas] e com nosso delicioso [Cardápio]")   
        await self.highrise.walk_to(Position(16.5 , 16.25 , 19.5 , "FrontRight"))
        
    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")  

        if        message.startswith("91") or      message.startswith("90") or      message.startswith("89") or             message.startswith("88") or             message.startswith("87") or message.startswith("86"):
            await self.highrise.walk_to(Position(13.5 , 16.25 , 19.5 , "FrontRight"))

        if        message.startswith("78") or      message.startswith("76") or      message.startswith("73") or             message.startswith("71") or             message.startswith("69") or message.startswith("68"):
            await self.highrise.walk_to(Position(17.5 , 16.25, 20.5 , "BackLeft"))

        if        message.startswith("67") or      message.startswith("65") or      message.startswith("63") or             message.startswith("62") or             message.startswith("61") or message.startswith("60"):
            await self.highrise.walk_to(Position(13.5 , 16.25, 23.0 , "FrontRight"))

        if        message.startswith("59") or      message.startswith("64") or      message.startswith("66") or             message.startswith("57") or             message.startswith("55") or message.startswith("54"):
            await self.highrise.walk_to(Position(13.5 , 16.25, 23.0 , "FrontLeft"))

        if        message.startswith("53") or      message.startswith("56") or      message.startswith("50") or             message.startswith("51") or             message.startswith("58") or message.startswith("52"):
            await self.highrise.walk_to(Position(17.5 , 16.25, 19.5 , "BackLeft"))
            
        if        message.startswith("79") or      message.startswith("77") or      message.startswith("75") or             message.startswith("74") or             message.startswith("72") or message.startswith("70"):
            await self.highrise.walk_to(Position(17.5 , 16.25, 19.5 , "FrontLeft"))

        if              message.startswith("Bar") or                                 message.startswith("bar"):
            await self.highrise.send_whisper(user.id,f"[📜]Balcão] - [Seja bem vindo ao nosso bar {user.username} Use: [Bebidas1] ou [Cardápio1] para ver nossa lista de bebidas e petiscos no balcão")
            await self.highrise.send_whisper(user.id,f"[📜]Mesas] - [se preferir ser atendido nas mesas ao lado {user.username} Use: [Bebidas2] ou [Cardápio2] para a nossa grande lista de petiscos nas mesas.")
            await self.highrise.walk_to(Position(16.5 , 16.25 , 19.5 , "FrontRight"))

        if              message.startswith("help") or                                 message.startswith("Help"):
            await self.highrise.send_whisper(user.id,f"[🆘️Mesas] - [ Bebidas2 | Cardápio2") 
            await self.highrise.send_whisper(user.id,f"[🆘️Balcão] - [Bebidas1 | Cardápio1]")
            
            
        if        message.startswith("85") or      message.startswith("84") or      message.startswith("83") or             message.startswith("82") or             message.startswith("81") or message.startswith("80"):
            await self.highrise.walk_to(Position(14.5 , 16.25 , 17.5 , "FrontRight"))
            
        if        message.startswith("😡") or      message.startswith("🤬") or      message.startswith("😤") or             message.startswith("🤨") or             message.startswith("😒") or message.startswith("🙄"):
            await self.highrise.send_emote("emote-boxer",user.id)
            await self.highrise.walk_to(Position(15.0 , 16.35 , 27.0 , "FrontRight"))
   
        if        message.startswith("🤔") or      message.startswith("🧐") or      message.startswith("🥸") or             message.startswith("🫤") or message.startswith("😕"):
            await self.highrise.send_emote("emote-confused",user.id)
            await self.highrise.walk_to(Position(17.5 , 16.25, 19.5 , "FrontLeft"))

        if        message.startswith("🤣") or      message.startswith("😂") or        message.startswith("jw") or        message.startswith("Jw") or      message.startswith("K") or      message.startswith("Js") or       message.startswith("k") or         message.startswith("js") or    message.startswith("jd") or           message.startswith("ja") or             message.startswith("Ha") or         message.startswith("Ka") or           message.startswith("Ja") or           message.startswith("ha") or          message.startswith("ks") or             message.startswith("kk") or             message.startswith("Kk") or message.startswith("😁") or message.startswith("😀"):
            await self.highrise.send_emote("emote-laughing",user.id)
            
        if        message.startswith("😗") or      message.startswith("😘") or      message.startswith("😙") or             message.startswith("💋") or       message.startswith("Bj") or          message.startswith("bjs") or         message.startswith("Te Amu") or      message.startswith("te amu") or      message.startswith("Te amo") or      message.startswith("te amo") or     message.startswith("beijos") or    message.startswith("Bjs") or   message.startswith("bj") or            message.startswith("😚"):
            await self.highrise.send_emote("emote-kiss",user.id)
            await self.highrise.walk_to(Position(13.5 , 16.35 ,26.0 , "BackLeft"))
        
        if        message.startswith("😊") or      message.startswith("🥰") or      message.startswith("😳") or message.startswith("🤗"):
            await self.highrise.send_emote("idle-uwu",user.id)
            await self.highrise.walk_to(Position(13.5 , 16.35 ,26.0 , "BackLeft"))

        if        message.startswith("🤢") or      message.startswith("🤮") or      message.startswith("🤧") or             message.startswith("😵‍💫") or message.startswith("🤒"):
            await self.highrise.send_emote("emoji-gagging",user.id)
            await self.highrise.walk_to(Position(14.5 , 16.25 , 17.5 , "FrontRight"))

        if        message.startswith("😱") or      message.startswith("😬") or      message.startswith("😰") or             message.startswith("😫") or message.startswith("😨"):
            await self.highrise.send_emote("idle-nervous",user.id)

        if message.startswith("🤯"):
            await self.highrise.send_emote("emote-headblowup",user.id)

        if        message.startswith("😭") or      message.startswith("😔") or      message.startswith("😮‍💨") or             message.startswith("😞") or             message.startswith("😓") or message.startswith("😖"):
            await self.highrise.send_emote("emote-sad",user.id)
            await self.highrise.walk_to(Position(17.5 , 16.25, 19.5 , "FrontLeft"))

        if        message.startswith("☺️") or      message.startswith("🫣") or       message.startswith("😍") or      message.startswith("🥺") or message.startswith("🥹"):
            await self.highrise.send_emote("emote-shy2",user.id)

        if        message.startswith("😏") or     message.startswith("🙃") or     message.startswith("🤤") or     message.startswith("😋") or     message.startswith("😏") or message.startswith("😈"):
            await self.highrise.send_emote("emote-lust",user.id)           

        if        message.startswith("🥵") or message.startswith("🫠"):
            await self.highrise.send_emote("emote-hot",user.id)
                   
        
        if              message.startswith("cardapio2") or    message.startswith("Cardápio2") or    message.startswith("cardápio2") or                              message.startswith("CARDAPIO2") or       message.startswith("Cardapio2"):
          await self.highrise.walk_to(Position(16.0 , 16.25 , 26.5, "BackRight"))
          await self.highrise.send_whisper(user.id,f"[📜] - [Ola {user.username} Gostaria de dar uma olhada no cardápio do bar?]")

        if              message.startswith("cardapio1") or    message.startswith("Cardápio1") or    message.startswith("cardápio") or                              message.startswith("CARDAPIO1") or       message.startswith("Cardapio1"):
          await self.highrise.walk_to(Position(16.5 , 16.25 , 19.5 , "FrontLeft"))
          await self.highrise.send_whisper(user.id,f"[📜] - [Ola {user.username} Gostaria de dar uma olhada no cardápio do bar?]")

        if              message.startswith("bebidas2") or                              message.startswith("Bebidas2") or       message.startswith("BEBIDAS2"):
            await self.highrise.walk_to(Position(16.0 , 16.25 , 26.5, "BackLeft"))
            await self.highrise.send_whisper(user.id,"[🔞]Cardapio] - [Tequila | Gim | Vinho | Vodka | Whisky | Rum | Champanhe | Cachaça | Conhaque | Cerveja | Corote | Red bull | Catuaba]")
            await self.highrise.send_whisper(user.id,"[✅️]Cardapio] - [ Coca cola | Suco | Agua | Milk Shake | Café | Chá | Sukita | Pepsi | Fanta | Sprite]")
            await self.highrise.send_whisper(user.id,"[🍼]Cardapio] - [ Toddynho | Leite | Nescau | Nesquik]")
                                                 
        if              message.startswith("bebidas1") or                              message.startswith("Bebidas1") or       message.startswith("BEBIDAS1"):
            await self.highrise.walk_to(Position(16.5 , 16.25 , 19.5 , "FrontLeft"))
            await self.highrise.send_whisper(user.id,"[🔞]Cardapio] - [Tequila | Gim | Vinho | Vodka | Whisky | Rum | Champanhe | Cachaça | Conhaque | Cerveja | Corote | Red bull | Catuaba]")
            await self.highrise.send_whisper(user.id,"[✅️]Cardapio] - [ Coca cola | Suco | Agua | Milk Shake | Café | Chá | Sukita | Pepsi | Fanta | Sprite]")
            await self.highrise.send_whisper(user.id,"[🍼]Cardapio] - [ Toddynho | Leite | Nescau | Nesquik]")
            
        if              message.startswith("sprite") or                                 message.startswith("Sprite"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está sua deliciosa sprite 🍋🧊 ")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")
   
        if              message.startswith("Nesquik") or                                 message.startswith("nesquik"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está seu docê nesquik 🥛🍓")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("Red bull") or                                 message.startswith("red bull"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está seu red bull 🥫🐂 ")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("nescau") or                                 message.startswith("Nescau"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está seu delicioso nescau 🍫🥛")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("fanta") or                                 message.startswith("Fanta"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está sua deliciosa fanta gelada 🍊🧃 ")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")
            
        if              message.startswith("catuaba") or                                 message.startswith("Catuaba"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está sua deliciosa catuaba 🍹 ")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("milk Shake") or                                 message.startswith("Milk Shake"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está seu delicioso Milk Shake 🍨🧊")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("Toddynho") or                                 message.startswith("toddynho"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está seu delicioso toddynho 🧃🍫 ")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("Sukita") or                                 message.startswith("sukita"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está sua deliciosa sukita gelada 🥤🧊")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("leite") or                                 message.startswith("Leite"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está seu  leite 🥛")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("Pepsi") or                                 message.startswith("pepsi"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está sua deliciosa pepsi gelada 🧊🥤 ")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("Chá") or                                 message.startswith("chá"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está seu delicioso chá 🫖🍵 ")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("café") or                                 message.startswith("Café"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está seu delicioso café quente ☕️ ")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")
            
        if              message.startswith("coca cola") or                                 message.startswith("Coca cola"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está sua deliciosa coca cola gelada 🧊🥤 ")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("Agua") or                                 message.startswith("agua"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está sua deliciosa agua gelada 🧊🥤 ")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")
          
        if              message.startswith("suco") or                                 message.startswith("Suco"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está seu delicioso suco natural 🧃")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("corote") or                                 message.startswith("Corote"):
            await self.highrise.send_whisper(user.id,f"{user.username} Aqui está seu corotinho. 🫙")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")
          
        if              message.startswith("Tequila") or                                 message.startswith("tequila"):
            await self.highrise.send_whisper(user.id,f"{user.username} se deliciando na Tequila 😄🥃")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")
          
        if              message.startswith("gim") or                                 message.startswith("Gim"):
            await self.highrise.send_whisper(user.id,f"vira vira todo o gim {user.username} 🥃")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("conhaque") or                                 message.startswith("Conhaque"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu conhaque {user.username} 🥃🥃")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("whisky") or                                 message.startswith("Whisky"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está seu Whisky  {user.username} 🥃")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("rum") or                                 message.startswith("Rum"):
            await self.highrise.send_whisper(user.id,f"Aqui Está seu Rum 🥃 {user.username}")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")
          
        if              message.startswith("Cachaça") or                                 message.startswith("cachaça"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está a Sua Cachaça {user.username} não beba muito 🥃")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")
            
        if              message.startswith("vodka") or                                 message.startswith("Vodka"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua  Vodka 🥃 {user.username} ")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")
            
        if              message.startswith("champanhe") or                                 message.startswith("Champanhe"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Champanhe {user.username} 🍾🥂")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("cerveja") or                                 message.startswith("Cerveja"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Cerveja {user.username} 🍺")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("vinho") or                                 message.startswith("Vinho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Vinho 🍷 {user.username}")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais alguma bebida {user.username}?]")

        if              message.startswith("OBG") or        message.startswith("Obg") or        message.startswith("obg") or                           message.startswith("obrigada") or     message.startswith("Obrigada") or     message.startswith("brigado") or     message.startswith("brigada") or      message.startswith("Brigado") or      message.startswith("Brigada") or     message.startswith("obrigado") or        message.startswith("Obrigado"):
            await self.highrise.send_whisper(user.id,f"[☺️] de nada {user.username} fico feliz que tenha gostado do atendimento. 🫶🏻")
            await self.highrise.send_emote("emote-kiss") 
            await self.highrise.react("heart",user.id)
            await self.highrise.react("heart",user.id)
            
        if              message.startswith("sim") or        message.startswith("sim") or        message.startswith("Sim") or                           message.startswith("Sim") or       message.startswith("SIM"):
            await self.highrise.send_whisper(user.id,f"[✅️]Cardapio] - [Camarão | Salada de alface | Salada de repolho | Macarrão | Pizza | Bolo de cenoura | Sanduíche | Bombom | Bolo de morango | Açai | | Sorvete | Cupcake | Batata frita | Espetinho | pão de alho | Torta | Pudim]")

        if              message.startswith("bombom") or                              message.startswith("Bombom") or       message.startswith("BOMBOM"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está seu delicioso bombom 🍬 ")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")

        if              message.startswith("pizza") or                              message.startswith("Pizza") or       message.startswith("PIZZA"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está sua deliciosa pizza 🍕")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")
            
        if              message.startswith("bolo de morango") or                              message.startswith("Bolo de morango") or       message.startswith("BOLO DE MORANGO"):
            await self.highrise.send_whisper(user.id,f"Aqui Está seu Delicioso Bolo de Morango {user.username} 🍰")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")
            
        if              message.startswith("salada de repolho") or                              message.startswith("Salada de repolho") or       message.startswith("SALADA DE REPOLHO"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Deliciosa salada de repolho {user.username} 🥬🥬")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")
        if              message.startswith("camarão") or                              message.startswith("Camarão") or       message.startswith("CAMARÃO"):  
            await self.highrise.send_whisper(user.id,f"🍤Aqui Está seu Delicoso Camarão 🍤 {user.username} 🍤")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")
            
        if              message.startswith("macarrão") or                              message.startswith("Macarrão") or       message.startswith("MACARRÃO"):
            await self.highrise.send_whisper(user.id,f"Aqui Está seu macarrão {user.username} aproveite 🍜🍝")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")
            
        if              message.startswith("salada de alface") or                              message.startswith("salada de alface") or       message.startswith("SALADA DE ALFACE"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está a Sua salada de alface {user.username} com um pouco de tomates por cima 🥬🥗")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")

        if              message.startswith("bolo de cenoura") or                              message.startswith("Bolo de cenoura") or       message.startswith("BOLO DE CENOURA"):  
            await self.highrise.send_whisper(user.id,f"aqui está seu bolo de cenoura  {user.username} 🥕🥮")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")
           
        if              message.startswith("AÇAI") or                              message.startswith("Açai") or     message.startswith("açaí") or     message.startswith("Açaí") or       message.startswith("açai"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Açai {user.username} 🍨 Aproveite")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")

        if              message.startswith("não") or                              message.startswith("Não") or         message.startswith("nao") or      message.startswith("Nao") or       message.startswith("NÃO"):
            await self.highrise.walk_to(Position(16.5 , 16.25 , 19.5 , "FrontRight"))
            await self.highrise.send_whisper(user.id,f"{user.username} se prescisar me chame novamente. 😊🫶🏻")
            await self.highrise.walk_to(Position(16.5 , 16.25 , 19.5 , "FrontLeft"))
            
        if              message.startswith("sorvete") or                             message.startswith("Sorvete"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu sorvete {user.username} 🍦🍨")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")
            
        if              message.startswith("pão de alho") or                              message.startswith("Pão de alho") or       message.startswith("PÃO DE ALHO"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua pão de alho {user.username} 🥖🧄")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")

        if              message.startswith("batata frita") or                              message.startswith("Batata frita") or       message.startswith("BATATA FRITA"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Batata Frita {user.username} aproveite 🍟")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")

        if              message.startswith("espetinho") or                              message.startswith("Espetinho") or       message.startswith("ESPETINHO"):
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Espetinho {user.username} 🍢🍢")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")

        if              message.startswith("cupcake") or                              message.startswith("Cupcake") or       message.startswith("CUPCAKE"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu cupcake {user.username} 🧁")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")

        if              message.startswith("Sanduíche") or                              message.startswith("Sanduíche") or       message.startswith("sanduíche"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu sanduíche {user.username} 🥪")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")

        if              message.startswith("PUDIM") or                              message.startswith("Pudim") or       message.startswith("pudim"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu pudim {user.username} 🍮")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")
            
        if              message.startswith("torta") or                              message.startswith("Torta") or       message.startswith("TORTA"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua deliciosa torta {user.username} 🥮")
            await self.highrise.send_emote("emoji-thumbsup")  
            await self.highrise.send_whisper(user.id,f"[📜] - [deseja mais algum petisco {user.username}?]")
