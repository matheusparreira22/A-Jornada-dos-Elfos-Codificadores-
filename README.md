
# Rastreamento dos Elfos Codificadores

---

## Descrição do Projeto
Este projeto foi desenvolvido para ajudar os elfos da Floresta da Codificação a otimizar seus caminhos mágicos. 
O objetivo é processar uma lista de movimentos que indicam direções e calcular a posição final no plano cartesiano, 
eliminando redundâncias de deslocamento.

---

## Lógica do Programa
O programa funciona da seguinte forma:

1. **Entradas**: Recebe uma lista de movimentos, onde cada movimento é uma string representando uma direção:
   - `"norte"`: Move para cima no eixo Y.
   - `"sul"`: Move para baixo no eixo Y.
   - `"leste"`: Move para a direita no eixo X.
   - `"oeste"`: Move para a esquerda no eixo X.

2. **Processamento**:
   - Inicializa as coordenadas no ponto `(0, 0)`.
   - Itera sobre a lista de movimentos.
   - Ajusta as coordenadas com base no movimento:
     - `norte` adiciona 1 ao eixo Y.
     - `sul` subtrai 1 do eixo Y.
     - `leste` adiciona 1 ao eixo X.
     - `oeste` subtrai 1 do eixo X.

3. **Saída**: Retorna uma tupla representando a posição final `(x, y)` no plano.

Exemplo de cálculo:
- Entrada: `["norte", "leste", "sul", "oeste", "norte", "leste"]`
- Processo:
  - Início: `(0, 0)`
  - `norte`: `(0, 1)`
  - `leste`: `(1, 1)`
  - `sul`: `(1, 0)`
  - `oeste`: `(0, 0)`
  - `norte`: `(0, 1)`
  - `leste`: `(1, 1)`
- Resultado: `(1, 1)`

---

## Requisitos
- Python 3.x instalado no sistema.
- Um editor de texto ou IDE (opcional para editar o código).

---

## Como Rodar o Projeto
1. **Clonar ou Criar o Arquivo**:
   - Copie o código para um arquivo chamado `rastreamento_elfos.py`.

2. **Executar o Script**:
   - Abra um terminal e navegue até o diretório onde o arquivo foi salvo:
     ```bash
     cd /caminho/para/o/arquivo
     ```
   - Execute o script:
     ```bash
     python rastreamento_elfos.py
     ```

3. **Verificar a Saída**:
   - O terminal exibirá a posição final dos elfos:
     ```
     Posição final otimizada: (1, 1)
     ```

---

## Customização
- Modifique a lista de movimentos diretamente no código:
  ```python
  movimentos = ["norte", "norte", "leste", "oeste", "sul"]
  ```

- Reexecute o script para ver o resultado atualizado.

---

## Exemplo de Código
```python
def rastrear_posicao(movimentos):
    x, y = 0, 0
    for movimento in movimentos:
        if movimento == "norte":
            y += 1
        elif movimento == "sul":
            y -= 1
        elif movimento == "leste":
            x += 1
        elif movimento == "oeste":
            x -= 1
    return x, y

# Exemplo de movimentos
movimentos = ["norte", "leste", "sul", "oeste", "norte", "leste"]
posicao_final = rastrear_posicao(movimentos)
print("Posição final otimizada:", posicao_final)
```

---

## Contribuição
Se tiver sugestões ou melhorias para o projeto, sinta-se à vontade para compartilhar! 🚀

---

**Divirta-se ajudando os elfos!** 🎉
