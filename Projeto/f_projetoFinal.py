import json
import matplotlib.pyplot as plt
import PySimpleGUI as sg
sg.theme('LightGreen1')

#-------------------------------------------------FUNÇÕES AUXILIARES------------------------------------------------------ 
def ordenaTitulo(lista):
    lista_ordenada = sorted(lista, key=lambda d: d.get('title',d.get('publish_date', '')))
    return lista_ordenada

def ordenaData(lista):
    lista_ordenada = sorted(lista, key=lambda d: d.get('publish_date', d.get('title', '')))
    return lista_ordenada

def topordena(par):
    return par[1]

def salvar_em_arquivo(output, nome_arquivo):
    if nome_arquivo[-5:]!='.json':
        nome_arquivo+='.json'
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    sg.popup(f"Dados salvos em '{nome_arquivo}'.")

def salvar_em_arquivo_comandos(output, nome_arquivo):
    if nome_arquivo[-5:]!='.json':
        nome_arquivo+='.json'
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    print(f"Dados salvos em '{nome_arquivo}'.")

def popup_salvar(lista):
    layout_salvar = [[sg.Text('Desejas salvar a pesquisa?')],
                    [sg.Button('Sim', size=(15, 1), key='~SIM~'), sg.Button('Não', size=(15, 1), key='~NAO~')]]
    window_salvar = sg.Window('Salvar Pesquisa', layout_salvar, modal = True)
    stp = False
    while not stp:
        e,_ = window_salvar.read()
        if e == '~SIM~':
            nome_arquivo = sg.popup_get_text('Insere o nome do arquivo (ex.:pesquisa.json)', title='Nome do Arquivo', size=(15, 1), font='Helvetica')      
            if nome_arquivo:
                salvar_em_arquivo(lista, nome_arquivo)
                window_salvar.close()
                stp = True
                
            else:
                sg.popup('Insira um nome para o arquivo', title='Erro', font= "Helvetica")
        elif e in ('~NAO~',sg.WINDOW_CLOSED) :
            sg.popup('Operação cancelada.', title='Cancelado')
            window_salvar.close()
            stp = True
            

def criar_help_window_criar():
    help_texto = (
        'Funcionamento da Janela de Criar Publicação:\n\n'
        '- Para criar uma nova publicação, é necessário preencher os campos desta janela, o título é obrigatório, já os restantes campos são arbitrários.\n'
        '- Após introduzir os dados de um autor, o utilizador deve clicar no botão "Adicionar Autor" para adicionar o autor à lista de autores da publicação.\n'
        '- Quando os campos pretendidos estiverem preenchidos, o utilizador deve clicar no botão "OK" para adicionar a publicação à base de dados.\n'
        '- A publicação poderá ser observada no lado direito da janela após ser criada e será automaticamente adicionada ao dataset em memória.\n'
        '- O botão "Help" abre esta janela de ajuda.\n'
        '- O botão "Cancel" fecha a janela sem criar a publicação.\n'
    )
    layout = [[sg.Text(help_texto, font=('Helvetica', 10), size=(80, None))], [sg.Button('Fechar', key='~FECHAR~')]]

    return sg.Window('Help', layout, modal=True)

#------------------------------------------------------EXIBIR PUBLICAÇÕES--------------------------------------------------------

def mostrar_publi(bd):
    if bd is None:
        return
    info_total = ''
    for publi in bd:
        title=publi.get('title', 'Não Existe')[:100]
        publish_date=publi.get('publish_date', 'Não Existe')
        abstract=publi.get('abstract', 'Não Existe')[:100]
        keywords=publi.get('keywords', 'Não Existe')[:100]
        doi = publi.get('doi', 'Não Existe')
        pdf = publi.get('pdf', 'Não Existe')
        url = publi.get('url', 'Não Existe')
        authors= ''
        for autor in publi.get('authors', []):
            name = autor.get('name', 'Não Existe')
            affiliation = autor.get('affiliation', 'Não Existe')
            orcid = autor.get('orcid', 'Não Existe')
            authors += f'Autor: {name}\nAffiliation: {affiliation}\nOrcid: {orcid}\n\n'
        info_total += f'''Abstract: {abstract}\n
KeyWords: {keywords}\n
{authors}
Doi: {doi}\n
Pdf: {pdf}\n
Publish Date: {publish_date}\n
Title: {title}\n
Url: {url}\n

-------------------------------------------------------\n'''
    return info_total

