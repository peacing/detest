FROM pytorch/pytorch

RUN apt-get update && apt-get install -y git

RUN git clone https://e63ebf4b45edf6fd75e323de4f4733d5272d939a@github.com/peacing/detest.git

WORKDIR /usr/local/detest

ENTRYPOINT [ "python", "src.test.py" ]