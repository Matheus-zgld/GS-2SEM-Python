#Nome e RM: Matheus Henrique Ferreira Camargo da Silva - RM 566232

import os
import time
import random

db_usuarios = {
    "ana.silva": {
        "email": "ana@fiap.com.br",
        "senha": "123",
        "nome_completo": "Ana Silva",
        "titulo_profissional": "Assistente Administrativo | Buscando transição",
        "cargo_atual_ia_bot": "assistente administrativo",
        "biografia": "Profissional organizada, aprendendo Python e Ética de IA.",
        "habilidades": {
            "pacote_office": {"endossos": ["bruno.costa"]},
            "comunicacao": {"endossos": []},
            "organizacao": {"endossos": ["bruno.costa", "admin"]},
        },
        "seguindo": ["bruno.costa"],
        "seguidores": ["bruno.costa", "admin"],
        "role": "usuario"
    },
    "bruno.costa": {
        "email": "bruno@fiap.com.br",
        "senha": "456",
        "nome_completo": "Bruno Costa",
        "titulo_profissional": "Desenvolvedor Júnior | Especialista em Python",
        "cargo_atual_ia_bot": "desenvolvedor júnior",
        "biografia": "Entusiasta de IA e Realidade Virtual. Mentor na FIAP.",
        "habilidades": {
            "python": {"endossos": ["ana.silva", "admin"]},
            "git": {"endossos": ["admin"]},
            "sql": {"endossos": []},
            "ia": {"endossos": []}
        },
        "seguindo": ["ana.silva", "admin"],
        "seguidores": ["ana.silva"],
        "role": "usuario"
    },
    "admin": {
        "email": "admin@fiap.com.br",
        "senha": "admin",
        "nome_completo": "Admin SYNAPSE",
        "titulo_profissional": "Administrador da Plataforma",
        "cargo_atual_ia_bot": "admin",
        "biografia": "Gerenciando a rede do futuro.",
        "habilidades": {"gestao_sistema": {"endossos": []}},
        "seguindo": ["ana.silva", "bruno.costa"],
        "seguidores": ["ana.silva", "bruno.costa"],
        "role": "admin"
    }
}

db_profissoes_futuro = {
    "P1": {
        "titulo": "Analista de Ética de IA",
        "descricao": "Garante que os sistemas de IA sejam justos, transparentes e imparciais.",
        "habilidades_necessarias": ["etica", "ia", "pensamento_critico", "legislacao_digital", "comunicacao"]
    },
    "P2": {
        "titulo": "Especialista em Transição Verde",
        "descricao": "Ajuda empresas a migrarem para modelos de negócio sustentáveis.",
        "habilidades_necessarias": ["sustentabilidade", "gestao_projetos", "economia_verde", "relatorios_esg"]
    },
    "P3": {
        "titulo": "Engenheiro de Ambientes Imersivos",
        "descricao": "Cria e mantém ambientes de trabalho em Realidade Virtual/Aumentada.",
        "habilidades_necessarias": ["realidade_virtual", "realidade_aumentada", "unity", "design_3d", "python"]
    },
    "P4": {
        "titulo": "Detetive de Dados (Data Detective)",
        "descricao": "Investiga e interpreta grandes volumes de dados para gerar insights de negócios.",
        "habilidades_necessarias": ["analise_dados", "sql", "python", "power_bi", "pensamento_critico"]
    }
}

db_cursos_reskilling = {
    "etica": {"titulo": "Curso de Ética Aplicada à IA", "fonte": "FIAP Academy (Mock)"},
    "ia": {"titulo": "Fundamentos de Inteligência Artificial", "fonte": "FIAP ON (Mock)"},
    "pensamento_critico": {"titulo": "Workshop de Pensamento Crítico", "fonte": "LinkedIn Learning (Mock)"},
    "legislacao_digital": {"titulo": "Introdução ao LGPD e Direito Digital", "fonte": "Alura (Mock)"},
    "sustentabilidade": {"titulo": "Princípios de Sustentabilidade Corporativa", "fonte": "Coursera (Mock)"},
    "gestao_projetos": {"titulo": "Certificação PMP/Agile", "fonte": "PMI (Mock)"},
    "economia_verde": {"titulo": "Finanças Verdes e Impacto", "fonte": "EdX (Mock)"},
    "relatorios_esg": {"titulo": "Como elaborar Relatórios ESG", "fonte": "FGV (Mock)"},
    "realidade_virtual": {"titulo": "Desenvolvimento VR com Unity", "fonte": "Udemy (Mock)"},
    "realidade_aumentada": {"titulo": "Bootcamp de Filtros e AR", "fonte": "Meta Spark (Mock)"},
    "unity": {"titulo": "Curso Completo de Unity 3D", "fonte": "FIAP (Mock)"},
    "design_3d": {"titulo": "Modelagem 3D com Blender", "fonte": "Pluralsight (Mock)"},
    "python": {"titulo": "Python para Data Science e IA", "fonte": "FIAP ON (Mock)"},
    "analise_dados": {"titulo": "Formação em Análise de Dados", "fonte": "Alura (Mock)"},
    "sql": {"titulo": "SQL para Análise de Dados", "fonte": "DataCamp (Mock)"},
    "power_bi": {"titulo": "Visualização de Dados com Power BI", "fonte": "Udemy (Mock)"}
}

db_risco_automacao = {
    "assistente administrativo": {"risco": "Alto", "sugestao_migracao": "P4"},
    "atendente de telemarketing": {"risco": "Alto", "sugestao_migracao": "P1"},
    "operador de caixa": {"risco": "Alto", "sugestao_migracao": "P2"},
    "desenvolvedor júnior": {"risco": "Baixo", "sugestao_migracao": "P3"},
    "estudante": {"risco": "N/A", "sugestao_migracao": "P1"},
    "admin": {"risco": "N/A", "sugestao_migracao": "P1"},
}

