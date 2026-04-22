Diagnóstico Inicial de Qualidade – Plataforma Local Eats
🔹 1. Respostas à Direção da Associação
Antes de detalhar os problemas, apresentamos o diagnóstico executivo respondendo aos questionamentos da direção:

O sistema possui qualidade adequada para continuar em operação?
Não em seu estado atual. O sistema foi lançado como um MVP (Produto Mínimo Viável) apressado para atender ao prazo do evento gastronômico. Ele carece de estabilidade básica. Continuar operando sem corrigir as falhas críticas agravará a crise de reputação junto aos comerciantes e causará perda irreversível de usuários (churn).

Quais aspectos da qualidade do produto estão comprometidos?
Com base na ISO/IEC 25010, os pilares mais comprometidos são: Adequação Funcional (o sistema não faz o básico corretamente, como buscas e salvamento de dados), Eficiência de Desempenho (não suporta carga/pico), Usabilidade (telas confusas) e Portabilidade (falhas em dispositivos específicos).

Quais problemas devem ser priorizados?

Alta Prioridade (Críticos): Resultados de busca incorretos e avaliações desaparecendo. (Impacto direto no Core Business e perda de dados gera quebra total de confiança).

Média Prioridade: Lentidão em horários de pico e falhas em smartphones específicos. (Impedem o uso e a conversão de vendas/acessos).

Baixa Prioridade (Melhoria Contínua): Telas confusas e inconsistência visual web/mobile. (Devem ser tratadas via redesign de UX após a estabilização técnica).

🔹 2. Matriz de Problemas e Atributos de Qualidade (ISO/IEC 25010)
Abaixo, relacionamos os relatos dos usuários com os atributos técnicos de qualidade de software, justificando o impacto técnico e de negócio.

https://docs.google.com/spreadsheets/d/1wvmMeVkF_zRs3XI8hTgJS_xYsiEvU-pd6EG-BrAXLrs/edit?usp=sharing

(Sou muito ruim com tabelas)


🔹 3. Conclusão e Próximos Passos
O diagnóstico revela que o Local Eats sofre de "Dívida Técnica" decorrente de um lançamento apressado.
O foco de qualidade agora não deve ser criar testes para adicionar novas funcionalidades,
mas sim implementar imediatamente Testes de Regressão e Testes de Carga/Estresse para estancar a perda de dados e garantir que o sistema não caia nos horários de maior movimento do festival gastronômico.
