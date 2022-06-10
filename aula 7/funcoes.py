class Cadastro():
    # salvar dados do login
    def dados_login(entry1, entry2):
        global armazenar_nome
        armazenar_nome = entry1.get()
        global armazenar_senha
        armazenar_senha = entry2.get()

    # mostrar a senha
    def mostrar_senha(variavel, entry):
        if (variavel.get() == 1):
            entry.config(show='')
        else:
            entry.config(show='*')


   