#------------------------------------------------------CRIAR PUBLICAÇÃO--------------------------------------------------------
def criar_publi(bd):
    publi = {}
    authors = []
    keywords = []
    lista = []
    full_date1 = []

    layout_esquerda = [[sg.Text('Criar publicação', font='Helvetica')],
           [sg.Text('Abstract:',font='Helvetica'), sg.Input(key='-ABSTRACT-')],
           [sg.Text('Keywords:', font='Helvetica'), sg.Input(key='-KEYWORD-'), sg.Button('Adicionar Keyword', key='-ADD-KEYWORD-')],
           [sg.Listbox(values=[], size=(30, 4), key='-KEYWORD-LIST-', enable_events=True, horizontal_scroll=True)],
           [sg.Text('Authors:', font='Helvetica')],
           [sg.Text('Name:', font='Helvetica'), sg.Input(key='-AUTHOR-NAME-')],
           [sg.Text('Affiliation:', font='Helvetica'), sg.Input(key='-AUTHOR-AFFILIATION-')],
           [sg.Text('Orcid:', font='Helvetica'), sg.Input(key='-AUTHOR-ORCID-')],
           [sg.Button('Adicionar Autor', key='-ADD-AUTHOR-')],
           [sg.Listbox(values=[], size=(30, 4), key='-AUTHOR-LIST-', enable_events=True, horizontal_scroll=True)],
           [sg.Text('Doi:',font='Helvetica'), sg.Input(key='-DOI-')],
           [sg.Text('Pdf:',font='Helvetica'), sg.Input(key='-PDF-')],
           [sg.Text('Publish date (AAAA-MM-DD):', font='Helvetica'), sg.Button('Adicionar Data', key='-ADD-DATE-')],
           [sg.Text('Title:',font='Helvetica'), sg.Input(key='-TITLE-')],
           [sg.Text('Url:',font='Helvetica'), sg.Input(key='-URL-')],
           [sg.Button('Help', key='-HELP-'),sg.OK(key = '-OK-'), sg.Cancel(key='-CANCEL-')] ]   
    results_layout = [[sg.Text('Publicação criada:', font='Helvetica')],
                      [sg.Multiline(size=(60, 30), key='-RESULTS-')]]  
    layout = [[
            sg.Column(layout_esquerda, element_justification='left', vertical_alignment='top'),
            sg.VSeparator(),
            sg.Column(results_layout, element_justification='left', vertical_alignment='top')
        ]
    ]

    window = sg.Window('Criar Publicação', layout, modal = True)
    
    stop = False
    while stop == False:
        e, v = window.read()
        if e in [sg.WINDOW_CLOSED, '-CANCEL-']:
            sg.popup("Janela fechada.", title="Aviso")
            stop = True
            window.close()

        elif e == '-HELP-':
            help_window = criar_help_window_criar()
            stp = False
            while not stp:
                help_event, _ = help_window.read()
                if help_event in (sg.WINDOW_CLOSED, '~FECHAR~'):
                    help_window.close()
                    stp = True

        elif e == '-ADD-AUTHOR-':
            name = v['-AUTHOR-NAME-'].strip()
            affiliation = v['-AUTHOR-AFFILIATION-'].strip()
            orcid = v['-AUTHOR-ORCID-'].strip()
            if name and affiliation:
                authors.append({"name": name, "affiliation": affiliation, "orcid": orcid})
                window['-AUTHOR-LIST-'].update(values=[f"{author['name']} | {author['affiliation']} | {author['orcid']}" for author in authors])
                window['-AUTHOR-NAME-'].update('')
                window['-AUTHOR-AFFILIATION-'].update('')
                window['-AUTHOR-ORCID-'].update('')
            else:
                sg.popup('É necessário introduzir nome e affiliation.', title='Input Error')
        
        elif e == '-ADD-DATE-':
            coluna_ano = [[sg.Text('Ano (ex.:2025):', font='Helvetica')], [sg.Input(key='-ANO-', size=(20, 1))]]
            coluna_mes = [[sg.Text('Mês (ex.:01):', font='Helvetica')], [sg.Input(key='-MES-', size=(20, 1))]]
            coluna_dia = [[sg.Text('Dia (ex.:28)', font='Helvetica')], [sg.Input(key='-DIA-', size=(20, 1))]]
            layout_data = [
                [sg.Text('Adicionar Data', font=('Helvetica', 14, 'bold'))],
                [sg.Column(coluna_ano, element_justification='center'),
                 sg.Column(coluna_mes, element_justification='center'),
                 sg.Column(coluna_dia, element_justification='center')],
                [sg.Button('OK', key='-OK-DATE-'), sg.Button('Sair', key='-CANCEL-DATE-')]
            ]

            window_data = sg.Window('Adicionar Data', layout_data, modal=True)
            date_stop = False
            while not date_stop:
                date_event, date_values = window_data.read()
                if date_event in (sg.WINDOW_CLOSED, '-CANCEL-DATE-'):
                    date_stop = True
                    window_data.close()
                elif date_event == '-OK-DATE-':
                    ano = date_values['-ANO-'].strip()
                    mes = date_values['-MES-'].strip()
                    dia = date_values['-DIA-'].strip()
                    if ano and mes and dia:
                        if len(ano) == 4 and len(mes) == 2 and len(dia) == 2: 
                            full_date = f"{ano}-{mes}-{dia}"
                            full_date1.append(full_date) 
                            date_stop = True
                            window_data.close()
                        else:
                            sg.popup("Data inserida incorretamente. Por favor, insira a data no formato AAAA-MM-DD.", title="Erro")
                    else:
                        sg.popup("Por favor, preencha todos os campos (Ano, Mês, Dia).", title="Erro")


        elif e == '-ADD-KEYWORD-':
            keyword = v['-KEYWORD-'].strip()
            if keyword:
                keywords.append(keyword)
                window['-KEYWORD-LIST-'].update(values=keywords)
                window['-KEYWORD-'].update('')
            else:
                sg.popup('É necessário introduzir uma keyword.', title='Input Error')
        elif e == '-OK-':
            if not v['-TITLE-']:
                sg.popup("Título é obrigatório.", title="Erro")
            else:
                x = len(full_date1)
                publi = {
                    "abstract": v['-ABSTRACT-'],
                    "keywords": ", ".join(keywords),
                    "publish_date": full_date1[x-1] if full_date1 else '',
                    "doi": v['-DOI-'],
                    "title": v['-TITLE-'],
                    "url": v['-URL-'],
                    "pdf": v['-PDF-'],
                    "authors": authors
                }        
                bd.append(publi)
                lista.append(publi)
                sg.popup('Publicação criada com sucesso!', title='Sucesso')
                window['-RESULTS-'].update(mostrar_publi(lista))
                window['-ABSTRACT-'].update('')
                window['-KEYWORD-'].update('')
                window['-AUTHOR-NAME-'].update('')
                window['-AUTHOR-AFFILIATION-'].update('')
                window['-AUTHOR-ORCID-'].update('')
                window['-AUTHOR-LIST-'].update(values=[])
                window['-DOI-'].update('')
                window['-PDF-'].update('')
                window['-TITLE-'].update('')
                window['-URL-'].update('')
                window['-KEYWORD-LIST-'].update(values=[])
                authors = []
                keywords = ""
                full_date = ""
    return bd


