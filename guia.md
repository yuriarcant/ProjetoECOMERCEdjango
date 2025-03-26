Guia- projeto ecommerce(loja)

https://docs.djangoproject.com/en/5.0/topics/auth/default/



1- Criar estrutura do django, rodar terminal (django-admin startproject + nome do projeto)

2- Vamos rodar no terminal  um cd ecommerce, para acessar o diretorio ecommerce. Caso voce volte no seu projeto verifique se seu terminal ta dentro do diretorio pra rodar os comandos

3- Agora vamos rodar um "python manage.py startapp + nome do aplicativo q voce quer" (loja), que vai criar o que chamamos de app(aplicativo), esse app tem q ser adicionado no arquivo settings no installed_apps para ser reconhecido pelo django

4- Testar se o serve ta no ar "python manage.py runserver"

5- Agora vamos mecher com as urls de nosso site, para isso vamos fazer com que no urls do nosso projeto(ecommerce) possua uma url que gerencia todas as urls vindo do nosso app(loja), entao vamos importa o include no arquivo urls do projeto(ecomerce), vamos adicionar um "path(''/, include('nome do app . o arquivo urls)) , esse arquivo urls temos que criar dentro do arquivo do nosso app(loja).

Agora dentro do urls do app(loja), vamos criar a msm estrutura do urls do projeto(ecommerce), pq vai ser ali que vamos gerenciar nossos links, nessa estrutura vamos passar 3 coisas, o caminho, a função que voce quer que rode, que ve la do arquivo views e um nome interno.

Agora dentro do app(loja) no nosso arquivo views é onde vamos fazer a nossas funçoes que correspondem a nossas paginas que sao gerenciadas pelo nosso urls, essas paginas estao sempre ligadas e para isso temos q importar as funçoes desse arquivo views para o nosso urls (from .views import homepage, etc) no nosso caso vamos colocar um asteristico que significa que vai importa tudo q for criado dentro arquivo views , o ponto antes do views indica que esse arquivo vem do mesmo local do nosso app(loja).


6- Vamos mecher nas funçoes , toda função vai receber um parametro request(requisição), seja ela metodo post ou get , e ela sempre vai retornar algo para o  usuario no nosso caso sera o template daquela pagina em especifico, e para isso dentro do nosso app(loja) vamos criar uma pasta com nome tempaltes no plural, onde ficaram nossos arquivos html corresponde a cada pagina e função.

OBS: Dar o nome da pasta de templates faz com que nao necessite ir no settings e adiconar ela no TEMPLATE, porque o django ja tem uma estrututa q faz com ele ele procure automaticamente por uma pasta com esse nome dentro do seu app, caso n fosse esse nome teriamos que adicionar la no settings.

6- Criar umarquivo base.html para e fazer a extenção dele para todas os outros templates

7- Criar uma pasta static dentro no mesmo local da pasta ecommerce que gerencia nosso projeto, essa pasta é responsavel pela imagem, arquivo css , java script e etc.  dentro dela vamos criar novas pastas com o que ira precisar seja ela qualquer uma das opçoes comentadas. lembrando que para essa pagina ter interação com seus tempaltes basta colocar {% load static %} nos tempaltes.

Agora temos que criar no arquivo settings o STATICFILES_DIRS (responsavel por procurar a pasta) e passar o caminho de onde esta a pasta responsavel pelos nossos arquivos estaticos(imagem/css e etc), para isso vamos importa a biblioteca os. base_dir corresponde ao caminho do nosso projeto

Agora basta puxar o arquivo css para dentro do template desejado, para puxar basta usar a tag <link>  e para puchar vamos usar o load static. se nao teriamos que por o link completo da imagem (ex:arcant.com/static/css/main.css)

8- Criar um barra de navegação no nosso base.html e colocar nossos links nessa barra, primeiramente de uma forma simples, dps vamos trabalhar mais nisso. Lembrando que vamos puchar os links atraves do url e vamos utilizar aquele parametro "name=" que criamos para nossos links la no arquivo urls.py. e dentro do nosso carrinhovai ter um link para o checkout pq so faz sentido ter esse link quando voce tiver no carrinho.


9- Agora vamos trabalhar no nosso arquivo moedels.py fazendo o nossos modelos que no caso sao nossas tabelas que vao ser armazenadas  no banco de dados (todas as class criadas sao cada tela do nosso banco de dados) . entao dentro do arquivo vamos crair nossas class e alguma delas estarao ligadas uma nas outras. lembrando que nao precisamos por o id pois ele ja e criado automaticamente pelo django.

No nosso site vai permitir que clientes que não estão cadastrados possasm relizar uma compra entao nessas classes temos que por parametros para possibilitar que os campos de nome , emael etc possam esta vazios ou não preenchidos (null=True, blank=True), alem disso precisaremos de um id_sessao para saber quem sao esses  usuarios que nao estao cadastrados.

Nossos usuarios serao da nossas classes ele iram fazer relação com a tabela usuarios que ja é criada automaticamente pelo django e pra fazer essa relação vamos usar o OneToOneField que é uma relação de 1 para 1 e para fazer essa relaçao temos que importar a tabela essa tabela(user). OBS:sempre que se cria um modelo que tem uma relçao com outra tabela voce passa o parametro on_delete=models.CASCADE , isso faz que se voce deletar algo relacionado as informaçoes criada na outra tabela correspondente tambem ira ser excluida.

Em algumas class usaremos o ForeignKey (chave estrangeira), isso perminite que tbm iremos relacionar as tabelas, basicamente ele é um campo da sua tabela(class) que esta relacionado com outra tabela, sendo que essa categoria esta relacionado um produto , mas a categoria que ele se relaciona pode esta relacionada com varios produtos

Lembrando que é uma boa pratica e evitar que um campo armazene mais de uma informação, por exemplo na class pedidos poderimos colocar um campo de itenspedido e seria uma lista de informaçoes, mas optamos po na class itenspedidos ter um campo que possua eapenas um pedido nele.


10- Agora depois deter cliado a modelagem da nossa tabela(class), vamo inicianor o processo de migrations que enviara tudo para o banco de dados e isso permitirar ver se esta tudo funcionando corretamente. lembrando então que sempre que voce estiver fazendo uma modificação em um campo de sua tabela tem quer ser realizado esse processo de migrations. para fazer essa migração voce tem que realizadr dois comandos.
1- python manage.py makemigrations (sempre primeiro)
2- python manage.py migrate

Depois do primeiro migrate nossa arena administrativa pode ser acessada


11- vamos partir para modificação para nossa area administrativa, para isso temos que criar um super user para acessar essa area para isso vamos rodar o comando "python manage.py createsuperuser" e criar nossa conta.

Quando acessarmos o administrativo do nosso site vamos perceber que nossas tabelas ainda nao estao aparecendo la mesmo ja sendo criadas, a proxima etapa é por elas no no nosso admnistrativo, para isso dentro do nosso arquivo admin.py vamos importa do arquivo models.py todas nossas class, agora basta registrar nossas class(tabelas) no arquivo admin.py


12- Agora vamos partir para as imagens do nossos produtos, pq para adicionar produtos temos que  no administrativo colocor uma foto, vamos modificar esse jeito de adicionar a foto ao produto que esta sendo adicionado para ficar mais intuitivo e mais facil. Na class produto o campo de imagem vai ser um imagefield e para  ser utilizado é necessario ter a bibiblioteca pillow , essa biblioteca nao vem instalada com django.

Depois de installar o pillow no nosso arquivo views que recebe o nosso template pra ser exibido no nosso site , temos que passar o que o django chama de contexto que nada mais é do que as informaçoes que sao exibidas dentro dos nossos templetes(html), e essas infoprmaçoes nada mais é as nossas tabelas que estao no nosso arquivo models entao vamos importalas para o arquivo views.

Agora podemos buscar informaçoes dessas tabelas e passar elas para o nosso context chamando a class respectiva da tabela, vamos observar que que se puxarmos as imagens atraves do  nosso html elas nao irao aparecer teremos que fazer algumas alteraçoes no nosso settings.

13- vamos ajeitar o caminho da nosso imagens , se voces perceberem quando subimos uma imagem ela nao foi direcionada para a pasta imagens que nos criamos na estrutura do nosso projeto, pra que ela seja direcionada precisamos no nosso arquivo settings criar a variavel MEDIA_ROOT=  que diz que essa é a pasta rais das nossas imagens.

Outro parametro que temos q adicionar é o MEDIA_URL, que é o padrao do link que teremos da nossas imagens, por exemplo: linkdosite/ nome que voce passar no media_url. Agora temos q importa essa varial para o arquivo urls do nosso projeto principal e não pro urls do app loja pq nesse urls do app ele puxa o link e a views(template), que vai carregar o link, o arquivo urls do projeto vai dizer onde ele vai carregar todas as imagens que o nosso site possue.

Entao no arquivo urls do projeto vamos importar o static do propio django e juntar o urlpatterns antigo com esse static. como definimos o nosso MEDIA_URL no nosso settings vamos p importa e passar como parametro dentro do static, e tbm irameos pegar o MEDIA_ROOT e passar em um parametro pq é la que estao nossas imagens. fazendo isso agora conseguimos mostrar nossos arquivos estaticos no nosso site.


13- Agora vamos trabalhar no nossos arquivos views e consequentemente no html correspondente, vamos fazer primeira mente a homepage do site que possui varios banner que nada mais sao do que imagens. agente poderia simplismete por as imagens dentro da pasta imagens e puxar elas mas n é o meto mais dinamico, pq assim teriamos que fazer isso manualemnte toda vez, entao pra isso seria bom ter uma tabala so para esses banners e ai sim pegar os banners dessa tabela,  entao para isso vamos no nosso arquivo models.py e criar essa tabela e dps vamos la no admin e adicionar os banner e passar o link destino que nos msm iremos criar.

Depois dessas etapas temos que ir no nosso arquivo views e na class de onde vamos mostrar esse banner  puxar eles para um context para ser exebido no html dele.  esse banner tbm serao interativos como um link se clicarmos nele ele ira direcionar para a respectiva oferta.


14- vamos trabalhar um pouco agora com filtros do django, vamos trabalhar nesses filtros  no nossa loja e no nossos home page. ja que temos  os banner e as camisetas que adicionamos , entao la no arquivo views na nossa função da homepage vamos puxar os banner apenas os que estao ativos, lembra que quando colocamos nossos banner poderiamos colocar eles ativos ou nao.
nos podemos fazer filtro abaixos de filtros por qualquer objeto que esta presente nas nossas class.


Agora vamos trabalhar com um filtro um pouco mais avançado digamos que queremos que ao clicar em um filtro que nos leva para uma pagina apenas de bermudas, entao para isso nos precisariamos de um link dinamico, por exemplo: 123.4324./loja/bermudas. para isso teremos que criar na no nosso urls um novo link(path), só que nesse path  iremos passar um valor dinamico entre <> pode ser um int, um str etc, esse valor dinamico   tem que estar lá na função da loja como parametro do msm modo que ele foi escrito no link e tambem vamos definir ele como none pq o usuario pode entrar no nosso link loja sem nenhum filtro, caso tenha algum filtro ai sim ele ira entra no outro link com o valor dinamico aplicado.

obs: quando for fazer esse tipo de link dinamico raramente voce poe so o path com a variavel, e uma boa pratica por "loja/ a variavel". 


15- Agora nos vamos usar esse valor dinamico para filtrar a nossa loja, esse etapa e um pouco complicada, na nossa função loja vamos fazer um if, no caso se tiver alguma categoria nos iremos filtrar atraves no nome da categoria, porem o  nome da categoria ele nao é um objeto da nossa class produto o nome categoria vem de um objeto que esta  class categoria, que é associado com nossa tabela produto, no caso nos queremos buscar algo  que esta no campo de um objeto da tabela que esta associada com o nosso produto, que é o campo da categoria, no caso queremos assoar esse resultado com alguma categoria que possui nessa class categoria. quando é asim podemos passar isso diretamente pelo parametro.

Entao como fazemos isso, primeiro voce ira passar o nome do campo(objeto) que faz associação com  a outra class no nosso caso o campo "categoria" depois dele  "_ _ "(dois underline) e por fim o nome do campo de onde voce quer buscar o valor no nosso caso (nome). Isso tudo é o filtro deps do if na nosa função loja. entao podemos fazer isso para categoria como vimos mais tbm podemos faszer isso para outras coisas como tipo de protudo etc.

agora temos que fazer uma pequena alteração la no nosso html da home page nos possuimos os links do nosso banner, os links ele ta como se fosse o link do nosso site / um valor dinamico, mais nas estapas acima nos definimos que para filtrar seria linkdo site / loja / valor dinamico, entao la no nosso html temos q concatenar o nosso link da loja o que é bem simples, so por o url da loja dps do nosso link


16- agora que ja temos alguns produtos adicionados, temos que criar um pagina para ver esse produto, entao nos faremos aquelas etapas, criar uma função, criar um html que vai ser passado para essa funçao e criar um link porem esse link ele vai receber tbm um valor dinamico pq sera priciso saber qual é o produto, é o valor dinamico sera o id de cada produto.
agora la na função eu pego o meu produto baseado no seu id e passo ele para o context que sera exibido no html.

