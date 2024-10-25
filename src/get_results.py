import os
import pickle

def pickle_to_txt(pickle_file, output_dir):
    try:
        print(f"Loading pickle file: {pickle_file}")
        with open(pickle_file, 'rb') as f:
            data = pickle.load(f)

        print(f"Creating output directory: {output_dir}")
        os.makedirs(output_dir, exist_ok=True)

        if not data:
            print("No data found in pickle file.")
            return

        for i, sample in enumerate(data):
            frame_id = sample['frame_id']
            boxes_lidar = sample['boxes_lidar']
            scores = sample['score']

            txt_file = os.path.join(output_dir, f"{frame_id}.txt")

            print(f"Writing to file: {txt_file}")
            with open(txt_file, 'w') as txt_f:
                for j, (box, score) in enumerate(zip(boxes_lidar, scores)):
                    x, y, z, length, width, height, rotation = box
                    line = f"{x} {y} {z} {length} {width} {height} {rotation} {score}\n"
                    txt_f.write(line)
                    print(f"Written box {j} for frame {frame_id}")

            print(f"Completed writing for frame {frame_id}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    # Choose output directory for the results txt file:
    output_dir = "/home/tauproj1/Innoviz_Project/OpenPCDet-master_New_copy/3D_Object_Detector/Evaluation/pvrcnn_evaluations/pvrcnn_best/detector_labels"

    # Write the path to the results pickle file:
    pickle_file = "/home/tauproj1/Innoviz_Project/OpenPCDet-master_New_copy/3D_Object_Detector/Evaluation/pvrcnn_evaluations/model_outputs/pv_rcnn_test_best/default/eval/eval_with_train/epoch_80/val/result.pkl"
    
    pickle_to_txt(pickle_file, output_dir)
