print("Bem-vindo ao Suporte de Redes")

router_on = False
apipa_ip = False
ping_ip_externo = False
ping_dns = False
is_wifi = False
weak_signal = False

diagnostico = ""
acao = ""

resposta = input("1. O roteador está ligado na tomada e com as luzes acesas? Sim ou Não? ")
if resposta.lower() == 's' or resposta.lower() == 'sim':
    router_on = True

if router_on == True:
    resposta = input("2. Ao checar seu IP (ipconfig), ele começa com 169.254.x.x? Sim ou Não? ")
    if resposta.lower() == 's' or resposta.lower() == 'sim':
        apipa_ip = True
        
    if apipa_ip == False:
        resposta = input("3. Você consegue pingar um IP externo com sucesso? (ex: ping 8.8.8.8) Sim ou Não? ")
        if resposta.lower() == 's' or resposta.lower() == 'sim':
            ping_ip_externo = True
            
        if ping_ip_externo == True:
            resposta = input("4. Você consegue pingar um site em texto com sucesso? (ex: ping google.com) Sim ou Não? ")
            if resposta.lower() == 's' or resposta.lower() == 'sim':
                ping_dns = True
                
        resposta = input("5. Você está conectado via Wi-Fi? Sim ou Não? ")
        if resposta.lower() == 's' or resposta.lower() == 'sim':
            is_wifi = True
            
            resposta = input("6. O sinal do Wi-Fi está fraco (menos de 3 barras)? Sim ou Não? ")
            if resposta.lower() == 's' or resposta.lower() == 'sim':
                weak_signal = True

print("\n--- Analisando Rede (Motor de Inferência) ---\n")

if router_on == False:
    diagnostico = "Problema Físico / Alimentação."
    acao = "Verifique a tomada, fonte de alimentação do roteador ou botão de Power. Se não ligar, o roteador pode estar queimado."

elif apipa_ip == True:
    diagnostico = "Falha no servidor DHCP (IP 169.254.x.x)."
    acao = "Seu computador não está recebendo IP do roteador. Verifique o cabo de rede, reinicie o roteador ou defina um IP manual."

elif ping_ip_externo == False:
    diagnostico = "Falta de comunicação com a Internet (Problema de Provedor/WAN)."
    acao = "A rede local funciona, mas não há saída para a internet. Reinicie o modem da operadora e verifique se a luz 'Internet' ou 'PON' está acesa/piscando."

elif ping_dns == False:
    diagnostico = "Falha de DNS."
    acao = "A conexão existe, mas os nomes de sites não estão sendo traduzidos. Mude o DNS da sua placa de rede para 8.8.8.8 (Google) ou 1.1.1.1 (Cloudflare) e digite 'ipconfig /flushdns' no CMD."

elif is_wifi == True and weak_signal == True:
    diagnostico = "Interferência ou Baixo Alcance do Wi-Fi."
    acao = "Aproxime-se do roteador ou acesse as configurações dele para alterar o canal de transmissão (evite os canais padrão para fugir de interferências de vizinhos)."

else:
    diagnostico = "Rede aparentemente normal."
    acao = "Os testes básicos passaram. Se o problema persiste em um site específico, o servidor daquele site pode estar fora do ar."

print("=== LAUDO DO PROBLEMA ===")
print("CAUSA PROVÁVEL: " + diagnostico)
print("SOLUÇÃO RECOMENDADA: " + acao)
print("=====================================")