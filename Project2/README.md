# Onboarding Project 2

Goal: Create a Chatbot that answers questions given to the Transformer paper 

Example)  
transformer = `{paper}`  

Q: What is the transformer architecture?  
A: The transformer is made of an encoder and decoder each with a self-attention submodule and a feedforward network..

Tip
1. 온보딩 프로젝트1에서 논문을 summarize 한 것을 prompt에 넣고 Q랑 A를 뒤에 추가할 수도 있습니다.
2. 하지만 질문이 어려워서 summarize된 내용에 없을 때 못 찾을 수 있어 논문을 새로운 방식대로 스캔해서 질문에 답할 수 있는 부분을 찾고 물어볼 수도 있습니다.
3. OpenAI의 embedding API도 활용해볼 수도 있을 것 같습니다!
https://beta.openai.com/docs/guides/embedding