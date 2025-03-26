var url = new URL(document.URL);
var itens = document.getElementsByClassName("item-ordenar");

for (i = 0; i < itens.length;  i++){
    url.searchParams.set("ordem", itens[i].value);
    itens[i].value = url.href;
}

//  aqui antes no lugar do value antes era o href porque quando construimos nossa lista de ordenar fizemos atravez de link, porem agora com os arquivos feitos apartir do html contruido , nos tamos usando as tags option que usaremos o valor(value) dela para puxar pra ca.