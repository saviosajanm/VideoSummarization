Dataset downloaded here : https://drive.google.com/file/d/1Bf0beMN_ieiM3JpprghaoOwQe9QJIyAN/view

Move the dataset videos into the "testVideos" folder and run the videos2frames bash file (provided bash and ffmpeg are installed prior to this)

# Commands:

# to split the dataset (vsumm)
python create_split.py -d datasets/eccv16_dataset_summe_google_pool5.h5 --save-dir datasets --save-name summe_splits  --num-splits 5

# to train the model
python main.py -d datasets/eccv16_dataset_summe_google_pool5.h5 -s datasets/summe_splits.json -m summe --gpu 0 --save-dir log/summe-split0 --split-id 0 --verbose --method <rank or knapsack> --rnn-cell <rnn, lstm or gru>

# to save the model
python main.py -d datasets/eccv16_dataset_summe_google_pool5.h5 -s datasets/summe_splits.json -m summe --gpu 0 --save-dir log/summe-split0 --split-id 0 --evaluate --resume C:/Users/<User>/VideoSummarization/log/summe-split0/model_epoch60.pth.tar --verbose --save-results --method <rank or knapsack> --rnn-cell <rnn, lstm or gru>

# graphs for analysis
### python parse_log.py -p C:/Users/<User>/VideoSummarization/log/summe-split0/log_train.txt
### python visualize_results.py -p C:/Users/<User>/VideoSummarization/log/summe-split0/result.h5
### python parse_json.py -p C:/Users/<User>/VideoSummarization/log/rewards.json -i 0

# to create a summary of a selected video using the previously trained model:
python summary2video.py -p C:/Users/<User>/VideoSummarization/log/summe-split0/result.h5 -d C:/Users/<User>/VideoSummarization/testVideos/frames/<Video> -i 0 --fps 30 --save-dir log --save-name <Video Name>.mp4