Lembrando que queremos que a imagens do produtos que estao presente na n ossa loja sejam itens clicaveis que vao ser direcionados para essa pagina de ver produtos que criamos acima, entao la no nosso html da loja temos que colocar essas imagens em uma ancora para ela virar um link, e no href dela vamo passar o url do ver_produto mas tbm passar o id pq é um parametro obrigatorio que colocamos

17- seguindo na pagina de ver produto, vamos fazer algumas inclementaçoes como tamanhos disponiveis, cores etc. Primeiramente vamos trabalhar com as cores, no nossa class item estoque nos temoso campo de tamanho , cores, quantidade etc, porem nos vamos criar uma nova class cores e adicionar ela no admin.py,  nela  tera duas informaçoes, o nome da cor e o numero hexadecimal dela, pq quando chegar na tela para exibir as cores é so pegar o numero hexadecinal associado a ela.

Agora a cor que esta no nosso itens estoque vai se relacionar com essa class cores, entao temos que trasformar a cor do itens em estoque sendo uma foreignkey. agora la no nosso admin podemos colocar cores e  o codigo hexadecimal dela. E agora quando entrarmos no admin no item em estoque pdemos selecionar uma camisa a cor que acabamos de adicionar.

Agora la na nossa funçao de ver_produtos vamos fazer um filtro para mostrar os produtos que tem mais do que 0 no estoque, aqui poderemiamos fazer um filtro  avançado igual aquele que fizemos da loja, mas iremos fazer do outro jeito para praticar. entoa vamos fazer um variavel item_estoque e fazer um filtro e passar ele para o nosso context, agora podemos puxar isso para o nosso html de ver produto

lembrando que terememos que usar as regras de query set para dizer que um campo e maior que algo no caso sera __gt= numero q voce quer q seja maior, ai pra ver todas as opçoes é so pesquisar a documentação do query set do django.


18- Agora detro da função ver_produto vamos fazer um if para verificar se tem produto em estoque ou não, dentro desse if vamos fazer um variavel tem_estoque que tbm vai ser passada para o nosso context, isso permitirar que la no html poderemos fazer um if para verificar se tem o produto em estoque, assim podemos colocar o produto como insdisponivel ou por as informaçoes do que tem disponivel.

Agora dentro do if, se tiver itens disponiveis vamos pegar as informaçoes dele, primeiramente vamos pegar as cores do produto atraves de um list comprehension para não precisa fazer um for estruturado que vai ser feito em um set{} para evitar q tenha item duplicados tipo duas cores brancas ou preta etc., agora que temos nossa lista de cores vamos passar ela para o nosso context e usar para exibir as cores no nosso hmtl fazendo um for para exibir todas as cores disponiveis. La no nosso html o codigo da cor nos vamos colocar ele na tag i que permite fazer com q vire um incone, ja que queremos que aparece uma bolinha com a cor daquele codigo , e pra isso vamos usar o font awesome, basta colocar font awesome cdn, pegar a link tag e aplicas la no nosso html base, ai podemos usar os incones traquilamente no nosso projeto, basta entrar no site do font awesome é pesquisar por uma tag.


19-Agora nos vamos filtrar um produto para exibir os tamanhos dos produtos de acordo com as cores, basicamente vamos fazer o msm que fizemos com o filtro da loja que aparece de acordo com a categoria etc. entao vamos fazer um link que recebera alem da categoria o id da cor, entao nossa funçao ver_produto vai receber esse parametro de id_cor que inicialmente sera none.

Entao agora teremos que criar um if, que no caso é se eu passei um id de cor, nos iremos filtrar o nosso item_estoque cujo a cor e igual aquele id que esta sendo passado, e dps percorrer o item estoque pegando os tamanhos que ficarao disponiveis e serao exibidos la no html.

obs: aqui ah uma coisa bem legal para economizar linhas de cogico, ate aqui nessafunçao de ver produto fizemos varios ifs e elses, mas podemos simplismente dps da estrutura ta correta e com todas as variaves prontas. podemos pegar essas variaveis e adicionalas ela no inicio do codigo como vazias e apenas ir acrecentando com if e modificando os seus valorez de vazios para algo, assim possibilita tirar todos os elses feito.

Agora la no nosso html iremos fazer um if tamanhos e percorrer o essses tamanhos, isso vai permitir que se agente selecione alguma cor, aparecera os tamanhos disponiveis para aquelas cores, entao aquele incone de cores que temos no nosso html sera na verdade um link clicavel que ira me jogar para aquel produto em especificos com tais cores disponiveis entao ele tem q tar dentro de uma ancora, e nessa ancora nos vamos passar o url  do ver_produto, esse nome vem la do parametro nome que demos no nosso arquivo urls.py,  junto com o id produto e tbm id da cor, que sao os parametros necessarios. ai quando cliclar vai levar la para aquele link(path) que criamos que recebe o id produto e o id da cor. Alem disso vamos querer pegar o nome da cor seleconada para ficar visivel qual a cor q estamos selecionando, pq no momento agene so clica nela e ela nao mostra qual a cor q selecionamos.

Entao no ver produtos vamos criar uma variavel cor selecionada que inicialmente sera none, fazer um if para verificar se tem um id_cor, se tiver pegamos esse id cor de acordo com o id_cor, e passamos o resultado para a variavel cor selecionada.


obs: No passo abaixo e importante lembrar que nosso site vai permitir que pessoas que nao possuem onta possam fazer compras etc
20- Agora vamos dar um foco em adicionar a funcionalidade de adicionar produtos em nossos carrinhos, vamos primeiramente trabalhar no nosso verproduto.html, primeiramente vamos trasnformar nosso if que ve os tamanhos em um formulario entao basta por eles dentro de um form, agora aqueles botoes de  tamanho vao virar botoes de opçao, que sao aqueles que quando voce clica em um desmarca o outro. Para isso temos que criar um imput e por o type dele como radio e para conectar os botoes passamos o parametro name= , os q possuem os msm name= estaram conectado e temos q passar o parametro value= que é o valor que vai ser enviado para o nosso site, no caso do nosso valor e o tamanho roupas, numero de calçados e etc.
Agora para aparecer algo escrito do lado do nosso imputs/botoes que acabamos de criar, vamos passar outro campo que o label, e passamos o que queremos q apareça do lado e para dizer que esta vinculado a algum input voce passa o parametro for e dentro desse for voce passa o value do input que voce quer relacionar.

Nosso botao vamos passar o type= como submit que significa que ele envia essas infprmaçoes presente no formulario , o nosso form vamos passar o method= dele que no nosso caso e um 'POST' ja que estamos enviando informaçoes para site, alem disso no form temos que passar a action desse formulario, que é o link para onde essa informçao iram ser enviada e lembre-se que em todo formulario criado é necessario por a tag csrf_token. 

Para fazer por o link que ira se usado vamos ter q criar uma função no nosso views que vai ser adiconar carrinho e fazer um path no nosso arquivo urls.py, nesse path ele vai deceber o id_produto porque precisamos saber qual vai ser o produto adicionado no carrinho com isso criado agora la no action do nosso form vamos passar o link que criamos. Na fuçao de adiconar carrinho vamos verificar se ta ta sendo enviado um method post e se possue um id caso caso tenha ou nao tenha vamos redirecionar para paginas diferentes para teste entao vamos importar o redirect , para redirecionar basta passar o nome q fizemos nos links/path.


21- Agora vamos aprender a pegar informaçoes desse formulario criado acima para serem utilizadas etc. para pegar essas informaçoes que foram inviadas nos pegamos direto do request com um request.POST.dict() isso vai nos retornas todas as informaçoes em forma de um dicionario, entao vamos fazer isso la no nossao funçao de adicionar_carrinho.

Aqui faremos uma alteraçao no nossa funçao ver_porduto, invez do nome_cor_selecionada q estava antes, vamos criar um cor_selecionada, aquele nome nome da cor q pegamos vai sumir, agora n temos so o nome da cor, agora temos a cor completa, com id e o nome dela. agora temos q mudar la no html ver produto tbm e na hora de printar vai ser cor_selecionada.nome.

Agora la no nosso form dps do for dos tamanho vamos fazer um novo input  que sera do type=hidden que é um input escondido não aparece para os usuarios do site. Essa alteraçoes fizemos para que quando enviarmos as informaçoes do nosso formulario ele ira passar o id da cor do produto selecionado e agora no vies podemos pegar esse id. vamos dar uma pausa por aqui
mas teremos que pegar quem é o cliente que enviou essa informação e criar o pedido.


22- vamos Criar o nosso carrinho, o nosso carrinho ele vai aparecer em  todos as nossas telas, entao pra isso  ele precisaria estar dentro do context de todas as nossas funçoes do arquivos views, pra isso vamos criar um arquivo chamado novos_context que vai ficar paras as funçoes que queremos que apareça em todo nosso site, e para fazer essas funçoes estaarem em todos site, basta ir no nosso settings nos TEMPLATES temos os "context_processors": que é tudo q é usado em todo o nossos  templates, site etc.  Entao e ai que vamos adicionar as nossas funçoes como o carrinho. 

Para adicionar coloca o nome do nosso app, nome do arquivo e por fim o nome da função. no nosso caso loja.novo_context.carrinho. agora vamos colocar uma imagem manualmente na nossa imagens pra poder ter essa imagem na nossa barra de navegação, lembrando que todas a pagina que tem uma imagem estatica precisa ter no inicio dela o {% load static %} , agora so puxar essa imagem para nossa barra de navegação do lado dessa imagem é onde vai ficar a quantidade de produtos que o usuarios esta a comprar e ainda nao foi finalizado o pedido.


23- Agora vamos criar as funcinalidades desse carrinho, lembrando que aqui teremos que ter duas estruturas porque o nosso site permite que usuarios logados e nao logados façam compra então esse primeiro passo vamos focar nos usuarios que estao logados.

Para verificar se um usuario esta logado com uma conta podemos fazer isso atraves do request, com o request.user.is_authenticated, entao para começarmos nos precisamos saber quem é o nosso cliente, a nossa class Cliente tem um campo usuario associado a ele, e esse campo e um "OneToOneField" , isso vai permitir que agente possa pegar  o usuario fazendo o cliente.usuario mas tambem que possamos fazer ao contrario usuario.cliente para pegar o cliente, pq é uma relação de 1 para 1. 

obs: essa funcionalidade que estamos fazendo necessita que o usuario precise necessariamente de um cliente, e no nosso caso estamos usando o usuario do admin e em momento algum fizemos um cliente associado a ele e se tentarmos ir no site agora o nosso site vai dar um erro. entao vamos comentar esse codigo que fizemos e entrar no admin e criar um cliente para eesse usuario do admin. Entao so pra lembrar sempre que o usuario criar uma conta nos nosso site vamos tambem criar um cliente para ele.

Agora q ja temos o cliente temos que pegar o pedido que ele ta querendo fazer, entao temos q fazer uma busca nos pedidos do cliente cujo ainda nao foi finalizado, so que nao vamos usar um get normal vamos fazer com o get_or_create porque  se tentarmos pegar pelo get pode dar um erro caso o usuario não tenha feito nenhum pedido, esse get_or_create ele basicamente faz com que crie um pedido para o usuario caso nao encontre nehum pedido, esse pedido vai estar vazio e caso o usuario queira algo so ira adiconar nesse pedido  que esta vazio assim fazemos com que sempre tenha um pedido criado, essa informação sempre vai retorna duas coisas, o pedido e se esse pedido foi criado ou nao.

Agora temos q pagar a quantidade de produtos que temos em nosso carrinho para exibilos, entao vamos precisar importar nossa class ItensPedidos, e ai vamos pegar o itens pedidos e vamos filtrar ele de acordo com esses pedidos que esta sendo realizado no momento. basta percorrer esse pedido  e agora na quantidade_produtos_carrinhos que vai ser inicialmente criada como 0 vamos  adicionar  de acordo com os item encontrados mais a quantidade deles , pq um pedido pode ter 1, 2 , 3  itens.

obs: agora com essa funcionalidade agente pode cair em um erro, pra agente dar continuidade no else vamos da um return {'quantidade_produto_carrinho': quantidade_produto_carrinho} por enquanto pra seguir pra proxima etapa.

24- agora vamos fazer a funcionalidade para mostrar os produtos que temos no carrinho e tambem fazer afunçao de quando clicar no botao de adicinar o carrinho funcionar. Entao  primeiramente vamos mostrar os itens no nosso carrinho, basicamente vamos fazer a msm estruturar q fizemos no nosso carrinho do arquivo do novos_context  no outra funçao do carrinhos. agora la no nosso html do carrinho vamos usar o que passamos para o context.

25- dando continuidade vamos somar  o total de cada produto presente no nosso carrinho, caso eu tenho o total de 3 camisas basica ira aparecer o total delas. Poderiamos fazer faze um for diretamente  para chegar ate esse valor no nossa  funçao do carrinho, mais a fomra que iremeos fazer vai ser criar uma função la na nossa class de itens_pedido, agora podemos simplesmente  usar essa função para mostrar o preço total de cada produto la no nosso html do carrinho. se chamarmos a função com () la no nosso site vai dar um erro, entao temos que chamar a função sem o (), e na nossa função vamos por um @property isso informa q vamos usar essa função como se ela fosse um campo da nossa class, entao em nenhum lugar vai ser necessario por o (), nem msm no nosso arquivo views.py ok.


