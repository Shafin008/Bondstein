import supervision as sv
from tqdm.notebook import tqdm

VIDEO_DIR_PATH = f"videos"
IMAGE_DIR_PATH = f"images"
FRAME_STRIDE = 10

video_paths = sv.list_files_with_extensions(
    directory=VIDEO_DIR_PATH,
    extensions=["mov", "mp4"])

TRAIN_VIDEO_PATHS, TEST_VIDEO_PATHS = video_paths[:3], video_paths[3:]
# print(video_paths)
# print(TRAIN_VIDEO_PATHS)
# print(TEST_VIDEO_PATHS)

for video_path in tqdm(TRAIN_VIDEO_PATHS):
    video_name = video_path.stem
    image_name_pattern = video_name + "-{:05d}.png"
    with sv.ImageSink(target_dir_path=IMAGE_DIR_PATH, image_name_pattern=image_name_pattern) as sink:
        for image in sv.get_video_frames_generator(source_path=str(video_path), stride=FRAME_STRIDE):
            sink.save_image(image=image)

image_paths = sv.list_files_with_extensions(
    directory=IMAGE_DIR_PATH,
    extensions=["png", "jpg", "jpg"])

print('image count:', len(image_paths))