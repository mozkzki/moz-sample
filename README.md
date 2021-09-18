# moz-sample

This is a Python sample package (library). It is supposed to be used from the program.

## Usage

Install

```sh
pip install moz-sample # install from PyPi (doesn't work)
# or
pip install moz-sample --extra-index-url https://test.pypi.org/simple # install from TestPyPi
# or
pip install git+https://github.com/mozkzki/moz-sample
```

Coding

```python
>>> from moz_sample.sample.module1 import Module1
>>> m = Module1()
>>> m.method()
module1's method called.
module2's method called.
```

## Develop

### Environment

| Tool | Tool Name |
|--|--|
| package manager | [Poetry](https://python-poetry.org/) |
| unit test | [pytest](https://docs.pytest.org/en/6.2.x/) |
| lint | [flake8](https://flake8.pycqa.org/en/latest/) |
| formatter | [black](https://github.com/psf/black) |
| type checker | [mypy](https://mypy.readthedocs.io/en/stable/) |

### Prepare

```sh
poetry install
poetry shell
```

This project is based on [template-python-simple](https://github.com/mozkzki/template-python-simple). See for details.

#### caution

`poetry install` command is install the project package (moz-sample) into local. See [here](https://cocoatomo.github.io/poetry-ja/cli/#install) for details. This install is **Editable** mode (same `pip install -e .`).

```txt
$ poetry install
Installing dependencies from lock file

No dependencies to install or update

  - Installing <your-package-name> (x.x.x)
```

### Run (Example)

```sh
python ./example/example.py
# or
make start
```

### Unit Test

test all.

```sh
pytest
pytest -v # verbose
pytest -s # show standard output (same --capture=no)
pytest -ra # show summary (exclude passed test)
pytest -rA # show summary (include passed test)
```

with filter.

```sh
pytest -k app
pytest -k test_app.py
pytest -k my
```

specified marker.

```sh
pytest -m 'slow'
pytest -m 'not slow'
```

make coverage report.

```sh
pytest -v --capture=no --cov-config .coveragerc --cov=main --cov-report=xml --cov-report=term-missing .
# or
make ut
```

### Lint

```sh
flake8 --max-line-length=100 --ignore=E203,W503 ./main
# or
make lint
```

### Packaging

- Pip can be installed from `pyproject.toml` in version 19.02.
- No need for `setup.py`, `setup.cfg`, `MANIFEST.in`.

Build package

```sh
poetry build
# created *.tar.gz and *.whl file under "dist/" directory.
# (setup.py is automatically generated according to pyproject.toml) 
```

Publish to TestPyPi

```sh
poetry publish -r testpypi
```

Build and publish

```sh
poetry publish -r testpypi --build
```

Install from TestPyPi (for test)

```sh
pip install moz-sample --extra-index-url https://test.pypi.org/simple
```

## Reference

- [コマンド - Poetry documentation (ver. 1.1.6 日本語訳)](https://cocoatomo.github.io/poetry-ja/cli/#install)
- [pyproject.toml ファイル - Poetry documentation (ver. 1.1.6 日本語訳)](https://cocoatomo.github.io/poetry-ja/pyproject/)
- [PyPI · The Python Package Index](https://pypi.org/)
- [TestPyPI · The Python Package Index](https://test.pypi.org/)
- [Classifiers · PyPI](https://pypi.org/classifiers/)
- [Poetryを使ったPythonパッケージ開発からPyPI公開まで - PYTHONIC BOOM BOOM HEAD](https://kk6.hateblo.jp/entry/2018/12/20/124151#f-124e5f32)
- [poetry使ってPythonパッケージをPyPIに公開しよう](https://jimaru.blog/programming/python/poetry/)
- [pip が 19.02 で pyproject.toml から pip install できるようになった - おろログ](https://orolog.hatenablog.jp/entry/2019/03/24/223531)
- [もうsetup.pyは要らない - イワモト・カイドウ](https://scrapbox.io/odiak/%E3%82%82%E3%81%86setup.py%E3%81%AF%E8%A6%81%E3%82%89%E3%81%AA%E3%81%84)
