FROM ubuntu:18.04

#Install python & libraries
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip && \
    pip3 install requests argparse
WORKDIR /app
COPY execute_get_api.py /app/execute_get_api.py


ENTRYPOINT ["python3", "/app/execute_get_api.py"]
CMD ["default_arg"]