#------------------------------------------------------ELIMINAR PUBLICAÇÕES--------------------------------------------------------
def eliminar_publi(bd):
    lista = []
    # 1) Procurar a publicação a eliminar pelo título
    layout = [ [sg.Text('Título a procurar:')],
           [sg.Input(key='-TITULO-')],
           [sg.OK(), sg.Cancel(key='-CANCEL-')] ]
    window = sg.Window('Procurar por Título', layout, modal = True)

    stop = False
    while not stop:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, '-CANCEL-'):
            sg.popup("Operação cancelada.", title="Aviso")
            stop = True
            window.close()
        elif not values['-TITULO-'].strip():
            sg.popup("Nenhum título inserido.", title="Aviso")
        else:
            titulo = values['-TITULO-'].strip()
            stop = True
            window.close()


            for publi in bd:
                if titulo.lower() in publi.get("title", '').lower():
                    lista.append(publi)
                
            if lista != []:
                if len(lista) > 1:
                    layout_escolha = [[sg.Text('Escolha a publicação a eliminar:')],
                                      [sg.Listbox(values=[f"Título: {publi['title']}" for publi in lista], size=(80, 10), key='-ESCOLHA-', horizontal_scroll=True)],
                                      [sg.OK(), sg.Cancel(key='-CANCEL-')]]
                    window_escolha = sg.Window('Escolher Publicação', layout_escolha, modal=True)
                    escolha = None
                    stop = False
                    while not stop:
                        ev, vals = window_escolha.read()
                        if ev in (sg.WINDOW_CLOSED, '-CANCEL-'):
                            sg.popup("Operação cancelada.", title="Aviso")
                            window_escolha.close()
                            stop = True
                        elif ev == 'OK' and vals['-ESCOLHA-']:
                            escolha = vals['-ESCOLHA-'][0]
                            window_escolha.close()
                            stop = True
                        else:
                            sg.popup("Nenhuma publicação selecionada.", title="Aviso")

                    if escolha:
                        for publi in lista:
                            if f"Título: {publi['title']}" == escolha:
                                lista = [publi]
                            else: None

                        layout_esquerda = [[sg.Text('Publicação a eliminar:')],
                            [sg.Text(f'{mostrar_publi(lista)}', font = ('Helvetica', 10))]]
                        layout_direita = [[sg.Text("Tem a certeza de que quer eliminar esta publicação?")],
                                    [sg.Button("Sim", key='-SIM-'), sg.Button("Não", key='-NAO-')]]
                        layout_el = [
                        [
                            sg.Column(layout_esquerda, element_justification='left', vertical_alignment='top', size = (800,600), scrollable=True),
                            sg.VSeparator(),
                            sg.Column(layout_direita, element_justification='left', vertical_alignment='top')
                        ]
                    ]
                        window_el = sg.Window("Eliminar Publicação", layout_el, modal = True)
                        st = False
                        while not st:
                            e, _ = window_el.read()
                            if e in (sg.WINDOW_CLOSED, '-NAO-'):
                                sg.popup("Operação cancelada.", title="Aviso")
                                st = True
                                window_el.close()
                            elif e == '-SIM-':
                                bd.remove(publi)
                                st = True
                                sg.popup('Publicação eliminada com sucesso')
                                window_el.close()
                        stop = True
                        window.close()

            else:
                sg.popup("Nenhuma publicação encontrada.", title='Aviso')
        
    return bd


#-----------------------------------------IMPORTAR FICHEIRO------------------------------------
def carregar_dataset(ficheiro):
    dados = []
    try:
        with open(ficheiro, encoding="utf-8") as f:
            dados = json.load(f)
        sg.popup(f'Dataset carregado!\nForam lidos {len(dados)} registos.',
                 title='Sucesso', font=('Helvetica', 20))
    except Exception as e:
        sg.popup(f'Erro ao carregar o dataset: {e}', title='Erro')
        
    return dados


#--------------------------------------FUNÇÕES DE PROCURA-----------------------------------

def procurar_autores(bd):
    lista = []
    layout = [ [sg.Text('Nome do Autor:')],
           [sg.Input(key='-AUTHOR-')],
           [sg.OK(), sg.Cancel()] ]
    window = sg.Window('Procurar por Autor', layout, modal = True)

    stop = False
    while not stop:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'Cancel') or not values['-AUTHOR-'].strip():
            sg.popup("Operação cancelada ou nenhum autor inserido.", title="Aviso")
            stop = True
            window.close()

        if event == 'OK' and values['-AUTHOR-']:
            autor = values['-AUTHOR-'].strip()

            for publi in bd:
                for author in publi["authors"]:
                    if autor.lower() in author["name"].lower():
                        lista.append(publi)
            stop = True
            window.close()

    # Popup para Ordenar            
    if lista != []:
        layout_ordenar = [[sg.Text('Ordenar por:')],
                        [sg.Button('Título', size=(15, 1), key='~TITULO~'), sg.Button('Data', size=(15, 1), key='~DATA~')]]
        window_ordenar = sg.Window('Ordenar Lista', layout_ordenar, modal = True)
        s = False
        while not s:
            ev,_ = window_ordenar.read()
            if ev == sg.WINDOW_CLOSED:
                sg.popup('Operação cancelada.', title='Cancelado')
                window_ordenar.close()
                s = True    
            elif ev == '~TITULO~':
                lista = ordenaTitulo(lista)
                window_ordenar.close()
                s = True
                popup_salvar(lista)
            elif ev == '~DATA~':
                lista = ordenaData(lista)
                window_ordenar.close()
                s = True
                popup_salvar(lista)

    return lista if lista != [] else sg.popup('Não foram encontradas publicações!')

def procurar_keywords(bd):
    lista = []
    layout = [ [sg.Text('Keyword a procurar:')],
           [sg.Input(key='-KEYWORD-')],
           [sg.OK(), sg.Cancel()] ]
    window = sg.Window('Procurar por Keyword', layout, modal = True)

    stop = False
    while not stop:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'Cancel') or not values['-KEYWORD-'].strip():
            sg.popup("Operação cancelada ou nenhuma keyword inserida.", title="Aviso")
            stop = True
            window.close()
        else:
            kw = values['-KEYWORD-'].strip()

            for publi in bd:
                if "keywords" in publi.keys():
                    if kw.lower() in publi["keywords"].lower():
                        lista.append(publi)
            stop = True
            window.close()
  
    # Popup para Ordenar            
    if lista != []:
        layout_ordenar = [[sg.Text('Ordenar por:')],
                        [sg.Button('Título', size=(15, 1), key='~TITULO~'), sg.Button('Data', size=(15, 1), key='~DATA~')]]
        window_ordenar = sg.Window('Ordenar Lista', layout_ordenar, modal = True)
        stp = False
        while not stp:
            ev,_ = window_ordenar.read()
        
            if ev == '~TITULO~':
                lista = ordenaTitulo(lista)
                stp = True
                window_ordenar.close()
                popup_salvar(lista)
            elif ev == '~DATA~':
                lista = ordenaData(lista)
                stp = True
                window_ordenar.close()
                popup_salvar(lista)
            elif ev == sg.WINDOW_CLOSED:
                sg.popup('Operação cancelada.', title='Cancelado')
                stp = True
                window_ordenar.close()

    return lista if lista != [] else sg.popup('Não foram encontradas publicações!')

