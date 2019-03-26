# vim:set ft=dockerfile:

FROM python:3.7

COPY tests/assets/hello_world.bf /bf/hello_world.bf
COPY src /build/src
COPY setup.py /build/setup.py
COPY README.rst /build/README.rst
COPY CHANGELOG.rst /build/CHANGELOG.rst

RUN cd /build && \
    python setup.py build bdist_wheel && \
    python -m pip install dist/*.whl && \
    rm -rf /build

ENTRYPOINT ["python", "-m", "fuckery", "-i", "/bf/hello_world.bf"]


