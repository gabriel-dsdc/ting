from typing import Dict, List
from ting_file_management.queue import Queue


def exists_word(
    word: str, instance: Queue
) -> List[Dict[str, str | List[Dict[str, int]]]]:
    result = []
    for index in range(len(instance)):
        occurrences = []
        process = instance.search(index)
        for n, row in enumerate(process["linhas_do_arquivo"]):
            if word.lower() in row.lower():
                occurrences.append({"linha": n + 1})

        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": process["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return result


def search_by_word(
    word: str, instance: Queue
) -> List[Dict[str, str | List[Dict[str, int | str]]]]:
    result = []
    for index in range(len(instance)):
        occurrences = []
        process = instance.search(index)
        for n, row in enumerate(process["linhas_do_arquivo"]):
            if word.lower() in row.lower():
                occurrences.append({"linha": n + 1, "conteudo": row})

        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": process["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return result