Agora vamos treinar um mais um pouco vamos fazer novas funçoes para poder mostra no nosso carrinho a soma do pedido total ou seja a soma de todos os itens do carrinho, e tbm mostra a quantidade de itens q tem no carrinho, lembrando que ja temos a quantidade de itens no carrinho, que é aquele q fica do lado da nossa imagem do carrinho, mas vamos fazer um função so pra treino.

Entao la na nossa class pedido, ja que queremos somar tudo do nosso pedido vamos fazer essa funçoes. entao para pegar a quatidade total de produtos temos que bucas a quantidade em nosso itens_pedidos de acordo com o id pedido do nossa class de itens_pedido,  que seja igual ao id pedido  q estamos olhando no momento que é o id da class Pedido.


26- Agora vamos trabalhar no adicionar um produto ao carrinho que vai ser na função adicionar_carrinho, entao primeiramente precisamos pegar o nosso cliente, entao vamos pegar atravees do request.user, dps de pegar o cliente nos vamos pegar o pedido de acordo com o cliente q acabamos de pegar e que o finalizado seja igual  a false pq ai sea um pedido que esta em andamento.

O proximo passo precisamos pegar o item estoque q esta associado ao nosso pedido para podemos saber qual é esse item q vai ser adicionado, agora temos q adicionar esse produto q foi pego la no nosso itenspedidos, só q sera feito atras tbm de um get_or_create pq se o produto ainda nao tiver no carrinho eu quero criar esse item e se ja estiver um produto igual no carrinho eu quero adicionar + 1, que vai ser de acordo com o item_estoque que fizemos e cujo o pedido é igual ao q criamos.
OBS:sempre q editarmos manualmente um campo da tabela igual fizemos com nosso item pedidos aqui temos q por dps um save()

27- agora o que vamos fazer, vai ser um contador para alterar q quantidade de itens diretamene no nosso carrinho que no caso ira ser dois botao do lados da nossa quantidade de itens. Entao la no carrinho.html temos por dois botoes em volta da nossa quantidades.

Esses botoes entao tera que adicionar ou remover um item do nosso carrinho, ja possuimos a função de adicionar um item ao nosso carrinho entao basta associar essa função ao botao de adicionar mais um item. Entao para associar esse botao com a função temos que fazer um formulario q vai enviar essas informaçoes, basicamente vai ser igual nosso formulario de do ver_produto.html so que sem o for dos tamanhos. 

Lembrando que a nossa função precisa receber o id do produto entao basta passar o id daquele item desejado dps do url do adicionar carrinho, alem disso ele precisa das variaveis de cor e tamanho, que ja possuimos tbm so que vamos enviar dois imput escondidos agora invez de um so que serao o tamanho e a cor, la no ver_produto era so a  cor. 

28- O que temos que fazer agora e fazer uma função de remover_carrinho para associar com o botao de - entao la no viwes.py vamos fazer essa função, despois temos que criar uma url para essa função la no arquivo urls.py.

Entao vamos trabalhar agora na nossa função de remover_carrinho que é muito parecida com a nossa função de adicionar_carrinho, entao vamos copiar ela e mudar algumas coisas, primeiro ela nao vai adicionar ao carrinho ela vai tirar, entao sera um -1, dps disso vamos fazer uma verificação na quantidade daquele item se ele for menor que zero vamos pegar o item pedido e deletar ele. Dps disso nossa funcinalidades  estao terminadas.

29- Agora vamos precisar ver essas funcionalidades para um usuario que nao esteja logado, precisamos identificar esse usuario que nao esta logado de alguma forma, normalmente os sites fazem isso atraves de cookies, no casso isso gera um id pra aquele usuario e amazena isso em algum lugar no naveador desse usuario e quando ele retorna podemos identificar ele por esse id, e como de se esperar um django tem esse funcinalidade para gerenciar esse cookies e gerar  um id unico para cada  usuario. No momento atual nos conseguimos navegar pelo site normalmente exceto um local que é o carrinho.

Primeiro entao nos temos que ver em que momento vamos gerenciar esse cookie para esse usuario anonimos, no nosso caso vai ser quando esse usuario adicionar um item no carrinho para quando ele voltar no nosso site aquele item ainda ta la, entao vamos fazer isso na nossao função de adicionar carrinho, entao caso ele nao encontro um cliente, la no else vamos gerar um id_sessao e é isso que vamos armazenar no cookies do navegador dess usuario anonimo, e para gerar esse id de sessao vamos importa o uuied que é uma biblioteca que gera uma sequencia de caracteres que nao pode ser iguais.

Depois de criar esse id_sessao nos temos que aprender a armazenar ele nos cookies do navegador usuario, e para isso temos que aprender a pegar a resposa do nosso views, que normalmente é um o redirect, um render etc. o que podemos fazer é por exemplo invez de no return fazer o redirect no return, e pegar esse redirect armazenar em uma variavem e no retun passar essa varial, a vantagem disso é que agora podemos editar essa informação armazenada, que é exatamente o que precisamos fazer para armazenar os cookies no navegador do usuario, editar essa informção armazenada.

entoa vamos armazenar essa resposta, vamos pegar essa resposta e passar um set_cookie(key=, value), onde a key(nome  que voce quer dar), value( valor daquilo no caso nosso id unico para o usuario).

Mas nesse else nos temos que verificar se ja possue esse cookies porque o usuario nao logado ja pode ter vindo no nosso site antes, e tambem caso ele ja tenha adicionado um item ele pode adiconar outro e  nao precisamos gerar um id_sessao novo para isso. entao vamos fazer um request.COOKIES  e procurar um id sessao mas vamos procurar atravez de um get, pq se fizermos request.COOKIES['id_sessa'] e nao tiver ele vai dar erro.

 basta relembrar as regras de dicionario se voce procura algo pelo get e tiver ele pega essa informação e se nao tiver ele volta none. Tambem vamos lembrar que la no nosso models.py na nossa class de cliente nos criamos nela um campo id_sessão e é ela que vamos usar para criar cum cliente para o nosso usuario anonimo, porque para realizar um pedido temos q ter um cliente. entao o que vamos fazer é criar ou pegar o cliente com um get_or_create.

Bom agora nessa parte temos q fazr uma alteração, nesse momento no nosso else tem um redirect('loja'), que so usamos para pode seguiar la no começo,mas não precisamos mais dele, mas se escluirmos ira dar um problema,  primeiro pq precisamos da variavel resposta que usamos para colocoar o cookies, mais o que vai acontecer agora é que o return que ta abaixo do save(), é o que vai servir para toda essa função entao ali que vai retorna a resposta que no caso leva a gente para o carrinho pq ela que manda o item para nosso carrinho. entao vamos ensima do if de verificação de isuarios logados ou nao, criar uma variavel resposta com um redirect para o carrinho e por a variavel no return la em baixo no save.

No momento ainda nao podemos testar isso porque aida existem outras logicas que so aceite se tiver um usuario logado, como o carrinho, entao temos que pegar todas essas logicas e fazer  nelas  um metodo para caso o usuario não esteja logado. porem se deslogamos nosso admin e colcoar um item no carrinho vai dar um erro, so que se logarmos no admin e ver  la no administrativo os pedidos ira ter um so com o id sessao preencido, que no caso é nosso usuario anonimo.


28-O que vamos fazer agora é permitir a vizualização dos produtos dentro do carrinho para o usuario anonimo, no momento esta dando erro pois so é possivel se tiver a varivel cliente. 
Entao la na nossa função carrinho vamos fazer basicamente a msm verificação que fizemos no adicionar_carrinho, verificar se tem cookies e se tiver pegar esse cliente. Depois vamos fazer um else para caso ele nao encontre, entao nesse else temos q fazer um contexte com os paramentros anteriores como NONE e tbm vamos adicionar no context antigo e novo um paramentro de cliente_existente, e la no nosso html do carrinho vamos fazer um if, pq so faz sentido ele monstra as informaçoes do carrinho se tiver um cliente e tambem fazer um else para informa o usuario que o carrinho esta vazio.

Vamos tambem mecher na quantidade do carrinho que possue na nossa barra de navegaçao la nos nosso arquivo novos_context.py para esses usuarios anonimos e tbm basicamente agente sempre segue a msm logica de verificar se tem um id_sessao. pega o cliente, entao vamos importa o cliente para esse arquivo ja que vamos usalo, nao precisava antes pq com o usuario logado ja vinha do request.usuer q é do usuario que esta logado entao vinha direto.

Outro ajuste que temos que fazer é na nossa class de remover carrinho, entao tambem vamos fazer um if verificando caso tenha um usuario anonimo, antes esta retornando apenas para a loja.

obs: Alguns navegadores podem não guardar esse cokies que estao sendo armazenado e caso voce feche o seu navegador simplismente aquele pedidos nao taria mais la, caso queira garantir que esse cokies fiquem armazenados em um determinado tempo. la no set_cookie, podemos passar 2 parametros o primeiro é o "expires=" que coloca uma data e o outro é "max_age=" que passamos quantos segundos voce quer q dure esse cookie. NO MEU NAO TEVE ESSE PROBLEMA MAS NO NOSSO ADICIONAR CARRINHO VAMOS DEIXAR UM EXEMPLO PARA 30 DIAS, passando uma conta 60segundos * 60min *24hr *30 dias


29- agora vamos vamos mecher no arquivo viwes.py na função do nosso chekout  e tbm la no nosso html do checkouts, entao no nosso checkout nos vamos ter a informaçoes de numero de pedido, total do pedido, numero de itens, nao vamos mostrar cada item la,  tambem vamos querer mostra la o endereço que sera um formulario q o usuario pode escolher caso ele tenha mais de um endereço associado ao email, alem disso para nosso usuarios anonimos vai ter um campo para ele por o email dele para poder entrar em contato. Entao vamos trabalhar aqui com usuarios logados, pra isso vamos no nosso admin, e criar dois endereços para o nosso cliente do admin que é  o que utilizamos ate o presente momento.

É muito importante reaproveitar codigos, a nossa logica do chekout é muito parecida com a logica que usamos na nossa função do carrinho, entao podemos copiar aquela logica e ir editando ela, e é isso que vamos fazer, entao basicamente vamos verificar cliente/ cokies, caso nao tenha vai ser redirecionado pra loja. depois vamos pegar os pedidos, e nao vamos pegar o itens pedidos igual no carrinho, pq não vamos exibir eles. O que vamos ter vai ser os endereços(precisamos criar).

Agora la no html do nosso checkout, vamos fazer a msm coisa vamos copiar o html do carrinho e vamos ir retirando o que nao queremos, basicamente ficou so o numero pedido, preço totais do pedido e quantiade total do produto.

O nosso endereço que sera exibido no checkout vai ser um formulario la no html, porque o usuario ira poder selecionar ele. entao ele vai ser aqueles input que é um botazinho de selecionar tipo radio.

 continuando no checkout vamos por no nosso formulario um input escondido type hidden que vai ser o valor total desse pedido, vamos fazer isso porque ai teremos essa informação no nosso banco de dados, para futuramente poder busca essa informação  e verificar se o usuario esta realmente pagando aquele valor.

Alem disso vamos tambem no nosso formulario la no html adicionar um link/botao que vai ser para o cliente poder adicionar um endereço pra ele colocar caso ele nao tenha nenhum. entao vamos ter que cruar um urls, uma views(função) e um templete que para adiconar um endereço.

 
30- Agora temos que trabalhar no metodo de adicioanr endereço, vamos começar pelo nosso html de adiconar endereço, basicamente o que vamos precisar la é um formaluario, para esse usuario por as informaçoes, e serem enviadas para o nosso banco de dados. diferente dos outros forms vamos ter que por a action desse  formulario como o url do adiconar endereço e  la na função(views) do adiconar endereco  nos vamos tratar o que vai acontecer. 

E para tratar nos vamos pegar as informaçoes desse metodo post, igual pegamos no remover carrinho por exemplo, alem disso temos que ter outra informção de quem é aquele cliente, entao basta verificar se tem cliente ou algum cookies assim como em todos os outros, e agora podemos criar a variavel  endereco no nosso views de adicionar_endereço, aqui finalizamos essas funçoes.
OBS:na hora de criar o endereço quando for pegar os parametros e importante verificar na no nosso models como colocamos cada campo, se e um campo de numero , texto etc, pra quando puxar os parametos garatir ele como cada forma , por exemplo: numero=int(dados.get("numero")), que garantimos como um inteiro. 


31- Agora vamos trabalhar na nossa barra de navegação e nela nos vamos trabalhar com filtros, parecido com o que fizemos nos nossos views "EX: nome__categoria=" esse foi um tipo, poderiamos fazer algo semelhante porem vamos fazer de outro jeito para praticar diversas formas ok.

Na nossa barra de navegaçao nos teremos os tipos(camisa, bermuda) e nossas categorias(infantil, adulto), isso tem que aparecer para todo o site, entao basicamente temos que fazer isso num contexto e alem disso lembrando que temos que adicionar tambem la no nosso settings  na parte templates, entao la no nosso novos_context vamos criar uma outra função que sera o nosso caregoria_tipos(), lembrando que em cad acategoria vai ter todos o tipos dentro dela, por exemplo na categoria feminino vai ter os tipos bermuda, calçados etc, assim como na categoria masculino. entao pra isso  no nosso html do nav bar vamos fazer um for pra percorrer as categorias e dentro desse for vamos fazer um forpra percorrer os tipos para cada categoria.

