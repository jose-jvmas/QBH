function PAA_result = PAA_approx(data,num_segments);
% Function to get the PAA coding of data
% Inputs:
% -- data : Raw data
% -- num_segments : Number of segments in which we divide the signal
%
% Output:
% -- PAA_result : Result of applying PAA on data


% PLOTTING ? %
plotting = 0;


% We normalize the signal (mean = 0; standard deviation = 1):
deviation = std(data,1);
data_norm = (data-mean(data))/std(data,1);

% Length of the data:
data_length = length(data_norm);

% Number of elements to analyze from the initial data for each segment:
win_size = floor(data_length/num_segments);                         

% PAA coding:
% - In case we do not approximate (number of segments equals length of
% data):
if data_length == num_segments
    PAA_result = data_norm;

% Convert to PAA.    
else
    % data_length is not dividable by num_segments (adding zeros):
    if (data_length/num_segments - floor(data_length/num_segments))                               
        temp = zeros(num_segments, data_length);
        for j = 1 : num_segments
            temp(j, :) = data_norm;
        end
        expanded_sub_section = reshape(temp, 1, data_length*num_segments);
        otro = reshape(expanded_sub_section, data_length, num_segments);
        PAA_result_prev = reshape(expanded_sub_section, data_length, num_segments);
        PAA_result = [mean(reshape(expanded_sub_section, data_length, num_segments))];
    % N is dividable by n
    else                          
        PAA_result = [mean(reshape(data_norm,win_size,num_segments))];
    end
end


% PLOTTING:
if plotting == 1
PAA_plot = [];
    for i=1:num_segments
        if i == 1
            PAA_plot = ones(1,win_size)*PAA_result(i);
        else
            PAA_plot = [PAA_plot ones(1,win_size)*PAA_result(i)];
        end
    end
    close all
    plot(data_norm);
    hold on;
    plot(PAA_plot,'r');
    hold off;
end
