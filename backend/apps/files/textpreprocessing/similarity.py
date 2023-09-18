import re

import torch

from .sentence_transformers import SentenceTransformer, models, util

torch.cuda.set_device(0)


def model():
    embedding_model = models.Transformer(
        model_name_or_path="KDHyun08/TAACO_STS",
        max_seq_length=256,
        do_lower_case=True,
    )

    pooling_model = models.Pooling(
        embedding_model.get_word_embedding_dimension(),
        pooling_mode_mean_tokens=True,
        pooling_mode_cls_token=False,
        pooling_mode_max_tokens=False,
    )
    model = SentenceTransformer(modules=[embedding_model, pooling_model])

    return model


def similar(text, model):
    docs = re.split('\. |\? |\!', text)

    document_embeddings = model.encode(docs)

    query = docs[0]
    query_embedding = model.encode(query)

    top_k = len(docs)

    # 입력 문장 - 문장 후보군 간 코사인 유사도 계산 후,
    cos_scores = util.pytorch_cos_sim(query_embedding, document_embeddings)[0]

    # 코사인 유사도 순으로 `top_k` 개 문장 추출
    top_results = torch.topk(cos_scores, k=top_k)

    # print(f"입력 문장: {query}")
    # print(f"\n<입력 문장과 유사한 {top_k} 개의 문장>\n")
    average = 0.0
    for i, (score, idx) in enumerate(zip(top_results[0], top_results[1])):
        average += score
    average /= len(docs)
    return average