def procurar_titulo(bd):
    lista = []
    layout = [ [sg.Text('Título a procurar:')],
           [sg.Input(key='-TITULO-')],
           [sg.OK(), sg.Cancel()] ]
    window = sg.Window('Procurar por Título', layout, modal = True)

    stop = False
    while not stop:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Cancel') or not values['-TITULO-'].strip():
            sg.popup("Operação cancelada ou nenhuma título inserido.", title="Aviso")
            stop = True
            window.close()
        else:
            titulo = values['-TITULO-'].strip()
            for publi in bd:
                if "title" in publi.keys():
                    if titulo.lower() in publi["title"].lower():
                        lista.append(publi)
            stop = True
            window.close()
    # Popup para Ordenar            
    if lista != []:
        layout_ordenar = [[sg.Text('Ordenar por:')],
                        [sg.Button('Título', size=(15, 1), key='~TITULO~'), sg.Button('Data', size=(15, 1), key='~DATA~')]]
        window_ordenar = sg.Window('Ordenar Lista', layout_ordenar, modal = True)
        s = False
        while not s:
            ev,_ = window_ordenar.read()
            if ev == '~TITULO~':
                lista = ordenaTitulo(lista)
                window_ordenar.close()
                s = True
                popup_salvar(lista)
            elif ev == '~DATA~':
                lista = ordenaData(lista)
                window_ordenar.close()
                s = True
                popup_salvar(lista)
            elif ev == sg.WINDOW_CLOSED:
                sg.popup('Operação cancelada.', title='Cancelado')
                window_ordenar.close()
                s = True
    return lista if lista != [] else sg.popup('Não foram encontradas publicações!')

def procurar_afiliacao(bd):
    lista = []
    layout = [ [sg.Text('Afiliação a procurar:')],
           [sg.Input(key='-AFILIACAO-')],
           [sg.OK(), sg.Cancel()] ]
    window = sg.Window('Procurar por Afiliação', layout, modal = True)

    stop= False
    while not stop:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Cancel') or not values['-AFILIACAO-'].strip():
            sg.popup("Operação cancelada ou nenhuma afiliação inserida.", title="Aviso")
            window.close()
            stop = True
        else:
            af = values['-AFILIACAO-'].strip()
            stop = True
            window.close()

            for publi in bd:
                for author in publi["authors"]:
                    if "affiliation" in author.keys():
                        if af.lower() in author["affiliation"].lower() and author["affiliation"] not in lista:
                            lista.append(publi)
            
    # Popup para Ordenar            
    if lista != []:
        layout_ordenar = [[sg.Text('Ordenar por:')],
                        [sg.Button('Título', size=(15, 1), key='~TITULO~'), sg.Button('Data', size=(15, 1), key='~DATA~')]]
        window_ordenar = sg.Window('Ordenar Lista', layout_ordenar, modal = True)
        st = False
        while not st:
            ev,_ = window_ordenar.read()
            if ev == '~TITULO~':
                lista= ordenaTitulo(lista)
                window_ordenar.close()
                st = True
                popup_salvar(lista)
            elif ev == '~DATA~':
                lista = ordenaData(lista)
                window_ordenar.close()
                st = True
                popup_salvar(lista)
            elif ev == sg.WINDOW_CLOSED:
                sg.popup('Operação cancelada.', title='Cancelado')
                window_ordenar.close()
                st = True
    return lista if lista != [] else sg.popup('Não foram encontradas publicações!')

def procurar_data(bd):
    lista = [] 
    coluna_ano = [[sg.Text('Ano (ex.:2025):', font = 'Helvetica', justification='center')],
                  [sg.Input(key='-ANO-', size=(20, 1))]]
    coluna_mes = [[sg.Text('Mês (ex.:01):', font = 'Helvetica', justification='center')],
                  [sg.Input(key='-MES-', size=(20, 1))]]
    coluna_dia = [[sg.Text('Dia (ex.:28)', font = 'Helvetica', justification='center')],
                  [sg.Input(key='-DIA-', size=(20, 1))]]
    layout_data =[[sg.Text('Procurar por Data', font = ('Helvetica', 14, 'bold'), justification='center')],
                    [sg.Column(coluna_ano, element_justification='center', vertical_alignment='top'),
                    sg.Column(coluna_mes, element_justification='center', vertical_alignment='top'),
                    sg.Column(coluna_dia, element_justification='center', vertical_alignment='top')],
                    [sg.Button('OK', key='-OK-'), sg.Button('Sair', key='-CANCEL-')]]
    window_data = sg.Window('Procurar por data', layout_data, font = 'Helvetica', element_justification='center', modal = True)
    stop = False
    while not stop:
        e, v = window_data.read()
        if e in (sg.WINDOW_CLOSED, '-CANCEL-'):
            sg.popup("Operação cancelada.", title="Aviso")
            stop = True
            window_data.close()
        elif e == '-OK-':
            ano = v['-ANO-'].strip()
            mes = v['-MES-'].strip()
            dia = v['-DIA-'].strip()
            for publi in bd:
                if "publish_date" in publi:
                    data_publi = publi["publish_date"].split("-")
                    if (not ano or ano == data_publi[0]) and (not mes or mes == data_publi[1]) and (not dia or dia == data_publi[2]):
                        lista.append(publi)
            if not lista:
                sg.popup('Publicação não encontrada ou data inserida incorretamente', title='Aviso')
            stop = True
            window_data.close()

    # Popup para Ordenar            
    if lista != []:
        layout_ordenar = [[sg.Text('Ordenar por:')],
                        [sg.Button('Título', size=(15, 1), key='~TITULO~'), sg.Button('Data', size=(15, 1), key='~DATA~')]]
        window_ordenar = sg.Window('Ordenar Lista', layout_ordenar, modal = True)
        s = False
        while not s:
            ev,_ = window_ordenar.read()
            if ev == '~TITULO~':
                lista = ordenaTitulo(lista)
                window_ordenar.close()
                s = True
                popup_salvar(lista)
            elif ev == '~DATA~':
                lista = ordenaData(lista)
                window_ordenar.close()
                s = True
                popup_salvar(lista)
            elif ev == sg.WINDOW_CLOSED:
                sg.popup('Operação cancelada.', title='Cancelado')
                window_ordenar.close()
                s = True

    return lista if lista != [] else sg.popup('Não foram encontradas publicações!')

#-------------------------------------------LISTAR AUTORES-------------------------------------------

