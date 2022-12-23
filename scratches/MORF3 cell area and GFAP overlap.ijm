v5_title = getTitle();
v5_title_ne = File.nameWithoutExtension;
run("Set Measurements...", "area mean standard modal min centroid center perimeter bounding fit shape feret's integrated median skewness kurtosis area_fraction stack limit display redirect=None decimal=3");

run("8-bit");
run("Z Project...", "projection=[Standard Deviation]");
run("Green");

setOption("ScaleConversions", true);
run("8-bit");
run("Auto Threshold", "method=Huang white");
run("Duplicate...", " ");
run("Invert");
run("Grays");
selectWindow("STD_" + v5_title);
run("Analyze Particles...", "size=10-Infinity exclude add");
selectWindow("STD_" + v5_title_ne +"-1.oib");
run("Analyze Particles...", "size=10-Infinity exclude add");
waitForUser("Take Care of V5 ROIs");
close();
close();
close();
waitForUser("Open GFAP Image and Crop it");
title = getTitle();

run("Split Channels");
selectWindow("C1-" + title);
run("Enhance Contrast", "saturated=0.35");

setOption("ScaleConversions", true);
run("8-bit");
run("Auto Local Threshold", "method=Phansalkar radius=15 parameter_1=0 parameter_2=0 white");
count = roiManager("count");
roiManager("select", count-1);
run("Measure");

roi_save_dir = "C:/Users/Acer/Desktop/rois/"
roiManager("select", count-1); //last roi is the cell outline
roiManager("Save", roi_save_dir + v5_title_ne + ".roi");
roiManager("select", 0); //first roi is the region with the cell
roiManager("Save", roi_save_dir + "crop_region_"+v5_title_ne + ".roi");
waitForUser("This will close all images");
close();
close();
roiManager("Delete");
roiManager("Deselect");
roiManager("Delete");



