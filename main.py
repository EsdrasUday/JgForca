import random
import sys
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from listas import *
from PIL import Image
from time import sleep

class JogoForcaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.root.geometry("600x400")
        self.root.minsize(width=600,height=400)
        self.root.configure(bg="#2c001e",fg_color="#2C001E")
        self.roxo = "#2C001E"
        self.laranja = "#E95420"
        self.oran_claro = "#D75F20"
        self.branco = "#FFFFFF"
        self.sec_text = "#D3D3D3"
        
        if sys.platform == "win32":
            try:
                self.root.iconbitmap("img/logo.ico")
            except:
                pass
        
        # Categorias e suas palavras
        self.categorias = {
            1: ("L. Programação", linguagens),
            2: ("Frutas", frutas),
            3: ("Idiomas", idiomas),
            4: ("Países", paises),
            5: ("Estados Brasileiros", estados_brasileiros)
        }

        # Dicionário para localizar vogais e c com cedilha
        self.vogais_acentuadas = {
            "a": ["a", "á", "à", "ã", "â"],
            "e": ["e", "é", "è", "ê"],
            "i": ["i", "í", "ì", "î"],
            "o": ["o", "ó", "ò", "ô", "õ"],
            "u": ["u", "ú", "ù", "û"],
            "c" : ["ç"]}

        self.frame_inicial()

    def frame_inicial(self):
        self.clear_frames()
        frame = ctk.CTkFrame(self.root,width=600,height=400, fg_color="transparent")
        frame.pack(side="bottom",pady=20, padx=20, fill="both", expand=True)
        try:
            imagem = ctk.CTkImage(light_image=Image.open("img/logo.png"), size=(90, 80))
            label_imagem = ctk.CTkLabel(frame, image=imagem, text="")
            label_imagem.pack(pady=8)
        except:
            print("Imagem não encontrada")
        
        label = ctk.CTkLabel(frame, text="Bem-vindo ao Jogo da Forca!", font=("Arial", 20, "bold"), text_color="#ffffff")
        label.pack(pady=7)
        
        btn_jogar = ctk.CTkButton(frame, text="Jogar",hover_color="#5c1f7e",fg_color=self.laranja, text_color=self.branco, command=self.selecionar_categoria)
        btn_jogar.pack(pady=7)
        
        btn_categorias = ctk.CTkButton(frame, text="Categorias",hover_color="#5c1f7e",fg_color=self.laranja, text_color=self.branco, command=self.mostrar_categorias)
        btn_categorias.pack(pady=7)
        
        btn_sair = ctk.CTkButton(frame, text="Sair",hover_color="#5c1f7e",fg_color=self.laranja, text_color=self.branco, command=self.root.quit)
        btn_sair.pack(pady=7)

        Dev = ctk.CTkLabel(frame, text="Developer Esdras Uday Da Silveira Maracajá", font=("Roboto", 8, "bold"), text_color="grey")
        Dev.pack(side='bottom',pady=1)
    
    def selecionar_categoria(self):
        self.clear_frames()
        frame = ctk.CTkFrame(self.root, fg_color=self.roxo)
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        label = ctk.CTkLabel(frame, text="Escolha uma categoria", font=("Arial", 16, "bold"), text_color="#ffffff")
        label.pack(pady=10)
        
        for num, (nome, _) in self.categorias.items():
            btn = ctk.CTkButton(frame, text=nome, fg_color=self.laranja,hover_color="#5c1f7e", command=lambda c=num: self.iniciar_jogo(c))
            btn.pack(pady=5)
        
        btn_voltar = ctk.CTkButton(frame, text="Voltar", fg_color="#fc4c02",hover_color="#5c1f7e", command=self.frame_inicial)
        btn_voltar.pack(pady=5)
    
    def iniciar_jogo(self, categoria):
        self.clear_frames()
        frame = ctk.CTkFrame(self.root, fg_color="transparent")
        frame.pack(pady=20,side="right", padx=20, fill="both", expand=True)
        frame2 = ctk.CTkFrame(self.root, fg_color="#383838",width=200)
        frame2.pack(side="left",pady=20, padx=20, fill="both", expand=True)
        
        # Escolher a palavra aleatória
        palavra = random.choice(self.categorias[categoria][1])
        self.acertos = [" " if _ == " "else '_' for _ in palavra]
        self.tentativas = 6
        self.letras_usadas = []

        self.label_palavra = ctk.CTkLabel(frame, text=" ".join(self.acertos), font=("Arial", 20), text_color="#ffffff")
        self.label_palavra.pack(pady=10)

        self.label_info = ctk.CTkLabel(frame, text=f"Tentativas restantes: {self.tentativas}", font=("Arial", 14), text_color="#ffffff")
        self.label_info.pack(pady=5)

        self.frame_letras_chutadas = ctk.CTkLabel(frame, text="Letras Chutadas: ", font=("Arial", 14), text_color="#ffffff")
        self.frame_letras_chutadas.pack(pady=10)

        self.entry_letra = ctk.CTkEntry(frame, placeholder_text="Digite uma letra", width=150)
        self.entry_letra.pack(pady=5)

        self.label_forca = ctk.CTkLabel(frame2, text=forcas[self.tentativas], font=("Arial", 16,"bold"), text_color="#ffffff")
        self.label_forca.pack(side="left",pady=10)

        btn_enviar = ctk.CTkButton(frame, text="Enviar" ,hover_color="#b33205",fg_color=self.laranja, text_color=self.branco, command=lambda: self.verificar_letra(palavra))
        btn_enviar.pack(pady=5)

        btn_voltar = ctk.CTkButton(frame, text="Voltar",hover_color="#b33205", fg_color=self.laranja, command=self.frame_inicial)
        btn_voltar.pack(pady=10)

        self.entry_letra.bind("<Return>", lambda event: self.verificar_letra(palavra))  # Enter

    def verificar_letra(self, palavra):
        letra = self.entry_letra.get().lower().strip()
        self.limpar_entrada()
        if letra in self.letras_usadas or not letra:
            return
        
        self.letras_usadas.append(letra)

        # Verificar se a letra digitada é uma vogal com acento
        letras_validas = [letra]
        if letra in self.vogais_acentuadas:
            letras_validas.extend(self.vogais_acentuadas[letra])

        # Verificar se a letra (ou variantes acentuadas) estão na palavra
        if any(l in palavra for l in letras_validas):
            for i in range(len(palavra)):
                if palavra[i] in letras_validas:
                    self.acertos[i] = palavra[i]
        else:
            self.tentativas -= 1
            self.label_forca.configure(text=forcas[self.tentativas]) 
            if self.tentativas == 0:
                self.label_forca.configure(text=forcas[self.tentativas]) 

        self.label_palavra.configure(text=" ".join(self.acertos))
        self.label_info.configure(text=f"Tentativas restantes: {self.tentativas}")
        self.atualizar_letra_forca()

        if "_" not in self.acertos:
            self.frame_inicial()
            CTkMessagebox(title="Vitória", message=f"Parabéns, você venceu! A palavra era {palavra.title()}", icon="check").show()

        elif self.tentativas == 0:
            self.frame_inicial()
            CTkMessagebox(title="Derrota", message=f"Você perdeu. A palavra era: {palavra.title()}", icon="cancel").show()
            

    def limpar_entrada(self):
        self.entry_letra.delete(0, "end")

    def atualizar_letra_forca(self):
        """Atualiza as letras que foram utilizadas e as forcas conforme os erros, adicionando a um frame de texto."""
        letras = ', '.join(self.letras_usadas)
        self.frame_letras_chutadas.configure(text=f"Letras Chutadas: {letras}")

    def mostrar_categorias(self):
        self.clear_frames()

        frame_principal = ctk.CTkFrame(self.root, fg_color="transparent")
        frame_principal.pack(pady=20, padx=20, fill="both", expand=True)

        label = ctk.CTkLabel(frame_principal, text="Categorias Disponíveis", font=("Arial", 16, "bold"), text_color="#ffffff")
        label.grid(row=0, column=0, columnspan=3, pady=5)  # Label ocupa a primeira linha

        # Frame rolável
        scroll_frame = ctk.CTkScrollableFrame(frame_principal, width=500, height=200, label_font=("arial", 14, "bold"), fg_color="grey")
        scroll_frame.grid(row=1, column=0, columnspan=3, pady=5)  # Scroll ocupa a segunda linha

        self.label_palavras = ctk.CTkLabel(scroll_frame, text="", font=("Arial", 14, "bold"), text_color="#ffffff", wraplength=480)
        self.label_palavras.pack(pady=10)

        # Criar botões dentro do frame principal usando grid
        coluna = 0
        linha = 2  # Começa na terceira linha
        for num, (nome, palavras) in self.categorias.items():
            btn = ctk.CTkButton(frame_principal, text=nome, fg_color=self.laranja, hover_color="#5c1f7e",
                                command=lambda p=palavras: self.exibir_palavras(p))
            btn.grid(row=linha, column=coluna, padx=10, pady=10, sticky="ew")  # sticky="ew" para expandir horizontalmente
            coluna += 1
            if coluna > 2:  # Define o número máximo de colunas
                coluna = 0
                linha += 1

        # Botão Voltar (criado apenas uma vez, fora do loop)
        btn_voltar = ctk.CTkButton(frame_principal, text="Voltar", fg_color="#4d4d4d",hover_color="#5c1f7e", command=self.frame_inicial)
        btn_voltar.grid(row=linha, column=coluna, columnspan=3, pady=10,padx=10, sticky="ew")  # sticky="w" alinha à esquerda

        # Configurar o frame principal para usar grid layout (pesos para redimensionamento)
        frame_principal.columnconfigure(0, weight=1)
        frame_principal.columnconfigure(1, weight=1)
        frame_principal.columnconfigure(2, weight=1)
        frame_principal.rowconfigure(1, weight=1) # peso para o scroll_frame
        for i in range(2, linha + 2): # peso para as linhas dos botões e do botão voltar
            frame_principal.rowconfigure(i, weight=1)

    def exibir_palavras(self, palavras):
        palavras_texto = ", ".join(palavras)
        
        # Quebrar o texto em linhas de no máximo 200 caracteres
        linhas = []
        while len(palavras_texto) > 200:
            corte = palavras_texto[:200].rfind(",")  # Evita cortar no meio de uma palavra
            if corte == -1:
                corte = 200  # Se não encontrar vírgula, corta no limite
            linhas.append(palavras_texto[:corte])
            palavras_texto = palavras_texto[corte+1:].strip()

        linhas.append(palavras_texto)  # Adiciona o restante do texto
        self.label_palavras.configure(text="\n".join(linhas))


    def clear_frames(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = ctk.CTk()
    app = JogoForcaApp(root)
    root.mainloop()
