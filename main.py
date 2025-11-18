import pandas as pd
import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(
    filename='execucao.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

def main():
    try:
        logging.info(" Iniciando automação RPA Challenge...")

        diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
        caminho_arquivo = os.path.join(diretorio_do_script, "challenge.xlsx")

        try:
            df = pd.read_excel(caminho_arquivo)
            df.columns = df.columns.str.strip()
            logging.info(f" Planilha carregada com sucesso! Total de linhas: {len(df)}")
        except FileNotFoundError:
            logging.error("Erro Crítico: Arquivo challenge.xlsx não encontrado.")
            return

        logging.info("Iniciando navegador Chrome...")
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico)
        wait = WebDriverWait(driver, 10) 

        driver.get("https://rpachallenge.com/")
        driver.maximize_window()

        botao_start = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Start')]")))
        botao_start.click()
        logging.info("Desafio iniciado (Botão Start clicado)!")

        for index, linha in df.iterrows():
            campos = [
                "First Name", "Last Name", "Company Name", 
                "Role in Company", "Address", "Email", "Phone Number"
            ]
            
            for campo in campos:
                valor = str(linha[campo]).strip()
                
                xpath = f"//label[text()='{campo}']/following-sibling::input"
                
                input_element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
                input_element.clear()
                input_element.send_keys(valor)
            
            btn_submit = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
            btn_submit.click()
            
            logging.info(f" Rodada {index + 1} concluída.")

        logging.info(" Desafio finalizado!")
        
        time.sleep(5)

    except Exception as e:
        logging.error(f" Ocorreu um erro inesperado durante a execução: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()
            logging.info("Navegador encerrado.")

if __name__ == "__main__":
    main()