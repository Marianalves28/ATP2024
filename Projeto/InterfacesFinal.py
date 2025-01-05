#duas interfaces

import PySimpleGUI as sg
import f_projetoFinal as fpj
import json
import os
import matplotlib.pyplot as plt



#----------------------------------------------------------------CRIAR JANELAS---------------------------------------------------------
def interfaceGrafica():
    sg.theme('LightGreen1')
    def criar_main_window():
        # Define o layout do menu que vai aparecer à esquerda
        menu_layout = [
            [sg.Button('Carregar Ficheiro', size=(15, 2), key='~CARREGAR~')],
            [sg.Button('Criar Publicação', size=(15, 2), key='~CRIAR~')],
            [sg.Button('Eliminar Publicação', size=(15, 2), key='~ELIMINAR~')],
            [sg.Button('Atualizar Publicação', size=(15, 2), key='~ATUALIZAR~')],
            [sg.Button('Procurar Publicação', size=(15, 2), key='~PROCURAR~')],
            [sg.Button('Listar Autores', size=(15, 2), key='~LISTARA~')],
            [sg.Button('Listar KeyWords', size=(15, 2), key='~LISTARK~')],
            [sg.Button('Estatísticas de Publicação', size=(15, 2), key='~STATS~')],
            [sg.Button('Importar Dados', size=(15, 2), key='~IMPORTAR~')],
            [sg.Button('Exportar Dados', size=(15, 2), key='~EXPORTAR~')],
            [sg.Button('Help', size=(15, 2), key='~HELP~')],
            [sg.Button('Sair', size=(15, 2), key='~SAIR~')]
        ]
        # Define o layout da area de outputs à direita
        results_layout = [
            [sg.Text('Resultados do teu input:', font=('Helvetica', 14))],
            [sg.Multiline(size=(60, 30), key='-RESULTS-', disabled=True)]
        ]
        # Combinado das duas secções no layout principal
        layout = [
            [
                sg.Column(menu_layout, element_justification='center', vertical_alignment='top'),
                sg.VSeparator(),
                sg.Column(results_layout, element_justification='left', vertical_alignment='top')
            ]
        ]

        # Main window
        return sg.Window('Sistema de Consulta e Análise de Publicações Científicas',
                        layout, finalize=True, resizable=True)
        
    def criar_help_window_main():
        help_texto = (
            'Ações possíveis no Sistema de Consulta e Análise de Publicações:\n\n'
            '- Carregar Ficheiro: Importa a tua base de dados. As restantes funções apenas funcionam após esta ser executada.\n'
            '- Criar publicação: Criar uma nova publicação e adiciona-la à base de dados em memória.\n'
            '- Eliminar Publicação: Eliminar uma publicação após ser procurada pelo seu título.\n'
            '- Atualizar Publicação: Atualizar uma publicação após ser procurada pelo seu título.\n'
            '- Procurar Publicação: Procurar publicações por variados parametros.\n'
            '- Listar Autores: Lista todos os autores na base de dados.\n'
            '- Estatísticas de Publicação: Calcula distribuições, fornece graficos e relatórios das mesmas. \n'
            '- Importar Dados: Importa dados de outros ficheiro e adiciona-os à database em memória.\n'
            '- Exportar Dados: Exporta a data base em memória para um ficheiro .json.\n'
            '- Help: Display desta informação de ajuda.\n'
            '- Sair: Sair da app guardando a informação em memória num ficheiro .json.\n\n'
        )
        layout = [[sg.Text(help_texto, font=('Helvetica', 10), size=(80, None))], [sg.Button('Fechar', key='~FECHAR~')]]

        return sg.Window('Help', layout, modal=True)


    def criar_procurar_window():
        menup_layout = [
            [sg.Text('Procurar por:', font=('Helvetica', 14))],
            [sg.Button('Autor', size=(15, 1), key='~AUTOR~')],
            [sg.Button('Keyword', size=(15, 1), key='~KEYWORD~')],
            [sg.Button('Título', size=(15, 1), key='~TITULO~')],
            [sg.Button('Afiliação', size=(15, 1), key='~AFILIACAO~')],
            [sg.Button('Data', size=(15, 1), key='~DATA~')],
            [sg.Button('Help', size=(15, 1), key='~HELP~')],
            [sg.Button('Sair', size=(15, 1), key='~SAIR~')]
        ]
        resultsp_layout=[
            [sg.Text('Resultados da tua procura:', font=('Helvetica', 14))],
            [sg.Multiline(size=(60, 30), key='-RESULTS-', disabled=True)]
        ]
        layoutp = [
            [
                sg.Column(menup_layout, element_justification='center', vertical_alignment='top'),
                sg.VSeparator(),
                sg.Column(resultsp_layout, element_justification='left', vertical_alignment='top')
            ]
        ]
        return sg.Window('Procurar Publicação Científica',
                        layoutp, finalize=True, resizable=True, modal=True)

    def criar_help_window_procurar():
        help_texto = (
            'Ações possíveis na Função de procura:\n\n'
            '- Procurar por Autor: Procurar publicações pelo autor inserido.\n'
            '- Procurar por Keyword: Procurar publicações pela keyword inserida.\n'
            '- Procurar por Título: Procurar publicações pelo título inserido.\n'
            '- Procurar por Afiliação: Procurar publicações pela afiliação inserida.\n'
            '- Procurar por Data: Procurar publicações pela data inserida, permite procurar apenas por um dos 3 parâmetros (ano, mês, dia) ou por vários.\n'
            '- Help: Display desta informação de ajuda.\n'
            '- Sair: Fecha a window da procura.\n\n'
            'Nota: após a procura, os resultados podem ser ordenados por título ou data de publicação, bem como ser salvos num ficheiro .json.\n'
            'Os resultados da pesquisa podem ser visualizados no lado direito desta janela.\n'
        )
        layout = [[sg.Text(help_texto, font=('Helvetica', 10), size=(80, None))], [sg.Button('Fechar', key='~FECHAR~')]]

        return sg.Window('Help', layout, modal=True)


    def criar_stats_window():
        menus_layout = [
            [sg.Text('Distribuição de Publicações:', font=('Helvetica', 14))],
            [sg.Button('Por Ano', size=(20, 2), key='~ANO~')],
            [sg.Button('Por Mês no Ano', size=(20, 2), key='~MES~')],
            [sg.Button('Pelos TOP20 Autores', size=(20, 2), key='~20AUTORES~')],
            [sg.Button('Por Ano de x Autor', size=(20, 2), key='~AUTOR~')],
            [sg.Button('Pelas TOP20 Keywords', size=(20, 2), key='~20KEYWORDS~')],
            [sg.Button('Por ano da keyword x', size=(20, 2), key='~KEYWORD~')],
            [sg.Button('Help', size=(20, 2), key='~HELP~')],
            [sg.Button('Sair', size=(20, 2), key='~SAIR~')]
        ]
        resultss_layout=[
            [sg.Text('Resultado:', font=('Helvetica', 14))],
            [sg.Multiline(size=(80, 8), key='-RESULTS-', disabled=True)],
            [sg.Image(key='-IMAGE-', expand_x=True, expand_y=True)],
            [sg.Button('Apagar Imagem', size=(20, 2), key='~CLEAR_IMAGE~')] 
        ]
        layouts = [
            [
                sg.Column(menus_layout, element_justification='center', vertical_alignment='top'),
                sg.VSeparator(),
                sg.Column(resultss_layout, element_justification='left', vertical_alignment='top')
            ]
        ]
        return sg.Window('Estatística da Base de Dados',
                        layouts, finalize=True, resizable=True, modal=True)


    def criar_help_window_stats():
        help_texto = (
            'Funcionamento da Janela de Estatística da Base de Dados:\n\n'
            '- Realiza estatísticas sobre a base de dados em memória.\n'
            '- Por Ano: Mostra a distribuição de publicações por ano.\n'
            '- Por Mês no Ano: Mostra a distribuição de publicações por mês no ano introduzido.\n'
            '- Pelos TOP20 Autores: Mostra a distribuição de publicações pelos 20 autores mais produtivos.\n'
            '- Por Ano de x Autor: Mostra a distribuição de publicações por ano do autor introduzido.\n'
            '- Pelas TOP20 Keywords: Mostra a distribuição de publicações pelas 20 keywords mais usadas.\n'
            '- Por ano da keyword x: Mostra a distribuição de publicações por ano da keyword introduzida.\n'
            '- Help: Display desta informação de ajuda.\n'
            '- Sair: Fecha a janela de estatística e permite regressar à janela principal.\n\n'
            'Nota: os resultados das estatísticas podem ser visualizados no espaço superior direito desta janela.\n'
            'Os resultados podem posteriormente ser observados graficamente e/ou guardados num ficheiro .json.\n'
            'Os gráficos, quando gerados, são automaticamente salvos em formato png e podem ser visualizados no espaço inferior direito desta janela.\n'
        )
        layout = [[sg.Text(help_texto, font=('Helvetica', 10), size=(80, None))], [sg.Button('Fechar', key='~FECHAR~')]]

        return sg.Window('Help', layout, modal=True)


    # ------------------------------------------------------ EVENT LISTENER ---------------------------------------------------------

    stopp = False
    dataset = None
    main_window = criar_main_window()
    while not stopp:
        event, values = main_window.read()
        if event in [sg.WINDOW_CLOSED, '~SAIR~']: #FEITO E DEBUGED
            stopp = True
            if dataset:
                fpj.salvar_em_arquivo(dataset, 'medical_papers_updated.json')

        elif event == '~CARREGAR~': #FEITO E DEBUGED
            ficheiro = sg.popup_get_file('Selecione o ficheiro JSON', file_types=(('JSON Files', '*.json'),) )
            if ficheiro:
                dataset = fpj.carregar_dataset(ficheiro)
                if dataset:
                    main_window['-RESULTS-'].update(f'Dataset carregado!\nForam lidos {len(dataset)} registos.')
        
        elif event == '~HELP~': #FEITO E DEBUGED
            help_window = criar_help_window_main()
            stp = False
            while not stp:
                help_event, _ = help_window.read()
                if help_event in (sg.WINDOW_CLOSED, '~FECHAR~'):
                    help_window.close()
                    stp = True

        elif event == '~CRIAR~': #FEITO E DEBUGED
            if dataset:
                a = len(dataset)
                dataset = fpj.criar_publi(dataset)
                b = len(dataset)
                if a < b:
                    main_window['-RESULTS-'].update(f"Publicação criada com sucesso!\nO dataset agora tem {len(dataset)} registos.")
            else:
                sg.popup('Por favor, carregue um dataset primeiro.', title='Alerta')

        elif event == '~ELIMINAR~': #FEITO E DEBUGED
            if dataset:
                a = len(dataset)
                dataset == fpj.eliminar_publi(dataset)
                b = len(dataset)
                if a > b:   
                    main_window['-RESULTS-'].update(f"Publicação eliminada do dataset!\nO dataset agora tem {len(dataset)} registos.")
            else:
                sg.popup('Por favor, carregue um dataset primeiro.', title='Alerta')
        
        elif event == '~ATUALIZAR~': #FEITO E DEBUGED
            if dataset:
                dataset = fpj.atualizaPubli(dataset)
            else:
                sg.popup('Por favor, carregue um dataset primeiro.', title='Alerta')

        elif event == '~PROCURAR~': #FEITO E DEBUGED
            if dataset:
                procurar_window = criar_procurar_window()
                s = False
                while not s:
                    e, v = procurar_window.read()
                    if e in [sg.WINDOW_CLOSED, '~SAIR~']:
                        s = True
                    
                    elif e == '~HELP~':
                        help_window = criar_help_window_procurar()
                        stp = False
                        while not stp:
                            help_event, _ = help_window.read()
                            if help_event in (sg.WINDOW_CLOSED, '~FECHAR~'):
                                help_window.close()
                                stp = True

                    elif e == '~AUTOR~': 
                        pa = fpj.procurar_autores(dataset)
                        if isinstance(pa, list):
                            procurar_window['-RESULTS-'].update(fpj.mostrar_publi(list(pa)))

                    elif e == '~KEYWORD~':
                        pk = fpj.procurar_keywords(dataset)
                        if isinstance(pk, list):
                            procurar_window['-RESULTS-'].update(fpj.mostrar_publi(list(pk)))

                    elif e == '~TITULO~':
                        pt = fpj.procurar_titulo(dataset)
                        if isinstance(pt, list):
                            procurar_window['-RESULTS-'].update(fpj.mostrar_publi(list(pt)))

                    elif e == '~AFILIACAO~':
                        paf = fpj.procurar_afiliacao(dataset)
                        if isinstance(paf, list):
                            procurar_window['-RESULTS-'].update(fpj.mostrar_publi(list(paf)))

                    elif e == '~DATA~':
                        pd = fpj.procurar_data(dataset)
                        if isinstance(pd, list):
                            procurar_window['-RESULTS-'].update(fpj.mostrar_publi(list(pd)))

                procurar_window.close()
            else:
                sg.popup('Por favor, carregue um dataset primeiro.', title='Alerta')

        elif event == '~LISTARA~':  #FEITO E DEBUGED
            if dataset:
                autores = fpj.listaAutores(dataset)
                main_window['-RESULTS-'].update(f"Autores encontrados no dataset:\n{'\n'.join(autores)}")
            else:
                sg.popup('Por favor, carregue um dataset primeiro.', title='Alerta')

        elif event == '~LISTARK~':  #FEITO E DEBUGED
            if dataset:
                keywords = fpj.listaKeywords(dataset)
                main_window['-RESULTS-'].update(f"KeyWords encontradas no data set:\n{'\n'.join(keywords)}")
            else:
                sg.popup('Por favor, carregue um dataset primeiro.', title='Alerta')
        
        elif event == '~STATS~':  #FEITO
            if dataset:
                stats_window = criar_stats_window()
                st = False
                while not st:
                    ev,_ = stats_window.read()
                    if ev in [sg.WINDOW_CLOSED, '~SAIR~']:
                        st = True
                    
                    elif ev == '~HELP~':
                        help_window = criar_help_window_stats()
                        stp = False
                        while not stp:
                            help_event, _ = help_window.read()
                            if help_event in (sg.WINDOW_CLOSED, '~FECHAR~'):
                                help_window.close()
                                stp = True

                    elif ev == '~ANO~':
                        da = fpj.distribAno(dataset)
                        stats_window['-RESULTS-'].update(da)
                        if da != {}:
                            layout_graf = [[sg.Text('Desejas ver a distribuição graficamente?')],
                                            [sg.Button('Sim', size=(15, 1), key='~SIM~'), sg.Button('Não', size=(15, 1), key='~NAO~')]]
                            window_graf = sg.Window('Ver Graficamente', layout_graf, modal = True)
                            e,_ = window_graf.read()
                            window_graf.close()
                            if e == '~SIM~':
                                graf_da_path = fpj.graf_distribAno(da)
                                sg.popup(f'Grafico salvo em {graf_da_path}', title='Grafico Salvo')
                                stats_window['-IMAGE-'].update(filename=graf_da_path)
                            elif e in ('~NAO~', sg.WINDOW_CLOSED):
                                sg.popup('Operação cancelada.', title='Cancelado')

                    elif ev == '~MES~':
                        dma = fpj.distribMêsAno(dataset)
                        stats_window['-RESULTS-'].update(dma)
                        if dma != {}:
                            layout_graf = [[sg.Text('Desejas ver a distribuição graficamente?')],
                                            [sg.Button('Sim', size=(15, 1), key='~SIM~'), sg.Button('Não', size=(15, 1), key='~NAO~')]]
                            window_graf = sg.Window('Ver Graficamente', layout_graf, modal = True)
                            e,_ = window_graf.read()
                            window_graf.close()
                            if e == '~SIM~':
                                graf_dma_path = fpj.graf_distribMêsAno(dma)
                                sg.popup(f'Grafico salvo em {graf_dma_path}', title='Grafico Salvo')
                                stats_window['-IMAGE-'].update(filename=graf_dma_path)
                            elif e in ('~NAO~', sg.WINDOW_CLOSED):
                                sg.popup('Operação cancelada.', title='Cancelado')
                        else:
                            None
                    elif ev == '~20AUTORES~':
                        d20a= fpj.distribTOP20Autor(dataset)
                        stats_window['-RESULTS-'].update(d20a)
                        if d20a != {}:
                            layout_graf = [[sg.Text('Desejas ver a distribuição graficamente?')],
                                            [sg.Button('Sim', size=(15, 1), key='~SIM~'), sg.Button('Não', size=(15, 1), key='~NAO~')]]
                            window_graf = sg.Window('Ver Graficamente', layout_graf, modal = True)
                            e,_ = window_graf.read()
                            window_graf.close()
                            if e == '~SIM~':
                                graf_d20a_path = fpj.graf_distribTOP20Autor(d20a)
                                sg.popup(f'Grafico salvo em {graf_d20a_path}', title='Grafico Salvo')
                                stats_window['-IMAGE-'].update(filename=graf_d20a_path)
                            elif e in ('~NAO~', sg.WINDOW_CLOSED):
                                sg.popup('Operação cancelada.', title='Cancelado')


                    elif ev == '~AUTOR~':
                        daa = fpj.distribAutorAno(dataset)
                        stats_window['-RESULTS-'].update(daa)
                        if daa != {}:
                            layout_graf = [[sg.Text('Desejas ver a distribuição graficamente?')],
                                            [sg.Button('Sim', size=(15, 1), key='~SIM~'), sg.Button('Não', size=(15, 1), key='~NAO~')]]
                            window_graf = sg.Window('Ver Graficamente', layout_graf, modal = True)
                            e,_ = window_graf.read()
                            window_graf.close()
                            if e == '~SIM~':
                                graf_daa_path = fpj.graf_distribAutorAno(daa)
                                sg.popup(f'Grafico salvo em {graf_daa_path}', title='Grafico Salvo')
                                stats_window['-IMAGE-'].update(filename=graf_daa_path)
                            elif e in ['~NAO~', sg.WINDOW_CLOSED]:
                                sg.popup('Operação cancelada.', title='Cancelado')
                        else:
                            None


                    elif ev == '~20KEYWORDS~':
                        d20k = fpj.distribTOP20Keywords(dataset)
                        stats_window['-RESULTS-'].update(d20k)
                        if d20k != {}:
                            layout_graf = [[sg.Text('Desejas ver a distribuição graficamente?')],
                                            [sg.Button('Sim', size=(15, 1), key='~SIM~'), sg.Button('Não', size=(15, 1), key='~NAO~')]]
                            window_graf = sg.Window('Ver Graficamente', layout_graf, modal = True)
                            e,_ = window_graf.read()
                            window_graf.close()
                            if e == '~SIM~':
                                graf_d20k_path = fpj.graf_distribTOP20Keywords(d20k)
                                sg.popup(f'Grafico salvo em {graf_d20k_path}', title='Grafico Salvo')
                                stats_window['-IMAGE-'].update(filename=graf_d20k_path)
                            elif e in ('~NAO~', sg.WINDOW_CLOSED):
                                sg.popup('Operação cancelada.', title='Cancelado')


                    elif ev == '~KEYWORD~':
                        dka = fpj.distribKeyWordAno(dataset)
                        stats_window['-RESULTS-'].update(dka)
                        if dka != {}:
                            layout_graf = [[sg.Text('Desejas ver a distribuição graficamente?')],
                                            [sg.Button('Sim', size=(15, 1), key='~SIM~'), sg.Button('Não', size=(15, 1), key='~NAO~')]]
                            window_graf = sg.Window('Ver Graficamente', layout_graf, modal = True)
                            e,_ = window_graf.read()
                            window_graf.close()
                            if e == '~SIM~':
                                graf_dka_path = fpj.graf_distribKeyWordAno(dka)
                                sg.popup(f'Grafico salvo em {graf_dka_path}', title='Grafico Salvo')
                                stats_window['-IMAGE-'].update(filename=graf_dka_path)
                            elif e in ('~NAO~', sg.WINDOW_CLOSED):
                                sg.popup('Operação cancelada.', title='Cancelado')
                        else:
                            sg.popup('Não foram encontradas publicações para a keyword introduzida.', title='Alerta')
                    
                    elif ev == '~CLEAR_IMAGE~':
                        stats_window['-IMAGE-'].update(filename='')  

                stats_window.close()
            else:
                sg.popup('Por favor, carregue um dataset primeiro.', title='Alerta')
                
        elif event == '~IMPORTAR~':   #FEITO E DEBUGED
            if dataset:
                ficheiro = sg.popup_get_file('Selecione o ficheiro JSON para importar', file_types=(('JSON Files', '*.json'),))
                if ficheiro:
                    dataset_importado = fpj.carregar_dataset(ficheiro)
                    if dataset_importado:
                        titulos_existentes = [publi.get('title') for publi in dataset]
                        novas_publis = [publi for publi in dataset_importado if publi.get('title') not in titulos_existentes]
                        if novas_publis:
                            dataset += novas_publis
                            main_window['-RESULTS-'].update(f'Dataset importado!\nForam lidos {len(novas_publis)} registos.\nO dataset agora tem {len(dataset)} registos.')
                        else:
                            main_window['-RESULTS-'].update(f'Nenhum novo registo foi adicionado.\nTodas as publicações já estão presentes no dataset.\nO dataset continua com {len(dataset)}registos.')
                elif 'Cancel':
                    sg.popup('Operação cancelada.', title='Cancelado')
                else: 
                    sg.popup('Não foi introduzido nenhum ficheiro.', title='Alerta')
            else:
                sg.popup('Por favor, carregue um dataset primeiro.', title='Alerta')
        
        elif event == '~EXPORTAR~':  #FEITO E DEBUGED
            if dataset:
                nome_arquivo = sg.popup_get_text('Nomeie o arquivo para salvar os dados em memória(exemplo: resultados.json):', title='Exportar Dataset')
                if nome_arquivo:
                    fpj.salvar_em_arquivo(dataset, nome_arquivo)
                else:
                    sg.popup('Não foi introduzido nenhum nome', title='Alerta')
            else:
                sg.popup('Por favor, carregue um dataset primeiro.', title='Alerta')

        else:
            print(f'Operação não suportada: {event} - {values}\n')
    stopp=True
    main_window.close()

