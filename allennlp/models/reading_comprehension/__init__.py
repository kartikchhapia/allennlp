"""
Reading comprehension is loosely defined as follows: given a question and a passage of text that
contains the answer, answer the question.

These submodules contain models for things that are predominantly focused on reading comprehension.
"""

from allennlp.models.reading_comprehension.bidaf import BidirectionalAttentionFlow
from allennlp.models.reading_comprehension.bidaf_ensemble import BidafEnsemble
from allennlp.models.reading_comprehension.dialog_qa import DialogQA
from allennlp.models.reading_comprehension.dialog_qa_question_dialog_bi_attention import DialogQAQuesDiaBiAttention
from allennlp.models.reading_comprehension.dialog_qa_question_dialog_vanilla_attention import DialogQAQuesDiaVanillaAttention