Nossas categoria e tipos vao ser links , alem disso nesse link nos vamos por o padrao, para esse links , para a categoria vai ser o link para levar pra loja + o nome do da categoria e para o tipos ira ser e para o nosso tipos vai ser o link para levar pra loja + o nome do da categoria + o nome do tipo, assim futuramente vamos poder filtrar apenas os calçados poor exemplo , bermudas e etc. 

Se clicarmos no nosso tipos la no link ele vai aparecer de uma form ""loja/feminino-Tênis%20Corrida" , a gente vai tratar para que no nosso link isso aparece de forma escrita noraml, o que aocntece é que quando se possue carcteristica especiais ele tem um formato difenrente quando vira um link por isso ele fica assim, tem dois jeitos de ajeitar isso , um e que la no nosso views nos teriamos que fazer o prescesso de enconding, mas desse modo geraria muito precupação porque teriamos que associar com a forma que o usuario procura no site.

Entao vamos fazer de outra forma que é utilizando um slug, que é basicamente de como alguma class por exemplo nossa class categoria vai ser utilizada em formato de link, entao na no nossa class categoria nos vamos criar um campo chamado slug e é nele que vamos por nossa regra, como por exem,plo sem carcteres especiais , sem traços etc. lembrabdo como criamos um campo novo temos que fazer os processos de migrations, agora na no admin no nossa categorias vamos ter o campo do slug e podemos por como queremos q ele seja escrito pra podermos utilziamos. vamos fazer a msm coisa pro tipo. so temo que agora ajeitar o nossa html invez de usar o categoria.nome la no link como dito no paso acima, vamos usar o .slug. Alem dessa alteração la no nosso viwes.py, quando filtramos o produtos fizemos uma filtragem avançada cujo a categoria tinha q ser igual ao nome daquele produto agora n vai ser mais o nome, agora vais ser o slug tbm. pq agora naquele nome_categoria vem na verdedade o nome do slug.


32- No nosso views a nossa função  tem 2 parametros, o request e o que colocamos como nome_categoria, esse segundo parametro nos vamos mudar para nome de filtro, para ficar mais intuitivo ja que realmente é o filtro que colocamos no site q é enviado para esse parametro. Lembrando que ao mudar o parametro ali temos q fmudar o nome tbm dentro dessa função, alem de mudar tbm  na no nosso arquivo urls, que recebe tbm esse parametro. Agora que mudamos vamos partir para a logica para poder filtrar de acordo com o tipo e catagoria ao mesmo tempo.

O que vamos fazer agora é criar um novo arquivo chamado utils.py, que basicamente vai ser um arquivo para por funçoes como de filtar, ordenar  e etc, para poder usamos na nossas funçoes dos arquivo views.py.

Primeira temos um if para verificar se tem um filtro, logo apos temos q verificar se possui um "-" no nosso filtro , porque lembrando que se possuir um filtro de categoria e tipo eles sao separado por -. entao se tiver vamos pegar esse tipo e categoria. para pegar esse filtro e separalos, o que vamos fazer vai ser um split apartir do - isso nos dara uma lista com dois item ai podemos fazer o nosso onepaken. agora basta importa essa função de filtrar pro nosso views e filtrar nosso produtos na nossa função loja.


33- o que vamos fazer agora , vai ser uma local no nosso site, que vamos poder filtrar os nosso produtos , atravez de preço , tipo e etc. é basicamente aquelas abas onde podemos escolher o produto q aparece para a gente de acordo com as caracteristicas que desejamos, que  vai ser basicamente um formulario.

Entao primeiramente vamos trabalhar no nosso loja.html, inicialemte vamos ter , preço , tamanho, categoria e tipo, entao como vai ser um formulario vamos fazer eles dentro de um form. O preço ele vai possuir dois input um vai ser de valor maximo e outro de valor mininmo, o nosso tamanho ele nos vamos colocar pra o nosso usuarios escolher um dos tamanhos, entao temos q ter ter um for para eprcorrer todos os tamanhos disponiveis, basicamente igual o nosso for la no  nosso ver_produtos.html, o que sera basicamente igual para nossa categoria e tipo que tbm ira ter um for, igual o que encontrameos basicamente na nosso navber.hmtl so que les seram separados, a outra diferença é que la no nosso navbar elas era links, mais aqui elas vao ser inputs a serem selecionados

Agora la no nosso views.html na nossa função da loja , nos temos que pagar aqueles valores que serao utilizados la no nosso formulario de filtro, inicialmente vamos colocar eles la manualmente para ver se esta  tudo ok com nosso formulario, depois pegaremos esses valores de formas dinamica.

Depois de testados, vamos primeramene trabalhar em como pegar os valores minimos e maximos, pra isso vamos importa  o django.db.models import min, max. o que vamos fazer e utilizar o aggregate, que vai pegar todos os itens da nossa tebela e junta em uma linha, dps vamos passar o MAX e dentro dele vamos dizer quem é que queremos pegar no nosso caso é o campo preco dos nosso produtos , so lembrando q esse campo ela do models.py, alem disso como queremos os valores desse campo temos que por o .value() para pegalos. so que queremos  pegar esse valor e para pegar esse valor temos q trasforma isso em uma lista python entao vamos pegar tudo isso e por em um list e depois pegar o valor do indice 0, porque o que ele retorna na verdade e um dic_values e assi m nao conseguimos epgar esse valor, agora e  so fazer a msm coisa pro minimo, agora podemos tirar aqueles maximo e minimo que colocamos manualmente para teste. e so vamos passar alim um round() que é uma ferramente parao do payto npara erredondar numero par anao ficar com varias casas decimais.

Lembrando que esse filtro vemd e  acordo com a lista que vem para agente, entao se filtramos para masculuno, os valores alteram , assim como para feminino  etc. vimos que se colocarmos o filtro calçado deu um erro, porue nao achou nenhum prodturo, entao vamos definir um minimo  e um maximo como 0 e dps fazer um if para verificar o tamanho da lista.

Construimos tudo isso na nossa função da loja, porem podemos faer uma função la naquele nosso arquivo utils.py e so chamar a função.


ex: site para consulta de criaterios como __gt, __in; https://docs.djangoproject.com/en/5.1/ref/models/querysets/
34- Agora nos vamos pegar os tamanhos, mas se olharmos nosso models.py vamos observar que na nossa class produtos, nao possui o campo tamanho, o nossos tamanhos na verdade esta na nossa  class itemestoque que é associada aos produtos, entao é basicamente do itemestoque que vamos tirar todos os nossos tamanhos. mas primeiro temos que pegar os itens que temos no nosso itens estoque cujo a quantidade é maior q 0, e o outro criterio é que o campo "produto" dos nosso itensestoque  que queremos esta dentro de uma lista de produtos que é nossa lista de produtos que filtramos. Entao o produto__in= produtos, quer dizer que o campor produto esta dentro da minha lista de produtos (a que nos filtramos). o que fizemos aqui foi pegar o nosso itensestoque e filtrar eles de acordo com os filtros que colocamos la no site. e agora dentro dessa lista vamos pega os tamanhos usando um value_list() e passando para ele o nome do campo que queremos pegar evamos coocar um .distinct() que tras os valores de formas unicas e nao repitinda por exemplo varios tamanhos p. O FLAT=TRUE serve para fazer um one pacck se nao passar ele vai entregar uam tupla, porque o caso  o value lsite voce pode pegar varias coisas junto, por exemplo ("cor", "tamanho",), ai ele retornaria uma tupla comm dois valores, mas como queremos so um campo.

Por exemplo se quisecemos pegar as cores, pegariasmo a cor que no caso ela  vai nos retorna od id das cores, e depois fariamos uma busca cujo id esta dentro do ids da cores que buscamos

ex: ids_cores = itens.values_list('tamanho', flat=True).distinct()
    cores= Cor.objects.filter(id__in=ids_cores)

35- Nessa etapa nos temos que aplicar os filtros do formulario q criamos,so para lembrar  o filtro que fizemos anteriormente pra quando clicamos la no nosso navbar vem de acordo com o link do nosso site.

Continuando na nossa função loja, ja filtramos os nossos produtos atraves do link, entao dps dess filtro, nos vamos construir o filtro do post pra isso vamos verificar se tem um post que veio apartir de um usuario, que nos caso vai confirar que o usuario utilizou os formulario para filtrar sua busca. agora temos que pegar os dados desse post, o que ja aprendemos a fazer com o request.post.dict e ai filtrar esses dados, nos podemos rebuscar nossa função de filtrar q utilizamos para filtrar pelo link, colocando ela pra filtrar precomaximo e minino, mas n vamos fazer isso no momento. lembrando tbm que o usuario pode inserir apens uma informação talvez so por preço ou so tamanho

agora que ja pegamos o dados, vamos primeiro filtrar os produtos de acordo com o preço, vamos usar para: __gte (maior ou =) e __lte(menor ou igual). depois vamos verificar pelo tamanho lembrando que os nosso dados ele é um dicionario entao se procurar o item "tamanho" ele verifica se tem aquela tabela ok.

Agora temos que filtrar o tamanho dos produtos , mas lembrando que o tamanho ele é uma caracteristica do itemestoque e nao do produto entao vai ser diferente. entao vamos verificar se tem "tamahos" nos dados, depois vamos pegar  os itens de acordo com nossos produtos ja filtrados  e tambem filtrar o tamanho de acordo com tamananhos do dados, entao nossos itens dessa filtragem pode ser camisa basica preta  tamanho m, camisa basica cor branca tamanho m, entao podemos ter diferentes variaçoes do msm produto 
 
depois vamos precisar pegar o ids do produtor vamos pegar com o value list , de acordo com o campo produto, agora vamos filtrar nossos produtos onde os id esta dentro da  nossa  lista de ids_pdotuors.


36- agora vamos continuar os filtros de acordo  com os tipos, entao vamos verificar categoria no nossos dados, e filtrar nossos produtos de acordo com o tipo,  alem disso vamos limitar a no nosso formulario a parte que mostra a categoria , pq ja conseguimos filtrar ela pelo link.

como fazemos isso vamos pegar os ids_categorias com o value_list, depois vamos filtras nossas categorias de acordo com esse ids, uma observação que ocorreu foi que la no nosso arquivo novos_context nos ja tinhas uma variavel chama categoria entao ela acabou sendo suistutuidas por essa que criamos agora, entao la no no arquivo novos_context nos vamos mudar o nome dessa variaveis para categorias_navegacao e tipos_navegacao, sem essa alteração a nossa barra de navegação tbm ficar limitada e nao mostrara todos os tipos. 

Alem disso la no for do tipo no nosso arquivo loja.html, atavos fazendo o for pelo tipo vindo da barra de navegação entao temos que mudar la tbm para tipos_navegação.

tbm temos que fazer a verificação para a categoria, ja q ela tbm pode ser utilizada no fomrulario

37- No proximo passo nos vamos criar um ordenador, para podermos selecionar por maior preço, menor preço, mais vendidos etc, mas antes vamos por nosso formulario e tbm o for de produtos dentro de uma div la no nosso arquivo loja.html so para facilitar a visialização. dando inicio ao sistema de ordem o que vamos fazer nada mais é do que uma lista html , no que vamo associar a cada alemento da lista a função para ordenar. 

o href desses links vao ser um # , porque queremos que ee continue na msm pagina, entao o # permite isso faz com q n direcione para nehuma outra pagina que carrega naquela propia pagina, tambem vamos  passar uma classe para esse links para que podemos editar esse itens igualmente com o javascript, alem disso vamos por o parametro name, para poder usar no java script, onde ele vai usar o parametro name para passar para o nosso link

Lembrando que o django ja permite essa interação em html. 

Alem disso vamos ter que usar um pouco de java script aqui, no dentro do nosso projeto nos criamos a pasta static, nela temos a pasta js que é nossa pasta para aquivos com java, nela nos vamos criar o arquivo main.js, esse arquivo ele vai precisar rodar na nossa pagina loja, aqui temos 2 opçoes , podemos colocar ele pra rodar apenas na nossa loja ou configurar para que esse arquivo estaja disponivel para todo as paginas do nosso projerto que nada mais é que adicionar ele (scrypt) la no nosso arquivo base.html, la no nosso body, baixo do block body, pq ai ele vai carregar toda a pagina e so dps ele vai carregar o nosso script.


38- vamos da a continuidade acima, so  lembrando que vamos utilizar o java para fazer de uma forma mais eficiente, mas poderiamos fazer da msm forma que fizemos com o link, que foi passar um parametro la no url, criar um url, views etc. 

O que nos iremos fazer vai ser, que  os links(mais vendidos , maior e menor preço) que criamos, eles possuem esse link vazio, entao vamos pegar e prencher esse link com um link do nosso site na qual qual estamos no momento e vamos acrecentar o name que assosianos a ele por exemplo o menor-preco.

