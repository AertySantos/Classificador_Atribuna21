<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Classificador de Páginas do Jornal A Tribuna e Sentenças Relacionadas ao Termo "Arquivo"</h1>

<p>Este projeto consiste em um algoritmo de classificação de páginas do jornal A Tribuna, utilizando técnicas de vetorização, bem como classificação de sentenças relacionadas ao significado da palavra "arquivo". O objetivo é automatizar a categorização dessas páginas e sentenças, facilitando a organização e busca de informações.</p>

<h2>Instalação</h2>

<p>Para executar o algoritmo, é necessário ter Python instalado, juntamente com as seguintes bibliotecas:</p>

<ul>
    <li>scikit-learn</li>
    <li>numpy</li>
    <li>pandas</li>
    <li>spacy</li>
</ul>

<p>Você pode instalar as dependências usando pip:</p>

<pre><code>pip install scikit-learn numpy pandas
</code></pre>
<pre><code>pip install spacy
</code></pre>
<pre><code>python3 -m spacy download pt_core_news_sm
</code></pre>
<h2>Utilização</h2>

<p>O algoritmo é composto por três etapas principais:</p>

<ol>
    <li><strong>Vetorização das Páginas do Jornal A Tribuna:</strong> As páginas do jornal são convertidas em vetores numéricos, utilizando técnicas como TF-IDF.</li>
    <li><strong>Classificação utilizando KNN, CBC e WiSARD:</strong> Os vetores das páginas são utilizados para treinar modelos de classificação utilizando os algoritmos KNN (k-nearest neighbors), CBC (Classifier Chain) e WiSARD (Wilkie, Stonham, Aleksander, and Riedmiller), a fim de categorizar as páginas em diferentes classes pré-definidas.</li>
    <li><strong>Classificação de Sentenças Relacionadas ao Termo "Arquivo":</strong> As sentenças relacionadas ao termo "arquivo" são extraídas das páginas classificadas e passam pelo mesmo processo de vetorização e classificação, permitindo a identificação automática de sentenças relevantes.</li>
</ol>

<p>Para utilizar o algoritmo, basta executar o script <code>Makefile</code>. Ele irá baixar as páginas da Atribuna e, em seguida, abrirá uma imagem conforme a seguir, onde você poderá escolher o que deseja fazer.</p>
<img src="/[imagem.jpg](https://github.com/AertySantos/Classificador_Atribuna21/blob/main/imagem.png)">

<h2>Contribuição</h2>

<p>Contribuições são bem-vindas! Se você encontrar algum problema ou tiver alguma sugestão de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.</p>

<h2>Licença</h2>

<p>Este projeto está licenciado sob a <a href="https://opensource.org/licenses/MIT">MIT License</a>.</p>

</body>
</html>

