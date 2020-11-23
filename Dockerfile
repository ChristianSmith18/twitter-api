    FROM continuumio/miniconda3
    
    WORKDIR /src
    RUN conda create -n env python=3.6
    COPY requirements.txt requirements.txt
    RUN pip install -r requirements.txt
    RUN conda install -c conda-forge spacy
    RUN python -m spacy download es_core_news_sm
    COPY . .
    COPY boot.sh ./
    RUN chmod +x boot.sh
    EXPOSE 5000
    ENTRYPOINT ["./boot.sh"]