entao la no nosso main.js vamos fazer uma  variavel, e para fazer uma variavel tem que por o var no inico depois o nome, vamos criar uma url, pra isso vamo usar new ULR(), temos que passar o document que é a nossa pagina e ULR é o que queremos criar, depois temos que pegar os itens da nossa pagina que possui algum elemento em especifico , no nosso caso nos demos uma class para esses itens e é por ela que vamos  pegar esse itens, entao la no nosso entao vamos pegar la com osso javascript, agora temos que percorrer esse itens pra ser mais dinamico, no java entre () nos colocamos as regras e {} nos colocar o que vai ficar em looping,


39- agora que nossa ordem esta indo para o nosso link nos conseguimos pegar essa informação, essa informação vai la para o nosso quest  da nossa função loja do arquivo viwes , entao vamos pegar essa ordem la no nosso views, no caso vamos colocar o parametros que queremos pegar , mais depois tambem vamos passar o parametro que caso nao nenhum parametro vamos por esse como principal, que no caso tem q ser um dos  parametros ja existentes, no nosso caso temos 3, menor-preco, maior-preco , mais vendidos. essa nosso viwes ja esta muito grande
entao  vamos fazer uma função no nosso arquivo utils para ordenar nossos produtos. so tem um detalhe os produtos mais vendidos nos teremos que criar de de outro jeito.

40 - Agora vamos ter que ver uma maneira de ordenar pelos produtos mais vendidos, se olharmos no nosso models, a quantidade dos nosso produtos esta no nosso itenspedido, entao temos que pegar essa quantidade que tem que esta relacionada a um produto em especifico.

Poderiamos fazer toda a logica na no nosso arquivo utils.py no elif dos mais-vendidos, porem acho q o que seria mais interessante, seria la no nosso arquivo models.py na nossa class de Produtos, criar uma função no qual calcula os totais de todos os produtos.

Entao vamos fazer um função de total_vendas la na nossa class produtos, pra isso nos precisamos saber todos os itenspedidos no qual o  pedido ja foi finalizado (pq queremos os mais vendidos). entao vamos pegar esse itens, alem disso nos temos que saber qual produto estamos olhando, no caso entao temos que fazer o se gundo filtro seja atravez do id daquele produto. 
agora que temos uma lista de itens que no caso e uma lista de itenspedidos, temos que somar a quantidade e vamos fazer isso atravez de um listening comprehension, agora la no nosso arquivo utils.py nos ja conseguimos percorrer nossa lista de produtos, so que precisamos que essa lista estaja ordenada de forma correta, pra isso vamos criar uma lsita de produtos vazia a cima do nosso for, entao dentro do for nos vamos armazenar nessa lista em foram de tupla o valor total de vendas e o segundo valor o objeto produto. ex; (3, produto:nome: camisa basica, catego: maculiano , tipo:camisa, preço :79.99). e a vantagem disso é que como o primeiro  item dessa tupla e um numero ou seja a quantidade de vendas e com isso podemos usar o sorted para ordenar essa lista , pq o sorted pega o primeiro item da lista para ordenar.

Agora o que acontece é que nossos produtos, agora vai ser o segundo item dessa lista que acabamos de ordenar porque queremos aquele produto e não o numero dele, e agora quando clicarmos ele vai trazer os produtos pela ordem de mais vendidos, a maioria das funcionalidades da nossa loja termina aqui.

41- Agora vamos mecher nos nossos views e nass nossa paginas de fazer login e minha_conta e tambem iremos criar uma pagina para o cria_conta com aquelas3 etapas uma views, um html e uma url para essa pagina, alem disso vamos ajeita alguns, lembrando que ja fizemos o views o urls para o login e para minha_conta, alem disso vamos  la no html do nosso navbar, ajeitar para que se o usuarios estiver logado so aparecer na nossa barra de navegação para ele ver a conta dele, e caso nao esta logado apreceça o link para ele fazer login, basicamente vamos fazer isso com um if usando o is_authenticated.

Despois da verificação com if vamos mecher no nosso html de login, la basicamente pra o usuario fazer o seu login ele vai precisar ter um formulario do method post, com tres campo, email, senha e um botao que vai ser do tipo subymit que vai enviar essa informaçoes, é depois tambem vamos fazer um formulario para criar_conta.

42- Agora o que vamos fazer vai ser o sistema para nosso usuario fazer login, lembrando que o nosso usuario ja possui um cliente autenticado quando ele for criar a conta etambem que o nosso usuario ele vai o login dele vai tambem ser sempre o email dele. o primeiro passo que vamos fazer vai ser la no nosso views.py mudar o nome da nossa função login para fazer_login , pq vamos importar  (login, logout, authenticated) e para nao ter problemas com nomes iguais vamos trocar, e consequentemente mudar onde esta função esta sendo utilziada.

o primeiro passo vai ser verificar se o usuario esta logado, o segundo passo vai ser verificar se o usuario que esta tentando logar preencheu  o nosso formulario entao temos que ve se foi enviado um metodo post, entao tambem la no nosso formulario o action dele vai ser o url desse fazer login, que no caso nos estamos enviando esse requisição para essse link. Entao se tiver um method post vamos pegar esses dados, que no casso sao nosso email e senha.

Para o nosso login dar certo esse dados que pegamos acima, tem que ter o nosso email e nossas senhas, caso nao tenha um dos dois entao vamos considerar que já é um erro, entao temos que fazer essa verificação, se tiver esse dados entao vamos  pegar esses dados preenchidos e abaixo autenticar atavres do authenticated que importamos, o authenticated pede o request,username e a nossa password. aqui passamos o request pq o djando ele vai procurar no Banco de dados se posssui um usuario com essa senha e email, pq lembra que importamos e  usamos o user  para criar nossas classes entao o django pega esse usuario e senha com esses informaçoes passadas e devolve para agente . 

Agora iremos fazer login , pra isso vamos fazer um if para verificar o usuario , e ai fazemos o login desse usuario atreves do login que importamos, caso de certo direcionamos ele para a loja. 

Nessa etapa fizemos elses como uma variavel de erro pq ai podemos usar essa variavel no nosso html para exibirmir mensagens de erro.


43- agora vamos fazer o precesso para criar cona no usuario, vai ter bastante coisa parecida com o login aqui tambem tera varios elses com erros diferente pq assim podemos demostrar isso para o nosso usuario , o primeiro passo vamos verificar se o cliente ta logado e se tiver vamos redirecionar pra loja normalmente e o link do nosso formulario vai ser o link do url criar conta. 

Segundo passo é verificar se esta sendo enviado o metodo post, e pegar esses dados  iualmente ao login so que nesse tem q ter noe email , senha e a confirmaçõ da senha entao vamos verificar se tem essas 3 coisas para seguidar para a proxima etapa.

Agora que pegamos os dados vamos, vamos separalos para utilizar eles para criar nossa conta, mas antes nos temos que validar esse email, no html ele meio que ja faz isso porem vamos fazer no nosso codigo tambem, pra isso vamos ter que importar 2 coisas o validate _email  e o validate erro. o que acontece é q vamos usar o validate_emal pra validar ele vai nos retornar o validate erro e para usar ele no nosso codigo precisamo importar o valide errro porque ele nao e nativo.

Entao para validar o email, vamos por ele dentro de um try pq ai ele vai tentar validar caso nao consiga significa que ele caiu no nosso validate erro entao excep validateerro , agente define um erro para mostra para o usuario

A proxima verificação  vai ser verificar se a senha e confimação de senha são iguais entao fazemso mais um if para isso, se ele passar dessa verificação vamos criar nossa conta aqui, lembrando que ja existe a nossa tabela de usuario por isso podemos criar a nossa conta direto pq ja usamos o use la no nosso models. O que vamos criar para fazer o usuario vai ser o get_or_create, pq caso ele ja possua aquele email e aquele usuario igual aquele email preenchido  o  criado vai ser false, entao ja ja possue um usuario com aquele email, e agora basta so definir a senha para desse usuario q esta sendo criado com set_password passando asenha que foi preenchida, lembrando que como editamos o usuario depois de ter criado temos que dar umsave.

obs; nesses passos nos fizemos com q o username e o email sempre senha iguais ou seja sempre o email o que tanhamos q garantir para nosso codio rodar liso, por causa de algumas estapas acima.


Agora temos q fazer o login pra esse usuario que foir criado, basicamente é autenticar esse usuario e fazer o login.

Agora e uma etapa muito importante , pq lembra que temos q associar um cliente para o usuario, caso isso nao tenha sido feito o nosso site vai começar a dar erro pois pra q nosso site funcione nos precisamos de um cliente associado ao nosso usuario.

 Lembrando tambem que podemos criar um cliente direto,  porem o que vamos fazer aqui tambem é verifficar se tem algum usuario anonimo no nosso site colocando comprar no carrinho, caso esse usuario estaja como anonimo colocando coisas no carrinho nos vamos pegar esse id seção e associar um cliente a ele caso ele queira criar uma conta, pq assim esse usuario anonimo nao perde as coisas que ele ja colocou no carrinho.

Entao basicamente vamos fazer igual fizemos pra verificar se tinha aquele id sessao e caso tenha o que temos q fazer é editar esse cliente colocando o email ali,  , e caso nao possua nenhum id sessao ai nos criamos o cliente normalmente.

44- O que temos que fazer agora é uma verificação la no html atravez dos if para exibir os erros para o usuarios, depois fazer o logout. Entao vamos começar pelos exibição de erros , aqui no caso vamos fazer um if para cada tipo de erro.

45- Agora vamos fazer o processo de logout, que na verdade e bem simples, basta la no nosso views fazer um função de fazer logout usar o logout que importamos e nesse logout passar o request, não precisamos passar um usuario pos essa informação ja esta contida no nosso request. lembre que pegamos o usuario atraves do request.user. dito isso como fizemos uma função temos que fazer um url para essa função tbm.

vamos tambem bloquear alguns views do nosso site para ser acessado somente para quem estiver logado, para isso vamos precisar importa os decorators, ai é so por o decorators emcima da função que voce quer q ele atue.

se o usuario tentar entrar no minha conta msm tando deslogado ele vai dar um erro , esse erro possui um camiha que e acconts/login/ etc. o que  vamos fazer aqui vai ser para que esse caminho seja o caminho para a pagina de fazer login do usuario, para isso basta ir no arquivo settings e  criar um LOGIN_URL=" NOME DO LINK DE FAZER LOGIN".

lembrando so estamos fazendo isso pq fezemos com que o caminho do fazer login fosse outro e nao o  que o djang normalmente define como padrao.

46- Agora vamos mecher na parte de redefinção de senha, mais nos vamos aproveitar a estrutura que o proprio django da, porque se nao teriamos que criar tudo zo zero.

Muito que vamos usar nessas etapas , tudo vai estar disponivel da DOC do django que ta la no inicio desse guia , lembrando q toda estrutura do django esta dentro do django.contrib.auth. , por exelmplo la tem todos os links q usamos do nosso urls por exemplo: login, logout , porem esses nos msm fizemos pq queriamos persoanlizar eles, porem muitos sites reutilizam a propia estrutura que ja e dada quando se trata desse sistema de alteração de senhae é isso que vamos fazer

Vamos supor que eu quero q meu usuario consiga redifinir a senha, para isso nos terimos que criar um url, uma views  e um templete e depois criar toda a logica para q isso aconteça certo?

Porem o django ja tem essas views prontas, basta agente importa essa views la no nosso arquivo urls.py atraves do contribi.auth, e  vamos utilizar essas views atraves dos links ,  entao  agora so presisamos passar os urls la no nosso arquivo urls, sem precisar criar nada no nosso arquivo views e nem templates, os path que vamos passar esta tudo na documentação do django.

Depois de colocar todos os path la no nosso urls, temos que agora naquele link de redefinir a senha, passar esse urls, entao vamos la no nosso html do login que é onde ta esse link e passar essa url e agora se tudo deu certo nosso sistema de redefinção de senha ja esta todo ponto.

Nesse parte quando se clica no esqueci miha senha, ele vai ter q enviar para o seu email um link para voce alterar sua senha, e para q isso aconteça nos temos que conectar a um serviço oficial de email  e etc para que faça tudo certinho mas n vamos fazer isso agora, o que vamos fazer vai ser que vamos pedir para o django fazer um print desse link para trocar de senha  no nosso console e para fazer isso temos que por la no nosso settings uma variavel que é:

EMAIL_BACKEND= "django.core.mail.backends.console.EmailBackend"


obs: o nosso site esta todo em ingles entao nessa parte vai estar tudo em ingles, caso queira colcoar tem portugues basta ir no arquivo settings na parte de internalization, e por "pt-br"e tambem pode colocar o horario la tbm "America/Sao_Paulo" .


47- o que vamos fazer agora vai ser exibir os pedidos relacionado aquela conta, pra isso nos temos que criar uma views, uma url e tambem um templete que vai ser o  meus_pedidos. mas pra que possamos testar  temos que ir no nosso admin e por um pedido como  finalizado, colocar um endereço , data e codigo de transação para aquele pedido 

Agora vmos la na nossa viwes do meus pedidos e a primeira coisa que vamos fazer vai ser pegao cliente, porque precisamos saber qual é o usuario logado, depois temos que pegar os pedidos desse cliente entao vamos fazer um filter de acordo com: o campo finalizado igual a TRUE  e que o cliente seja igual o cliente que esta logado que foi pego acima , agora bas passar esse pedido po context.

