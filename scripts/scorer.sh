ARRAY=(quac_question_appended_with_attention_from_dialog_1 \
       quac_dialog_context_first_ans_bi_attention \
       quac_dialog_context_first_ans_vanilla_attention \
       quac_dialog_context_bi_attention \
       quac_dialog_context_vanilla_attention \
       quac_dialog_full_bi_attention \
       quac_dialog_full_vanilla_attention)

for i in ${ARRAY[@]}; do
    echo "Doing for ${i}"
    python scorer.py --val_file val.json --model_output ../${i}/predictions.json

done