db_posts = {
    "post_001": {
        "autor_username": "bruno.costa",
        "timestamp": "12/11/2025 10:30",
        "conteudo": "Acabei de finalizar meu projeto em Python para a GS! Usei IA para analisar tendências de mercado. #python #ia #fiap",
        "curtidas": ["ana.silva", "admin"],
        "comentarios": [
            {"username": "ana.silva", "comentario": "Parabéns, Bruno! Deve ter ficado incrível!"},
            {"username": "synapse_bot", "comentario": "IA é uma habilidade essencial para o 'Analista de Ética de IA'. Continue assim!"}
        ]
    },
    "post_002": {
        "autor_username": "ana.silva",
        "timestamp": "12/11/2025 14:00",
        "conteudo": "Iniciando hoje o curso de 'Fundamentos de IA' da FIAP ON. Um pouco nervosa, mas animada para o reskilling! #futurodotrabalho #ia",
        "curtidas": ["bruno.costa"],
        "comentarios": []
    }
}

db_projetos = {
    "proj_001": {
        "autor_username": "bruno.costa",
        "titulo": "GS 1ES - Análise de Tendências",
        "descricao": "Sistema em Python que usa IA para prever tendências de mercado.",
        "habilidades_tags": ["python", "ia", "analise_dados"]
    }
}

db_trilhas = {
    "trilha_001": {
        "autor_username": "bruno.costa",
        "titulo": "Trilha para Engenheiro de Ambientes Imersivos",
        "descricao": "Meu caminho para aprender a criar mundos em VR.",
        "etapas": [
            {"tipo": "curso", "id_curso": "python", "obs": "Base de tudo"},
            {"tipo": "curso", "id_curso": "realidade_virtual", "obs": "Conceitos de VR/AR"},
            {"tipo": "projeto", "titulo_projeto": "Meu primeiro ambiente no Unity"}
        ]
    }
}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def aguarde(segundos=2):
    time.sleep(segundos)

def validar_input(mensagem, tipo="str"):
    while True:
        entrada = input(mensagem).strip()
        if not entrada:
            print("❌ Erro: Esta entrada não pode ficar vazia. Tente novamente.")
        elif tipo == "email" and "@" not in entrada:
            print("❌ Erro: Formato de e-mail inválido. Tente novamente.")
        elif tipo == "username" and " " in entrada:
            print("❌ Erro: Username não pode conter espaços. Tente novamente.")
        else:
            return entrada

def obter_escolha_menu(max_opcao):
    while True:
        try:
            escolha = int(input("➡️ Digite sua opção: "))
            if 0 <= escolha <= max_opcao:
                return escolha
            else:
                print(f"❌ Opção inválida! Digite um número entre 0 e {max_opcao}.")
        except ValueError:
            print("❌ Erro: Por favor, digite apenas números.")
            aguarde(1)

def gerar_id_unico(prefixo, db):
    while True:
        novo_id = f"{prefixo}_{random.randint(100, 999)}"
        if novo_id not in db:
            return novo_id

def cadastrar_usuario(db_usuarios):
    limpar_tela()
    print("--- 🆕 CADASTRO DE NOVO USUÁRIO (SYNAPSE) ---")
    
    while True:
        email = validar_input("Digite seu e-mail: ", "email").lower()
        if any(u['email'] == email for u in db_usuarios.values()):
            print("❌ Erro: Este e-mail já está cadastrado.")
        else:
            break
            
    while True:
        username = validar_input("Crie um username (ex: ana.silva): ", "username").lower()
        if username in db_usuarios:
            print("❌ Erro: Este username já está em uso.")
        else:
            break

    while True:
        senha = validar_input("Crie uma senha (mín. 6 caracteres): ")
        if len(senha) < 6:
            print("❌ Erro: A senha deve ter no mínimo 6 caracteres.")
        else:
            senha_confirma = validar_input("Confirme sua senha: ")
            if senha != senha_confirma:
                print("❌ Erro: As senhas não coincidem.")
            else:
                break
                
    nome_completo = validar_input("Seu nome completo: ")
    titulo_profissional = validar_input("Seu título profissional (ex: Estudante): ")
    cargo_atual_ia_bot = validar_input("Seu cargo para o Bot de IA (ex: assistente administrativo): ").lower()

    db_usuarios[username] = {
        "email": email,
        "senha": senha,
        "nome_completo": nome_completo,
        "titulo_profissional": titulo_profissional,
        "cargo_atual_ia_bot": cargo_atual_ia_bot,
        "biografia": "Olá! Sou novo(a) no SYNAPSE.",
        "habilidades": {},
        "seguindo": [],
        "seguidores": [],
        "role": "usuario"
    }
    
    print(f"\n✅ Usuário {username} cadastrado com sucesso!")
    aguarde()

def realizar_login(db_usuarios):
    limpar_tela()
    print("--- 🔑 LOGIN NO SYNAPSE ---")
    
    login = validar_input("Digite seu username ou e-mail: ").lower()
    senha = validar_input("Digite sua senha: ")
    
    usuario_encontrado = None
    
    if login in db_usuarios:
        if db_usuarios[login]["senha"] == senha:
            usuario_encontrado = login
    
    if not usuario_encontrado:
        for username, dados in db_usuarios.items():
            if dados["email"] == login and dados["senha"] == senha:
                usuario_encontrado = username
                break

    if usuario_encontrado:
        print(f"\n✅ Login bem-sucedido! Bem-vindo(a), {db_usuarios[usuario_encontrado]['nome_completo'].split()[0]}.")
        aguarde()
        return usuario_encontrado
    else:
        print("\n❌ Erro: Username/e-mail ou senha incorretos.")
        aguarde()
        return None

