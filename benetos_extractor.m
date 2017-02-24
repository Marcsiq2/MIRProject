function [  ] = benetos_extractor(out_path, filename, threshold, iter,S,sz,su,sh)
    filename_audio = filename(30:end);
    [benetosResults] = transcription(filename_audio,iter,S,sz,su,sh);
    
    maximo = 0;
    
    for i = 1:size(benetosResults,2)
        cont = 0;
        aux = benetosResults(benetosResults(:,i)>threshold, i);
        if (maximo < length(aux))
            maximo = cont;
        end
    end

    f0s = zeros(size(benetosResults,2),maximo+1);
    f0s(:,1) = 0:0.01:((size(benetosResults,2)-1)*0.01);
    
    for i = 1:size(benetosResults,2)
        aux = benetosResults(:, i);
        cont = 2;
        for j = 1:size(benetosResults,1)
            if (aux(j) > threshold)
                f0s(i,cont) = 27.5*2.^(((j-1)*10)/120);
                cont = cont + 1;
            end
        end
    end
    
    f = strsplit(filename_audio, '/');
    f = f{end}(1:end-3);
    dlmwrite(strcat(out_path, f, 'f0s'),f0s,'precision','%10.4f', 'delimiter', '\t');
end