def listaAutores(bd):
    lista = []
    for publi in bd:
        for author in publi.get("authors",[]):
            if author.get("name",'') not in lista:
                lista.append(author.get("name",''))
    lista_ordenada = sorted(lista)
    for elem in lista_ordenada:
        if elem == '':
            lista_ordenada.remove(elem)
    #Popup para salvar
    if lista != []:
        layout_salvar = [[sg.Text('Desejas salvar a lista?')],
                        [sg.Button('Sim', size=(15, 1), key='~SIM~'), sg.Button('Não', size=(15, 1), key='~NAO~')]]
        window_salvar = sg.Window('Salvar Lista', layout_salvar, modal = True)
        stop = False
        while not stop:
            e,_ = window_salvar.read()
            if e == '~SIM~':
                nome_arquivo = sg.popup_get_text('Insere o nome do arquivo (ex.:pesquisa.json)', title='Nome do Arquivo', size=(15, 1), font='Helvetica')
                if nome_arquivo:
                    salvar_em_arquivo(lista, nome_arquivo)
                    window_salvar.close()
                    stop = True
                else:
                    sg.popup('Nome do arquivo não inserido', title='Alerta')
            elif e in ['~NAO~',sg.WINDOW_CLOSED] :
                sg.popup('Operação cancelada.', title='Cancelado')
                window_salvar.close()
                stop = True
    return lista_ordenada

#-------------------------------------------LISTAR KEYWORDS-------------------------------------------
def listaKeywords(bd):
    lista = []
    for publi in bd:
        for keyword in publi.get("keywords",'').split(', '):
            if keyword not in lista:
                lista.append(keyword)
    lista_ordenada = sorted(lista)
    for elem in lista_ordenada:
        if elem == '':
            lista_ordenada.remove(elem)
    #Popup para salvar
    if lista != []:
        layout_salvar = [[sg.Text('Desejas salvar a lista?')],
                        [sg.Button('Sim', size=(15, 1), key='~SIM~'), sg.Button('Não', size=(15, 1), key='~NAO~')]]
        window_salvar = sg.Window('Salvar Lista', layout_salvar, modal = True)
        stop = False
        while not stop:
            e,_ = window_salvar.read()
            if e == '~SIM~':
                nome_arquivo = sg.popup_get_text('Insere o nome do arquivo (ex.:pesquisa.json)', title='Nome do Arquivo',size=(15, 1), font='Helvetica')
                if nome_arquivo:
                    salvar_em_arquivo(lista, nome_arquivo)
                    window_salvar.close()
                    stop = True
                else:
                    sg.popup('Nome do arquivo não inserido', title='Alerta')
            elif e in ['~NAO~',sg.WINDOW_CLOSED] :
                sg.popup('Operação cancelada.', title='Cancelado')
                window_salvar.close()
                stop = True
    return lista_ordenada

#----------------------------------------------------STATS DE PUBLICAÇÃO------------------------------------------------------------
def distribAno(bd):
    d = {}
    for publi in bd:
        if publi.get('publish_date', 'Sem data').split("-")[0] not in d:
            d[publi.get('publish_date', 'Sem data').split("-")[0]] = 1
        else:
            d[publi.get('publish_date', 'Sem data').split("-")[0]] += 1
    # Popup para Ordenar            
    if d != {}:
        layout_ordenar = [[sg.Text('Ordenar por:')],
                        [sg.Button('Ano', size=(15, 2), key='~ANO~'), sg.Button('Número de Publicações', size=(15, 2), key='~NPUBLI~')]]
        window_ordenar = sg.Window('Ordenar Lista', layout_ordenar, modal = True)
        stop = False
        while not stop:
            ev,_ = window_ordenar.read()
            if ev == '~ANO~':
                lista = sorted(list(d.items()))
                stop = True
                window_ordenar.close()
            elif ev == '~NPUBLI~':
                lista = sorted(list(d.items()), key=topordena, reverse=True) 
                stop = True
                window_ordenar.close()
            elif ev == sg.WINDOW_CLOSED:
                lista = []
                sg.popup('Operação cancelada.', title='Cancelado')
                stop = True
                window_ordenar.close()
    d = dict(lista)
    return d

def graf_distribAno(d):
    plt.clf()  
    plt.figure(figsize=(10, 8))
    anos = list(d.keys())
    publicacoes = list(d.values())
    bars = plt.bar(anos, publicacoes, color='#a0b5a9', width=0.5)
    plt.xlabel('Anos', fontsize=11)
    plt.ylabel('Nº de Publicações', fontsize=11)
    plt.title('Distribuição de publicações por ano', fontsize=11)
    plt.xticks(rotation = 35, rotation_mode = 'anchor', ha = 'right')
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.bar_label(bars, fontsize=9)
    plt.tight_layout()
    graf_da_path = 'distribAno.png'
    plt.savefig(graf_da_path)
    return graf_da_path



def distribMêsAno(bd):
    d = {}
    ano = sg.popup_get_text('Indica o ano do qual pretendes ver a distribuição de publicações?', title='Inserir Ano')
    if ano:
        for publi in bd:
            if publi.get('publish_date', 'Sem data').split("-")[0] == f'{ano}':
                if publi.get('publish_date', 'Sem data').split("-")[1] not in d:
                    d[publi.get('publish_date', 'Sem data').split("-")[1]] = 1
                else:
                    d[publi.get('publish_date', 'Sem data').split("-")[1]] += 1
        # Popup para Ordenar            
        if d != {}:
            layout_ordenar = [[sg.Text('Ordenar por:')],
                            [sg.Button('Mês', size=(15, 2), key='~MES~'), sg.Button('Número de Publicações', size=(15, 2), key='~NPUBLI~')]]
            window_ordenar = sg.Window('Ordenar Lista', layout_ordenar, modal = True)
            stop = False
            while not stop:
                ev,_ = window_ordenar.read()
                if ev == '~MES~':
                    lista = sorted(list(d.items()))
                    stop = True
                    window_ordenar.close()
                elif ev == '~NPUBLI~':
                    lista = sorted(list(d.items()), key=topordena, reverse=True) 
                    stop = True
                    window_ordenar.close()
                elif ev == sg.WINDOW_CLOSED:
                    lista = []
                    sg.popup('Operação cancelada.', title='Cancelado')
                    stop = True
                    window_ordenar.close()
            d = dict(lista)
        else:
            sg.popup('Não foram encontradas publicações para o ano introduzido', title='Alerta')
    elif 'Cancel':
        sg.popup('Operação cancelada.', title='Cancelado')
    elif not ano:
        sg.popup('Não foi introduzido nenhum ano', title='Alerta')       
    return d 

def graf_distribMêsAno(d):
    plt.clf()  
    plt.figure(figsize=(10, 8))
    meses = list(d.keys())
    publicacoes = list(d.values())
    bars = plt.bar(meses, publicacoes, color='#a0b5a9', width=0.5)
    plt.xlabel(f'Meses do ano', fontsize=11)
    plt.ylabel('Nº de Publicações', fontsize=11)
    plt.title(f'Distribuição de publicações por mês', fontsize=11)
    plt.xticks(rotation = 35, rotation_mode = 'anchor', ha = 'right')
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.bar_label(bars, fontsize=9)
    plt.tight_layout()
    graf_da_path = 'distribMêsAno.png'
    plt.savefig(graf_da_path)
    return graf_da_path