def editar_perfil(username_logado, db_usuarios):
    limpar_tela()
    print("--- ✍️ EDITAR PERFIL ---")
    usuario = db_usuarios[username_logado]
    
    print("Deixe em branco para manter a informação atual.\n")
    
    novo_titulo = input(f"Título Profissional ({usuario['titulo_profissional']}): ").strip()
    if novo_titulo:
        usuario['titulo_profissional'] = novo_titulo
        print("   -> Título atualizado!")

    nova_bio = input(f"Biografia ({usuario['biografia']}): ").strip()
    if nova_bio:
        usuario['biografia'] = nova_bio
        print("   -> Biografia atualizada!")
    
    novo_cargo_bot = input(f"Cargo para IA-Bot ({usuario['cargo_atual_ia_bot']}): ").strip().lower()
    if novo_cargo_bot:
        usuario['cargo_atual_ia_bot'] = novo_cargo_bot
        print("   -> Cargo para IA-Bot atualizado!")
        
    print("\n✅ Perfil salvo com sucesso!")
    aguarde()

def gerenciar_habilidades(username_logado, db_usuarios):
    limpar_tela()
    print("--- 🛠️ GERENCIAR HABILIDADES ---")
    habilidades = db_usuarios[username_logado]['habilidades']
    
    print("Suas Habilidades Atuais:")
    if not habilidades:
        print("   (Nenhuma habilidade cadastrada)")
    else:
        for hab, dados in habilidades.items():
            print(f"   • {hab.capitalize()} (Endossos: {len(dados['endossos'])})")
            
    print("\n1. ➕ Adicionar Habilidade")
    print("2. ➖ Remover Habilidade")
    print("0. Voltar")
    escolha = obter_escolha_menu(2)
    
    if escolha == 1:
        hab_nova = validar_input("Habilidade a adicionar (ex: python, ia): ").lower().replace(" ", "_")
        if hab_nova in habilidades:
            print("❌ Erro: Você já possui essa habilidade.")
        else:
            habilidades[hab_nova] = {"endossos": []}
            print("✅ Habilidade adicionada!")
            print("   -> Publicando no feed da sua rede...")
    elif escolha == 2:
        hab_remover = validar_input("Habilidade a remover: ").lower().replace(" ", "_")
        if hab_remover not in habilidades:
            print("❌ Erro: Habilidade não encontrada.")
        else:
            del habilidades[hab_remover]
            print("✅ Habilidade removida!")
    aguarde()

def menu_meu_perfil(username_logado, db_usuarios):
    while True:
        limpar_tela()
        print("--- 👤 MEU PERFIL SYNAPSE ---")
        print("1. 👁️ Visualizar Meu Perfil (Como os outros veem)")
        print("2. ✍️ Editar Perfil (Título, Bio, Cargo-Bot)")
        print("3. 🛠️ Gerenciar Habilidades (Adicionar/Remover)")
        print("0. Voltar ao Menu Principal")
        
        escolha = obter_escolha_menu(3)
        if escolha == 1:
            visualizar_perfil_usuario(username_logado, username_logado, db_usuarios, db_projetos)
        elif escolha == 2:
            editar_perfil(username_logado, db_usuarios)
        elif escolha == 3:
            gerenciar_habilidades(username_logado, db_usuarios)
        elif escolha == 0:
            break

def criar_post(username_logado, db_posts):
    limpar_tela()
    print("--- 💬 NOVO POST NO SYNAPSE ---")
    
    while True:
        conteudo = input("O que você está pensando? (Máx 500 caracteres)\n> ")
        if not conteudo:
            print("❌ Erro: O post não pode estar vazio.")
        elif len(conteudo) > 500:
            print(f"❌ Erro: Limite de 500 caracteres excedido. (Você digitou {len(conteudo)})")
        else:
            break
            
    novo_post_id = gerar_id_unico("post", db_posts)
    db_posts[novo_post_id] = {
        "autor_username": username_logado,
        "timestamp": time.strftime("%d/%m/%Y %H:%M"),
        "conteudo": conteudo,
        "curtidas": [],
        "comentarios": []
    }
    
    print("\n✅ Post publicado com sucesso no seu feed!")
    
    if " ia " in conteudo.lower() or " automação " in conteudo.lower() or "python" in conteudo.lower():
        print("   -> 🤖 SYNAPSE-BOT está analisando seu post...")
        aguarde(1)
        db_posts[novo_post_id]["comentarios"].append({
            "username": "synapse_bot",
            "comentario": "Post relevante! Habilidades em IA e Python são cruciais para o futuro. Confira as profissões P1 e P3."
        })
        print("   -> 🤖 SYNAPSE-BOT comentou no seu post!")
        
    aguarde()

def visualizar_feed(username_logado, db_usuarios, db_posts):
    limpar_tela()
    print("--- 📰 SEU FEED SYNAPSE ---")
    print("Mostrando posts de quem você segue...\n")
    
    seguindo = db_usuarios[username_logado]["seguindo"]
    seguindo.append(username_logado)
    
    posts_no_feed = []
    for post_id, post in db_posts.items():
        if post["autor_username"] in seguindo:
            posts_no_feed.append((post_id, post))

    if not posts_no_feed:
        print("Seu feed está vazio. Siga pessoas ou crie um post!")
        aguarde()
        return

    posts_no_feed.sort(key=lambda x: x[1]['timestamp'], reverse=True)
    
    while True:
        limpar_tela()
        print("--- 📰 SEU FEED SYNAPSE ---")
        
        opcoes_posts = {}
        idx = 1
        for post_id, post in posts_no_feed:
            autor_nome = db_usuarios[post["autor_username"]]["nome_completo"]
            ja_curtiu = "❤️" if username_logado in post["curtidas"] else "🤍"
            
            print("--------------------------------------------------")
            print(f"[{idx}] Post de @{post['autor_username']} ({autor_nome})")
            print(f"    Em: {post['timestamp']}")
            print(f"\n    {post['conteudo']}\n")
            print(f"    {ja_curtiu} {len(post['curtidas'])} Curtidas  |  💬 {len(post['comentarios'])} Comentários")
            
            if post["comentarios"]:
                for com in post["comentarios"][:2]:
                    print(f"      -> @{com['username']}: {com['comentario']}")
                if len(post["comentarios"]) > 2:
                    print(f"      ... (e mais {len(post['comentarios']) - 2})")
            
            opcoes_posts[idx] = post_id
            idx += 1
        
        print("--------------------------------------------------")
        print("\nEscolha um post para interagir (1, 2, ...)")
        print(f"Ou digite [D] para Deletar um post seu.")
        print("Ou digite [0] para Voltar.")
        
        escolha = input("➡️ Digite sua opção: ").strip().lower()
        
        if escolha == '0':
            break
        elif escolha == 'd':
            deletar_post(username_logado, db_posts)
            visualizar_feed(username_logado, db_usuarios, db_posts)
            break
            
        try:
            escolha_int = int(escolha)
            if escolha_int in opcoes_posts:
                post_id_selecionado = opcoes_posts[escolha_int]
                interagir_post(username_logado, post_id_selecionado, db_posts)
            else:
                print("❌ Opção inválida.")
                aguarde(1)
        except ValueError:
            print("❌ Opção inválida.")
            aguarde(1)

