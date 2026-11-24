%% Init add-on
addpath("ltspice2matlab/")

%% Read raw
raw = LTspice2Matlab('./Activity_19_1N4001.raw');
t = raw.time_vect;
v_IN1 = raw.variable_mat(2,:);
v_IN2 = raw.variable_mat(1,:);
i_D = raw.variable_mat(4,:);


%% Plot
fig1 = figure(1);
yyaxis left
plot(t*1e3, v_IN1, t*1e3, v_IN2)
ylabel('Spannungen in V')
grid

yyaxis right
plot(t*1e3, i_D*1e6)
ylabel('Strom in \muA')

xlabel('Zeit t in ms')
legend('v_{IN1}(t)','v_{IN2}(t)','i_D(t)')