depois disso nos vamos ter que percorrer nossos pedidos e por as informaçoes que queremosque seja exibida para o usuario ver, esses pedidos iram vir la do nosso context da nossa views de meus_pedidos. lembrando q os campos desse pedidos estao tudo na no models, alem disso lembresse que tem algumas classes que possum funçoes especifica para elas tipo o preço_tottal dos pedidos.

Agora temos que pegar todos o itens relacionados a esse pedido, nos temos duas formas a ormeira seria fazer uma função para nossa classes pedidos  que pegue esse itens, ou podemos pegar esses itens la na nossa views meus_pedidos e manda eles pelo context.

vamos fazer o da fução para exercitar isso, entao no nosso pedido vamos fazer uma funçao itens(), nessa função entao vamos pega nosso itens q inclusive ja pegamos esse itens para uma outra função dentro do pedidos e ai é so fazer um return com esses itens.

agora la no nosso html podemos percorrer esse itens, e ai mostrar o que queremos , no nosso caso vai ser imagem, quantiade, preço e o produto. lembrando que pra iamgem temos que fazer todo o caminho da nossas classes ate chegar na imagem.

48-  Agora vamos fazer a pagina do minha conta, aqui nos vamos ter 2 formulario , um e o formulario para os dados do cliente e outro vai ser para alterar senha, o formulario de alterar senha aqui poderiamos fazer por um link que leva para aquela pagina de alterar senha, bastando passar o urls daquela pagina, porem vamos seguir com dois formularios para intuito de treino.

Ambos o formularios vao ser do metodo post, e ambos vao enviar para o proio url do minha conta, no input vamos fazer uma verificação para caso tenha algo escrito para aquele input ele ja prencha automaticamente, caso nao tenha nada vai aparecer o placeholder que criamos.

49- Agora nos temos que tratar esses formularios que estao sendo enviados la na nossa pagina lembrando q a pagina tem dois formularios e vamos fazer tudo na msm verificação, primeiro vamos tratar o formulario de senhas, entao la no views(class) minha conta,  vamos por uma variavel erro para exibir isso para nosso usuario que inicialmente ela vai estar none, depois vamos verifficar se ouve um method post , que no caso é se o nosso formulario foi enviado, entao pegaremos todos esses dados que foi eviado atrasves do .post.dict.

Aqui nos vamos verificar se a uma "senha atual" esta nesses dados, porque se a senha atual esta nesses dados é porque o usuario esta tentando modifficar essa senha entao ele enviou o ormulario de trocar de senhas, caso esteja nos vamos pegar todos os dados que foram enviado no fomulario.

Agora vamos verificar se a nova_senha é igual a confirmação de senha com um if , depois nos temos que veririficar a enha_atual que foi preenchida corresponde com a esnha que essta criptografada no nosso bancos,  e como vamos fazer para verificar essa senha ses ela ta criptografada.

Aqui nos vamo procurar um ussuario atraves do authenticated, pq ele conegue veriricar msm tando com essa criptografia, basta  procurar  o userame que corresponde o email daquele uuario e cujoa senha seja igual a senha_atual ue foi pasada no formulario, entao vamo fazer um if usuario, pq caso ele encontre esse usuario significa que as senhas sao iguais , dai é so modificar a ssenha setando a senha com a nova_senha, salvando , tambem vamos colocar uma variavel de alterado para que possamosss exibir uma menssagem de suceso ou d e erro para o  nossso ussuario.


Agora nos vamos fazer um elif e verificar se tem "email" nessses dados caso tenha ele enviou o formulario para alteração de  seus dados, caso tenha vamos fazer a msm coisa que no formulario de cima, pegar cada dado enviado, depois vamos verificar com um if se o email que foi prenchiado no formulario é diferente do email do nosso usuario, pq isso significa q ele ta tentando trocar seu email, porque lembra que nesses formularios nos colocamos pra alguns dados ja virem prenchido com o proprio email nome etc. 

O que temos que fazer aqui é garantir para que esse email que foi preenchido não seja igual a outro email que ja esta cadastrado, entao vamos procurar se tem algum usuario preenchido com esse email atraver dede um filter, dps é so verificar se o tamanho do usuario for > 0 sigffficica que ja tem alguem com esse email cadrastrado, se nao for entao podemos fazer as modificaçoes.

Entao if not erro, se nao ouver um erro, vamos pegar primeiro o nosso cliente atraves do request. lembrando ue aqui temos que trocar tanto o email desse cliente como tambem o email que e relacionado a esse usuario. lembra que todo usuario criado tem um cliente associado.

vamos trocar o email do usuario e do cliente para o email prenchido e as outras informaçoes e dpois dar um save tanto para o usuario quanto para o cliente, aqui terminamos a verificaçoes dos nossos ffformularios.

Agora o que resta é ir la no html da miha conta e fazer os if de todos os erros.

50 - Agora vamos começar a mexer na funcionalidade de finalizar o nossos pedidos, lembrando que  nesse projeto vamos fazer a integração real com uma api verdadeira, que vai  ser a api do mercado pago, masss nessa etapa de agora n vamos fazer isso inda.

Entao quando etamos no nosso carrinho nos podemos ir para a nossa pagina de chekout, nessa pagina basicamente temos um ormularios com os nosso pedido, com opçoes de por endereço e etc. 


Primeiramente o que iremos fazer vai ser criar um norvo arquivo chamado api_mercadopago.py que vai ficar n o msm lugar dos arquivo views etc, esse arquivo que vai ter todas a nossas funcionalidades relacionadas ao mercado pago, é sempre bom fafzer um arquivo desse quando voce vai relacionar com um api externa, depois e so importa essas funcionalidade para onde voce quer usar. 

Segundo o que vamos fazer vai ser criar uma nova views que vai ser o finalizar_pedido, que vai receber o request e o id_pedido pq temos que saber qual é o pedido a ser finalizado, tbm tremos que criar  uma url para essa views que tera  tambem o id do pedido . O formulario da nossa pagina do chekout vai ser conectada comm essa pagina do finalizar_pedido, entao la no action do formulario da nossa pagina de checkout que ainda n tinha nada vamos por o url do nosso finalizar_pedido e tambem passar o pedido.id que é o que precisamos. 

obs: aqui so pra saber se essas estapas estao funcionando colocamos o nossa views para apenas redirect para a loja, entao quando colocar um pedido no carrinho clicar no cekout adicionar um endereço clicar no botao de finaliar pedido temos q voltar para a loja

A terceira etapa é ter que fazer o tratamento de alguns dados pata quando se clicar nesse botao de finalizar compra e redirecionar para a pagina de pagamento  esta tudo correto, lembrando que temos duas opçoes aqui, primeira do usuario logado que temos q garantir que ele colocou um endereço, e pro usuario deslogado alem do endereço temos que garantir que ele colocou um email ali se nao teremos problemas. 

Entao a primeira coisa dessa terceira etapa  e pegar todos os dados que esta vindo desse formulario, entao vamos fazer a verificação para ver se tev um method post que no caso é q se enviaram um formulario, depois pegar os dados, depois vamos verificar se nao tiver um endereço nos dados, aqui temos que lembrar q quando pegamos o endereço na verade o que nos estamos recebendo é o id do endereço entoa temos que pega o endereço na nossa tabela de indereço se nao mais pra frente no metodo de pagamento vai dar um erro ,vamos mostra um erro  para o nosso cliente entao temos que por esse erros num context e passar no nosso redirect , caso contrario vamos pegar esse endereço.

Agora temos que verificar se o usuario não esta logado  entao caso o usuario nao esta logados, temos que pegar o email, porque estamos presupondo que ele preencheu o email, depos vamos fazer uma try para fazer a validação desse email caso ele consiga validar o email é porque tem um email ali, caso nao entao vai ddar um excep validation err ai nos demostramos algum erro.

OBS: para testas basta por um print do erro depois do context, e ir simulando erros no nosso site q aparecera os erro no nosso terminal 

Uma coisa importante tbm vai ser q temos que pegar o total do pedido na no começo desses tratamentos, porque temos que ver se o total que esta vindo  corresponde com o total que esta no nosso banco de dados, porque se o usuario sabe mecher html, css ele pode alterar esse total manualmente, e alem  do total nos vamos tambem pegar o nosso pedido, para fazer esse verificação . vamos fazer essa estapa antes das verificaçoes acima para garantir.

51- O que temos que fazer agora é que quando o usuario  tiver nessa pagina do checkout e tentar finalizar , caso ele não preencha algum dos requisitos que acabamos de fazer,  ele volte para a pagina de chekout e mostre alguns dos erros.

Temos duas formas de fazer a primeira com um redirect pra nossa pagina de checkout, e nesse redirect  passar um parametro ue no casso seria o nosso erro por exemplo: return redirect("checkout", erro) la no redirect depois do erro , mas dessa forma nossa views teria que receber nosso o erro tambem ao lado do request que a principio seria none, porem o views que receberia isso e a chekout que mostra toa a nossa pagina de chekout.

A segunda forma que é a que vamos fazer vai ser, utilizar o checkout.html da nossa views checkout, é utilizar ela na nossa views finalizar pedido, nos conseguimos fazer isso, pq para esse html ele precisa basicamente de um pedido e os endereços, sendo que na nossa views finalizar pedido nos ja temos um pedido que é o pedido cujo esta relacionado aquele que quer ser finalizado, entao nos teremos que pegar apenas o endereço relacionado ao cliente daquele pedido.

Entao o que vamos fazer vai ser dps da verificação de erros nos vamos verificar se possui algum erro (if erro),  entao vamos pegar o endereço do cliente que esta querendo finalizar o pedido atraves de um filter, o pedido nos ja temos entao n precisamos pegar. Agora o nosso context q antes possuia os erros vai ficar dentro desse if, mas recebendo tanto o endereço quanto o pedido, depois vamosdar un return com um render com a request, a pagina html do checkout e com o nosso context com todas nossas informaçoes, alem disso o que vamos fazer vai ser q la no context que enta na nossa views do checkout, vamos por  um   erro cujo o valor dele inicial vai ser none.

Agora temos que pegar esses erros e mostrar la na nossa pagina de checkout , entao temos que ir la no html da nossa pagina de checkout e fazer os if para o nossos erros, agora se formos no nosso site e fizermos os teste tem q esta mostrando essa mensagens de erro.

Agora nos vamos fazer uma etapa muito importante que não fizemos quando verificamos se o usuario nao estava logado, entao la no if que verificamos se o usuario nao esta logado depois depois do try de validiação pra ver se o usuario preencheu ou nao ou email, se o usuario preencheu o email e nao deu nenhum erro nos temos q verificar se aquele email ja esta no nosso banco de dados, porque derrepente aquela usuario apenas n logou na conta dele.

entao o que vamos  fazer vai ser um if not erro depois desse try, entao vamos  procurar no nosso cliente se possui alguem registrado com esse email, entao vamos fazer um if cliente para caso ele ache esse cliente, entao caso ele ache um clente nos vamos pegar o pedido.cliente que o cliente relacionado ao pedido que estamos tentando finalizar e alterar para o cliente que achamos na lista q o filter nos retornou.

caso ele nao encontre , podemos associar o email que ele prencheu ao cliente.email daquele pedido.

Agora nos temos que associar um endereço a esse pedido, que é bem simples la quando verificamos se o usuario colocou algum endereço basta  pegar aquele endereço e por ele no pedido.endereco.

obs: aqui a cada atribuição ao pedido como no pedido.endeco ou no pedido.cliente que vai ser igual ao cliente q cfoi encontrado, como editamos o nosso pedido nos teriamos que dar o pedido.save.  em cada um deles, porem podemos coocar o pedido.save( fora desses if e salver ele apenas no final)

alem disso nos temos que associar um codigo de transação para esse pedido , que pode ser qualquer numero por exemplo poderiamos usar o uuid que era numero aleatorio, mais o que iremos fazer vai ser pegar o id do pedido e concatenar com a epoch data que o usuario finalizou o pedido.

pra isso vamos importar o date time e usar o datetime.now junto com o timestamp que nos da essa data epoch


obs:EPOCH é uma serie de digitos que corresponde aquela data, esse numero ele corresponde a quantos segundos essa data esta de uma data especifica que é uma referencia  de janeiro de 970.

52- O que vamos fazer agora vai ser a integração com o meio de pagamento, iremos usar a do mercado pago, a que vamos utilizar vai vai ser a aba preferencias, que é basicamente um link que vai direcionar para uma pagina de pagamento.    

O primeiro passo vai ser criar uma conta no mercadopago nessa conta nos vamos criar uma aplicação com o nome do projeto que voce esta fazendo porem nao vamos usar isso agora, o que vamos fazer vi ser usar contas de testes e seguir ate o nosso projeto esta finalizado depois no final , entao nessa conta de mercado pago nos vamos criar uma conta de teste uma para vendendor e outra para comprador, quando essas contas ja tiverem criadas nos iremos abrir a guia anonima do google, e entrar no site do mercadopago la vamos entrar na conta usando o usuario e a senha do vendedor que acabamos de criar.

O segundo passo vai ser fazer uma integração igual nos fizemos na nossa conta , entoa nessa conta nos iremos entrar nas credenciais de produção  la  nos teremos nossas chaves de acesso.

