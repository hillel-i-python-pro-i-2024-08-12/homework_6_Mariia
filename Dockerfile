FROM python:3.12

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/home/appuser
ARG USER=appuser

WORKDIR ${WORKDIR}

RUN useradd --system --create-home --shell /bin/bash ${USER}

RUN apt update && apt upgrade --yes

COPY --chown=${USER}:${USER} requirements.txt ${WORKDIR}/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --requirement ${WORKDIR}/requirements.txt

COPY --chown=${USER}:${USER} . .

USER ${USER}

ENTRYPOINT ["python", "main.py"]
