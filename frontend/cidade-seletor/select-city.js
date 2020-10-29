//Menu de seleção com apenas cidades da Paraíba
//Primeiro definimos uma função por padrão get pois vai pegar informações
function getCities(){
    //É definida uma contante que será um mapa com as cidades
    const citySelect = document.querySelector("[name=city]")
    //Vamos accesar uma API de localidades, a servicodados, que tem dados sobre todas
    //as localidades no Brasil e é possível obter esses dados de várias formas
    //Nesse caso vamos pegar o link específico com os dados sobre o estado Paraíba, se
    //quisessemos pegar de outra localidade bastaria alterar a sigla para a do estado referente
    const url = `https://servicodados.ibge.gov.br/api/v1/localidades/estados/PB/municipios`
    //Aqui estamos adicionando uma "opção" que será exibida no menu de opções
    //com a intrução para o usuário, no caso, "Selecione a cidade"
    //ATENÇÃO: ESSA OPÇÃO NÃO SERÁ EXIBIDA ENQUANTO O USUÁRIO NÃO CLICAR NO MENU DE OPÇÕES
    //SE DESEJAR EXIBIR ESSE TEXTO DEVE IR NO HTML DA PÁGINA TAG <option> E ESCREVÊ-LO!
    //citySelect.innerHTML = "<option value>Selecione a cidade</option>"
    //A API fetch provê ao navegador uma interface para a execução de requisições HTTP
    //através de Promises. Promises é uma classe que permite a construção de funções de
    //processamento assíncrono representando um valor que poderá estar disponível no futuro
    //Leia sobre em: https://www.devmedia.com.br/javascript-fetch/41206
    fetch(url)
        //Vai retornar a resposta da requisição,no caso GET, em formato JSON
        .then(res => res.json())
        //Vai pegar as cidades como se fossem itens de uma lista/mapa
        .then(cities => {
            //Vai percorrer por cada cidade na lista/mapa
            for(city of cities){
            //vai adicionar ao nosso mapa de cidades cada uma das cidades e exibi-las como opções
            citySelect.innerHTML = citySelect.innerHTML + `<option value="${city.nome}">${city.nome}</option>`
            }
        //Ativa o menu de opções ao clicar nele, por padrão ele fica desativado
        citySelect.disabled = false
    })
}
//Executa a função
getCities()
