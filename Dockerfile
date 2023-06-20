# vim:set ft=dockerfile:

FROM python:3.11

COPY tests/assets /bf
COPY src /build/src
COPY README.rst /build/README.rst
COPY pyproject.toml /build/pyproject.toml


RUN cd /build && \
    python -m pip install --verbose . && \
    rm -rf /build

ENTRYPOINT ["python", "-m", "fuckery", "-i", "/bf/hello_world.bf"]