#----------------------------------------------------------Interface linha de comandos---------------------------------------------------------------------#
def interfacelinhadecomandos():
    def exibir_help():
        print("\nComandos disponíveis:")
        print("-------------------------------|-------------------------------------------")
        print("|       Comando                |                 Descrição                |")
        print("|------------------------------|------------------------------------------|")
        print("|   1. Carregar Dataset        | Carregar uma base de dados               |")
        print("|   2. Criar publicação        | Inserir nova publicação                  |")
        print("|   3. Eliminar publicação     | Elimina uma publicação                   |") 
        print("|   4. Consultar publicação    | Consultar uma publicação na base de dados|")
        print("|   5. Listar Autores          | Listar os autores da bases de dados      |")
        print("|   6. Listar Keywords         | Listar as keywords da base de dados      |")
        print("|   7. Estatísticas            | Gerar relatórios de estatísticas         |")  
        print("|   8. Importar dados          | Importar dados                           |")
        print("|   9. Guardar dados           | Exportar dados                           |")
        print("|   10. Help                   | Imprime esta mensagem de ajuda           |")
        print("|   0. Sair                    | Fechar a aplicação.                      |")
        print("|------------------------------|------------------------------------------|")

    def help_estatísticas():
        print("Funcionamento da Janela de Estatística da Base de Dados:\n\n'")
        print("-------------------------------|--------------------------------------------------------------------------")
        print("|       Comando                |                 Descrição                                                |")
        print("|------------------------------|--------------------------------------------------------------------------|")
        print("|   1. Por Ano                 | Mostra a distribuição de publicações por ano.                            |\n")
        print("|   2. Por Mês no Ano          | Mostra a distribuição de publicações por mês no ano introduzido          |\n")
        print("|   3. Pelos TOP20 Autores     | Mostra a distribuição de publicações pelos 20 autores mais produtivos.   |\n") 
        print("|   4. Por Ano de x Autor      | Mostra a distribuição de publicações por ano do autor introduzido.       |\n")
        print("|   5. Pelas TOP20 Keywords    | Mostra a distribuição de publicações pelas 20 keywords mais usadas.      |\n")
        print("|   6. Por ano da keyword x    | Mostra a distribuição de publicações por ano da keyword introduzida.     |\n")
        print("|   0. Sair                    | Fecha a janela de estatística e permite regressar à janela principal     |\n")
        print("|------------------------------|-----------------------------------------                                -|")
        print('Nota:os resultados das estatísticas podem ser visualizados no espaço superior direito desta janela.\n')
        print('Os resultados podem posteriormente ser observados graficamente e/ou guardados num ficheiro .json.\n')
        print('Os gráficos, quando gerados, são automaticamente salvos em formato png e podem ser visualizados no espaço inferior direito desta janela.\n')
        
    def help_procurar():
        print("Ações possíveis na Função de procura:\n\n")
        print("-------------------------------|--------------------------------------------------------------------------")
        print("|       Comando                |                 Descrição                                                |")
        print("|------------------------------|--------------------------------------------------------------------------|")
        print("|   1. Procurar por Autor      | Procurar publicações pelo autor inserido.                                |\n")
        print("|   2. Procurar por Keyword    | Procurar publicações pela keyword inserida.                              |\n")
        print("|   3. Procurar por Título     | Procurar publicações pelo título inserido.                               |\n") 
        print("|   4. Procurar por Afiliação  | Procurar publicações pela afiliação inserida.                            |\n")
        print("|   5. Procurar por Data       | Procurar publicações pela data inserida.                                 |\n")
        print("|   0. Sair                    | Fecha a window da procura.                                               |\n")
        print("|------------------------------|--------------------------------------------------------------------------|")

    def help_criar():
        print("Ações possíveis na Função de criar:\n\n")
        print("---------------------------------------------------------------------------------------------------------")
        print(""""
        '- Para criar uma nova publicação, é necessário preencher os campos desta janela, o título é obrigatório, já os restantes campos são arbitrários.\n'
        '- Após introduzir os dados de um autor, o utilizador deve clicar no botão "Adicionar Autor" para adicionar o autor à lista de autores da publicação.\n'
        '- Quando os campos pretendidos estiverem preenchidos, o utilizador deve clicar no botão "OK" para adicionar a publicação à base de dados.\n'
        '- A publicação poderá ser observada no lado direito da janela após ser criada e será automaticamente adicionada ao dataset em memória.\n'
        '- O botão "Help" abre esta janela de ajuda.\n'
        '- O botão "Cancel" fecha a janela sem criar a publicação.'                                         \n""")
        print("--------------------------------------------------------------------------------------------------------")


    #-----------------------------------Carregar dataset----------------------------------#

    def carregar_dataset():
        dataset = input("Digite o nome do dataset (somente JSON) no seu diretório de trabalho: ").strip()
        if not dataset.lower().endswith('.json'):
            print("Erro: O arquivo não possui extensão .json.")
            return None
        if not os.path.exists(dataset):
            print("Erro: Arquivo não encontrado.")
            return None
        with open(dataset, encoding="utf-8") as f:
            info = json.load(f)
        return info

    def criar_publi(bd):
        publi = {}
        authors = []
        keywords = []
        data = []

        print("Criar publicação")
        publi["abstract"] = input("Abstract: ").strip()
        publi["title"] = input("Title: ").strip()
        publi["doi"] = input("Doi: ").strip()
        publi["pdf"] = input("Pdf: ").strip()
        publi["url"] = input("Url: ").strip()

        add_data = True 
        while add_data:
            date = input("Deseja inserir uma data? (s/n): ").strip().lower()
            if date == 'n':
                add_data = False  
            elif date == 's':
                Ano = input("AAAA: ").strip()
                Mês = input("MM: ").strip()
                Dia = input("DD: ").strip()
                if Ano and Mês and Dia:
                    if len(Ano) == 4 and len(Mês) == 2 and len(Dia) == 2: 
                        data.append(f"{Ano}-{Mês}-{Dia}")
                    else:
                        print("Data inserida incorretamente. Por favor, insira a data no formato AAAA-MM-DD.")
                else:
                    print("É necessário introduzir todos os campos.")
            else:
                print("Opção inválida. Digite 's' para sim ou 'n' para não.")
    
       
        add_more_authors = True  

        while add_more_authors:
            add_author = input("Deseja adicionar um autor? (s/n): ").strip().lower()
            if add_author == 'n':
                add_more_authors = False  
            elif add_author == 's':
                name = input("Name: ").strip()
                affiliation = input("Affiliation: ").strip()
                orcid = input("Orcid: ").strip()
                if name and affiliation:
                    authors.append({"name": name, "affiliation": affiliation, "orcid": orcid})
                else:
                    print("É necessário introduzir nome e affiliation.")
            else:
                print("Opção inválida. Digite 's' para sim ou 'n' para não.")
    
        add_more_keywords = True  
        while add_more_keywords:
            add_keywords = input("Deseja adicionar uma keyword? (s/n): ").strip().lower()
            if add_keywords == 'n':
                add_more_keywords = False  
            elif add_keywords == 's':
                keyword = input("Keyword: ").strip()
                if keyword:
                    keywords.append(keyword)
                else:
                    print("É necessário introduzir nome e affiliation.")
            else:
                print("Opção inválida. Digite 's' para sim ou 'n' para não.")

        publi["keywords"] = ", ".join(keywords)
        publi["authors"] = authors
        publi["publish_date"] = data[0]
        bd.append(publi)
        print("Publicação criada com sucesso!")
        return bd
    

    def mostrar_publi(lista):
        for publi in lista:
            print(f"Título: {publi.get('title', 'N/A')}")
            print(f"Abstract: {publi.get('abstract', 'N/A')}")
            keywords = publi.get('keywords', [])
            if isinstance(keywords, str):
                keywords = [keywords]
            print(f"Keywords: {', '.join(keywords)}")
            authors = publi.get('authors', [])
            authors_info = []
            for author in authors:
                name = author.get('name', 'N/A')
                affiliation = author.get('affiliation', 'N/A')
                authors_info.append(f"{name} ({affiliation})")
            print(f"Authors: {', '.join(authors_info)}")
            print(f"DOI: {publi.get('doi', 'N/A')}")
            print(f"PDF: {publi.get('pdf', 'N/A')}")
            print(f"Publish Date: {publi.get('publish_date', 'N/A')}")
            print(f"URL: {publi.get('url', 'N/A')}")
            print("-" * 40)

    def eliminar_publi(bd):
        lista = []
        titulo = input("Digite o título da publicação a procurar: ").strip()

        for publi in bd:
            if titulo.lower() in publi.get("title", '').lower():
                lista.append(publi)
        if lista:
            print("Publicação(s) encontrada(s):")
            mostrar_publi(lista)
            if len(lista) > 1:
                qual = input("Qual publicação deseja eliminar? (Digite o título): ")
                confirm = input("Tem a certeza de que quer eliminar esta publicação? (s/n): ").strip().lower()
                if confirm == 's':
                    for publi in lista:
                        if qual.lower() == publi.get("title", '').lower():
                            bd.remove(publi)
                            print("Publicação eliminada com sucesso!")

            else:
                confirm = input("Tem a certeza de que quer eliminar esta publicação? (s/n): ").strip().lower()
                if confirm == 's':
                    bd.remove(lista[0])
                    print("Publicação(ões) eliminada(s) com sucesso!")
                else:
                    print("Operação cancelada.")
        else:
            print("Nenhuma publicação encontrada.")

        return bd

    #--------------------------------Consultar publicação----------------------------------#

    def procurar_autores(bd):
        autor = input("Digite o nome do autor: ").strip()
        if not autor:
            print("Operação cancelada ou nenhum autor inserido.")
            return

        lista = []
        for publi in bd:
            for author in publi.get("authors", []):
                if autor.lower() in author.get("name", '').lower():
                    lista.append(publi)

        if lista:
            print("Ordenar por:")
            print("1. Título")
            print("2. Data")
            escolha = input("Escolha uma opção (1 ou 2): ").strip()
            if escolha == '1':
                lista = fpj.ordenaTitulo(lista)
            elif escolha == '2':
                lista = fpj.ordenaData(lista)
            else:
                print("Operação cancelada.")
                return
            
            salvar = input("Desejas salvar a pesquisa? (s/n): ").strip().lower()
            if salvar == 's':
                nome_arquivo = input("Insere o nome do arquivo (exemplo: pesquisa.json): ").strip()
                if not nome_arquivo:
                    nome_arquivo = 'pesquisa.json'
                fpj.salvar_em_arquivo_comandos(lista, nome_arquivo)
            else:
                print("Operação cancelada.")
        else:
            print("Não foram encontradas publicações!")
        mostrar_publi(lista)

    def procurar_keywords(bd):
        kw = input("Digite a keyword a procurar: ").strip()
        if not kw:
            print("Operação cancelada ou nenhuma keyword inserida.")
            return

        lista = []
        for publi in bd:
            if "keywords" in publi.keys():
                if kw in publi["keywords"]:
                    lista.append(publi)

        if lista:
            print("Ordenar por:")
            print("1. Título")
            print("2. Data")
            escolha = input("Escolha uma opção (1 ou 2): ").strip()
            if escolha == '1':
                lista = fpj.ordenaTitulo(lista)
            elif escolha == '2':
                lista = fpj.ordenaData(lista)
            else:
                print("Operação cancelada.")
                return

            salvar = input("Desejas salvar a pesquisa? (s/n): ").strip().lower()
            if salvar == 's':
                nome_arquivo = input("Insere o nome do arquivo (exemplo: pesquisa.json): ").strip()
                if not nome_arquivo:
                    nome_arquivo = 'pesquisa.json'
                fpj.salvar_em_arquivo_comandos(lista, nome_arquivo)
            else:
                print("Operação cancelada.")
        else:
            print("Não foram encontradas publicações!")

        mostrar_publi(lista)

    def procurar_titulo(bd):
        titulo = input("Digite o título a procurar: ").strip()
        if not titulo:
            print("Operação cancelada ou nenhum título inserido.")
            return

        lista = []
        for publi in bd:
            if titulo.lower() in publi.get("title", '').lower():
                lista.append(publi)

        if lista:
            print("Ordenar por:")
            print("1. Título")
            print("2. Data")
            escolha = input("Escolha uma opção (1 ou 2): ").strip()
            if escolha == '1':
                lista = fpj.ordenaTitulo(lista)
            elif escolha == '2':
                lista = fpj.ordenaData(lista)
            else:
                print("Operação cancelada.")
                return

            salvar = input("Desejas salvar a pesquisa? (s/n): ").strip().lower()
            if salvar == 's':
                nome_arquivo = input("Insere o nome do arquivo (exemplo: pesquisa.json): ").strip()
                if not nome_arquivo:
                    nome_arquivo = 'pesquisa.json'
                fpj.salvar_em_arquivo_comandos(lista, nome_arquivo)
            else:
                print("Operação cancelada.")
        else:
            print("Não foram encontradas publicações!")

        mostrar_publi(lista)

    def procurar_afiliacao(bd):
        af = input("Digite a afiliação a procurar: ").strip()
        if not af:
            print("Operação cancelada ou nenhuma afiliação inserida.")
            return

        lista = []
        for publi in bd:
            for author in publi["authors"]:
                if "affiliation" in author:
                    if af in author["affiliation"] and author["affiliation"] not in lista:
                        lista.append(publi)

        if lista:
            print("Ordenar por:")
            print("1. Título")
            print("2. Data")
            escolha = input("Escolha uma opção (1 ou 2): ").strip()
            if escolha == '1':
                lista = fpj.ordenaTitulo(lista)
            elif escolha == '2':
                lista = fpj.ordenaData(lista)
            else:
                print("Operação cancelada.")
                return

            salvar = input("Desejas salvar a pesquisa? (s/n): ").strip().lower()
            if salvar == 's':
                nome_arquivo = input("Insere o nome do arquivo (exemplo: pesquisa.json): ").strip()
                if not nome_arquivo:
                    nome_arquivo = 'pesquisa.json'
                fpj.salvar_em_arquivo_comandos(lista, nome_arquivo)
            else:
                print("Operação cancelada.")
        else:
            print("Não foram encontradas publicações!")

        mostrar_publi(lista)

    def procurar_data(bd):
        ano = input("Digite o ano (YYYY): ").strip()
        mes = input("Digite o mês (MM): ").strip()
        dia = input("Digite o dia (DD): ").strip()

        lista = []
        for publi in bd:
            if "publish_date" in publi.keys():
                pub_date = publi["publish_date"].split("-")
                if (not ano or ano == pub_date[0]) and (not mes or mes == pub_date[1]) and (not dia or dia == pub_date[2]):
                    lista.append(publi)

        if lista:
            print("Ordenar por:")
            print("1. Título")
            print("2. Data")
            escolha = input("Escolha uma opção (1 ou 2): ").strip()
            if escolha == '1':
                lista = fpj.ordenaTitulo(lista)
            elif escolha == '2':
                lista = fpj.ordenaData(lista)
            else:
                print("Operação cancelada.")
                return

            salvar = input("Desejas salvar a pesquisa? (s/n): ").strip().lower()
            if salvar == 's':
                nome_arquivo = input("Insere o nome do arquivo (exemplo: pesquisa.json): ").strip()
                if not nome_arquivo:
                    nome_arquivo = 'pesquisa.json'
                fpj.salvar_em_arquivo_comandos(lista, nome_arquivo)
            else:
                print("Operação cancelada.")
        else:
            print("Não foram encontradas publicações!")

        mostrar_publi(lista)


    def consultar_publicação(bd):
        print("\n===== Consultar Publicação =====")
        print("Escolha o método de consulta:")
        print("1. Por Autor")
        print("2. Por Keyword")
        print("3. Por Título")
        print("4. Por Afiliação")
        print("5. Por Data")
        print("6. Help")
        print("0. Sair")

        escolha_opcao = input("\nDigite o número correspondente à opção desejada: ").strip()

        if escolha_opcao == "1":
            procurar_autores(bd)
        elif escolha_opcao == "2":
            procurar_keywords(bd)
        elif escolha_opcao == "3":
            procurar_titulo(bd)
        elif escolha_opcao == "4":
            procurar_afiliacao(bd)
        elif escolha_opcao == "5":
            procurar_data(bd)
        elif escolha_opcao == "6":
            help_procurar()
        elif escolha_opcao == "0":
            return
        else:
            print("Opção inválida. Tente novamente.")
        
    #-------------------------------------------LISTAR AUTORES-------------------------------------------
    def mostrar_resultados(lista):
        if not lista:
            print("Nenhum resultado encontrado.")
            return

        for i, item in enumerate(lista, start=1):
            print(f"\nResultado {i}: {item}")

    def listaAutores(bd):
        lista = []
        for publi in bd:
            for author in publi.get("authors", []):
                if author.get("name", '') not in lista:
                    lista.append(author.get("name", ''))
        lista_ordenada = sorted(lista)
        lista_ordenada = [elem for elem in lista_ordenada if elem]  

        mostrar_resultados(lista_ordenada)

        if lista_ordenada:
            salvar = input("Desejas salvar a lista? (s/n): ").strip().lower()
            if salvar == 's':
                nome_arquivo = input("Insere o nome do arquivo (exemplo: autores.json): ").strip()
                if not nome_arquivo:
                    nome_arquivo = 'autores.json'
                fpj.salvar_em_arquivo_comandos(lista_ordenada, nome_arquivo)
            else:
                print("Operação cancelada.")
        else:
            print("Não foram encontrados autores.")

        return lista_ordenada

    #------------------------------------Listar Keywords-----------------------------------------#
    def listaKeywords(bd):
        lista = []
        for publi in bd:
            keywords = publi.get("keywords", [])
            if isinstance(keywords, str):
                keywords = keywords.split(', ')
            for keyword in keywords:
                if keyword and keyword not in lista:
                    lista.append(keyword)
        lista_ordenada = sorted(lista)
        for elem in lista_ordenada:
            if elem == '':
                lista_ordenada.remove(elem)
        print("Keywords encontradas:")
        for keyword in lista_ordenada:
            print(keyword)

        if lista_ordenada:
            salvar = input("Desejas salvar a lista? (s/n): ").strip().lower()
            if salvar == 's':
                nome_arquivo = input("Insere o nome do arquivo (exemplo: keywords.json): ").strip()
                if not nome_arquivo:
                    nome_arquivo = 'keywords.json'
                fpj.salvar_em_arquivo_comandos(lista_ordenada, nome_arquivo)
            else:
                print("Operação cancelada.")
        else:
            print("Não foram encontradas keywords.")

        return lista_ordenada

    #------------------------------------Estatísticas-----------------------------------------#

    def mostrar_resultados(lista):
        if not lista:
            print("Nenhum resultado encontrado.")
            return

        for i, item in enumerate(lista, start=1):
            print(f"\nResultado{i}: {item}")

    def distrib_ano(bd):
        d = {}
        for publi in bd:
            ano = publi.get('publish_date', 'Sem data').split("-")[0]
            if ano not in d:
                d[ano] = 1
            else:
                d[ano] += 1

        if d:
            print("Ordenar por:")
            print("1. Ano")
            print("2. Número de Publicações")
            escolha = input("Escolha uma opção (1 ou 2): ").strip()
            if escolha == '1':
                lista = sorted(d.items())
            elif escolha == '2':
                lista = sorted(d.items(), key=fpj.topordena, reverse=True)
            else:
                print("Opção inválida. Operação cancelada.")
                return

            sorted_dict = dict(lista)
            mostrar_resultados(lista)
            graf_distrib_ano(sorted_dict )
            
            salvar = input("Desejas salvar o relatório? (s/n): ").strip().lower()
            if salvar == 's':
                nome_arquivo = input("Insere o nome do arquivo (exemplo: distrib_ano.json): ").strip()
                if not nome_arquivo:
                    nome_arquivo = 'distrib_ano.json'
                fpj.salvar_em_arquivo_comandos(dict(lista), nome_arquivo)
                grafico_arquivo = nome_arquivo.replace('.json', '.png')
                os.rename('distrib_ano.png', grafico_arquivo)
                print(f"Relatório salvo em {nome_arquivo} e gráfico salvo em {grafico_arquivo}") 
            else:
                print("Operação cancelada.")        
        else:
            print("Nenhum dado encontrado.")
        return dict(lista)

    def graf_distrib_ano(d):
        plt.clf()
        anos = list(d.keys())
        publicacoes = list(d.values())
        bars = plt.bar(anos, publicacoes, color='skyblue', width=0.5)
        plt.xlabel('Anos', fontsize=11)
        plt.ylabel('Nº de Publicações', fontsize=11)
        plt.title('Distribuição de publicações por ano', fontsize=11)
        plt.xticks(rotation=35, rotation_mode='anchor', ha='right')
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.bar_label(bars, fontsize=9)
        plt.tight_layout()
        plt.savefig('distrib_ano.png')
        plt.show()
        

        
    def distrib_mes_ano(bd):
        d = {}
        ano = input("Indica o ano do qual pretendes ver a distribuição de publicações: ").strip()
        if ano:
            for publi in bd:
                if publi.get('publish_date', 'Sem data').split("-")[0] == ano:
                    mes = publi.get('publish_date', 'Sem data').split("-")[1]
                    if mes not in d:
                        d[mes] = 1
                    else:
                        d[mes] += 1
        else:
            print("Não foi introduzido nenhum ano. Operação cancelada.")
            return

        if d:
            print("Ordenar por:")
            print("1. Mês")
            print("2. Número de Publicações")
            escolha = input("Escolha uma opção (1 ou 2): ").strip()
            if escolha == '1':
                lista = sorted(d.items())
            elif escolha == '2':
                lista = sorted(d.items(), key=fpj.topordena, reverse=True)
            else:
                print("Opção inválida. Operação cancelada.")
                return

            sorted_dict = dict(lista)
            mostrar_resultados(lista)
            graf_distrib_mes_ano(sorted_dict)

            salvar = input("Desejas salvar o relatório? (s/n): ").strip().lower()
            if salvar == 's':
                nome_arquivo = input("Insere o nome do arquivo (exemplo: distrib_mes_ano.json): ").strip()
                if not nome_arquivo:
                    nome_arquivo = 'distrib_mes_ano.json'
                fpj.salvar_em_arquivo_comandos(dict(lista), nome_arquivo)
                grafico_arquivo = nome_arquivo.replace('.json', '.png')
                os.rename('distrib_mes_ano.png', grafico_arquivo)
                print(f"Relatório salvo em {nome_arquivo} e gráfico salvo em {grafico_arquivo}")
            else:
                print("Operação cancelada.")
                return sorted_dict
        else:
            print("Nenhum dado encontrado.")


    def graf_distrib_mes_ano(d):
        plt.clf()
        meses = list(d.keys())
        publicacoes = list(d.values())
        bars = plt.bar(meses, publicacoes, color='skyblue', width=0.5)
        plt.xlabel(f'Meses do ano', fontsize=11)
        plt.ylabel('Nº de Publicações', fontsize=11)
        plt.title(f'Distribuição de publicações por mês', fontsize=11)
        plt.xticks(rotation=35, rotation_mode='anchor', ha='right')
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.bar_label(bars, fontsize=9)
        plt.tight_layout()
        plt.savefig('distrib_mes_ano.png')
        plt.show()


    def distrib_top20_autor(bd):
        d = {}
        for publi in bd:
            for autor in publi.get('authors', ''):
                nome_autor = autor.get('name', 'Sem data')
                if nome_autor not in d:
                    d[nome_autor] = 1
                else:
                    d[nome_autor] += 1

        lista = sorted(d.items(), key=fpj.topordena, reverse=True)[:20]
        d = dict(lista)

        sorted_dict = dict(lista)
        mostrar_resultados(lista)
        graf_distrib_top20_autor(sorted_dict)

        salvar = input("Desejas salvar o relatório? (s/n): ").strip().lower()
        if salvar == 's':
            nome_arquivo = input("Insere o nome do arquivo (exemplo: top20_autores.json): ").strip()
            if not nome_arquivo:
                nome_arquivo = 'top20_autores.json'
            fpj.salvar_em_arquivo_comandos(dict(lista), nome_arquivo)
            grafico_arquivo = nome_arquivo.replace('.json', '.png')
            os.rename('distrib_top20_autores.png', grafico_arquivo)
            print(f"Relatório salvo em {nome_arquivo} e gráfico salvo em {grafico_arquivo}")  
        else:
            print("Operação cancelada.")

        return d

    def graf_distrib_top20_autor(d):
        plt.clf()
        autores = list(d.keys())
        publicacoes = list(d.values())
        bars = plt.bar(autores, publicacoes, color='skyblue', width=0.5)
        plt.xlabel('Autores', fontsize=11)
        plt.ylabel('Nº de Publicações', fontsize=11)
        plt.title('TOP20 Autores', fontsize=11)
        plt.xticks(rotation=35, rotation_mode='anchor', ha='right', fontsize=9)
        plt.yticks(fontsize=9)
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.bar_label(bars, fontsize=9)
        plt.tight_layout()
        plt.savefig('distrib_top20_autores.png')
        plt.show()


    def distrib_autor_ano(bd):
        d = {}
        autor = input("Pretende calcular a distribuição de publicações por ano de que autor? ").strip()
        if autor:
            for publi in bd:
                for author in publi.get('authors', ''):
                    if author.get('name', 'Sem data') == autor:
                        ano = publi.get('publish_date', 'Sem data').split("-")[0]
                        if ano not in d:
                            d[ano] = 1
                        else:
                            d[ano] += 1
        else:
            print("Não foi introduzido nenhum autor. Operação cancelada.")
            return

        if d:
            print("Ordenar por:")
            print("1. Ano")
            print("2. Número de Publicações")
            escolha = input("Escolha uma opção (1 ou 2): ").strip()
            if escolha == '1':
                lista = sorted(d.items())
            elif escolha == '2':
                lista = sorted(d.items(), key=fpj.topordena, reverse=True)
            else:
                print("Opção inválida. Operação cancelada.")
                return

            sorted_dict = dict(lista)
            mostrar_resultados(lista)
            graf_distrib_autor_ano(sorted_dict)

            salvar = input("Desejas salvar o relatório? (s/n): ").strip().lower()
            if salvar == 's':
                nome_arquivo = input("Insere o nome do arquivo (exemplo: distrib_autor_ano.json): ").strip()
                if not nome_arquivo:
                    nome_arquivo = 'distrib_autor_ano.json'
                fpj.salvar_em_arquivo_comandos(dict(lista), nome_arquivo)
                grafico_arquivo = nome_arquivo.replace('.json', '.png')
                os.rename('distrib_autor_ano.png', grafico_arquivo)
                print(f"Relatório salvo em {nome_arquivo} e gráfico salvo em {grafico_arquivo}")  
            else:
                print("Operação cancelada.")
                
        else:
            sorted_dict = {}
            print("Nenhum dado encontrado. Tente novamente.")
            

        return sorted_dict

    def graf_distrib_autor_ano(d):
        plt.clf()
        anos = list(d.keys())
        publicacoes = list(d.values())
        bars = plt.bar(anos, publicacoes, color='skyblue', width=0.5)
        plt.xlabel('Anos', fontsize=11)
        plt.ylabel('Nº de Publicações', fontsize=11)
        plt.title(f'Distribuição de publicações por ano', fontsize=11)
        plt.xticks(rotation=35, rotation_mode='anchor', ha='right')
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.bar_label(bars, fontsize=9)
        plt.tight_layout()
        plt.savefig('distrib_autor_ano.png')
        plt.show()

    def distrib_top20_keywords(bd):
        d = {}
        for publi in bd:
            for palavra in publi.get('keywords', 'Sem palavra').split(', '):
                if palavra not in d:
                    d[palavra] = 1
                else:
                    d[palavra] += 1
        lista = sorted(list(d.items()), key=fpj.topordena, reverse=True) 
        lista = lista[1:21]
        d = dict(lista)

        sorted_dict = dict(lista)
        mostrar_resultados(lista)
        graf_distrib_top20_keywords(sorted_dict)

        salvar = input("Desejas salvar o relatório? (s/n): ").strip().lower()
        if salvar == 's':
            nome_arquivo = input("Insere o nome do arquivo (exemplo: top20_keywords.json): ").strip()
            if not nome_arquivo:
                nome_arquivo = 'top20_keywords.json'
            fpj.salvar_em_arquivo_comandos(dict(lista), nome_arquivo)
            grafico_arquivo = nome_arquivo.replace('.json', '.png')
            os.rename('distrib_top20_keywords.png', grafico_arquivo)
            print(f"Relatório salvo em {nome_arquivo} e gráfico salvo em {grafico_arquivo}")  
        else:
            print("Operação cancelada.")

        return d

    def graf_distrib_top20_keywords(d):
        plt.clf()
        keywords = list(d.keys())
        publicacoes = list(d.values())
        bars = plt.bar(keywords, publicacoes, color='skyblue', width=0.5)
        plt.xlabel('Keywords', fontsize=11)
        plt.ylabel('Nº de Publicações', fontsize=11)
        plt.title('TOP20 Keywords', fontsize=11)
        plt.xticks(rotation=35, rotation_mode='anchor', ha='right', fontsize=9)
        plt.yticks(fontsize=9)
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.bar_label(bars, fontsize=9)
        plt.tight_layout()
        plt.savefig('distrib_top20_keywords.png')
        plt.show()


    def distrib_keyword_ano(bd):
        d = {}
        kw = input("Pretende calcular a distribuição de publicações por ano de que KeyWord? ").strip()
        if kw:
            for publi in bd:
                for palavra in publi.get('keywords', 'Sem data').split(', '):
                    if palavra == kw:
                        ano = publi.get('publish_date', 'Sem data').split("-")[0]
                        if ano not in d:
                            d[ano] = 1
                        else:
                            d[ano] += 1
        else:
            print("Não foi introduzido nenhuma KeyWord. Operação cancelada.")
            return

        if d:
            print("Ordenar por:")
            print("1. Ano")
            print("2. Número de Publicações")
            escolha = input("Escolha uma opção (1 ou 2): ").strip()
            if escolha == '1':
                lista = sorted(d.items())
            elif escolha == '2':
                lista = sorted(d.items(), key=fpj.topordena, reverse=True)
            else:
                print("Opção inválida. Operação cancelada.")
                return

            sorted_dict = dict(lista)
            mostrar_resultados(lista)
            graf_distrib_keyword_ano(sorted_dict)

            salvar = input("Desejas salvar o relatório? (s/n): ").strip().lower()
            if salvar == 's':
                nome_arquivo = input("Insere o nome do arquivo (exemplo: distrib_keyword_ano.json): ").strip()
                if not nome_arquivo:
                    nome_arquivo = 'distrib_keyword_ano.json'
                fpj.salvar_em_arquivo_comandos(dict(lista), nome_arquivo)
                grafico_arquivo = nome_arquivo.replace('.json', '.png')
                os.rename('distrib_keyword_ano.png', grafico_arquivo)
                print(f"Relatório salvo em {nome_arquivo} e gráfico salvo em {grafico_arquivo}")  
            else:
                print("Operação cancelada.")
        else:
            sorted_dict = {}
            print("Nenhum dado encontrado. Tente novamente.")
        return sorted_dict
    
    def graf_distrib_keyword_ano(d):
        plt.clf()
        anos = list(d.keys())
        publicacoes = list(d.values())
        bars = plt.bar(anos, publicacoes, color='skyblue', width=0.5)
        plt.xlabel('Anos', fontsize=11)
        plt.ylabel('Nº de Publicações', fontsize=11)
        plt.title(f'Distribuição anual da keyword', fontsize=11)
        plt.xticks(rotation=35, rotation_mode='anchor', ha='right')
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.bar_label(bars, fontsize=9)
        plt.tight_layout()
        plt.savefig('distrib_keyword_ano.png')
        plt.show()

    def menu_estatisticas(bd):
        executando = True
        while executando:
            print("\n===== Relatórios de estatísticas =====")
            print("Escolha o tipo de distribuição:")
            print("1) Por Ano ")
            print("2) Por Mês no Ano ") 
            print("3) Pelos TOP20 Autores ")   
            print("4) Por Autor de x Ano ")
            print("5) Pelas TOP20 Keywords ")
            print("6) Por ano da Keyword x ")
            print("7) Help ")
            print("0) Sair ") 

            escolha = (input("Escolha uma opção de gráfico de distribuição: ")).strip()
            if escolha == "1":
                distrib_ano(bd)
            elif escolha == "2":
                distrib_mes_ano(bd)
            elif escolha == "3":
                distrib_top20_autor(bd)
            elif escolha == "4":
                distrib_autor_ano(bd)
            elif escolha == "5":
                distrib_top20_keywords(bd)
            elif escolha == "6":
                distrib_keyword_ano(bd)
            elif escolha == "7":
                help_estatísticas()
            elif escolha == "0":
                executando = False
            else:
                print("Opção inválida. Tente novamente.")
    

    def importar_dataset(dataset):
        ficheiro = input('Selecione o ficheiro JSON para importar: ').strip()
        if ficheiro:
            if not ficheiro.lower().endswith('.json'):
                print("Erro: O arquivo não possui extensão .json.")
                return None
            try:
                with open(ficheiro, 'r', encoding='utf-8') as f:
                    dataset_importado = json.load(f)
                    if dataset_importado:
                        titulos_existentes = [publi.get('title') for publi in dataset]
                        novas_publis = [publi for publi in dataset_importado if publi.get('title') not in titulos_existentes]
                        if novas_publis:
                            dataset += novas_publis
                            print(f'Dataset importado!\nForam lidos {len(novas_publis)} registos.\nO dataset agora tem {len(dataset)} registos.')
                        else:
                            print(f'Nenhum novo registo foi adicionado.\nTodas as publicações já estão presentes no dataset.\nO dataset continua com {len(dataset)} registos.')
                    else:
                        print("O arquivo selecionado está vazio ou não contém publicações válidas.")
            except Exception as e:
                print(f'Erro ao carregar o dataset: {e}. Por favor, tente novamente.')
                return importar_dataset(dataset) 
        else:
            print("Nenhum arquivo foi selecionado. Por favor, selecione um arquivo JSON.")
            return importar_dataset(dataset)  


    def exportar_dados(dataset):
        nome_arquivo = input("Nomeie o arquivo para salvar os dados em memória (exemplo: resultados.json): ").strip()
        if nome_arquivo:
            if not nome_arquivo.lower().endswith('.json'):
                print("Erro: O nome do arquivo deve ter a extensão .json. Por favor, tente novamente.")
                return None  
            else:
                fpj.salvar_em_arquivo_comandos(dataset, nome_arquivo)
                print(f"Dados salvos em {nome_arquivo}.")
        else:
            print("Nome do arquivo não fornecido. Operação cancelada.")

            

    def menu():
        print("\n=== Menu ===")
        print("1. Carregar Dataset")
        print("2. Criar publicação")
        print("3. Eliminar publicação")
        print("4. Consultar publicação")
        print("5. Listar Autores")
        print("6. Listar Keywords")
        print("7. Estatísticas")
        print("8. Importar dados")
        print("9. Guardar dados")
        print("10. Help")
        print("0. Sair")

    carregada_e_guardada = False
    publicacoes = []
    executando = True
    while executando:
        menu()
        op = input("Escolha uma opção: ").strip()
        if op == '0':
            print("Saiu do sistema!")
            executando = False
        elif op == '1':
            publicacoes = carregar_dataset()
            if publicacoes:
                carregada_e_guardada = True
                print("Dataset carregado com sucesso.")
            else:
                carregada_e_guardada = False
        elif op == '2':
            if carregada_e_guardada:
                criar_publi(publicacoes)
            else:
                print("Carregue e salve uma base de dados primeiro.")
        elif op == '3':
            if carregada_e_guardada:
                eliminar_publi(publicacoes)
            else:
                print("Carregue e salve uma base de dados primeiro.")
        elif op == '4':
            if carregada_e_guardada:
                consultar_publicação(publicacoes)
            else:
                print("Carregue e salve uma base de dados primeiro.")
        elif op == '5':
            if carregada_e_guardada:
                listaAutores(publicacoes)
            else:
                print("Carregue e salve uma base de dados primeiro.")
        elif op == '6':
            if carregada_e_guardada:
                listaKeywords(publicacoes)
            else:
                print("Carregue e salve uma base de dados primeiro.")
        elif op == '7':
            if carregada_e_guardada:
                menu_estatisticas(publicacoes)
            else:
                print("Carregue e salve uma base de dados primeiro.")
        elif op == '8':
            if carregada_e_guardada:
                importar_dataset(publicacoes)
            else:
                print("Carregue e salve uma base de dados primeiro.")
        elif op == '9':
            if carregada_e_guardada:
                exportar_dados(publicacoes)
            else:
                print("Carregue e salve uma base de dados primeiro.")
        elif op == '10':
            exibir_help()
        else:
            print("Opção inválida. Tente novamente.")

    exit()


