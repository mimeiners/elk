%% STEMlab measurements for Bode plots
% @author: Mirco Meiners (HSB)
% Input signal: DF_IN1
% Output signal: DF_IN2
clear;

%% Define Red Pitaya as TCP client object
IP = '192.168.111.181';  % IP of your Red Pitaya ...
port = 5000;
RP = tcpclient(IP, port);

%% Open connection to Red Pitaya
RP.ByteOrder = 'big-endian';
configureTerminator(RP, 'CR/LF');
flush(RP);

%% Generate continous signal
func = 'TRIANGLE';  % Signalform (SINE, SQUARE, TRIANGLE)
ampl = 0.5;  % Amplitude (-1 V ... 1 V)
freq = 1000;  % Frequenz (0 Hz ... 62.5e6 Hz)
offset = 0.5;  % Offset (-1 V ... 1 V)
t = linspace(0, 2.097e-3, 16384);  % Skalierung der Zeitachse (Sampling)


% Send SCPI command to Red Pitaya to turn ON generator
writeline(RP,'GEN:RST');  % Reset Generator
writeline(RP,strcat("SOUR1:FUNC ", func));  % Set function of output signal
writeline(RP,strcat("SOUR1:VOLT ", num2str(ampl)));  % Set amplitude
writeline(RP,strcat("SOUR1:VOLT:OFFS ", num2str(offset)));  % Set offset
writeline(RP,strcat("SOUR1:FREQ:FIX ", num2str(freq)));  % Set frequency
writeline(RP,'OUTPUT1:STATE ON');  % Turn on output OUT1
    
writeline(RP,'SOUR1:TRIG:INT');  % Generate trigger
    
pause(1);

% Trigger
writeline(RP,'ACQ:RST ');  % Input reset
% writeline(RP,'ACQ:DATA:FORMAT ASCII')
% writeline(RP,'ACQ:DATA:UNITS VOLTS')
writeline(RP,'ACQ:DEC 16');  % Decimation (1, 8, 16, 64, 1024, 8192)
writeline(RP,'ACQ:AVG ON');  % Averaging (OFF, ON)
writeline(RP,'ACQ:TRIG:LEV 0.5');  % Trigger level
writeline(RP,'ACQ:RST');  % Input reset
writeline(RP,'ACQ:DEC 16');  % Decimation
writeline(RP,'ACQ:TRIG:LEV 0.5');  % Trigger level

% Set trigger delay to 0 samples
% 0 samples delay sets trigger to the center of the buffer
% Signal on your graph will have the trigger in the center (symmetrical)
% Samples from left to the center are samples before trigger
% Samples from center to the right are samples after trigger
writeline(RP,'ACQ:TRIG:DLY 8192')  % Delay

% Start & Trigger
% Trigger source setting must be after ACQ:START
% Set trigger to source 1 positive edge
writeline(RP,'ACQ:START')  % Start der Messung

% writeline(RP,'ACQ:SOUR1:GAIN LV');  % Sets gain to LV/HV (should be the same as jumpers)
% writeline(RP,'ACQ:SOUR2:GAIN LV');  % Sets gain to LV/HV (should be the same as jumpers)

% After acquisition is started some time delay is needed in order to acquire fresh samples in the buffer
pause(1);
% Here we have used time delay of one second, but you can calculate the exact value by taking into account buffer
% length and sampling rate
writeline(RP,'ACQ:TRIG NOW')  % Trigger setzen

for n = 1:5
    % Input IN1
    % pause(0.1);
    IN1 = writeread(RP,'ACQ:SOUR1:DATA?');
    % Convert values to numbers.
    % The first character in string is "{" and the last 3 are 2 spaces and "}".
    IN1_num = str2num(IN1(1, 2:length(IN1)-3));
    DF_IN1(:,n) = IN1_num';

    % Input IN2
    % pause(0.1)
    IN2 = writeread(RP,'ACQ:SOUR2:DATA?');

    IN2_num = str2num(IN2(1, 2:length(IN2)-3));
    DF_IN2(:,n) = IN2_num';
end

% Turn off generator OUT1
writeline(RP,'OUTPUT1:STATE OFF');
    
%% Close connection to Red Pitaya
clear RP;

%% Save data as mat file
% save('./data/IN_D1.mat', 'DF_IN1', 'DF_IN2');
save('./data/IN1_D1.mat', 'DF_IN1');
save('./data/IN2_D1.mat', 'DF_IN2');

%% Save data as csv file
% Not recommended, old version
% csvwrite('./data/IN1_D1.csv', 'DF_IN1');
% csvwrite('./data/IN2_D1.csv', 'DF_IN2'); 

% Better cross-platform compatibility, new version
writematrix('DF_IN1', './data/IN1_D1.mat.csv');
writematrix('DF_IN2', './data/IN2_D1.mat.csv');

%% Save data as parquet file
% parquet data is of type table, no matrix operations
% parquetwrite('data/IN1_D1.mat.parquet', array2table(DF_IN1));
% parquetwrite('data/IN2_D1.mat.parquet', array2table(DF_IN2));

%% Save data as excel sheet
% data is table data, no matrix operations
% writematrix(DF_IN1, './data/IN1_D1.mat.xlsx');
% writematrix(DF_IN1, './data/IN2_D1.mat.xlsx');
% writematrix(DF_IN1, './data/IN_D1.mat.xlsx', 'Sheet', 1);
% writematrix(DF_IN2, './data/IN_D1.mat.xlsx', 'Sheet', 2);