O terceiro passo vai agora vai ser baixar a biblioteca do mercado pago pip install mercadopago, e la no arquivo do mercado pago que criamos no vamos iporta a biblioteca do mercado pago e criar  nossa public key e nosso token que vao ser as que esta la no nosso usuario de vendedor. 

OBS: esses sao os dois que teremos que trocar caso queira que realmente o projeto vai pro ar e as pessoas paguem para cair na sua conta entao basta troacr esses dois para o que tem na sua conta.

53-OBS.:Para testar o nosso site e quiser efetivar uma conta , nos temos que esta em uma aba do navegador que estaja logada na conta do nosso comprador ai vamos utilizar um cartao que ele disponibiliza para essa conta de teste.

<!-- sdk = mercadopago.SDK(token)


#CONFIGURAÇÃO DE CREDENCIAIS
sdk = mercadopago.SDK(token)


preference_data = {
    "items": [
        {
            "title": "My Item",
            "quantity": 1,
            "unit_price": 75.76
        }
    ],
    # "back_urls": {
    #     "success":link,
    #     "pending":link,
    #     "failure":link,
    # }
}
preference_response= sdk.preference().create(preference_data)
resposta = preference_response["response"]
link= resposta["init_point"]
id_pagamento = resposta["id"]
print(id_pagamento) -->


Mas antes temos que contruir todo nosso codigo nossa estrutura que vamos precisar. que coisiste em um sdk que vai receber nosso token, de umarequisição que vai ter o itens que o cliente quer comprar com todos os dados que no nosso caso é o preference_data.

Agora nos temos que configurar nossas credenciais  no sdk iremos passar o nosso token.

Embaixo nos temos o preference data ou (payment_data), aqui temo os dados que iremos mandar pra requisição, que no caso é o que queremos cobrar do nosso uauarios etc.

O preference_response ou (result) e como vamos criar esse requisição, que no caso é criar um metodo de pagamento  com os dados que temos para cobrar nosso cliente. aqui se printarmos vamos ver que ele nos retornarar um dicionario 

o preference ou  (payment) é a resposta que queremos, no caso o o preference e o preference_responde so que navegando no nosso item response.

entao dentro desse responde nos temos um init_point que nada mais é do que o link de pagamento daquela requisição e esse é o link mais importante.

O que vamos fazer agora vai ser no nosso preference data, vamos adicionar os backs_url, para exibir uma mensagem de erro.

uma outra informação que temos que pegar alem do link de pagamento e  o id, porque é ele que diz para a gente e para o mercado pago qual é aquele pagamento


54- o que temos que fazer agora é conectar essa api do mercado pago com o nosso sitema, para a pi funcionar nos precisamos enviar os produtos que o cliente ta comprando, la no nosso finalizar pedido nos fizemos todos os tratamento para quando desse um erro ao fonalizar peedido, entao o nosso else nessa view vai ser o que ocorre quando finaliza um pedido é ali que vamos usar essa api do mercado pago.

O priemiro passo a fazer é como vamos chamar essa api para a nossa views, entao basicamente o que vamos fazer vai ser colocar tudo que fizemos no arquivo api_mercadopago e trasnforma ela em uma função  que vai receber os produtos que vai ser cobrado, que no nosso caso e os itens_pedido, e um link que vai ser o link que vai ser para onde o usuario ira ser direcionado depois de tentar fazer o pagamento.

O segundo passo vai ser is la na views.py é importar essa função que vai receber o itens_pedido e os links, que ainda vmaos pegar. para pegar os itens pedidos basta agente fazer um filter no nossos Itenspedidos e filtrar de acordo com o pedido que estamos vendo no momento, e no nosso link nos vamos por um testo vazio depois iremos ver o que vamos fazer com esse links ex: (link='').

O terceiro passo nos temos que  ir la nossa função da api do mercado pago e percorrer o nossos itens pedidos e extrair todas a informaçoes necessarias para finalizar nosso pedido.
o nosso itens_pedido que é enviado para essa função nada mais é do que uma lista com os produtos que o cliente quer finalizar.

Entao o que vamos fazer vai ser criar uma lista vazia que vamos chamar de itenns=[], agora no vamos fazer um for e percorrer cada item do itens_pedido e entao pegar as informaçoes , dps vamos adicionar essas informaçoes em um dicionario na nossa lista vazia. Agora no nosso prefenrece data o nossos "itens" vai ser a nossa lista de itens onde estamos adiconando os produtos. 

Agora podemos simular um teste real la no nosso site , la na nossa função do api mercado pago temos que dar um print do link e do id_pagamento, ai veremos se esta tudo certo, se der certo nos vamos receber o link e o id no nosso comand prompt do editor e podemos verificar, lembre de verificar com uma conta que ja tenha todos os dados preenchido etc.

Aqui no caso daria um erro naquela verificação de endereço da nossa class finalizar_pedido, caso tivessemos so pego o endereço direto pelo dados.get('endereço').

bom aqui tivemos um erro de o preço total e o preço total do pedido estava dando como diferente, ao printar esses valores podemos verificar que um estava vindo 9999.99 e outro invez de vir com . estava vindo com virgula, isso pode ter sido porque trocamos o nosso site para portugues etc.  mas e facil trocar basa pegar um deles e dar um replace e trocar a , por um ponto. entao la no na nossa class finalizar pedidos vamos fazer um replace com o preço total. alem disso o pedido.preco_total ele é um decimalfield isso faz com q ele seja diferente do float do python ,  entao para ficar igual temos que na compração de total ser diferente do pedido.preco_total no nosso flinalizar pedido o pedido.preco_total tambem ter q ser posto como flot do python.

Agora ao finalizar pedido, nos iremos receber o link e o id no nosso prompt com o total desse produtos que finalizamos.



55- Nessa estapa nos vamos testar o nosso modelo de pagamento com as contas com aquelas contas de teste que criamos no mercado pago, essa etapa envolve a part dos links do nossa função da api do mercado pago,  no caso o que acontece é que quando nos finalizamos alguma compra esses links  eles recebem informaçoes como por exemplo o id daquela compra ou o status se ele foi finalizado ou se deu algum erro etc, e sempre que quisermos verificar essa informaçoes podemos  acessar alguns sites como por exemplo o webhook que é o que vamos usar para testar. ele gera um link unico. 

O que vamos fazer e q la na nossa função do finalizar pedido na nossa variavel link vamos por esse link, entao basta copiar e por ela na variavel, esse site ele vai mostra para agente as informaçoes que e atribuida ao link qquando suspostamente finalizamos uma compra 
.

Agora o que vamos fazer vai ser abir uma guia anaonima e ir no mrcadopago e entra com nossa conta do comprador, para testar sempre temos que estar  logado na nossa conta do comprador. 

O proximo passo para testar e simular uma compra la no nosso site pra gerar aquele link, vamos pegar esse link e abrir na gia anonima onde esta a nossa conta de teste do comprador, la vmaos por os cartoes de teste que aparece na nossa conta principal do mercado pago, no nome do titular la no site do mercado pago temos os nome para ele fazer funçoes quando queremos finalizados ou q noa foi finalizado, basta por os dados do cartao e finalizar, e no site do webhook ele vai mostrar tudo assodciado ao link.

Esses dados que vem no link é  o que vamos usar por  exempo se tiver status aprovado vamos fazer tal coisa se tiver status rejeitad  vamos fazer tal coisa.

Bom entao vamos contrui esse codigos, primeiro de tudo nos precisamos do dados que veem da nossa função da api_mercado pago que no caso é o link e o id_pagamento entao essa função ela vai nos retorna isso. porque quando o usuario clicar no botao de finalizar pedido ele tem que ser redirecionado para esse link  e pra saber qual é o pagamento daquele pedido nos precisamos do id.
 
Entao la na nossa função finalizar pedido a nossa função daa api vai ser  o link_pagamento, id_pagamentom, vamos retorna para nosso link_pagamento , porem nos precisamos registrar esse pagamento em algum lugar, para isso la no nosso arquivo models.py nos vamos criar outra class que vai ser a pagamento que vai possuir o campo id_pagamento e o pedido para saber qual pedido ele é associado , lembrando que quando criamos uma class nos vamos registrar ela la no arquivo admin.py

Outra coisa que temos que lembrar é que como editamos nosso bando de dados temos q fazer o  makemigrations e o migrate.

Agora la no nosso finalizar pedido  podemos criar um pagamento com um creat cujo  o id_pagamento vai ser o id_pagamento e o pedido=pedido, e depois salvar ja q vamos editar isso.


56- agora o que vamos fazer vai ser trablhar no link, porque colocamos um link de test. A query string  é aquelas informaçoes que veem associado ao link que acabamos de testar acima ela  vem na nossa requisição, nos podemos pegar ela dando um request.get.dict iremos usar isso nas proximas etapas.

Nos tambem vamos criar uma nova função que vai ser a finalizar_pagamento nela vamos dar um redirect para a  loja so pra funcionar, ela q vai receber o pagamento verificar se foi pago ou se nao foi etc, e como criamos uma views temos que fazer um url para ela, nessa função nos vamos por  um print no request.get.dict  so para quando fizermos um teste de finalizar pedido la no  nosso site ela printar essa informaçoes que vao vir associada ao link.

A nossa api la do mercado pago, ela precisa receber o link completo, que no caso é o dominio do seu site + a aba que ela esta EX.: https://yuriarcant/finalizar_pagamento. ,  entao temos que dar um jeito de pegar esse link.

Para pegar esse link nos temos que importar o reverse, o reverse ele pega  o nome  da url, que e aquele parametro name que colcoamos em todas urls e pega  o link dela, porem o reverse ele pega o link mais nao é o link completo ele da o que chamamos de link relativo que fasicamento so o /finalizar_pagamento. 

Para que que venha o link completo nos temos que usar o reverse junto com  o request.buid_absolute_uri , que faz pegar o link absoluto que é na verdade o dominio da requisição . entao basta passar isso  junto com o reverse que ele vai pegar o link absoluto do reverse que estamos passadando,  entao vamos subistituir o link de teste por essas etapas la no nosso finalizar pedido.

Depois disso vamos testar, lembrando que pra testar um pagamento nos temos q ir numa guia anonima, entrar na  nossa conta do comprandor, nessa guia anonima nos vamos abri  outra aba e entra no nosso site e simular uma conta, se tudo der certo vamos conseguir finalizar o pedido e la no nosso terminal devem printar nossas informaçoes.

La na nossa api do mercado pago n o preference_data vamos por um auto return, so pra quando finalizar ja voltar automatico para o nosso site .

57- Agora o que vamos fazer vai ser contruir o nosso finalizar pagamento, entao primeiro vamos pegar aquelas informaçoes que estao vindo no nosso request, dps no vamos pegar os status que nos precisamos, que sao o o status e o id daquele pedido.

lemebrando que sabemos os nomes para pegar esse dados pq fizemos aquele print com as informaçoes do nossos dados que vem do link etc.

Depois disso temos que verificar o status do pagamento se ele foi aprovado ou nao, caso ele foi aprovado , primeiro nos vamos pegar esse pagamento cujo o id_pagamento = id_pagamento que pegamos acima, entao vamos mudar o aprovado dele para true  ja que por padrao vem false.

Agora temos que pegar o pedido que corresponde a esse pagamento, pq esse pagamento ele ta associado a algum pedido e depois trocar o estado de finalizado  desse pedido para true pq  por padrao ele tambem e false.

O nosso class pedido tambem tem um capo de data de finalização e como agora esse pedido ira ser fializado e so pegar e finalizar com um datetime.now() e salvar o pedido e o nosso pagamento.

entao se der  certo essa etapa nosso clientes tem que ser redirecionados para alguam pagina, para usuarios logados nos vamos retorna ele para a pagina do pedidos dele no caso os meus pedidos.

Para usuarios nao logados o que vamos fazer vai ser criar  uma nova função que vai ser o pedido_aprovado e nela  nos iremos fazer um render para  uma pagina ja que aquele usuario n pode acessar algumas , essa função vai receber tambem o id_pedido para que agora nessa função nos conseguimos pegar nosso pedido atraves do id.

 Lembrando que temos que uma urls e um html para essa função. no html dessa função nos basicamente iremos mostrar os pedidos, entao  basicamente vai ser igual a pagina dos meus pedidos so que sem  um looping for.

E por fim caso o status nao tiver como aprovado no vamos fazer apenas um else, que ira retorna para a pagina de checkout para o usuario tentar pagar novamente.

Agora é so fazer os teste e ver se esta tudo certo, lembrando que para fazer os testes nos temos que esta em uma  guia anonima, finalizar uma compra e ve se esta tudo certo.


58- Nessa etapa nos vamos tratar alguns erros, o primeiro deles é que se voltarmos la no nosso site na aba  loja nos temos aqueles caixas que apareciam o preço minimo e preço maximo elas sao preenchidas automaticamente de acordo com os valores dos nossos produtos, se repararem agora elas nao esta aparecendo, isso se da porque nos trocamos a linguaguem do nosso site para pt-br na no setings, isso faz com que o nosso numeros agora tenham , invez de ponto, por isso tivemos que fazer o replace do total la no nosso finalizar pedido, o motivo pelo qual nao esta aparecendo la no nosso site é pq o html ele tbm nao consegue ler a linguagem pt-br, ele le numeros no formato padrao que é com .(ponto) invez de ,(virgula).

