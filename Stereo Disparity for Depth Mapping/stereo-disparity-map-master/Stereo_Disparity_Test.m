clc;
clear;


%PIXEL_DISP(leftImage, rightImage, outputImage, plot, greyscale, scan_window_size, support_scale); 


PIXEL_DISP('IN/MapL.tif', 'IN/MapU.tif', 'OUT/MapStereo.tif', 0, 1, 7, 3);


%Consider using gray threshhold to create bianary image of map for noise 

%Box size 25 too large
%Usual "support_scale" is 3



