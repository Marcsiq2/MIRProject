addpath('Benetos');
addpath('matlab-midi-master/src');

A = importdata('Dataset\maps\maps_dataset.txt');
out_path = ('evaluation/Maps_benetos/th_');
iter = 30;
S = 3;
sz = 1;
su = 1;
sh = 1;
threshold =[ 0.05, 0.01, 0.005, 0.001];
for th = threshold
    out = strcat(out_path,num2str(th,3),'/');
    mkdir(out);
    parfor d=1:length(A)
        benetos_extractor(out, A{d}, th, iter,S,sz,su,sh)
    end
end