Nos temos duas opçoes para isso, a primeira e que quando enviamos esse valor minimo e maximo para o html, ele ja tem que estar com o formato, e a segunda e fazer com que la no html ele ignore aquela formatação  em portugues, sendo assim para aquele template aquele formatação que fizemos la no settings para portugues  nao ira funcionar.

É a segundo opção que iremos fazer , para isso la no arquivo html que queremos que isso aconteça nos temos que fazer um loading no gereciador de tradução  que e o USE_I18N ele fica la embaixo no settingss junto onde trocamos para ptbr, para fazer esse loading nos vamos importar ele la na nossa pagina atraves do {% load l10n %} , e agora  o  valor que voce quer que aconteça essa tradução ou nao voce pode colocar ele entre uma tag , {% localize on%} para que ocorra a tradução e  "off" para que nao ocorra.

O segundo erro e que na na nosso site em loja se clicarmos em mais vendidos ele dara um erro, no nosso caso isso ta acontecendo porque temos dois produtos com a mesma quantidade de vendas o sorted ele tenta ordenar pelo primeiro se ele nao consegui ele tenta ordenar pelo segundo, sendo que o nosso item é o nosso produto em si n faz sentido ele ordenar por ali, entao temos que fazer ele ordenar apenas pelo primeiro item.
Para isso no nosso arquivo utils, na função de ordenas la no sorted nos vamos , nos vamos passar parametro chave que vai receber um afunçã lambda que devolve o primeiro item da tupla :key= lambda x :x[0] 


59- A proxima estapa vai ser configurar o nosso sitema de envio de email , entao vamos mechar naquele EMAIL_BACKEND, lembra que colocamos para aparecer esse envios de email para o nosso consolo , o que vamos fazer vai ser trocar para o smtp que e um protocolo no qual normamento os email utilizao para fazer a comunicação. 

Nos iremos usar o gmail, porque normalmente ele é o mais utilizado.

Enta a primiero prasso e trocar para o smtp la no no nosso arquivo settings no email_backend.

O segundo passo é que temos que ir no nosso email que vamos usar para isso e gerar uma senha para aplicativo, feito isso nos temos que configurar algumas coisa no ep.

Os tres primeiro sao informaçoes publicas entao é so pesquisar
EMAIL_HOST-  varia de acordo com o e-mail que estamos usando
EMAIL_PORT-   qual a porta que o e  e-mail usa
EMAIL_USE_TLS- aqui é basicamente uma criptografia de segurança que os email usam
EMAIL_HOST_USER - aqui é o seu email que voce gerou a senha
EMAIL_HOST_PASSWORD - aquela sennha q voce gerou

Agora pra testar isso nos podemos ir la no nosso site, e colocoar pra redefinir senha, para um email que voce tenha acesso para ver se chega o email.


60- Agora que nossas configuraçoes para enviar email esta pronto , oque vamos fazer vai ser enviar uma emnsagem de email quando rolar uma compra bem sucessida, aqui nos temos duas opçoes criar um novo arquivo python que tera a função para enviar todas as nossas coisas de email, ou usar a função do django que envia email e é isso qeu vamos fazer , vamos importa essa biblioteca que é o send_email.

Entao o que vamos fazer vai ser uma função que vai ser o enviar_email_compra la no nosso aquivo utils.py , esa função vai ter q receber como parametro o  pedido , primeiro  nos temos que pegar o email daquele cliente, pq precisamos enviar essa mensagem para o email daquele pedido.

Depois de pegar esse email o send_mail precisa de 4 coisas o assunto, o corpo de texto e o rementente, e depois uma lista de email para onde ele vai enviar.

A gora para testar , temos que fazer aquelas etapas em uma guia anonima para usando os cartoes de teste do mercado pago etc, entao basta entra no nossso site em uma guia anonima finalizar um pedido etc.

60- Bom agora nos vamos mecher la com nosso administrador , no nosso admin nos temos a parte de Autenticação e Autorização nessa aba somente usuarios com permissao podem usar , o que iremos fazer e fazer um grupo onde  podemos colocar admnistratores, caso esse usuario seja da nossa equipe ele pode fazer coisas dentro do nosso site que  outros usuarios normais nao podem.

Entao la nesse grupo que criamos nos vamos colocar um usurio  dentro desse grupo chamado equipe , e vamos fazer agora algumas funcionalidades que vai parecer somente pra esse usuario que esta na equipe, vamos fazr isso la no nosso navbar.

Porem antes disso nos precisamos no nosso novo context fazer uma função para verificar se possui uma equipe no nosso admin, assim podemos criar um context para que possa ser usado la no html. lembrabndo que toda vez que criamos um context nos temos que la no nosso settings adicionar ele nos nossos templates
Entao la vamos partir do principio que a equipe estaja false, em seguida  vamos verificar se a um usuario logado, depois vamos  verificar se esse usuario esta na tabela do grupo  filtrando de acordo com o nome que demos para aquele grupo se existir agora o equipe sera true, e isso vai nos retona um context com esse equipe.

agora la no arquivo do html do nosso nav bar nos podemos verificar esse  grupo equipe e caso esse equipe venha para nos como true, nos vamos libera para esse usuario que faz parte dessa equipe um novo botao que vi ser o botao de gereciar loja, que vai dar acesso a  ele a tela de gerencia loja. aqui temos que criar a url ,views e htrml para essa pagina, sendo que pra ficar mais organizado nos vamos criar uma pasta pra esse coisas que seriam de coisas internas do nosso grupo.

lembrando que na na nossa views no tempos que tbm fazer a verificarção de  if request.user.groups.filter(name="equipe").exists(): porque se nao qualque usuario logado vai conseguir entrar nessa pagna e essa pagina so pode ser logada por pessoas que fazem parte da equipe.

61- Agora o que vamos fazer vi ser as funcionalidades deesse nosso gerenciar loja, que so quem faz parte da equipe tem acesso. Nessa views basicamente nos teremos um resumo das inormaçoes das nossa loja como quantidade pedido , quantidade de produtos e pedidos etc.


Entao la na nossa views gerrernciar loja, depois de fazer a verificação do usuario esta na equipe  nos vmaos pegar as informaçoes, pegar os pedidos finalizados de acordo com o finalizado igual a true  porquee dai que vamos tirar as nossas informaçoes.

A quantidade de pedidos é basicamente o tamanho da lista de pedidios finalizados.

O meu faturamento é a soma do preço total de cada pedido finalizado, entao o que vamos fazer vai ser percorrer um for atras de um listen comprehenshion do preço total que ja possuimos , da nossa lista de pedidos finalizados.

E a quantidade de produtos é a msm coisa porem com os nosso quantidade totais , quenos da a quantidade total de itens do pedido.

Agora é  so passar essas informaçoes para um context e  usar essas informaçoes no nosso html para ser exibido nas nossa pagina de gerenciar loja.

Alem disso nessa pagina ela vai ter links que vai fazer algumas funcionalidades como exporta pedido, clientes etc. entao cada link desse vai ser associado a alguma funcionalidade que ainda vamos criar.

Pra essa funcionalidade nos vamos criar uma views que vai ser a função  exporta relatorio, ela vai receber o request e alem disso o relatorio que vai ser enviado, agora vamos criar uma urls para essa função.

Entao aqueles link que vao direcionar a inporatação dessa função vai receber  a url do exporta relatorio mais o texto que queremos passar que no caso é o parametro necessario para função rodar..

62- agora nos vamos criar as funcionalidades para das exportaçoes, o primeiro passo e fazer a verificação de qual importantação esta sendo enviada, caso seja aquela exportação temos que pegar os dados do nosso banco correspondente as exportaçoes.

Depois de pegar essas informaçoes nos teriamos que exporta essa informaçoes dos relatorios  e para isso la no nosso aquivo utils nos vamos fazer uma função que vai ser a exporta_csv que vai ser usarano nosso função exporta relatorio.

Essa função ela vai receber a informaçoes que estamos pegando de acordo com o botao que o cliente clicar. aqui nessa etapa nos colocamos uma variavel chamada resposta  com um texto vazio, e colocamos a função pra retorna essa resposta, caso clicarmos la no nosso site em algum dos link vai nos dar um erro. 

Porem fizemos isso para poder ver duas informaçoes, que o caso sao  informaçoes.model que nos retorna a class loja.models.pedido e a informaçoes.model._meta.fields que vai nos retorna uma lista com os nomes que seram as colunas da nosso arquivo csv.

def exporta_csv(informaçoes):
    print(informaçoes.model)
    print(informaçoes.model._meta.fields)
    resposta=''
    return resposta

Porque como queremos fazer um arquivo csv, nos vamos usar esse nomes para ser as colunas da nosso arquivo csv atraves do list copreheshion.

Como queremos fazer um arquivo csv no nosso arquivo utils, nova vamos importa o csv que é uma biblioteca nativa do python que cria ele para gente , o csv.writer cria o arquivo csv e cada linha que voce queira criar no seu csv voce usa csv.writerow(e passa a linha que v ai ser criada).

A nossa resposta que vai retornar para na nossaunção exporta csv, ele tem quer ser uma resposta htpp para isso nos vamos importa do django o httpresponse, pq ai conseguiriamos criar uma resposta htpp para o cliente do tipo download, entao nossa varavel resposta vai ser um http response , onde o contet type (que é o tipo de conteudo que tem nele) dele vai ser um text/csv que informa que vai ser um arquivo csv.

entao o arquivo dcv vai receber como parametro essa resposta que criamos, e o delimitador dele tem q ser ; , porque as informaçoes que ele vai escrever no arquivo é separado por ;.

Mas se observamos nao temos nada dizendo que nossa resposta temos que fazer o download dela  temos que avisar isso para o navegador, pra isso passaremos o parametro Content-Disposition, alem disso temos que passar o valor "attachment"que mostra que isso é um anexo que no caso que é um arquivo donwload e o nome do arquivo que e o filename  separados po um ;.


A nosa informaçoes ela é um query set entao ela contem varias coisas dentro dele, oque vamos fazer agora vai ser percorrer o informaçoes.value_list() porque o value list ele pega todos os valores dentro da nossas informaçoes e tranformando ela em uma lista e com isso nos podemos escrever nossa linhas no nosso arquivo csv.


O que vamos fazer agora é la na nossa viewns ver produto, nos vamos pegar itens similares a algum produto, porque quando formos adaptar  o html e css desse site vai ter essa opção, entao pra isso nos vamos pegar la no nosso views de ver produtos, nos vamos filtrar os produtos cujo o id da categoria seja igual ao id da categoria daquele produtos que estamos vendo, e cujo o id do tipo, seja igual ao id do tipo daquele produto

IMPORTANTE:

ATÉ AQUI NOS TEMOS A BASE DO NOSSO SITE E TODAS AS FUNCIONALIDADES DO NOSSO SITE , AGORA O QUE VAMOS FAZER VAI SER O VISUAL DO NOSSO SITE APARTIR DE HTML E CSS, EU VOU UTILIZAR OS ARQUIVOS JA PRONTO QUE O CURSO HASTGTREINAMENTOS DISPONIBILIZOU, MAS CASO FUTURAMENTE TENHA INTERESSEO CURSO HTML E CSS IMPRESSIONADOR MOSTRA NA PRATICA COMO FAZER ESSAS PAGINAS DO ZERO.

1-A primeira coisa que vamos fazer para essa adpção é pegar os arquivos disponibilizados (frontend) copiar e colocar cada um em suas respectivas paginas , as imagens no lugar onde fica as imaens do nosso site , os aquivos css na nossa pasta css do site, e o java script na nossa pasta js do nosso site. 

uma outra coisa que temos que fazer é que no nosso arquivo bse.html nos temos que ver se o links entao corretos do csss e  javascrip. o nosso arquivo css ja esta tudo  ok, porem se olharmos agora nos temos diversos arquivos java script, antes nos nso possuiamos o arquivo main.js que fazia a função de ordenar nosso prosutos de acordo com cada link que clicamos(mais vendidos, menor preço , maior preço). vamos fazer um script no nosso arquivo base para cada  arquivo js.

2- A gora o que vamos fazer vai ser a adaptaçao da home do nosso site, entao vamos abri o arquivo home.html que foi disponibilizado e vamos ver o que precisamo adptar, vamos começar elo head da pagina e vamos comprar o que ja tem nos vamos manter igual no nosso e as outras coisas nos vamos coiar e cololar no nosso arquivo base.html do projeto. nos usamos um link do font-awesome mais agora nao vamos mais usar ele, nos vamos apagar , no caso vou deixar comentando

Agora a outra coisa que vamos fazer vai ser ir na home.html que foi disponibilizada e ir no footer que nada mais e que o nosso rodape, como nos nao temos nenhum rodape nos vamos copiar o footer. nos podeiamos colar esse footer direto no nosso arquivo base , mas oque vamos fazer vai criar um arquivo novo chamado rodape.html e puxar ele para o nosso arquivo base atraves do include.


A proxima alteração no visial do nosso site vai ser a barra de navegação , que no nosso caso agora esta toda desconfigurada, pq estamos mechendo nessa parte visual , o que vamos fazer que la no arquivo home que pegamos ja pronto vamo copiar o header dess a pagina e colcar abaixo do nosso nav do nosso arquivo navbar e ir fazendo as adtaçoes nessessarias para rodar tudo conforme o nosso site.