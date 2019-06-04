# Leitor de Planilhas

Este Software foi desenvolvido com o intuito de ler e realizar alguns filtros em uma planilha .csv ou .xlsx. 

## Instalação

A aplicação utiliza recursos da versão 3.6+ do Python. Utilize o comando abaixo para checar a versão do interpretador instalado em sua máquina.

```bash
python --version
```

Use o package manager [pip](https://pip.pypa.io/en/stable/) para instalar as bibliotecas "pandas" e "xldr" que foram utilizadas neste projeto.

```bash
pip install pandas
```


```bash
pip install xldr
```

### Ubuntu

Talvez as bibliotecas sejam instaladas no python 2.7, caso não seja possível acessa-la com o interpretador python 3.6+, utilize os comandos abaixo:

```bash
sudo apt-get install python3-pandas
```


```bash
sudo apt-get install python3-xldr
```

## Uso

Para utilizar o software, use o seguinte comando no terminal dentro da pasta onde se encontram os arquivos do software.

```bash
python main.py 
```
Nota: Por padrão, o arquivo a ser análisado no programa é "exemplo2.csv". Para alterá-lo, altere o nome do arquivo na seguinte linha dentro do arquivo main.py:

```python
fileName = 'exemplo2.csv'
```

## Autor

Luiz Henrique Longo 

## License
[MIT](https://choosealicense.com/licenses/mit/)
