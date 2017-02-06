clear all;

addpath('Benetos');
addpath('matlab-midi-master/src');

% Inputs:
%  filename filename for .wav file
%  iter     number of iterations (e.g. 30)
%  S        number of sources (e.g. 3)
%  sz       sparsity parameter for pitch activation (e.g. 1.0-1.3)
%  su       sparsity parameter for source contribution (e.g. 1.0-1.3)
%  sh       sparsity parameter for pitch shifting (e.g. 1.0-1.3)
%
% Outputs:
%  pianoRoll raw piano-roll output (dims: P x T, P: pitch index, T: 20ms step)

filename_audio = '/home/manu/Dropbox/MasterUPF/Asignaturas/2Trim/Music Information Retrieval/MIR Project/evaluation/2Saarland.wav';

iter = 30;
S = 3;
sz = 1;
su = 1;
sh = 1;

[benetosResults] = transcription(filename_audio,iter,S,sz,su,sh);
threshold = 0.035;
benetosResults(benetosResults<threshold) = 0;

%  Process PIANOROLL to f0s
f0s = zeros(max(sum(benetosResults>1,1))+1,size(benetosResults,2));
t = 0:0.01:(0.01*(length(f0s)-1));
f0s(1,:) = t;

for i = 1:size(benetosResults,2)
    if ~(isempty(midi2freq(find(benetosResults(:,i)>0))))
        f0s(1+(1:sum(benetosResults(:,i)>0)),i)  = midi2freq(find(benetosResults(:,i)>0)-1);
    end
end

tiempo = 0;
[M,N] = size(f0s);
resultadoBenetos = zeros(N*2,M+1);
j = 1;
for i = 1:2:N*2
    resultadoBenetos(i,1) = tiempo;
    resultadoBenetos(i+1,1) = tiempo + 0.01;
    resultadoBenetos(i,2:11) = f0s(:,j);
    resultadoBenetos(i+1,2:11) = f0s(:,j);
    tiempo = tiempo + 0.02;
    j = j + 1;
end

cd ('/home/manu/Dropbox/MasterUPF/Asignaturas/2Trim/Music Information Retrieval/MIR Project/evaluation/evaluation/dataBenetos')

dlmwrite('resultadoBenetos.txt',resultadoBenetos,' ');