def interagir_post(username_logado, post_id, db_posts):
    post = db_posts[post_id]
    autor_username = post["autor_username"]
    
    while True:
        limpar_tela()
        print(f"--- Interagindo com Post de @{autor_username} ---")
        print(f"    {post['conteudo']}\n")
        
        print("Comentários:")
        if not post["comentarios"]:
            print("   (Seja o primeiro a comentar!)")
        else:
            for com in post["comentarios"]:
                print(f"   -> @{com['username']}: {com['comentario']}")
        
        print("\n1. ❤️ Curtir / Descurtir")
        print("2. 💬 Comentar")
        print("0. Voltar ao Feed")
        escolha = obter_escolha_menu(2)
        
        if escolha == 1:
            if username_logado in post["curtidas"]:
                post["curtidas"].remove(username_logado)
                print("   -> 🤍 Descurtido.")
            else:
                post["curtidas"].append(username_logado)
                print("   -> ❤️ Curtido!")
            aguarde(1)
        elif escolha == 2:
            comentario = validar_input("Seu comentário: ")
            post["comentarios"].append({"username": username_logado, "comentario": comentario})
            print("   -> 💬 Comentário adicionado!")
            aguarde(1)
        elif escolha == 0:
            break

def deletar_post(username_logado, db_posts):
    print("\n--- 🗑️ DELETAR POST ---")
    posts_do_usuario = []
    for post_id, post in db_posts.items():
        if post["autor_username"] == username_logado:
            posts_do_usuario.append((post_id, post))
            
    if not posts_do_usuario:
        print("Você não tem posts para deletar.")
        aguarde()
        return

    print("Seus Posts:")
    opcoes_delete = {}
    for idx, (post_id, post) in enumerate(posts_do_usuario, 1):
        print(f"   [{idx}] {post['conteudo'][:40]}... ({post['timestamp']})")
        opcoes_delete[idx] = post_id
    
    print("\n[0] Cancelar")
    escolha = obter_escolha_menu(len(opcoes_delete))
    
    if escolha == 0:
        return
        
    post_id_deletar = opcoes_delete[escolha]
    
    confirmar = validar_input(f"Tem certeza que quer deletar o post {escolha}? (s/n): ").lower()
    if confirmar == 's':
        del db_posts[post_id_deletar]
        print("✅ Post deletado com sucesso.")
    else:
        print("Operação cancelada.")
    aguarde()

def buscar_usuarios(username_logado, db_usuarios):
    limpar_tela()
    print("--- 🔍 BUSCAR PROFISSIONAIS ---")
    print("1. Buscar por Nome ou Username")
    print("2. 🌟 Buscar por Habilidade (Skill)")
    print("0. Voltar")
    escolha_busca = obter_escolha_menu(2)
    
    if escolha_busca == 0:
        return
        
    termo_busca = validar_input("Digite o termo de busca: ").lower()
    
    resultados = []
    if escolha_busca == 1:
        for username, dados in db_usuarios.items():
            if (termo_busca in username.lower() or termo_busca in dados["nome_completo"].lower()) and username != username_logado:
                resultados.append(username)
    
    elif escolha_busca == 2:
        for username, dados in db_usuarios.items():
            if termo_busca in dados["habilidades"] and username != username_logado:
                resultados.append(username)
                
    if not resultados:
        print(f"\nNenhum profissional encontrado com o termo '{termo_busca}'.")
        aguarde()
        return

    print(f"\n--- 🔎 Resultados para '{termo_busca}' ---")
    opcoes_perfil = {}
    for idx, username in enumerate(resultados, 1):
        dados = db_usuarios[username]
        print(f"[{idx}] {dados['nome_completo']} (@{username})")
        print(f"    {dados['titulo_profissional']}")
        opcoes_perfil[idx] = username
        
    print("\n[0] Voltar")
    escolha_perfil = obter_escolha_menu(len(opcoes_perfil))
    
    if escolha_perfil > 0:
        username_alvo = opcoes_perfil[escolha_perfil]
        visualizar_perfil_usuario(username_logado, username_alvo, db_usuarios, db_projetos)