def distribTOP20Autor(bd):
    d = {}
    for publi in bd:
        for autor in publi.get('authors', ''):
            if autor.get('name', 'Sem data') not in d:
                d[autor.get('name', 'Sem data')] = 1
            else:
                d[autor.get('name', 'Sem data')] += 1
    lista = sorted(list(d.items()), key=topordena, reverse=True) 
    lista = lista[1:21]
    d = dict(lista)
    return d

def graf_distribTOP20Autor(d):
    plt.clf()  
    autores = list(d.keys())
    publicacoes = list(d.values())
    bars = plt.bar(autores, publicacoes, color='#a0b5a9', width=0.5)
    plt.xlabel('Autores', fontsize=11)
    plt.ylabel('Nº de Publicações', fontsize=11)
    plt.title('TOP20 Autores', fontsize=11)
    plt.xticks(rotation = 35, rotation_mode = 'anchor', ha = 'right', fontsize=9)
    plt.yticks(fontsize=9)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.bar_label(bars, fontsize=9)
    plt.tight_layout()
    graf_da_path = 'distribTOP20Autor.png'
    plt.savefig(graf_da_path)
    return graf_da_path


def distribAutorAno(bd):
    autor = sg.popup_get_text('Pretende calcular a destribuição de publicações por ano de que autor?', title='Inserir Autor')
    d = {}
    if autor:
        for publi in bd:
            for author in publi.get('authors', ''):
                if author.get('name', 'Sem data') == autor:
                    if publi.get('publish_date', 'Sem data').split("-")[0] not in d:
                        d[publi.get('publish_date', 'Sem data').split("-")[0]] = 1
                    else:
                        d[publi.get('publish_date', 'Sem data').split("-")[0]] += 1          
        if d != {}:
            layout_ordenar = [[sg.Text('Ordenar por:')],
                            [sg.Button('Ano', size=(15, 2), key='~ANO~'), sg.Button('Número de Publicações', size=(15, 2), key='~NPUBLI~')]]
            window_ordenar = sg.Window('Ordenar Lista', layout_ordenar, modal = True)
            stop = False
            while not stop:
                ev,_ = window_ordenar.read()
                if ev == '~ANO~':
                    lista = sorted(list(d.items()))
                    stop = True
                    window_ordenar.close()
                elif ev == '~NPUBLI~':
                    lista = sorted(list(d.items()), key=topordena, reverse=True) 
                    stop = True
                    window_ordenar.close()
                elif ev == sg.WINDOW_CLOSED:
                    lista = []
                    sg.popup('Operação cancelada.', title='Cancelado')
                    stop = True
                    window_ordenar.close()
            d = dict(lista)

        else:
            sg.popup('Não foram encontradas publicações para o autor inserido', title='Alerta')
    elif 'Cancel':
        sg.popup('Operação cancelada.', title='Cancelado')
    elif not autor:
        sg.popup('Não foi introduzido nenhum autor', title='Alerta')
    return d
    
def graf_distribAutorAno(d):
    plt.clf()  
    plt.figure(figsize=(12, 6))
    anos = list(d.keys())
    publicacoes = list(d.values())
    bars = plt.bar(anos, publicacoes, color='#a0b5a9', width=0.5)
    plt.xlabel('Anos', fontsize=11)
    plt.ylabel('Nº de Publicações', fontsize=11)
    plt.title(f'Distribuição de publicações por ano', fontsize=11)
    plt.xticks(rotation = 35, rotation_mode = 'anchor', ha = 'right')
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.bar_label(bars, fontsize=9)
    plt.tight_layout()
    graf_da_path = 'distribAutorAno.png'
    plt.savefig(graf_da_path)
    return graf_da_path
        


def distribTOP20Keywords(bd):
    d = {}
    for publi in bd:
        for palavra in publi.get('keywords', 'Sem palavra').split(', '):
            if palavra not in d:
                d[palavra] = 1
            else:
                d[palavra] += 1
    lista = sorted(list(d.items()), key=topordena, reverse=True) 
    lista = lista[1:21]
    d = dict(lista)
    return d

def graf_distribTOP20Keywords(d):
    plt.clf()  
    plt.figure(figsize=(12, 6))
    keywords = list(d.keys())
    publicacoes = list(d.values())
    bars = plt.bar(keywords, publicacoes, color='#a0b5a9', width=0.5)
    plt.xlabel('Keywords', fontsize=11)
    plt.ylabel('Nº de Publicações', fontsize=11)
    plt.title('TOP20 Keywords', fontsize=11)
    plt.xticks(rotation = 35, rotation_mode = 'anchor', ha = 'right', fontsize=9)
    plt.yticks(fontsize=9)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.bar_label(bars, fontsize=9)
    plt.tight_layout()
    graf_da_path = 'distribTOP20Keywords.png'
    plt.savefig(graf_da_path)
    return graf_da_path


def distribKeyWordAno(bd):
    d = {}
    kw = sg.popup_get_text('Pretende calcular a destribuição de publicações por ano de que KeyWord?', title='Inserir KeyWord')
    if kw:
        for publi in bd:
            for palavra in publi.get('keywords', 'Sem data').split(', '):
                if palavra == kw:
                    if publi.get('publish_date', 'Sem data').split("-")[0] not in d:
                        d[publi.get('publish_date', 'Sem data').split("-")[0]] = 1
                    else:
                        d[publi.get('publish_date', 'Sem data').split("-")[0]] += 1
    else:
        sg.popup('Não foi introduzido nenhuma KeyWord', title='Alerta')
    # Popup para Ordenar            
    if d != {}:
        layout_ordenar = [[sg.Text('Ordenar por:')],
                        [sg.Button('Ano', size=(15, 2), key='~ANO~'), sg.Button('Número de Publicações', size=(15, 2), key='~NPUBLI~')]]
        window_ordenar = sg.Window('Ordenar Lista', layout_ordenar, modal = True)
        stop = False
        while not stop:
            ev,_ = window_ordenar.read()
            if ev == '~ANO~':
                lista = sorted(list(d.items()))
                stop = True
                window_ordenar.close()
            elif ev == '~NPUBLI~':
                lista = sorted(list(d.items()), key=topordena, reverse=True) 
                stop = True
                window_ordenar.close()
            elif ev == sg.WINDOW_CLOSED:
                lista = []
                sg.popup('Operação cancelada.', title='Cancelado')
                stop = True
                window_ordenar.close()
        d = dict(lista)
    return d

