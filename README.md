# requisicaoajaxsimples
Uma simples requisição ajax utilizando python + django 

O arquivo não só parece, como é simples. 
Para passar mais valores pelo ajax, basta somente você adicionar a referencia e o valor na parte data.
Ex:
na função ajax dentro do index.html, adicionamos valores na data

<pre>function meuAjax(){
    var campoNome =  document.getElementById('nome').value;
    $.ajax({
        url:"{% url 'ajax' %}",
        type: 'GET',
        data:{
            nome: campoNome,
        },
        success: function(msg){
           document.getElementById("retorno").innerHTML = msg;
        }
    });
}
</pre>

Ou seja, dentro de data já temos um valor e podemos adicionar quantos quisermos, ex:

        data:{
            nome: campoNome,
            idade: campoIdade,
            cidade: campocidade,
        },
Onde os valores da direita, são os valores que vem dos campos input do seu formulário, já os da esquerda passam pelo get e ficaram com as seguintes representações:

request.GET['nome'],
request.GET['idade'],
request.GET['cidade']

<h3>Alterando os valores pelo objeto que vem do banco de dados</h3>

Na 'view', criamos a seguinte função:
<pre>
def filtroAjax(request):
    if request.method=='GET':
        nome = request.GET['nome']
        return HttpResponse(nome)
</pre>

Porém para pegarmos o que vem do banco de dados, precisamos importar a model que criou
<pre>from .model import *</pre>
<strong>Note, que onde está o símbolo de asterisco "*", poderíamos adicionar qualquer classe criada dentro do modelo, basta adicionar o nome da classe que desejar.</strong>

Após adicionarmos a importação do banco, poderemos chamar o objeto antes do return.

<pre>suavariavel = nomeModelo.objects.filter(coluna=nome)</pre>

desse jeito, para retornar no HttpResponse, basta adicionar a instancia no lugar  no nome no antigo código dentro do return.

<h3>Adicionando o caminho na url</h3>
Agora na urls.py da sua app, precisa adicionar o caminho para a requisição ajax.

<pre>urlpatterns = [
    path('', views.index, name='index'), #aqui fazemos nosso apontamento raíz para nosso index na view do appAjax.
    path('ajax', views.filtroAjax, name='ajax'), #essa url é responsável por receber os valores do ajax
]
</pre>

o segundo caminho adicionado é o da requisição, onde o primeiro parâmetro é a url em si, ou seja, o que sera escrito na URL do navegador.
O segundo parâmetro é a função dentro do seu arquivo views que fará a análise dos dados enviados pelo ajax.
O terceiro é o nome que podemos seguir como um atalho ao adicionarmos no template o caminho da url, como no exemplo abaixo:

<pre><a href="{% url 'terceiroparametroaqui' %}">Link</a></pre>
onde o terceiro parâmetro é o name adicionado no path no arquivo urls.
