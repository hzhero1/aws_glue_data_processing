import hanlp
recognizer_cn = hanlp.load(hanlp.pretrained.ner.MSRA_NER_BERT_BASE_ZH)
recognizer_cn(list())