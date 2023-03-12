import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    inputs = [
    {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [...]
    },
    {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": [...]
    },
    {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": [...]
    },
    ]
    instance = PriorityQueue()
    for input in inputs:
        instance.enqueue(input)
    assert len(instance) > 0
    assert instance.search(0)["qtd_linhas"] == 4

    metadata = instance.dequeue()
    assert type(metadata) == dict
    assert metadata["qtd_linhas"] == 4
    assert instance.dequeue()["qtd_linhas"] == 2
    assert instance.dequeue()["qtd_linhas"] == 6

    with pytest.raises(IndexError):
        instance.search(42)