def visualizar_perfil_usuario(username_logado, username_alvo, db_usuarios, db_projetos):
    while True:
        limpar_tela()
        usuario_alvo = db_usuarios[username_alvo]
        
        print(f"--- Perfil de @{username_alvo} ---")
        print(f"Nome: {usuario_alvo['nome_completo']}")
        print(f"Título: {usuario_alvo['titulo_profissional']}")
        print(f"\nBiografia: {usuario_alvo['biografia']}")
        
        print("\n--- Habilidades ---")
        habilidades = usuario_alvo['habilidades']
        if not habilidades:
            print("   (Nenhuma habilidade cadastrada)")
        else:
            for hab, dados in habilidades.items():
                endossado_por_mim = "⭐" if username_logado in dados["endossos"] else ""
                print(f"   • {hab.capitalize()} (Endossos: {len(dados['endossos'])}) {endossado_por_mim}")

        print("\n--- Projetos ---")
        projetos_usuario = [p for p in db_projetos.values() if p['autor_username'] == username_alvo]
        if not projetos_usuario:
            print("   (Nenhum projeto cadastrado)")
        else:
            for proj in projetos_usuario:
                print(f"   • {proj['titulo']} (Skills: {', '.join(proj['habilidades_tags'])})")
                
        print("\n--- Rede ---")
        print(f"Seguindo: {len(usuario_alvo['seguindo'])} | Seguidores: {len(usuario_alvo['seguidores'])}")

        if username_logado == username_alvo:
            print("\n(Este é o seu perfil. Use o menu 'Meu Perfil' para editar.)")
            print("\n0. Voltar")
            obter_escolha_menu(0)
            break
        
        print("\n--- Ações ---")
        esta_seguindo = username_logado in usuario_alvo["seguidores"]
        if esta_seguindo:
            print("1. 🚫 Deixar de Seguir")
        else:
            print("1. ✅ Seguir")
            
        print("2. 🌟 Endossar Habilidade")
        print("0. Voltar")
        
        escolha = obter_escolha_menu(2)
        
        if escolha == 1:
            if esta_seguindo:
                db_usuarios[username_logado]["seguindo"].remove(username_alvo)
                db_usuarios[username_alvo]["seguidores"].remove(username_logado)
                print(f"🚫 Você deixou de seguir @{username_alvo}.")
            else:
                db_usuarios[username_logado]["seguindo"].append(username_alvo)
                db_usuarios[username_alvo]["seguidores"].append(username_logado)
                print(f"✅ Você agora está seguindo @{username_alvo}!")
            aguarde(1)
            
        elif escolha == 2:
            print("Qual habilidade você quer endossar?")
            hab_endossar = validar_input("> ").lower()
            if hab_endossar not in usuario_alvo["habilidades"]:
                print("❌ Habilidade não encontrada no perfil.")
            elif username_logado in usuario_alvo["habilidades"][hab_endossar]["endossos"]:
                print("❌ Você já endossou essa habilidade.")
            else:
                usuario_alvo["habilidades"][hab_endossar]["endossos"].append(username_logado)
                print(f"🌟 Você endossou @{username_alvo} em '{hab_endossar}'!")
            aguarde(1)
            
        elif escolha == 0:
            break

def menu_conexoes(username_logado, db_usuarios):
    while True:
        limpar_tela()
        print("--- 🌐 REDE SYNAPSE ---")
        print("1. 🔍 Buscar Profissionais (por Nome ou Habilidade)")
        print("2. ➡️ Meus Seguindo")
        print("3. ⬅️ Meus Seguidores")
        print("0. Voltar ao Menu Principal")
        
        escolha = obter_escolha_menu(3)
        if escolha == 1:
            buscar_usuarios(username_logado, db_usuarios)
        elif escolha == 2 or escolha == 3:
            lista_tipo = "seguindo" if escolha == 2 else "seguidores"
            lista_usernames = db_usuarios[username_logado][lista_tipo]
            
            print(f"\n--- {lista_tipo.upper()} ({len(lista_usernames)}) ---")
            if not lista_usernames:
                print("   (Nenhum usuário encontrado)")
            else:
                for username in lista_usernames:
                    print(f"   • {db_usuarios[username]['nome_completo']} (@{username})")
            print("\nPressione Enter para voltar...")
            input()
        elif escolha == 0:
            break

def analisar_carreira(username_logado, db_usuarios, db_profissoes_futuro, db_cursos_reskilling):
    limpar_tela()
    print("--- 🧭 ANÁLISE DE CARREIRA (SKILL GAP) ---")
    
    usuario = db_usuarios[username_logado]
    habilidades_usuario = set(usuario['habilidades'].keys())
    
    if not habilidades_usuario:
        print("❌ Você não possui habilidades cadastradas.")
        print("Vá em 'Meu Perfil' -> 'Gerenciar Habilidades' para adicioná-las.")
        aguarde(3)
        return

    print("Escolha uma profissão do futuro para analisar seu 'skill gap':\n")
    
    opcoes_profissoes = {}
    i = 1
    for pid, profissao in db_profissoes_futuro.items():
        print(f"[{i}] {profissao['titulo']}")
        opcoes_profissoes[i] = pid
        i += 1
    print("\n[0] Voltar ao menu")

    escolha = obter_escolha_menu(len(opcoes_profissoes))
    
    if escolha == 0:
        return

    pid_escolhido = opcoes_profissoes[escolha]
    profissao_escolhida = db_profissoes_futuro[pid_escolhido]
    
    habilidades_necessarias = set(profissao_escolhida['habilidades_necessarias'])
    
    habilidades_atuais = habilidades_usuario.intersection(habilidades_necessarias)
    habilidades_faltantes = habilidades_necessarias.difference(habilidades_usuario)
    
    limpar_tela()
    print(f"--- 📊 RESULTADO DA ANÁLISE: {profissao_escolhida['titulo']} ---")
    
    print("\n✅ Habilidades que você JÁ POSSUI:")
    if habilidades_atuais:
        for hab in habilidades_atuais:
            print(f"   • {hab.capitalize()}")
    else:
        print("   (Nenhuma habilidade correspondente)")

    print("\n❗️ Habilidades FALTANTES (Seu 'Skill Gap'):")
    if habilidades_faltantes:
        for hab in habilidades_faltantes:
            print(f"   • {hab.capitalize()}")
    else:
        print("   🎉 Parabéns! Você já possui todas as habilidades chave para esta profissão!")
        print("\nPressione Enter para voltar...")
        input()
        return

    print("\n--- 📚 TRILHA DE REQUALIFICAÇÃO SUGERIDA (SYNAPSE) ---")
    print("Para cobrir seu 'skill gap', sugerimos os seguintes cursos/temas:")
    
    for hab in habilidades_faltantes:
        curso = db_cursos_reskilling.get(hab, {"titulo": f"Buscar curso de '{hab}'", "fonte": "Externo"})
        print(f"\n   Para '{hab.capitalize()}':")
        print(f"   ➡️ Curso: {curso['titulo']}")
        print(f"   ➡️ Fonte: {curso['fonte']}")

    print("\n\nLembre-se: O aprendizado ao longo da vida é central.")
    print("Pressione Enter para voltar ao menu...")
    input()

