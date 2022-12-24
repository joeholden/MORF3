parent_dir = "E:/MORF3 Images/3233 LE done/single cells/"
save_dir = "C:/Users/joema/Desktop/save/"

list = getFileList(parent_dir);
for (i=0; i<list.length; i++) {
    open(parent_dir + list[i]);
	title = getTitle();
	title_ne = File.nameWithoutExtension;

	selectWindow(title);
	run("Split Channels");
	run("Z Project...", "projection=[Standard Deviation]");
	selectWindow("C3-" + title);
	close();
	run("Green");
	//run("Brightness/Contrast...");
	run("Enhance Contrast", "saturated=0.35");
	selectWindow("C2-" + title);
	close();
	selectWindow("C1-" + title);
	run("Z Project...", "projection=[Standard Deviation]");
	selectWindow("C1-" + title);
	close();
	run("Red");
	run("Enhance Contrast", "saturated=0.35");
	run("Merge Channels...", "c1=[STD_C3-" + title + "] c2=[STD_C1-" + title + "] create");

	run("Flatten");
	saveAs("PNG", save_dir + title_ne + ".png");
	close();
 }
 