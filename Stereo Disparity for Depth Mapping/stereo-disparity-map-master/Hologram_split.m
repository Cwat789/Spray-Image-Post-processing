
I = imread('rec_300mm_500px.tif');

[x, y] = size(I);

img1 = zeros(x,y);
img2 = zeros(x,y);

for l = 1:x
    if l>= x/2
        img1(:,l) = I(:,l);
        img2(:,l) = 0;
    else
        img1(:,l) = 0;
        img2(:,l) = I(:,l);
    end
end
        
        


