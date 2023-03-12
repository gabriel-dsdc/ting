import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file: str, instance: Queue):
    for index in range(len(instance)):
        if path_file == instance.search(index)["nome_do_arquivo"]:
            return

    text_list = txt_importer(path_file)
    if text_list:
        processed_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(text_list),
            "linhas_do_arquivo": text_list
        }
        instance.enqueue(processed_data)
        print(processed_data, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
