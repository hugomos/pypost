# AI Post Generator

Aplicação desktop para geração automática de posts de blog utilizando IA (Google Gemini), desenvolvida com PyQt5 e arquitetura limpa.

## 📋 Sobre o Projeto

O **AI Post Generator** é uma ferramenta que permite criar posts de blog otimizados para SEO de forma automatizada. A aplicação utiliza o modelo Gemini 2.5 Flash da Google para gerar conteúdo de qualidade baseado em um assunto e palavras-chave fornecidos pelo usuário.

### Funcionalidades Principais

- ✍️ Geração automática de posts com IA
- 🎯 Otimização para SEO com palavras-chave
- 📝 Suporte para múltiplos formatos (Markdown, Plain Text, HTML)
- 👁️ Preview em tempo real do conteúdo gerado
- 📂 Exportação direta para arquivo
- 🎨 Interface moderna com tema dark

## 🏗️ Arquitetura

O projeto segue os princípios de **Clean Architecture** e **Domain-Driven Design**:

```
├── domain/              # Entidades e regras de negócio
│   ├── either.py       # Tipo Either para tratamento de erros
│   └── use_case.py     # Classe base para casos de uso
├── infra/              # Infraestrutura e adaptadores
│   ├── ai/             # Integração com IA
│   │   └── gemini/     # Adaptador Google Gemini
│   └── ui_controller.py # Controle de UI
├── modules/            # Módulos da aplicação
│   └── post/           # Módulo de posts
│       ├── application/    # Casos de uso
│       ├── infra/         # Factories
│       └── ui/            # Interface gráfica
└── main.py            # Ponto de entrada
```

### Padrões Utilizados

- **Clean Architecture**: Separação de responsabilidades em camadas
- **Use Case Pattern**: Encapsulamento da lógica de negócio
- **Factory Pattern**: Criação de objetos complexos
- **Adapter Pattern**: Integração com serviços externos
- **Either Monad**: Tratamento funcional de erros

## 🚀 Tecnologias

- **Python 3.x**
- **PyQt5**: Framework para interface gráfica
- **Google Gemini AI**: Modelo de IA para geração de conteúdo
- **Markdown**: Processamento e renderização
- **python-slug**: Geração de slugs para nomes de arquivo

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd ai-post-generator
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure a API Key do Google AI:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione sua chave:
```env
GOOGLE_AI_API_KEY=sua_chave_aqui
```

4. Execute a aplicação:
```bash
python main.py
```

## 🎯 Como Usar

1. **Preencha o Assunto**: Digite o tema principal do seu post
2. **Adicione Palavras-chave**: Insira palavras-chave separadas por vírgula (opcional)
3. **Selecione o Formato**: Escolha entre Markdown, Plain Text ou HTML
4. **Escolha o Diretório**: Selecione onde o arquivo será salvo
5. **Clique em Executar**: Aguarde a geração do conteúdo
6. **Visualize o Preview**: Confira o resultado na área de visualização

### Exemplo de Uso

**Assunto:** "Agricultura de Precisão: O Caminho para uma Colheita Superior"

**Palavras-chave:** "agricultura,colheita,dados"

**Resultado:** Post completo em Markdown com:
- Título otimizado (H1)
- Subtítulos estruturados (H2, H3)
- Conteúdo rico com listas
- Palavras-chave naturalmente integradas
- Estrutura de introdução, desenvolvimento e conclusão

## 🔧 Configuração do Gemini

O projeto utiliza o modelo `gemini-2.5-flash` por padrão. Para alterar:

```python
# Em infra/ai/gemini/genai.py
class GenAIAdapter(Agent):
  AGENT_MODEL = "gemini-2.5-flash"  # Altere aqui
```

### Parâmetros de Geração

- **Temperature**: 0.7 (equilíbrio entre criatividade e coerência)
- **System Instruction**: Prompt otimizado para geração de posts de blog

## 🎨 Interface

A interface utiliza um tema moderno baseado em **shadcn/ui**, com:
- Cores neutras e elegantes
- Componentes bem espaçados
- Feedback visual claro
- Suporte a temas light/dark

## 🛡️ Segurança

O prompt do sistema inclui proteções contra:
- **Prompt Injection**: Ignora instruções maliciosas no input
- **Formato inconsistente**: Garante saída sempre em Markdown
- **Desvio de função**: Mantém foco na geração de posts

## 📝 Estrutura de Dados

### Input
```python
{
    "subject": str,      # Assunto do post
    "keywords": str      # Palavras-chave (opcional)
}
```

### Output
- Arquivo `.md` salvo no diretório escolhido
- Preview renderizado na interface
- Feedback de sucesso com caminho do arquivo

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autores

- Desenvolvido por Vitor Hugo Oliveira

## 🐛 Problemas Conhecidos

- O preview HTML pode não renderizar estilos complexos
- Necessária conexão com internet para usar a API do Gemini

<!-- ## 🔮 Roadmap

- [ ] Suporte para múltiplos modelos de IA
- [ ] Editor de posts integrado
- [ ] Histórico de posts gerados
- [ ] Templates personalizáveis
- [ ] Exportação em batch
- [ ] Análise de SEO integrada -->

<!-- ## 📞 Suporte

Para problemas ou sugestões:
- Abra uma [issue](link-para-issues)
- Entre em contato: [email]

--- -->

**Nota**: Esta aplicação requer uma API Key válida do Google AI para funcionar. Obtenha a sua em [Google AI Studio](https://makersuite.google.com/app/apikey).
