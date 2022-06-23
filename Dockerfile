FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY . .
RUN conda env create -f environment.yml
#RUN --mount=type=cache,target=/opt/conda/pkgs conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "chatbot", "/bin/bash", "-c"]

# Demonstrate the environment is activated:

#RUN python -m nltk.downloader wordnet
#RUN python -m nltk.downloader punkt

RUN python -m nltk.downloader omw-1.4

RUN python chatbot.py
#RUN python -m nltk.downloader omw-1.4
# The code to run when container is started:
# COPY run.py .
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "chatbot", "python", "app.py"]
