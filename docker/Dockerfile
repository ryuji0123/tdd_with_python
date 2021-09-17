FROM selenium/standalone-chrome:4.0.0-rc-2-prerelease-20210915

# apt-get
USER root
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq && \
    apt-get install -y \
      curl libopencv-dev lsof git python3-pip sudo tmux tree vim wget zsh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/apk/*

# python
ENV WORK_PATH /workspace
WORKDIR $WORK_PATH
ENV PYTHONPATH "/workspace:${PYTHONPATH}"
ENV PIP_OPTIONS "--no-cache-dir --progress-bar off"
COPY docker/requirements.txt $WORK_PATH/docker/
RUN pip install ${PIP_OPTIONS} -r $WORK_PATH/docker/requirements.txt && \
    pip install ${PIP_OPTIONS} -U setuptools

# settings
ENV SETTING_PATH /duser/settings
COPY docker/settings $SETTING_PATH
WORKDIR $SETTING_PATH
RUN $SETTING_PATH/setup.sh
SHELL ["/bin/zsh", "-c"]

WORKDIR $WORK_PATH
