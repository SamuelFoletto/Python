from agenda import add_contact, view_contacts, delete_contacts

def main():
    while True:
        print("Agenda de contatos")
        print("1 - Adiciona contato")
        print('2 - Listar contato')
        print('3 - Remover contatos')
        print('4 - Sair')

        choice = input('Escolha a opção desejada:\n')

        if choice == "1":
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            delete_contacts()
        elif choice == '4':
            break
        else:
            print('Digite uma opção válida!')

if __name__ == '__main__':
    main()