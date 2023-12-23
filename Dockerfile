# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

FROM jupyter/datascience-notebook:latest
# FROM jupyter/all-spark-notebook:lab-3.1.12

# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

# install deps
RUN pip install -r requirements.txt
