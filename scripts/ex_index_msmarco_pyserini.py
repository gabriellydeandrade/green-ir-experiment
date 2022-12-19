import os

from codecarbon import track_emissions


@track_emissions(offline=False, country_iso_code="BRA", project_name="BM25 Indexing (pyserini)")
def run():
    collection_dir = "collections/msmarco-passage-unicoil-b8"
    index_path = "collections"
    os.system(f'python3 -m pyserini.index.lucene -collection JsonCollection ' +
              f'-generator DefaultLuceneDocumentGenerator -threads 1 ' +
              f'-input {collection_dir} -index {index_path}')


if __name__ == '__main__':
    run()
