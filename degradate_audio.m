function [  ] = degradate_audio(out_path, filename, degradation )
    %MIDITOFREQ Summary of this function goes here
    %   Detailed explanation goes here
    disp(sprintf('Degradating: %s with %s',filename, degradation));
    addpath(genpath(fullfile(pwd,'audio-degradation-toolbox-master')));
    [f_audio,samplingFreq]=audioread(filename);
    f_audio_out = applyDegradation(degradation, f_audio, samplingFreq);
    fil = strsplit(filename, '/');
    disp(fil{end})
    fil = fil{end};
    audiowrite(fullfile(out_path, fil), f_audio_out, samplingFreq);

end
