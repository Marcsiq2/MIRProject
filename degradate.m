clear all

A = importdata('Dataset\maps\maps_dataset.txt');
degradation = 'radioBroadcast';
out_path = strcat('Dataset\maps_', degradation, '/');
mkdir(out_path);
parfor i=1:length(A)
    degradate_audio(out_path, A{i}(30:end), degradation);
end
