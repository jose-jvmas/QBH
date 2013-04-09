function SAX_result = SAX_implementation(data,num_segments,alphabet_size);
% Function to get the SAX coding of data
% Inputs:
% -- data : Raw data
% -- num_segments : Number of segments in which we divide the signal (PAA)
% -- alphabet_size : Number levels for the coding (SAX)
%
% Output:
% -- SAX_result : Result of applying SAX on data

% We obtain the PAA approximation of data:
PAA_result = PAA_approx(data,num_segments);

% We initialize the outputs of SAX: levels and codes
SAX_result_level = zeros(1,length(PAA_result));
SAX_result = cell(1,length(PAA_result));

% Borders for the amplitude discretization. Follows gaussian distribution:
switch alphabet_size
        case 2, cut_points  = [-inf 0];
        case 3, cut_points  = [-inf -0.43 0.43];
        case 4, cut_points  = [-inf -0.67 0 0.67];
        case 5, cut_points  = [-inf -0.84 -0.25 0.25 0.84];
        case 6, cut_points  = [-inf -0.97 -0.43 0 0.43 0.97];
        case 7, cut_points  = [-inf -1.07 -0.57 -0.18 0.18 0.57 1.07];
        case 8, cut_points  = [-inf -1.15 -0.67 -0.32 0 0.32 0.67 1.15];
        case 9, cut_points  = [-inf -1.22 -0.76 -0.43 -0.14 0.14 0.43 0.76 1.22];
        case 10, cut_points = [-inf -1.28 -0.84 -0.52 -0.25 0. 0.25 0.52 0.84 1.28];
        case 11, cut_points = [-inf -1.34 -0.91 -0.6 -0.35 -0.11 0.11 0.35 0.6 0.91 1.34];
        case 12, cut_points = [-inf -1.38 -0.97 -0.67 -0.43 -0.21 0 0.21 0.43 0.67 0.97 1.38];
        case 13, cut_points = [-inf -1.43 -1.02 -0.74 -0.5 -0.29 -0.1 0.1 0.29 0.5 0.74 1.02 1.43];
        case 14, cut_points = [-inf -1.47 -1.07 -0.79 -0.57 -0.37 -0.18 0 0.18 0.37 0.57 0.79 1.07 1.47];
        case 15, cut_points = [-inf -1.5 -1.11 -0.84 -0.62 -0.43 -0.25 -0.08 0.08 0.25 0.43 0.62 0.84 1.11 1.5];
        case 16, cut_points = [-inf -1.53 -1.15 -0.89 -0.67 -0.49 -0.32 -0.16 0 0.16 0.32 0.49 0.67 0.89 1.15 1.53];
        case 17, cut_points = [-inf -1.56 -1.19 -0.93 -0.72 -0.54 -0.38 -0.22 -0.07 0.07 0.22 0.38 0.54 0.72 0.93 1.19 1.56];
        case 18, cut_points = [-inf -1.59 -1.22 -0.97 -0.76 -0.59 -0.43 -0.28 -0.14 0 0.14 0.28 0.43 0.59 0.76 0.97 1.22 1.59];
        case 19, cut_points = [-inf -1.62 -1.25 -1 -0.8 -0.63 -0.48 -0.34 -0.2 -0.07 0.07 0.2 0.34 0.48 0.63 0.8 1 1.25 1.62];
        case 20, cut_points = [-inf -1.64 -1.28 -1.04 -0.84 -0.67 -0.52 -0.39 -0.25 -0.13 0 0.13 0.25 0.39 0.52 0.67 0.84 1.04 1.28 1.64];
        otherwise disp('Error! alphabet_size is too big');           
end;

% For the coding of the amplitude discretization:
string_equivalent = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

% Discretization:
for i = 1 : length(PAA_result)
    % We check where, in the borders of the distribution, our sample is:
    SAX_result_level(i) = sum( (cut_points <= PAA_result(i)),2);
    % We code the level in 
    SAX_result(i) = string_equivalent(SAX_result_level(i));
end;