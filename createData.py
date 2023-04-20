import h5py
h5_file_name = 'videoModel'
f = h5py.File(h5_file_name, 'w')

# video_names is a list of strings containing the 
# name of a video, e.g. 'video_1', 'video_2'
for name in video_names:
    f.create_dataset(name + '/features', data=data_of_name)
    f.create_dataset(name + '/gtscore', data=data_of_name)
    f.create_dataset(name + '/user_summary', data=data_of_name)
    f.create_dataset(name + '/change_points', data=data_of_name)
    f.create_dataset(name + '/n_frame_per_seg', data=data_of_name)
    f.create_dataset(name + '/n_frames', data=data_of_name)
    f.create_dataset(name + '/picks', data=data_of_name)
    f.create_dataset(name + '/n_steps', data=data_of_name)
    f.create_dataset(name + '/gtsummary', data=data_of_name)
    f.create_dataset(name + '/video_name', data=data_of_name)

f.close()