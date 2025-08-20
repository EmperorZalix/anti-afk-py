import tkinter as tk
from tkinter import ttk
import threading
import time
from pynput.keyboard import Key, Controller

class StealthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stealth - Automatizador de Teclas")
        self.root.geometry("300x150")
        self.root.resizable(False, False)
        
        # Controlador do teclado
        self.keyboard = Controller()
        
        # Flag para controlar a automação
        self.automacao_ativa = False
        self.thread_automacao = None
        
        self.setup_ui()
    
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        titulo = ttk.Label(main_frame, text="Automatizador LSHIFT", 
                          font=("Arial", 14, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Status
        self.status_label = ttk.Label(main_frame, text="Status: Inativo", 
                                     font=("Arial", 10))
        self.status_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))
        
        # Botões
        self.btn_ativar = ttk.Button(main_frame, text="Ativar", 
                                    command=self.ativar_automacao,
                                    style="Accent.TButton")
        self.btn_ativar.grid(row=2, column=0, padx=(0, 5), pady=5, sticky="ew")
        
        self.btn_desativar = ttk.Button(main_frame, text="Desativar", 
                                       command=self.desativar_automacao,
                                       state="disabled")
        self.btn_desativar.grid(row=2, column=1, padx=(5, 0), pady=5, sticky="ew")
        
        # Configurar grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
    
    def ativar_automacao(self):
        """Ativa a automação da tecla LSHIFT"""
        if not self.automacao_ativa:
            self.automacao_ativa = True
            self.status_label.config(text="Status: Ativo - Pressionando LSHIFT a cada 5s")
            self.btn_ativar.config(state="disabled")
            self.btn_desativar.config(state="normal")
            
            # Inicia thread para automação
            self.thread_automacao = threading.Thread(target=self.executar_automacao, daemon=True)
            self.thread_automacao.start()
    
    def desativar_automacao(self):
        """Desativa a automação da tecla LSHIFT"""
        self.automacao_ativa = False
        self.status_label.config(text="Status: Inativo")
        self.btn_ativar.config(state="normal")
        self.btn_desativar.config(state="disabled")
    
    def executar_automacao(self):
        """Executa a automação em loop"""
        while self.automacao_ativa:
            try:
                # Pressiona e solta a tecla LSHIFT
                self.keyboard.press(Key.shift_l)
                time.sleep(0.1)  # Mantém pressionado por 100ms
                self.keyboard.release(Key.shift_l)
                
                # Aguarda 5 segundos antes do próximo pressionamento
                for _ in range(50):  # Verifica a cada 0.1s se deve parar
                    if not self.automacao_ativa:
                        break
                    time.sleep(0.1)
                    
            except Exception as e:
                print(f"Erro na automação: {e}")
                break
    
    def on_closing(self):
        """Função chamada ao fechar a aplicação"""
        self.desativar_automacao()
        self.root.destroy()

def main():
    root = tk.Tk()
    app = StealthApp(root)
    
    # Configurar fechamento da aplicação
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    # Executar aplicação
    root.mainloop()

if __name__ == "__main__":
    main()

