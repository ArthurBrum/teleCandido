%% pseudo-codigo
% 1) Converter valor binario de caracter ascii para uma onda
%    (testar dividir em 2 bits: 4 possiveis freq
%
% 2) Juntar caracteres todo texto em uma lista. Colocando uma 5a freq para
% indicar inicio de novo caracter e ajudar na sincronia
%
% 3) Testar se som reconhece




Fs = 14400;                                     % Sampling Frequency
t  = linspace(0, 1, Fs);                        % One Second Time Vector
w = 2*pi*1000;                                  % Radian Value To Create 1kHz Tone
s = sin(w*t);                                   % Create Tone
sound(s, Fs)                                    % Produce Tone As Sound


%% Referencias
% https://www.mathworks.com/help/audio/signal-io-and-waveform-generation.html