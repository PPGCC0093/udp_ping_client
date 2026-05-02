import socket
import time

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)

sent_packets = 10
received_packets = 0
rtts = []

for i in range(1, sent_packets + 1):
    message = f"ping {i}"
    start_time = time.time()

    try:
        client_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))

        response, server_address = client_socket.recvfrom(1024)

        end_time = time.time()
        rtt = (end_time - start_time) * 1000

        received_packets += 1
        rtts.append(rtt)

        print(f"Resposta {i}: {response.decode()} | RTT = {rtt:.2f} ms")

    except socket.timeout:
        print(f"Ping {i}: tempo esgotado. Pacote perdido.")

client_socket.close()

lost_packets = sent_packets - received_packets
loss_rate = (lost_packets / sent_packets) * 100

print("\n===== Estatísticas =====")
print(f"Pacotes enviados: {sent_packets}")
print(f"Pacotes recebidos: {received_packets}")
print(f"Pacotes perdidos: {lost_packets}")
print(f"Taxa de perda: {loss_rate:.2f}%")

if rtts:
    avg_rtt = sum(rtts) / len(rtts)
    print(f"RTT médio: {avg_rtt:.2f} ms")
else:
    print("RTT médio: não calculado, pois nenhum pacote foi recebido.")