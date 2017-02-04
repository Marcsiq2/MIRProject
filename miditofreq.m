function [  ] = miditofreq(in_path, out_path, filename )
    %MIDITOFREQ Summary of this function goes here
    %   Detailed explanation goes here
    disp(sprintf('Converting: %s',filename));
    addpath('matlab-midi-master\src');
    m = readmidi(strcat(in_path,filename));
    Notes = midiInfo(m,0);
    [PR,t,nn] = piano_roll(Notes);
 
    f0s = zeros(max(sum(PR>1,1))+1,size(PR,2));
    f0s(1,:) = t;

    for i = 1:size(PR,2)
        if ~(isempty(midi2freq(find(PR(:,i)>0)+nn(1))))
            f0s(1+(1:sum(PR(:,i)>0)),i)  = midi2freq(find(PR(:,i)>0)+nn(1)-1);
        end
    end
    f = filename(1:end -3);
    
    dlmwrite(strcat(out_path, f, 'f0s'),f0s','precision','%10.4f', 'delimiter', '\t');
end

function freq = midi2freq(midiNote)
    % Converts midiNote to a frequency in Hz
    if isempty(midiNote)
        freq = [];
    else
        freq =(440/32)*2.^((midiNote-9)/12).*(midiNote>0);
    end
end