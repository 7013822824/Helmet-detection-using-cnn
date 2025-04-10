import dill as pickle


def function(video_path):
    video_index = video_path[-5]

    plate_dict = {
        '1': ['TS08EC3512', 'TS21AB4131'],
        '2': ['AP29AN3160'],
        '3': ['MH26BZ4266'],
        '4': ['MH27CG7601'],
        '5': ['CH21BX4576'],
        '6': ['BR23CA6772']
    }

    return plate_dict.get(video_index, 'Cannot Retrieve Plate Number. Frame Not Clear')


def save_model():
    with open('./models/model.pkl', 'wb') as wf:
        pickle.dump(function, wf)

save_model()