def consultor_ia_simulado(username_logado, db_usuarios, db_profissoes_futuro, db_risco_automacao):
    limpar_tela()
    print("--- 🤖 CONSULTOR DE IA (SYNAPSE-BOT) ---")
    
    usuario = db_usuarios[username_logado]
    cargo_formatado = usuario['cargo_atual_ia_bot'].lower()
    
    analise_risco = db_risco_automacao.get(cargo_formatado)
    
    print(f"Olá, {usuario['nome_completo'].split()[0]}. Meu nome é SYNAPSE-BOT.")
    print(f"Eu analiso como a IA e a automação impactam sua carreira.\n")
    
    if not analise_risco:
        print(f"Não possuo dados específicos sobre o cargo '{usuario['cargo_atual_ia_bot']}'.")
        print("Meu conselho geral é: continue aprendendo! As habilidades mais procuradas são:")
        print("   • Pensamento Crítico, Criatividade, Análise de Dados e IA")
    else:
        risco = analise_risco['risco']
        pid_sugestao = analise_risco['sugestao_migracao']
        profissao_sugerida = db_profissoes_futuro[pid_sugestao]['titulo']
        
        print(f"Análise do cargo: {usuario['cargo_atual_ia_bot'].capitalize()}")
        print(f"Nível de Risco de Automação: {risco}")
        
        if risco == "Alto":
            print("\n[!] ALERTA: Seu cargo atual possui tarefas com alto potencial de automação.")
            print("Isso NÃO significa que ele vai acabar, mas que vai mudar muito.")
            print("\nMINHA SUGESTÃO (Reskilling):")
            print(f"Com base no seu perfil, uma excelente área para migração é:")
            print(f"   ➡️ {profissao_sugerida}")
            print("Use a 'Análise de Carreira' para ver o que falta para chegar lá!")
        elif risco == "Baixo":
            print("\n[✓] Ótimo! Seu cargo está em uma área de baixa automação e alta demanda.")
            print("Isso significa que seu papel é mais analítico e menos repetitivo.")
            print("\nMINHA SUGESTÃO (Upskilling):")
            print("Para se destacar ainda mais, considere a área de:")
            print(f"   ➡️ {profissao_sugerida}")
            print("Use a 'Análise de Carreira' para ver como complementar suas habilidades.")
        else:
            print("\nSeu cargo (Estudante ou Admin) é o ponto de partida!")
            print("MINHA SUGESTÃO:")
            print("Explore todas as profissões e comece sua jornada de aprendizado agora.")

    print("\nPressione Enter para voltar ao menu...")
    input()

def explorar_profissoes_futuro(db_profissoes_futuro):
    limpar_tela()
    print("--- 🚀 PROFISSÕES DO FUTURO (SYNAPSE) ---")
    print("Estas são as carreiras em alta, baseadas nas tendências:\n")
    
    for pid, profissao in db_profissoes_futuro.items():
        print(f"[{pid}] {profissao['titulo']}")
        print(f"   Descrição: {profissao['descricao']}")
        print(f"   Habilidades Chave: {', '.join(profissao['habilidades_necessarias'])}\n")
        
    print("\nPressione Enter para voltar ao menu...")
    input()

def menu_futuro_do_trabalho(username_logado, db_usuarios, db_profissoes_futuro, db_cursos_reskilling, db_risco_automacao):
    while True:
        limpar_tela()
        print("--- 🚀 FUTURO DO TRABALHO ---")
        print("Analise o mercado e planeje sua carreira.")
        print("1. 🧭 Análise de Carreira (Skill Gap)")
        print("2. 🤖 Consultor de IA (Risco de Automação)")
        print("3. 🗺️ Explorar Profissões do Futuro")
        print("0. Voltar ao Menu Principal")
        
        escolha = obter_escolha_menu(3)
        
        if escolha == 1:
            analisar_carreira(username_logado, db_usuarios, db_profissoes_futuro, db_cursos_reskilling)
        elif escolha == 2:
            consultor_ia_simulado(username_logado, db_usuarios, db_profissoes_futuro, db_risco_automacao)
        elif escolha == 3:
            explorar_profissoes_futuro(db_profissoes_futuro)
        elif escolha == 0:
            break

def menu_projetos(username_logado, db_usuarios, db_projetos):
    while True:
        limpar_tela()
        print("--- 📂 HUB DE PROJETOS ---")
        print("Mostre seu trabalho e veja o dos outros.")
        print("1. 💡 Criar Novo Projeto")
        print("2. 🌍 Explorar Projetos da Rede")
        print("0. Voltar ao Menu Principal")
        
        escolha = obter_escolha_menu(2)
        if escolha == 1:
            criar_projeto(username_logado, db_projetos)
        elif escolha == 2:
            explorar_projetos(db_projetos, db_usuarios)
        elif escolha == 0:
            break

def criar_projeto(username_logado, db_projetos):
    limpar_tela()
    print("--- 💡 CRIAR NOVO PROJETO ---")
    titulo = validar_input("Título do Projeto: ")
    descricao = validar_input("Descrição do Projeto: ")
    
    habilidades_tags = []
    print("Etiquete as habilidades usadas (ex: python, ia, 'fim' para parar):")
    while True:
        hab = validar_input("Habilidade: ").lower().replace(" ", "_")
        if hab == 'fim':
            break
        habilidades_tags.append(hab)
        
    novo_proj_id = gerar_id_unico("proj", db_projetos)
    db_projetos[novo_proj_id] = {
        "autor_username": username_logado,
        "titulo": titulo,
        "descricao": descricao,
        "habilidades_tags": habilidades_tags
    }
    print("✅ Projeto criado e adicionado ao seu perfil!")
    aguarde()

