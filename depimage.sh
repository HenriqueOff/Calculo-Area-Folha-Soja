#!/bin/bash

# Nome do ambiente
ENV_NAME="ImagemProcessamento"
PYTHON_SCRIPT="processamento_imagem.py"

# Função para verificar e instalar dependências
install_dependencies() {
    conda install -y -n $ENV_NAME -c conda-forge opencv numpy
}

# Verificar se o ambiente conda já existe
if conda env list | grep -q "$ENV_NAME"; then
    echo "Ativando ambiente conda '$ENV_NAME'..."
    source activate $ENV_NAME

    echo "Verificando e instalando dependências necessárias..."
    install_dependencies
else
    echo "Criando ambiente conda '$ENV_NAME'..."
    conda create --name $ENV_NAME -y
    source activate $ENV_NAME

    echo "Instalando bibliotecas necessárias..."
    install_dependencies
fi

# Executar o código Python e mostrar apenas os resultados das áreas
echo "Executando $PYTHON_SCRIPT..."
python3 $PYTHON_SCRIPT

