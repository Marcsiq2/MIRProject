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

filename_audio = '/home/manu/MTG/SaarlandWav/2Saarland.wav';

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
    if ~(isempty(midi2freq(find(benetosResults(:,i)>0)+nn(1))))
        f0s(1+(1:sum(benetosResults(:,i)>0)),i)  = midi2freq(find(benetosResults(:,i)>0)+nn(1)-1);
    end
end

tiempo = 0;
[M,N] = size(f0s);
resultadoBenetos = zeros(N,M+1);
j = 1;
for i = 1:1:N
    resultadoBenetos(i,1) = tiempo;
    resultadoBenetos(i,2:11) = f0s(:,i);
    tiempo = tiempo + 0.02;
end

cd ('/home/manu/Documentos/MIR/MIRProject')

dlmwrite('resultadoBenetos.txt',resultadoBenetos,' ');