def explorar_projetos(db_projetos, db_usuarios):
    limpar_tela()
    print("--- 🌍 EXPLORAR PROJETOS ---")
    
    if not db_projetos:
        print("Nenhum projeto na plataforma ainda.")
        aguarde()
        return

    for proj in db_projetos.values():
        autor_nome = db_usuarios[proj["autor_username"]]["nome_completo"]
        print("--------------------------------------------------")
        print(f"Projeto: {proj['titulo']} (por @{proj['autor_username']} - {autor_nome})")
        print(f"   Descrição: {proj['descricao']}")
        print(f"   Skills: {', '.join(proj['habilidades_tags'])}")
        
    print("\nPressione Enter para voltar...")
    input()

def menu_aprendizado(username_logado, db_trilhas, db_cursos_reskilling, db_usuarios):
    while True:
        limpar_tela()
        print("--- 📚 TRILHAS DE APRENDIZAGEM ---")
        print("Crie e compartilhe seu caminho de requalificação.")
        print("1. 🛤️ Criar Nova Trilha de Aprendizagem")
        print("2. 🌍 Explorar Trilhas da Rede")
        print("0. Voltar ao Menu Principal")
        
        escolha = obter_escolha_menu(2)
        if escolha == 1:
            criar_trilha(username_logado, db_trilhas, db_cursos_reskilling)
        elif escolha == 2:
            explorar_trilhas(db_trilhas, db_usuarios)
        elif escolha == 0:
            break

def criar_trilha(username_logado, db_trilhas, db_cursos_reskilling):
    limpar_tela()
    print("--- 🛤️ CRIAR NOVA TRILHA ---")
    titulo = validar_input("Título da Trilha (ex: De Adm para Dev): ")
    descricao = validar_input("Descrição da Trilha: ")
    
    etapas = []
    print("Adicione as etapas da sua trilha (digite 'fim' para parar):")
    
    idx_etapa = 1
    while True:
        print(f"\n--- Etapa {idx_etapa} ---")
        tipo_etapa = validar_input("Tipo de etapa? ('curso', 'projeto' ou 'fim'): ").lower()
        
        if tipo_etapa == 'fim':
            break
        elif tipo_etapa == 'curso':
            tag_curso = validar_input("Qual a tag do curso (ex: python, ia)? ").lower()
            if tag_curso not in db_cursos_reskilling:
                print("⚠️ Aviso: Curso não encontrado no nosso DB, mas será adicionado.")
            obs = validar_input("Observação (ex: Focar no módulo 3): ")
            etapas.append({"tipo": "curso", "id_curso": tag_curso, "obs": obs})
            
        elif tipo_etapa == 'projeto':
            titulo_projeto = validar_input("Título do projeto (ex: Fazer meu 1º app): ")
            etapas.append({"tipo": "projeto", "titulo_projeto": titulo_projeto})
        else:
            print("❌ Tipo inválido. Use 'curso', 'projeto' ou 'fim'.")
            continue
            
        idx_etapa += 1
        
    novo_trilha_id = gerar_id_unico("trilha", db_trilhas)
    db_trilhas[novo_trilha_id] = {
        "autor_username": username_logado,
        "titulo": titulo,
        "descricao": descricao,
        "etapas": etapas
    }
    print("✅ Trilha de Aprendizagem criada e publicada!")
    aguarde()

def explorar_trilhas(db_trilhas, db_usuarios):
    limpar_tela()
    print("--- 🌍 EXPLORAR TRILHAS ---")
    
    if not db_trilhas:
        print("Nenhuma trilha na plataforma ainda.")
        aguarde()
        return

    for trilha in db_trilhas.values():
        autor_nome = db_usuarios[trilha["autor_username"]]["nome_completo"]
        print("--------------------------------------------------")
        print(f"Trilha: {trilha['titulo']} (por @{trilha['autor_username']} - {autor_nome})")
        print(f"   Descrição: {trilha['descricao']}")
        print("   Etapas:")
        for etapa in trilha["etapas"]:
            if etapa['tipo'] == 'curso':
                curso_titulo = db_cursos_reskilling.get(etapa['id_curso'], {}).get('titulo', etapa['id_curso'])
                print(f"      [Curso] {curso_titulo} - Obs: {etapa['obs']}")
            elif etapa['tipo'] == 'projeto':
                print(f"      [Projeto] {etapa['titulo_projeto']}")
        
    print("\nPressione Enter para voltar...")
    input()

def gerenciar_profissoes(db_profissoes_futuro):
    limpar_tela()
    print("--- 🛠️ GERENCIAR PROFISSÕES ---")
    print("Profissões existentes:")
    for pid, prof in db_profissoes_futuro.items():
        print(f"   [{pid}] {prof['titulo']}")
    
    print("\n1. ➕ Adicionar Nova Profissão")
    print("0. Voltar")
    escolha = obter_escolha_menu(1)
    
    if escolha == 1:
        titulo = validar_input("Título da nova profissão: ")
        descricao = validar_input("Descrição: ")
        habilidades = []
        print("Digite as habilidades necessárias (uma por uma, 'fim' para parar):")
        while True:
            hab = validar_input("Habilidade: ").lower().replace(" ", "_")
            if hab == 'fim':
                break
            habilidades.append(hab)
        
        novo_pid = f"P{len(db_profissoes_futuro) + 1}"
        db_profissoes_futuro[novo_pid] = {
            "titulo": titulo,
            "descricao": descricao,
            "habilidades_necessarias": habilidades
        }
        print("✅ Nova profissão cadastrada com sucesso!")
        aguarde(2)

