# api_test


### Setting the environment

Use python version 3.6+

```python
python3 -m pip install -r requirements.txt
```

or

```python
pip install -r requirements.txt
```


### Start tests

**Start all tests**

```python
python3 -m pytest -v ./tests_api
```


**Start minor tests**
```python
python3 -m pytest -m Minor -v ./tests_api
```


**Start medium tests**
```python
python3 -m pytest -m Medium -v ./tests_api
```


**Start critical tests**
```python
python3 -m pytest -m Critical -v ./tests_api
```
