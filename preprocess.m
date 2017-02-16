clear all

A = importdata('Dataset\maps\maps_dataset_midi.txt');
for i=1:length(A)
    miditofreq('Dataset\maps\', 'evaluation\Maps\', A{i}(30:end));
end
