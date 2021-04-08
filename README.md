# DeteccaoFacialHC - HaarCascade

Resumo

Hoje, mesmo que a IA seja um topico relativamente recente (levando em conta o avanco exponencial do setor de tecnologia no mundo nas ultimas 5 decadas) e apenas "cortejada" como topico futurista em filmes como Matrix a alguns anos, ela ja esta presente e ao nosso redor. Independende do nicho de atuacao esta ajudando organizacoes a prestarem melhores servicos, um deles, o que vou abordar aqui, a Visao Computacional um dos bracos da inteligencia artificial.

A Visao Computacional (CV) esta presente em cameras de seguranca, identificadores de produtos, servico policial e etc, e ja constitui parte importante (e talvez essencial) do funcionamento de alguns sistemas do nosso dia-a-dia. Este simples projeto, na qual fiz o reconhecimento facial atraves de uma webcam comum.

Neste projeto de referencia pense que utilizamos varias imagens de faces e outras tantas que nao sao faces (caes, gatos, lagos, e etc), percebe-se que as imagens com faces (que vamos comecar a chamar de imagens positivas) obedecem em sua maioria um padrao, elas possuem olhos, boca, nariz e orelhas, enquanto as outras (chamadas imagens negativas) nao possuem esse padrao. Atraves da identificacao desses padroes utilizando algoritmo HaarCascades da biblioteca OpenCV, podemos fazer um algoritmo novo treinado a verificar a existencia ou nao dos mesmos padroes das imagens positivas (olhos, boca...) e posteriormente, identifica-las em outras fontes.
