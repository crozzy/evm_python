import ffvideo
import os
from numpy import zeros, size
from build_Gdown_stack import build_Gdown_stack
from ideal_bandpassing import ideal_bandpassing
from cv import *

def amplify_spacial_Gdown_temporal_ideal(video_file, output_dir, alpha, level,
                                         f1, fh, sampling_rate,
                                         chromAttenuation):
    name = os.path.splitext(os.path.basename(video_file))[0]
    video_name = '%s-ideal-from-%i-to-%i-alpha-%i-level-%i-chromAtn-%i.avi' % (name, f1, fh, alpha, level, chromAttenuation)
    output_name = os.path.join(output_dir, video_name)

    # Read with ffvideo
    video = ffvideo.VideoStream(video_file)

    nChannels = 3

    start_index = 1
    end_index = video.duration - 10

    # Write with opencv
    vidout = CreateVideoWriter('algo2.avi', CV_FOURCC('F', 'M', 'P', '4'), video.framerate, (800, 600), True)

    print 'Spacial filtering...'
    Gdown_stack = build_Gdown_stack(video_file, start_index, end_index, level)
    print 'finished'

    print 'Temporal filtering...'
    filtered_stack = ideal_bandpassing(Gdown_stack, 1, f1, fh, sampling_rate)
    print 'finished'

    # amplify_
    filtered_stack(:,:,:,1) = filtered_stack(:,:,:,1) .* alpha

    for i in range(start_index, end_index):
        frame = LoadImage()
        WriteFrame(vidout, frame)
    del vidout
