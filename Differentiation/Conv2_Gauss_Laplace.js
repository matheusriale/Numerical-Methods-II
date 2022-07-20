//filtros e variáveis
let img;
let GaussianK = [[1/16,2/16,1/16],
                 [2/16,4/16,2/16],
                 [1/16,2/16,1/16]]

let Laplace = [[1/6,4/6,1/6],[4/6,-20/6,4/6],[1/6,4/6,1/6]]

//funcao de convolução
function conv(filtro,indX,indY){

  var beginX = indX === 0 ? 0 : indX -1 
  var beginY = indY === 0 ? 0 : indY -1
  
  var j = 0;
  var i = 0;
  var soma = 0;
  for (let x = beginX   ; x < beginX + 3; x++){
    j = 0;
    for(let y = beginY; y < beginY + 3;y++){
      var pix = get(x,y) 
      soma = soma + pix[0]*filtro[i][j]  
      j = j + 1
    }
    i = i + 1
  }
  if (soma > 255){
    return 255
  }
  else{
    if (soma < 0 ){
      return 0
    }
    else
    {
      return soma
    }
  }
}  

//Pré carrega a imagem na memória
function preload(){
  img = loadImage('malenia.jpg');
}

function setup() {
  createCanvas(img.width+2, img.height+2);// (WIDTH, HEIGHT) parametros serão usados posteriormente
  noLoop()
}

function draw() {
  background(0)//define background para 'imagem'
  image(img,1,1)
  var mpix = []
  var A = []
  var B = []
  loadPixels()
  
  
  //------------------------------------------------------------------------------//
  //Aplicar o filtro gaussiano
  
  for(var i = 0; i < img.width;i++){
    var linha = []
    for(var j = 0; j< img.height; j++){
      linha.push(conv(GaussianK,i,j))
    }
    mpix.push(linha)
  }
  
  
  for (var i = 0; i< mpix.length ; i++){
    for (var j = 0; j< mpix[i].length ; j++){
      set(i,j,mpix[i][j])
    }
  }
   updatePixels() 
  
  //------------------------------------------------------------------------------//
  //Aplicar filtro de laplace
  A = []
  for(var i = 0; i < img.width;i++){
    var linha = []
    for(var j = 0; j< img.height; j++){
      linha.push(conv(Laplace,i,j))
    }
    A.push(linha)
  }
  
  
  for (var i = 0; i< A.length ; i++){
    for (var j = 0; j< A[i].length ; j++){
      set(i,j,A[i][j])
    }
  }
   updatePixels() 
  
  B = []
  let threshold = 10
  for(var i = 0; i < img.width;i++){
    var linha = []
    for(var j = 0; j< img.height; j++){
      if (A[i][j] < threshold || A[i][j] == threshold){
        linha.push(0)  
      }
      else
      {
        linha.push(255) 
      }
      
    }
    B.push(linha)
  }
  
  
  for (var i = 0; i< B.length ; i++){
    for (var j = 0; j< B[i].length ; j++){
      set(i,j,B[i][j])
    }
  }
   updatePixels() 
  
  
}
