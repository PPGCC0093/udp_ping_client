FROM python:3.13-slim

WORKDIR /app

COPY udp_ping_clien.py .

CMD ["python", "udp_ping_clien.py"]
