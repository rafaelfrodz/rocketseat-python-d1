contatos = []

def adicionar_contato(contatos, 
                      nome_contato, 
                      telefone_contato, 
                      email_contato, 
                      favorito_contato):
    contato = {
        "nome":nome_contato.capitalize(),
        "telefone":telefone_contato,
        "email":email_contato,
        "favorito": True if favorito_contato == "1" else False
    }
    contatos.append(contato)
    print(f"O contato {contato['nome']} foi adicionado!")
    print(contatos)
def ver_contatos(contatos):
    print("\nLista de contatos:")
    for index, contato in enumerate(contatos):
        print(f"{index+1}. Nome: {contato["nome"]}, Tel: {contato["telefone"]}, E-mail: {contato["email"]}, Favorito: {"Sim" if favorito_contato else "Não"} ")
    return
def ver_contatos_favoritos(contatos):
    contatos_favoritos = []
    for contato in contatos:
        if contato["favorito"]:
            contatos_favoritos.append(contato)
    if len(contatos_favoritos) > 0:
        for index, contato in enumerate(contatos_favoritos):
            print(f"{index+1}. Nome: {contato["nome"]}, Tel: {contato["telefone"]}, E-mail: {contato["email"]} ")
    else:
        print("Você não tem nenhum contato favoritado!")                  
    return           
def editar_contato(contatos, index, opcao, novo_dado):
    index = int(index)-1
    if opcao == "1":
        nome_antigo = contatos[index]["nome"]
        contatos[index]["nome"] = novo_dado.capitalize()
        print(f"\nO nome do contato {nome_antigo} foi atualizado para {contatos[index]["nome"]}!")
    elif opcao == "2":
        telefone_antigo = contatos[index]["telefone"]
        contatos[index]["telefone"] = novo_dado
        print(f"\nO telefone {telefone_antigo} foi atualizado para {contatos[index]["telefone"]}!")
    elif opcao == "3":
        email_antigo = contatos[index]["email"]
        contatos[index]["email"] = novo_dado
        print(f"\nO e-mail {email_antigo} foi atualizado para {contatos[index]["email"]}!")
    else:
        print("Escolha invalida!")
    return   
def favoritar_desavoritar(contatos, index, opcao):
    index = int(index)-1
    if opcao == "1":
        contatos[index]["favorito"] = True
        print(f"O contato {index}. {contatos[index]["nome"]} foi favoritado!")
    elif opcao == "2":
        contatos[index]["favorito"] = False
        print(f"O contato {index+1}. {contatos[index]["nome"]} foi desfavoritado!")
    else:
        print("Escolha invalida!")
def deletar_contato(contatos, index):
    index = int(index)-1
    contato_antigo = contatos[index]["nome"]
    contatos.remove(contatos[index])
    print(f"Contato {index+1}. {contato_antigo} deletado!")
        
    
            
    

while True: 
    print("\nMenu do Gerenciador de contatos:")
    print("\n1. Adicionar novo contato")
    print("2. Visualizar a lista de contatos")
    print("3. Visualizar a lista de contatos favoritos")
    print("4. Editar um contato")
    print("5. Marcar/Desmarcar um contato como favorito")
    print("6. Apagar um contato")
    print("7. Sair do programa")
    
    escolha = input("\nDigite a sua escolha: ")
    if escolha == "1":
        nome_contato = input("\nQual o nome do contato? ")
        telefone_contato = input("Qual o número de contato? ")
        email_contato = input("Qual o endereço de email de contato? ")
        favorito_contato = input("Deseja registrar o contato como favorito? 1-Sim | 2-Não ")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato, favorito_contato)
    elif escolha == "2":
        if len(contatos) > 0:
            ver_contatos(contatos)
        else:
            print("\nLista de contatos vazia!")
    elif escolha == "3":
        if len(contatos) > 0:
            ver_contatos_favoritos(contatos)
        else:
            print("\nLista de contatos vazia!")
    elif escolha == "4":
        if len(contatos) > 0:
            ver_contatos(contatos)
            index = input("Qual o index do contato que você deseja alterar? ")
            if len(contatos) >= int(index):
                while True:
                    print("\nQual dado você deseja alterar?")
                    print("\n1. Nome do contato")
                    print("2. Telefone do contato")
                    print("3. E-mail do contato")
                    print("4. Voltar para o menu inicial")
                    escolha_4 = input("/nDigite a sua escolha: ")
                    if escolha_4 == "1":
                        novo_nome = input("\nDigite o novo nome do contato: ")
                        editar_contato(contatos, index, escolha_4, novo_nome)
                    if escolha_4 == "2":
                        novo_telefone = input("\nDigite o novo telfone do contato: ")
                        editar_contato(contatos, index, escolha_4, novo_telefone)
                    if escolha_4 == "3":
                        novo_email = input("\nDigite o novo e-mail do contato: ")
                        editar_contato(contatos, index, escolha_4, novo_email)
                    if escolha == "4":
                        break
        else:
            print("\nLista de contatos vazia!")
    elif escolha == "5":
        if len(contatos) > 0:
            ver_contatos(contatos)
            index = input("\nQual o index do contato que você deseja favoritar/desfavoritar? ")
            escolha_5 = input("\n1-Para favoritar | 2-Para desfavoritar: ")
            favoritar_desavoritar(contatos, index, escolha_5)
        else:
            print("\nLista de contatos vazia!")
    elif escolha == "6":
        if len(contatos) > 0:
            ver_contatos(contatos)
            index = input("\nQual o index do contato que você deseja deletar? ")
            deletar_contato(contatos, index)
        else:
            print("\nLista de contatos vazia!")
        
            
    elif escolha == "7":
        break