import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file in str(instance._data):
        return None
    txt_dic = txt_importer(path_file)

    data_process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_dic),
        "linhas_do_arquivo": txt_dic
    }

    instance.enqueue(data_process)
    return sys.stdout.write(str(data_process))


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        file = instance.dequeue()['nome_do_arquivo']
        print(f"Arquivo {file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        arquivo = instance.search(position)
        print(arquivo, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