def gerenciar_cursos(db_cursos_reskilling):
    limpar_tela()
    print("--- 🛠️ GERENCIAR CURSOS ---")
    print("Cursos existentes (por tag de habilidade):")
    for tag, curso in db_cursos_reskilling.items():
        print(f"   [{tag}] {curso['titulo']}")

    print("\n1. ➕ Adicionar Novo Curso")
    print("0. Voltar")
    escolha = obter_escolha_menu(1)
    
    if escolha == 1:
        tag_hab = validar_input("Tag de habilidade (ex: ia, python, etica): ").lower().replace(" ", "_")
        titulo = validar_input("Título do curso: ")
        fonte = validar_input("Fonte/Plataforma do curso: ")
        
        if tag_hab in db_cursos_reskilling:
            print("⚠️ Aviso: Tag já existe. O curso anterior será sobrescrito.")
            
        db_cursos_reskilling[tag_hab] = {
            "titulo": titulo,
            "fonte": fonte
        }
        print("✅ Novo curso cadastrado com sucesso!")
        aguarde(2)

def listar_usuarios(db_usuarios):
    limpar_tela()
    print("--- 📋 LISTA DE USUÁRIOS (SYNAPSE) ---")
    
    for username, dados in db_usuarios.items():
        print(f"\nUsuário: {dados['nome_completo']} (@{username})")
        print(f"   E-mail: {dados['email']}")
        print(f"   Título: {dados['titulo_profissional']}")
        print(f"   Permissão: {dados['role']}")
        print(f"   Habilidades: {', '.join(dados['habilidades'].keys())}")
    
    print("\n\nPressione Enter para voltar...")
    input()

def menu_logado_admin(db_usuarios, db_profissoes_futuro, db_cursos_reskilling):
    while True:
        limpar_tela()
        print(f"--- ⚙️ PAINEL ADMIN (SYNAPSE) ---")
        print("Bem-vindo ao gerenciamento do SYNAPSE.\n")
        print("1. 🚀 Gerenciar Profissões do Futuro")
        print("2. 📚 Gerenciar Cursos de Reskilling")
        print("3. 📋 Listar Todos os Usuários")
        print("\n0. 🚪 Voltar ao Menu Principal")
        
        escolha = obter_escolha_menu(3)
        
        if escolha == 1:
            gerenciar_profissoes(db_profissoes_futuro)
        elif escolha == 2:
            gerenciar_cursos(db_cursos_reskilling)
        elif escolha == 3:
            listar_usuarios(db_usuarios)
        elif escolha == 0:
            break

def menu_logado(username_logado, db_usuarios, db_posts, db_profissoes_futuro, db_cursos_reskilling, db_risco_automacao, db_projetos, db_trilhas):
    while True:
        limpar_tela()
        nome_usuario = db_usuarios[username_logado]["nome_completo"].split()[0]
        print(f"--- 🧠 BEM-VINDO AO SYNAPSE, {nome_usuario} ---")
        print("A Rede Social do Futuro do Trabalho\n")
        
        print("1. 📰 Visualizar Feed (e Criar Post)")
        print("2. 👤 Meu Perfil (Editar, Habilidades)")
        print("3. 🌐 Minha Rede (Buscar, Seguir)")
        print("4. 📂 Hub de Projetos (Criar, Explorar)")
        print("5. 📚 Trilhas de Aprendizagem (Criar, Explorar)")
        print("6. 🚀 Futuro do Trabalho (Análise de Gap, IA Bot)")
        
        if db_usuarios[username_logado]["role"] == "admin":
            print("9. ⚙️ PAINEL DE ADMINISTRAÇÃO")
            
        print("\n0. 🚪 Fazer Logout")
        
        escolha = obter_escolha_menu(9 if db_usuarios[username_logado]["role"] == "admin" else 6)
        
        if escolha == 1:
            while True:
                limpar_tela()
                print("--- 📰 FEED & POSTS ---")
                print("1. Visualizar Feed (Interativo)")
                print("2. 💬 Criar Novo Post")
                print("0. Voltar")
                esc_feed = obter_escolha_menu(2)
                if esc_feed == 1:
                    visualizar_feed(username_logado, db_usuarios, db_posts)
                elif esc_feed == 2:
                    criar_post(username_logado, db_posts)
                elif esc_feed == 0:
                    break
        elif escolha == 2:
            menu_meu_perfil(username_logado, db_usuarios)
        elif escolha == 3:
            menu_conexoes(username_logado, db_usuarios)
        elif escolha == 4:
            menu_projetos(username_logado, db_usuarios, db_projetos)
        elif escolha == 5:
            menu_aprendizado(username_logado, db_trilhas, db_cursos_reskilling, db_usuarios)
        elif escolha == 6:
            menu_futuro_do_trabalho(username_logado, db_usuarios, db_profissoes_futuro, db_cursos_reskilling, db_risco_automacao)
        elif escolha == 9 and db_usuarios[username_logado]["role"] == "admin":
            menu_logado_admin(db_usuarios, db_profissoes_futuro, db_cursos_reskilling)
        elif escolha == 0:
            print(f"Fazendo logout... Até logo, {nome_usuario}!")
            aguarde(1)
            break

def menu_principal(db_usuarios, db_posts, db_profissoes_futuro, db_cursos_reskilling, db_risco_automacao, db_projetos, db_trilhas):
    while True:
        limpar_tela()
        print("--- 🧠 BEM-VINDO AO SYNAPSE ---")
        print("Conectando Habilidades ao Futuro do Trabalho\n")
        print("1. 🔑 Fazer Login")
        print("2. 🆕 Cadastrar-se")
        print("\n0. ❌ Sair do Programa")
        
        escolha = obter_escolha_menu(2)
        
        if escolha == 1:
            username_logado = realizar_login(db_usuarios)
            if username_logado:
                menu_logado(username_logado, db_usuarios, db_posts, db_profissoes_futuro, db_cursos_reskilling, db_risco_automacao, db_projetos, db_trilhas)
        elif escolha == 2:
            cadastrar_usuario(db_usuarios)
        elif escolha == 0:
            limpar_tela()
            print("Obrigado por usar o SYNAPSE!")
            print("Lembre-se: 'O futuro do trabalho não é uma ameaça, é uma oportunidade de reimaginar.'")
            aguarde(2)
            break

if __name__ == "__main__":
    menu_principal(db_usuarios, db_posts, db_profissoes_futuro, db_cursos_reskilling, db_risco_automacao, db_projetos, db_trilhas)