sg.theme('LightGreen1')
cor_clara = sg.theme_background_color()
cor_escura = sg.theme_button_color()[1]

layout_escolherinterface = [
    [sg.Push(background_color=cor_clara),
     sg.Button('Interface Gráfica', size=(30, 2), font=("Cooper Hewitt", 14), button_color=(cor_clara, cor_escura),
               tooltip='Clique para escolher Interface Gráfica', key='Interface Gráfica'),
     sg.Button("Interface Linha de Comandos (CLI)", size=(30, 2), font=("Cooper Hewitt", 14), button_color=(cor_clara, cor_escura),
               tooltip='Clique para escolher CLI', key='Interface Linha de Comandos'),
     sg.Push(background_color=cor_clara)]
]

cabecalhointerfaces = [
    [sg.Text("Escolha uma Interface", size=(35, 1), expand_x=True, justification="center", font=("Cambria", 32, "bold"),
             background_color=cor_clara, text_color=cor_escura)],
    [sg.Text("MENU", size=(35, 1), expand_x=True, justification="center", font=("Cambria", 20),
             background_color=cor_clara, text_color=cor_escura)],
    [sg.Push(background_color=cor_clara),
     sg.Text('  ' * 205, justification="center", background_color=cor_escura, pad=(0, 15)),
     sg.Push(background_color=cor_clara)]
]

layoutfinal = [
    cabecalhointerfaces,
    layout_escolherinterface,
    [sg.Push(background_color=cor_clara), sg.Text('  ' * 205, justification="center", background_color=cor_escura, pad=(0, 15)), sg.Push(background_color=cor_clara)],
    [sg.Button("Sair", size=(20, 1), font=("Cooper Hewitt", 18), button_color=(cor_escura, cor_clara),
               tooltip='Clique para sair da aplicação')]
]

window_escolherinterface = sg.Window(title="Escolha uma interface", resizable=True, background_color=cor_clara, layout=layoutfinal)

stop = False
while not stop:
    eventosinterfaces, valoresinterfaces = window_escolherinterface.read()
    if eventosinterfaces == sg.WIN_CLOSED or eventosinterfaces == "Sair":
        stop = True
        window_escolherinterface.close()
    elif eventosinterfaces == 'Interface Gráfica':
        window_escolherinterface.close()
        interfaceGrafica()
        stop = True
    elif eventosinterfaces == 'Interface Linha de Comandos':
        window_escolherinterface.close()
        interfacelinhadecomandos()
        stop = True