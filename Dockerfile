FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt /app/
# First upgrade pip resolve CVE-2023-5752
# and install requirements
RUN python3 -m pip install --upgrade pip>=23.3.2 && \
    pip3 install -r /app/requirements.txt
COPY . .
RUN chmod +x entrypoint.sh

EXPOSE 5555

ENTRYPOINT ["/app/entrypoint.sh"]
