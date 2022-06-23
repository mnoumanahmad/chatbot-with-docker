FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY . .
RUN conda env create -f environment.yml
#RUN --mount=type=cache,target=/opt/conda/pkgs conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "chatbot", "/bin/bash", "-c"]


#RUN python -m nltk.downloader wordnet
#RUN python -m nltk.downloader punkt

RUN python -m nltk.downloader omw-1.4

RUN python chatbot.py

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "chatbot", "python", "app.py"]