def graf_distribKeyWordAno(d):
    plt.clf()  
    plt.figure(figsize=(12, 6))
    anos = list(d.keys())
    publicacoes = list(d.values())
    bars = plt.bar(anos, publicacoes, color='#a0b5a9', width=0.5)
    plt.xlabel('Anos', fontsize=11)
    plt.ylabel('Nº de Publicações', fontsize=11)
    plt.title(f'Distribuição anual da keyword', fontsize=11)
    plt.xticks(rotation = 35, rotation_mode = 'anchor', ha = 'right')
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.bar_label(bars, fontsize=9)
    plt.tight_layout()
    graf_da_path = 'distribKeyWordAno.png'
    plt.savefig(graf_da_path)
    return graf_da_path
        

        
#----------------------------------------------ATUALIZAR PUBLICAÇÕES------------------------------------------
def atualizaPubli(bd):
    lista = []
    full_date1 = []
    keywords = []

    # 1) Procurar a publicação a eliminar pelo título
    layout = [[sg.Text('Título a procurar:')],
              [sg.Input(key='-TITULO-')],
              [sg.OK(key='-OK-'), sg.Button('Cancelar', key='-CANCEL-')]]
    window = sg.Window('Procurar por Título', layout, modal=True)

    stop = False
    while not stop:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, '-CANCEL-'):
            sg.popup("Operação cancelada.", title="Aviso")
            stop = True
            window.close()
        elif not values['-TITULO-'].strip():
            sg.popup("Nenhum título inserido.", title="Aviso")
        else:
            titulo = values['-TITULO-'].strip()
            stop = True
            window.close()

            for publi in bd:
                if titulo.lower() in publi.get("title", "").lower():
                    lista.append(publi)
                

            if lista != []: 
                if len(lista) > 1:
                    layout_escolha = [[sg.Text('Escolha a publicação a atualizar:')],
                                      [sg.Listbox(values=[f"Título: {publi['title']}" for publi in lista], size=(80, 10), key='-ESCOLHA-', horizontal_scroll=True)],
                                      [sg.OK(), sg.Cancel(key='-CANCEL-')]]
                    window_escolha = sg.Window('Escolher Publicação', layout_escolha, modal=True)
                    escolha = None
                    stop = False
                    while not stop:
                        ev, vals = window_escolha.read()
                        if ev in (sg.WINDOW_CLOSED, '-CANCEL-'):
                            sg.popup("Operação cancelada.", title="Aviso")
                            window_escolha.close()
                            stop = True
                        elif ev == 'OK' and vals['-ESCOLHA-']:
                            escolha = vals['-ESCOLHA-'][0]
                            window_escolha.close()
                            stop = True
                        else:
                            sg.popup("Nenhuma publicação selecionada.", title="Aviso")

                    if escolha:
                        for publi in lista:
                            if f"Título: {publi['title']}" == escolha:
                                lista = [publi]
                            else: None
                

                        # 2) Atualizar a publicação 
                        publi = lista[0]  
                        layout_esquerda = [[sg.Text('Publicação a atualizar:')],
                                        [sg.Text(f'{mostrar_publi([publi])}')]]

                        layout_direita = [[sg.Text('Atualiza os campos que pretendes:')],
                                        [sg.Text('Abstract:', font='Helvetica'), sg.Input(key='-ABSTRACT-')],
                                        [sg.Text('Keywords:', font='Helvetica'), sg.Input(key='-KEYWORD-'), sg.Button('Adicionar Keyword', key='-ADD-KEYWORD-')],
                                        [sg.Listbox(values=[], size=(30, 4), key='-KEYWORD-LIST-', enable_events=True, horizontal_scroll=True)],
                                        [sg.Text('Authors:', font='Helvetica'), sg.Button('Eliminar', key='-ELEMINAR-'), sg.Button('Adicionar', key='-ADICIONAR-'), sg.Button('Editar', key='-EDITAR-')],
                                        [sg.Text('Doi:', font='Helvetica'), sg.Input(key='-DOI-')],
                                        [sg.Text('Pdf:', font='Helvetica'), sg.Input(key='-PDF-')],
                                        [sg.Text('Publish date (AAAA-MM-DD):', font='Helvetica'), sg.Button('Adicionar Data', key='-ADD-DATE-')],
                                        [sg.Text('Title:', font='Helvetica'), sg.Input(key='-TITLE-')],
                                        [sg.Text('Url:', font='Helvetica'), sg.Input(key='-URL-')],
                                        [sg.OK(key='-OK-'), sg.Button('Cancelar', key='-CANCEL-')]]

                        layout_at = [[sg.Column(layout_esquerda, element_justification='left', vertical_alignment='top', size=(500, 500), scrollable=True),
                                    sg.VSeparator(),
                                    sg.Column(layout_direita, element_justification='left', vertical_alignment='top')]]

                        window_at = sg.Window('Atualizar Publicação', layout_at, modal=True)

                        stp = False
                        while not stp:
                            e, v = window_at.read()
                            if e in [sg.WINDOW_CLOSED, '-CANCEL-']:
                                sg.popup("Operação cancelada", title="Aviso")
                                stp = True
                                window_at.close()

                            elif e == '-ELEMINAR-':
                                a = sg.popup_get_text("Qual autor pretendes eliminar?", title='Eliminar Autor')
                                if not a:
                                    sg.popup('Não foi inserido nenhum autor', title='Aviso')
                                else:
                                    autores = publi.get('authors', [])
                                    autor_encontrado = False
                                    normalized_input = a.strip().lower()
                                    novos_autores = []

                                    for autor in autores:
                                        if normalized_input == autor.get('name', '').strip().lower():
                                            autor_encontrado = True
                                            sg.popup('Autor eliminado com sucesso!', title='Eliminado')
                                        else:
                                            novos_autores.append(autor)

                                    if not autor_encontrado:
                                        sg.popup('Autor não encontrado', title='Aviso')
                                    else:
                                        publi['authors'] = novos_autores
                                
                            elif e == '-ADICIONAR-':
                                layout_add = [[sg.Text('Nome do Autor:'), sg.Input(key='-NOME-')],
                                            [sg.Text('Afiliação do autor:'), sg.Input(key='-AFILIACAO-')],
                                            [sg.Text('Orcid do autor:'), sg.Input(key='-ORCID-')],
                                            [sg.OK(), sg.Button('Cancelar', key='-CANCEL-')]]
                                window_add = sg.Window('Adicionar Autor', layout_add, modal=True)

                                st = False
                                while not st:
                                    ev, val = window_add.read()
                                    if ev in (sg.WINDOW_CLOSED, '-CANCEL-'):
                                        sg.popup('Operação cancelada.', title='Cancelado')
                                        st = True
                                        window_add.close()
                                    elif ev == 'OK':
                                        dici = {}
                                        if val['-NOME-']:
                                            dici["name"] = val['-NOME-']
                                        if val['-AFILIACAO-']:
                                            dici["affiliation"] = val['-AFILIACAO-']
                                        if val['-ORCID-']:
                                            dici["orcid"] = val['-ORCID-']
                                        publi.get('authors', []).append(dici)
                                        sg.popup('Autor adicionado com sucesso!', title='Adicionado')
                                        st = True
                                        window_add.close()

                            elif e == '-EDITAR-':
                                aa = sg.popup_get_text('Qual autor pretendes alterar?', title='Editar Autor')
                                if aa:
                                    encontrado = False
                                    for autor in publi.get('authors', []):
                                        if autor.get('name', '').strip().lower() == aa.strip().lower():
                                            encontrado = True
                                            layout_edit = [[sg.Text('Nome do Autor:'), sg.Input(key='-NOME-', default_text=autor.get('name', ''))],
                                                        [sg.Text('Afiliação do autor:'), sg.Input(key='-AFILIACAO-', default_text=autor.get('affiliation', ''))],
                                                        [sg.Text('Orcid do autor:'), sg.Input(key='-ORCID-', default_text=autor.get('orcid', ''))],
                                                        [sg.OK(), sg.Button('Cancelar', key='-CANCEL-')]]
                                            window_edit = sg.Window('Editar Autor', layout_edit, modal=True)

                                            s = False
                                            while not s:
                                                ev, val = window_edit.read()
                                                if ev in [sg.WINDOW_CLOSED, '-CANCEL-']:
                                                    sg.popup('Operação cancelada.', title='Cancelado')
                                                    s = True
                                                    window_edit.close()
                                                elif ev == 'OK':
                                                    if val['-NOME-']:
                                                        autor['name'] = val['-NOME-']
                                                    if val['-AFILIACAO-']:
                                                        autor['affiliation'] = val['-AFILIACAO-']
                                                    if val['-ORCID-']:
                                                        autor['orcid'] = val['-ORCID-']
                                                    sg.popup('Autor editado com sucesso!', title='Editado')
                                                    window_edit.close()
                                                    s = True
                                    if not encontrado:
                                        sg.popup('Não foi encontrado nenhum autor.', title='Aviso')
                                else:
                                    sg.popup('Não foi inserido nenhum autor.', title='Aviso')
                            elif e == '-ADD-DATE-':
                                
                                coluna_ano = [[sg.Text('Ano (ex.:2025):', font='Helvetica')], [sg.Input(key='-ANO-', size=(20, 1), default_text=publi.get('publish_date', '').split('-')[0])]]
                                coluna_mes = [[sg.Text('Mês (ex.:01):', font='Helvetica')], [sg.Input(key='-MES-', size=(20, 1), default_text=publi.get('publish_date', '').split('-')[1])]]
                                coluna_dia = [[sg.Text('Dia (ex.:28)', font='Helvetica')], [sg.Input(key='-DIA-', size=(20, 1), default_text=publi.get('publish_date', '').split('-')[2])]]
                                layout_data = [
                                    [sg.Text('Adicionar Data', font=('Helvetica', 14, 'bold'))],
                                    [sg.Column(coluna_ano, element_justification='center'),
                                    sg.Column(coluna_mes, element_justification='center'),
                                    sg.Column(coluna_dia, element_justification='center')],
                                    [sg.Button('OK', key='-OK-DATE-'), sg.Button('Sair', key='-CANCEL-DATE-')]
                                ]

                                window_data = sg.Window('Adicionar Data', layout_data, modal=True)
                                date_stop = False
                                while not date_stop:
                                    date_event, date_values = window_data.read()
                                    if date_event in (sg.WINDOW_CLOSED, '-CANCEL-DATE-'):
                                        date_stop = True
                                        window_data.close()
                                    elif date_event == '-OK-DATE-':
                                        ano = date_values['-ANO-'].strip()
                                        mes = date_values['-MES-'].strip()
                                        dia = date_values['-DIA-'].strip()
                                        if ano and mes and dia:
                                            if len(ano) == 4 and len(mes) == 2 and len(dia) == 2: 
                                                full_date = f"{ano}-{mes}-{dia}"
                                                full_date1.append(full_date)
                                                date_stop = True
                                                window_data.close()
                                            else:
                                                sg.popup("Data inserida incorretamente. Por favor, insira a data no formato AAAA-MM-DD.", title="Erro")
                                        else:
                                            sg.popup("Por favor, preencha todos os campos (Ano, Mês, Dia).", title="Erro")

                            elif e == '-ADD-KEYWORD-':
                                keyword = v['-KEYWORD-'].strip()
                                if keyword:
                                    keywords.append(keyword)
                                    window_at['-KEYWORD-LIST-'].update(values=keywords)
                                    window_at['-KEYWORD-'].update('')
                                else:
                                    sg.popup('É necessário introduzir uma keyword.', title='Input Error')

                            elif e == '-OK-':
                                if v['-ABSTRACT-']:
                                    publi['abstract'] = v['-ABSTRACT-']
                                if v['-DOI-']:
                                    publi['doi'] = v['-DOI-']
                                if v['-TITLE-']:
                                    publi['title'] = v['-TITLE-']
                                if v['-URL-']:
                                    publi['url'] = v['-URL-']
                                if v['-PDF-']:
                                    publi['pdf'] = v['-PDF-']
                                if full_date1:
                                    x = len(full_date1)
                                    publi['publish_date'] = full_date1[x-1]
                                if keywords:
                                    publi['keywords'] = ", ".join(keywords)
                                sg.popup('Publicação atualizada com sucesso!', title='Atualizado')
                                sg.popup_scrolled(f'Publicação atualizada:\n\n{mostrar_publi([publi])}', title='Publicação Atualizada')
                                stp = True
                                window_at.close()

            else:
                sg.popup('Não foi encontrada nenhuma publicação', title='Aviso')   
    return bd